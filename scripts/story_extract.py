#!/usr/bin/env python3
"""Extract the narrative from docs/story-notes.md, without the working notes.

The working draft holds milestones, link lines and checks. This script keeps only
what the reader sees: chapter titles, point titles and texts, the transition at the
end of each chapter, and the closing. It also keeps the capsules cited by each point.

Each link line carries the sentence that leads from one point to the next. Its label
("Link 2.1 → 2.2 (reason)") is dropped, and its sentence opens the next point, so the
text flows from point to point.

A point may end with three added lines, **Effect:**, **Challenge:** and **Pivot:**, one
line each (docs/story-editorial-guide.md). They go to the point's `effect`, `challenge`
and `pivot` fields. The point text before them still gives the bullets.

Section M15, "The complete story" (docs/story-cement.md), is read into `thread` (title,
opening, closing) and into each chapter's `intro`.

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
DRAFT = ROOT / "docs/story-notes.md"
OUT_MD = ROOT / "docs/story.md"
OUT_JSON = ROOT / "app/src/story.json"

sys.path.insert(0, str(ROOT / "scripts"))
from tree_walk import iter_all  # noqa: E402

CHAPTER_RE = re.compile(r"^## M\d+ — Chapter (\d+)\. (.+)$")
POINT_RE = re.compile(r"^\*\*Point (\d+\.\d+) — (.+?)\.\*\*(?:\s*\*\((.+?)\)\*)?\s*$")
HANDOFF_RE = re.compile(r"^\*\*Hands off:\*\*\s*(.+)$")
CLOSING_RE = re.compile(r"^\*\*Closing — (.+?)\.\*\*\s*$")
LINK_RE = re.compile(r"^↳ \*\*Link [^*]+\*\*\s*(.*)$")
ADD_RE = re.compile(r"^\*\*(Effect|Challenge|Pivot):\*\*\s*(.*)$")
ADDS = ("effect", "challenge", "pivot")
THREAD_HEAD = "## M15 — The complete story"
THREAD_TITLE_RE = re.compile(r"^\*\*Title:\*\*\s*(.+)$")
THREAD_PART_RE = re.compile(r"^\*\*(Opening|Chapter (\d+)|Closing)\.\*\*\s*$")


def cap(s):
    return s[:1].upper() + s[1:] if s else s


def split_adds(pid, lines):
    """A point's lines → (point text, {effect|challenge|pivot: sentence}). The added lines come last."""
    text, adds = [], {}
    for ln in (ln.strip() for ln in lines):
        m = ADD_RE.match(ln)
        if m:
            key = m.group(1).lower()
            if key in adds:
                raise SystemExit(f"point {pid}: two {m.group(1)} lines")
            adds[key] = m.group(2)
        elif adds:
            raise SystemExit(f"point {pid}: text after an added line; the Effect, Challenge and Pivot lines must come last")
        else:
            text.append(ln)
    return " ".join(text), adds


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
            body, adds = split_adds(m.group(1), lines[1:])
            cur = {"id": m.group(1), "title": m.group(2), "capsules": caps,
                   "lead": pending, "text": body, "adds": adds}
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


def parse_thread(text):
    """Section M15: {title, opening, closing, chapters: {num: paragraph}}, or None when it is absent."""
    if THREAD_HEAD not in text:
        return None
    section = re.split(r"\n## ", text.split(THREAD_HEAD, 1)[1], maxsplit=1)[0]
    thread = {"title": "", "opening": "", "closing": "", "chapters": {}}
    for block in re.split(r"\n\s*\n", section):
        lines = block.strip().splitlines()
        if not lines:
            continue
        m = THREAD_TITLE_RE.match(lines[0].strip())
        if m:
            thread["title"] = m.group(1).strip()
            continue
        m = THREAD_PART_RE.match(lines[0].strip())
        if not m:
            continue        # the section's note and its Check block are working notes
        body = " ".join(ln.strip() for ln in lines[1:])
        if m.group(1) == "Opening":
            thread["opening"] = body
        elif m.group(1) == "Closing":
            thread["closing"] = body
        else:
            thread["chapters"][int(m.group(2))] = body
    return thread


SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")


def sentences(text):
    """Split a paragraph into its sentences, word for word."""
    parts = [s.strip() for s in SENTENCE_END.split(text.strip()) if s.strip()]
    # guard: splitting must not lose or change a single word
    assert " ".join(parts).split() == text.split(), text[:80]
    return parts


def to_markdown(chapters, thread=None):
    """Slide layout: title, effect line, the transition sentence as a lead line, challenge,
    pivot, then one bullet per sentence."""
    out = ["# The Databricks data and AI story", ""]
    if thread:
        out += [f"**{thread['title']}**", "", thread["opening"], ""]
    for ch in chapters:
        out += [f"## {ch['num']}. {ch['title']}", ""]
        if thread and thread["chapters"].get(ch["num"]):
            out += [thread["chapters"][ch["num"]], ""]
        for p in ch["points"]:
            adds = p.get("adds") or {}
            out += [f"### {p['title']}", ""]
            if adds.get("effect"):
                out += [adds["effect"], ""]
            if p["lead"]:
                out += [f"*{p['lead']}*", ""]
            for k in ("challenge", "pivot"):
                if adds.get(k):
                    out += [adds[k], ""]
            out += [f"- {s}" for s in sentences(p["text"])] + [""]
            if p["capsules"]:
                out += [f"*Capsules: {', '.join(p['capsules'])}*", ""]
        if ch["handoff"]:
            out += [f"*{ch['handoff']}*", ""]
    if thread and thread["closing"]:
        out += ["## Closing", "", thread["closing"], ""]
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


def to_json(chapters, thread=None):
    idx, key = capsule_index()
    unresolved = []
    out = {"chapters": []}
    if thread:
        unknown = set(thread["chapters"]) - {ch["num"] for ch in chapters}
        if unknown:
            raise SystemExit(f"section M15 has paragraphs for unknown chapters: {sorted(unknown)}")
        out = {"thread": {k: thread[k] for k in ("title", "opening", "closing")}, "chapters": []}
    for ch in chapters:
        c = {"num": ch["num"], "title": ch["title"], "handoff": ch["handoff"], "points": []}
        if thread and thread["chapters"].get(ch["num"]):
            c["intro"] = thread["chapters"][ch["num"]]
        for p in ch["points"]:
            refs = []
            for label in p["capsules"]:
                hits = idx.get(key(label), [])
                if not hits:
                    unresolved.append((p["id"], label))
                refs += hits
            adds = p.get("adds") or {}
            c["points"].append({"id": p["id"], "title": p["title"], "lead": p["lead"],
                                **{k: adds[k] for k in ADDS if adds.get(k)},
                                "bullets": sentences(p["text"]), "refs": refs})
        out["chapters"].append(c)
    if unresolved:
        raise SystemExit("unresolved capsule labels: " + ", ".join(f"{i} '{lbl}'" for i, lbl in unresolved))
    return out


if __name__ == "__main__":
    text = DRAFT.read_text(encoding="utf-8")
    chapters, thread = parse(text), parse_thread(text)
    OUT_MD.write_text(to_markdown(chapters, thread), encoding="utf-8")
    data = to_json(chapters, thread)
    OUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    n_points = sum(len(c["points"]) for c in chapters)
    n_refs = sum(len(p["refs"]) for c in data["chapters"] for p in c["points"])
    print(f"wrote {OUT_MD.relative_to(ROOT)} and {OUT_JSON.relative_to(ROOT)}: "
          f"{len(chapters)} chapters, {n_points} points, {n_refs} capsule references")
