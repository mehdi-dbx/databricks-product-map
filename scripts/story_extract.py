#!/usr/bin/env python3
"""Extract the narrative from docs/protostory.md, without the working notes.

The working draft holds milestones, link lines and checks. This script keeps only
what the reader sees: chapter titles, point titles and texts, the transition at the
end of each chapter, and the closing. It also keeps the capsules cited by each point.

Each link line carries the sentence that leads from one point to the next. Its label
("Link 2.1 → 2.2 (reason)") is dropped, and its sentence opens the next point, so the
text flows from point to point.

Usage:
  python3 scripts/story_extract.py
    writes docs/story.md       (human-readable slides)
    writes app/src/story.json  (data for the Story tab; capsules resolved to tree paths)
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DRAFT = ROOT / "docs/protostory.md"
OUT_MD = ROOT / "docs/story.md"
OUT_JSON = ROOT / "app/src/story.json"

sys.path.insert(0, str(ROOT / "scripts"))
from tree_walk import iter_all  # noqa: E402

CHAPTER_RE = re.compile(r"^## M\d+ — Chapter (\d+)\. (.+)$")
POINT_RE = re.compile(r"^\*\*Point (\d+\.\d+) — (.+?)\.\*\*(?:\s*\*\((.+?)\)\*)?\s*$")
HANDOFF_RE = re.compile(r"^\*\*Hands off:\*\*\s*(.+)$")
CLOSING_RE = re.compile(r"^\*\*Closing — (.+?)\.\*\*\s*$")
LINK_RE = re.compile(r"^↳ \*\*Link [^*]+\*\*\s*(.*)$")


def cap(s):
    return s[:1].upper() + s[1:] if s else s


def parse(text):
    """Return a list of chapters: {num, title, points: [{id, title, capsules, text}], handoff}."""
    chapters, ch, cur, pending = [], None, None, ""
    for block in re.split(r"\n\s*\n", text):
        lines = block.strip().splitlines()
        if not lines:
            continue
        head = lines[0].strip()
        m = CHAPTER_RE.match(head)
        if m:
            ch = {"num": int(m.group(1)), "title": m.group(2), "points": [], "handoff": ""}
            chapters.append(ch)
            cur = None
            continue
        if ch is None or head.startswith("## M11"):
            if head.startswith("## M11"):
                break
            continue
        m = LINK_RE.match(head)
        if m:
            pending = " ".join([m.group(1)] + [ln.strip() for ln in lines[1:]]).strip()
            continue
        m = POINT_RE.match(head)
        if m:
            # "both trees" is an annotation in the draft, not a capsule name
            caps = [c.strip() for c in (m.group(3) or "").split(",")
                    if c.strip() and c.strip() != "both trees"]
            body = " ".join(ln.strip() for ln in lines[1:])
            cur = {"id": m.group(1), "title": m.group(2), "capsules": caps,
                   "lead": pending, "text": body}
            pending = ""
            ch["points"].append(cur)
            continue
        m = CLOSING_RE.match(head)
        if m:
            cur = {"id": f"{ch['num']}.end", "title": m.group(1).capitalize(), "capsules": [],
                   "lead": "", "text": " ".join(ln.strip() for ln in lines[1:])}
            ch["points"].append(cur)
            continue
        m = HANDOFF_RE.match(head)
        if m:
            body = " ".join([m.group(1)] + [ln.strip() for ln in lines[1:]])
            ch["handoff"] = cap((pending + " " + cap(body)).strip())
            pending = ""
            cur = None
            continue
        # anything else (Receives, Link, Check, bullets) is a working note: skip it
    return chapters


SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")


def sentences(text):
    """Split a paragraph into its sentences, word for word."""
    parts = [s.strip() for s in SENTENCE_END.split(text.strip()) if s.strip()]
    # guard: splitting must not lose or change a single word
    assert " ".join(parts).split() == text.split(), text[:80]
    return parts


def to_markdown(chapters):
    """Slide layout: title, the transition sentence as a lead line, one bullet per sentence."""
    out = ["# The Databricks data and AI story", ""]
    for ch in chapters:
        out += [f"## {ch['num']}. {ch['title']}", ""]
        for p in ch["points"]:
            out += [f"### {p['title']}", ""]
            if p["lead"]:
                out += [f"*{p['lead']}*", ""]
            out += [f"- {s}" for s in sentences(p["text"])] + [""]
            if p["capsules"]:
                out += [f"*Capsules: {', '.join(p['capsules'])}*", ""]
        if ch["handoff"]:
            out += [f"*{ch['handoff']}*", ""]
    return "\n".join(out).rstrip() + "\n"


def capsule_index():
    """Map a short capsule label to every d2 capsule it names, in either tree.

    The draft cites capsules by short name: "Lakebase" for "Lakebase — serverless
    Postgres", "AI Search" for "AI Search (ex-Vector Search)". A label matches a capsule
    when it equals the capsule name without its parentheses and without its " — " suffix.
    """
    def key(name):
        return re.sub(r"\s*\(.*?\)", "", name).split(" — ")[0].strip().lower()

    idx = {}
    for x in iter_all():
        if x["depth"] == 2:
            idx.setdefault(key(x["path"][2]), []).append(
                {"tree": x["tree"].split("-")[0], "path": x["path"]})
    return idx, key


def to_json(chapters):
    idx, key = capsule_index()
    unresolved = []
    out = {"chapters": []}
    for ch in chapters:
        c = {"num": ch["num"], "title": ch["title"], "handoff": ch["handoff"], "points": []}
        for p in ch["points"]:
            refs = []
            for label in p["capsules"]:
                hits = idx.get(key(label), [])
                if not hits:
                    unresolved.append((p["id"], label))
                refs += hits
            c["points"].append({"id": p["id"], "title": p["title"], "lead": p["lead"],
                                "bullets": sentences(p["text"]), "refs": refs})
        out["chapters"].append(c)
    if unresolved:
        raise SystemExit("unresolved capsule labels: " + ", ".join(f"{i} '{lbl}'" for i, lbl in unresolved))
    return out


if __name__ == "__main__":
    chapters = parse(DRAFT.read_text(encoding="utf-8"))
    OUT_MD.write_text(to_markdown(chapters), encoding="utf-8")
    data = to_json(chapters)
    OUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    n_points = sum(len(c["points"]) for c in chapters)
    n_refs = sum(len(p["refs"]) for c in data["chapters"] for p in c["points"])
    print(f"wrote {OUT_MD.relative_to(ROOT)} and {OUT_JSON.relative_to(ROOT)}: "
          f"{len(chapters)} chapters, {n_points} points, {n_refs} capsule references")
