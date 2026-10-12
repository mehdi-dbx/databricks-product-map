#!/usr/bin/env python3
"""Copy the story additions (effect, challenge, pivot) into docs/story-notes.md.

  python3 scripts/apply_story_additions.py docs/story-additions.json
  python3 scripts/apply_story_additions.py docs/story-additions.json --check   # validate, write nothing

The additions follow docs/story-editorial-guide.md. Each item holds the three sentences
of one point and the capsule fields they rest on. The tools are described in
docs/story-additions-setup.md.

- Every source is checked against the trees. Its `text` must equal the field (`note`,
  `solves[i].problem` or `solves[i].solution`) of the capsule `refs[ref]` of the point
  in app/src/story.json. A sentence that is not empty needs at least one source. An item
  that fails is refused, and nothing of it is written.
- The sentences become the last lines of the point's block, one line each:
  **Effect:** …, **Challenge:** …, **Pivot:** …. Their sources go to the end of the
  chapter's Check block, under "- Additions N.k (editorial guide):".
- Existing lines are never changed. The only lines replaced are the ones this script
  wrote, when their item has changed. Running it again on the same file changes nothing.
- Each sentence is also checked for the writing faults that earlier drafts showed: a
  digit, a "Label: …" formula, a buzzword, a fragment too short to be a sentence, a pivot
  that only says "addresses this", and a sentence too close to the point's own lead or
  bullets or to a bullet of chapter 1. These are warnings: they do not block the item.
  Each one is either fixed or kept on purpose, and that choice goes into docs/story-journal.md.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
NOTES = ROOT / "docs/story-notes.md"
STORY = ROOT / "app/src/story.json"
TREES = {"ai": ROOT / "app/src/ai-tree.json", "ds": ROOT / "app/src/ds-tree.json"}

ADDS = (("effect", "Effect"), ("challenge", "Challenge"), ("pivot", "Pivot"))
ADD_RE = re.compile(r"^\*\*(Effect|Challenge|Pivot):\*\* ")
FIELD_RE = re.compile(r"solves\[(\d+)\]\.(problem|solution)")
BUZZWORDS = re.compile(r"\b(seamless|unlock|empower|revolution|game.?chang|journey|leverage|cutting.edge|"
                       r"world.class|effortless|supercharge)", re.I)


def words(text):
    """Content words, plural folded into singular, so that a reworded sentence still matches."""
    return {w[:-1] if len(w) > 4 and w.endswith("s") else w
            for w in re.findall(r"[a-z]+", text.lower()) if len(w) > 3}


def product_names(refs):
    """Short names a pivot can use for the point's capsules: "Lakehouse / Delta Lake" gives
    "lakehouse" and "delta lake", "AI Dev Kit + internal coding agents (Isaac)" gives "ai dev kit"."""
    names = set()
    for r in refs:
        full = re.sub(r"\s*\(.*?\)", "", r["path"][-1])
        for part in re.split(r" / | \+ | & | — | for ", full):
            if part.strip():
                names.add(part.strip().lower())
    return names


def closeness(a, b):
    """Share of the shorter text's words that the other text also uses."""
    wa, wb = words(a), words(b)
    return len(wa & wb) / max(1, min(len(wa), len(wb)))


def warnings(item, point, chapter1, threshold=0.6):
    """Writing faults seen in earlier drafts, as warnings (they do not refuse the item)."""
    out = []
    for key, label in ADDS:
        text = sentence(item, key)
        if not text:
            continue
        if re.search(r"\d", text):
            out.append(f"{label} has a digit (fine only inside a product name)")
        if re.match(r"^[A-Z][\w /&-]{0,30}: ", text):
            out.append(f"{label} starts with a \"Label: …\" formula")
        if BUZZWORDS.search(text):
            out.append(f"{label} uses a buzzword")
        if len(text.split()) < 5 and key != "pivot":
            out.append(f"{label} looks like a fragment, not a sentence")
        if re.search(r"\baddress(es)? (this|these|it)\b", text, re.I):
            out.append(f"{label} only says the product addresses it")
        if key == "pivot" and not any(n in text.lower() for n in product_names(point.get("refs", []))):
            out.append("Pivot names no product of this point")
        for own in [point.get("lead", "")] + point.get("bullets", []):
            if own and closeness(text, own) >= threshold:
                out.append(f"{label} is close to its own text: {own[:60]}…")
        for b in chapter1:
            if closeness(text, b) >= threshold:
                out.append(f"{label} is close to chapter 1: {b[:60]}…")
    return out


def node(trees, ref):
    n = trees[ref["tree"]]
    for name in ref["path"][1:]:
        n = next((c for c in n.get("children", []) if c.get("n") == name), None)
        if n is None:
            return None
    return n


def field_value(n, field):
    if field == "note":
        return n.get("note")
    m = FIELD_RE.fullmatch(field or "")
    if not m:
        return None
    rows, i = n.get("solves", []), int(m.group(1))
    return rows[i][m.group(2)] if i < len(rows) else None


def sentence(item, key):
    return (item.get(key) or "").strip()


def check(item, points, trees):
    """The reason an item is refused, or None."""
    pid = item.get("point")
    if pid not in points:
        return "no such point in story.json"
    chapter, refs = points[pid]
    if item.get("chapter") != chapter:
        return f"the point is in chapter {chapter}"
    if not refs:
        return "the point cites no capsule"
    for key, label in ADDS:
        if "\n" in sentence(item, key):
            return f"{label} spans several lines"
        srcs = (item.get("sources") or {}).get(key) or []
        if sentence(item, key) and not srcs:
            return f"{label} has no source"
        for s in srcs:
            ref = s.get("ref")
            if not isinstance(ref, int) or not 0 <= ref < len(refs):
                return f"{label}: ref {ref!r} is not a capsule of the point"
            name, n = refs[ref]["path"][-1], node(trees, refs[ref])
            have = field_value(n, s.get("field")) if n else None
            if have is None:
                return f"{label}: no field {s.get('field')!r} on {name}"
            if have != s.get("text"):
                return f"{label}: the text given for {s['field']} on {name} is not the text in the tree"
    return None


def block_bounds(lines, pid):
    """(start, end) of the point's block: from its Point line to the next blank line."""
    start = next((i for i, ln in enumerate(lines) if ln.startswith(f"**Point {pid} — ")), None)
    if start is None:
        return None
    end = start + 1
    while end < len(lines) and lines[end].strip():
        end += 1
    return start, end


def check_bounds(lines, chapter):
    """(start, end) of the chapter's Check block; end is the line after its last non-blank line."""
    sec = next((i for i, ln in enumerate(lines) if re.match(rf"## M\d+ — Chapter {chapter}\. ", ln)), None)
    if sec is None:
        return None
    start = sec + 1
    while start < len(lines) and not lines[start].startswith(("**Check M", "## ")):
        start += 1
    if start == len(lines) or lines[start].startswith("## "):
        return None
    end = start + 1
    while end < len(lines) and lines[end].strip() != "---" and not lines[end].startswith("## "):
        end += 1
    while not lines[end - 1].strip():      # the blank lines before --- stay where they are
        end -= 1
    return start, end


def source_lines(pid, item, refs):
    out = [f"- Additions {pid} (editorial guide):"]
    for key, label in ADDS:
        if not sentence(item, key):
            continue
        by_capsule = {}
        for s in item["sources"][key]:
            by_capsule.setdefault(refs[s["ref"]]["path"][-1], []).append(s["field"])
        out.append(f"  - {label} ← " + "; ".join(f"{name}, {', '.join(f)}" for name, f in by_capsule.items()))
    return out


def main(path, check_only):
    items = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    story = json.loads(STORY.read_text(encoding="utf-8"))
    points = {p["id"]: (c["num"], p["refs"]) for c in story["chapters"] for p in c["points"]}
    texts = {p["id"]: p for c in story["chapters"] for p in c["points"]}
    chapter1 = [b for c in story["chapters"] if c["num"] == 1 for p in c["points"] for b in p["bullets"]]
    warned = []
    trees = {k: json.loads(v.read_text(encoding="utf-8")) for k, v in TREES.items()}
    lines = NOTES.read_text(encoding="utf-8").split("\n")
    applied, already, refused, empty = [], [], [], []

    for item in items:
        why = check(item, points, trees)
        if why:
            refused.append((item, why))
            continue
        pid = item["point"]
        chapter, refs = points[pid]
        warned += [(pid, w) for w in warnings(item, texts[pid], chapter1)]
        new = [f"**{label}:** {sentence(item, key)}" for key, label in ADDS if sentence(item, key)]
        if not new:
            empty.append(item)
            continue
        b, c = block_bounds(lines, pid), check_bounds(lines, chapter)
        if b is None or c is None:
            refused.append((item, "the point or the chapter's Check block is not in story-notes.md"))
            continue
        start, end = b
        old_idx = [i for i in range(start + 1, end) if ADD_RE.match(lines[i])]
        if old_idx and old_idx != list(range(old_idx[0], end)):
            refused.append((item, "the added lines are not the last lines of the point"))
            continue
        src_new = source_lines(pid, item, refs)
        cs, ce = c
        h = next((i for i in range(cs, ce) if lines[i] == src_new[0]), None)
        k = h
        if h is not None:
            k = h + 1
            while k < ce and lines[k].startswith("  - "):
                k += 1
        if [lines[i] for i in old_idx] == new and (h is not None and lines[h:k] == src_new):
            already.append(item)
            continue
        applied.append(item)
        if check_only:
            continue
        # the Check block comes after the point, so write it first: the point's indexes stay valid
        if h is not None:
            lines[h:k] = src_new
        else:
            lines[ce:ce] = src_new
        lines[old_idx[0] if old_idx else end:end] = new

    if applied and not check_only:
        NOTES.write_text("\n".join(lines), encoding="utf-8")

    verb = "would apply" if check_only else "applied"
    print(f"{len(items)} items: {verb} {len(applied)}, already applied {len(already)}, refused {len(refused)}"
          + (f", nothing to write {len(empty)}" if empty else "") + f", warnings {len(warned)}")
    for x in applied:
        print(f"  ok   {x['point']}")
    for x in empty:
        print(f"  --   {x['point']}: no sentence")
    for x, why in refused:
        print(f"  REFUSED {x.get('point')}: {why}")
    for pid, w in warned:
        print(f"  WARN {pid}: {w}")
    for x in items:
        if (x.get("report") or "").strip():
            print(f"  report {x.get('point')}: {x['report']}")
    return 1 if refused else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--check"]
    if len(args) != 1:
        raise SystemExit(__doc__)
    sys.exit(main(args[0], "--check" in sys.argv[1:]))
