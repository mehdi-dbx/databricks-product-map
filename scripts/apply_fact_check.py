#!/usr/bin/env python3
"""Apply a fact-check report (wrong / outdated items) to the content sources.

  python3 scripts/apply_fact_check.py docs/fable-fact-check-results.json

The report is cumulative (one batch after another) and the script can be re-run on it:
an item whose correction is already in place is counted as already applied.

- Tree items (ai-tree.json, ds-tree.json) are matched by exact node path. A path step
  renamed by an item of the report (field "n") is also found under its new name. The
  field value must equal the item's `current` (or already equal the correction),
  otherwise the item is reported and skipped.
- Tree fields: plain node fields, solves[i].problem|solution, docs[i], and docs (the
  element equal to `current`).
- Story items are applied to app/src/story.json, the only source of the Story's text. The
  `current` text must appear exactly once in its sentences. Run scripts/story_check.py afterwards.
- A tree item also updates the slides' sources (`sources` in story.json) that quote the same
  field of the same capsule, so that they still equal the tree.
- OVERRIDES replaces a proposed correction when it conflicts with a content rule.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TREES = {"ai-tree.json": ROOT / "app/src/ai-tree.json", "ds-tree.json": ROOT / "app/src/ds-tree.json"}
STORY = ROOT / "app/src/story.json"

# the app shows no dates; keep the fix (drop "announced") without adding one
OVERRIDES = {
    "Version 3.0, announced, covers 97 risks and 73 controls, including 35 risks specific to agents.":
        "Version 3.0 covers 97 risks and 73 controls, including 35 risks specific to agents.",
}


def fix_of(x):
    return OVERRIDES.get(x["current"], x["correct"])


def find(root, path, renames):
    if root.get("n") != path[0]:
        return None
    n = root
    for k in range(1, len(path)):
        kids = n.get("children", [])
        n = next((c for c in kids if c.get("n") == path[k]), None)
        if n is None and tuple(path[:k + 1]) in renames:      # renamed by an item already applied
            n = next((c for c in kids if c.get("n") == renames[tuple(path[:k + 1])]), None)
        if n is None:
            return None
    return n


def slot(node, field, current, new):
    """The (container, key) holding a report field, or None."""
    m = re.fullmatch(r"solves\[(\d+)\]\.(problem|solution)", field)
    if m:
        rows, i = node.get("solves", []), int(m.group(1))
        return (rows[i], m.group(2)) if i < len(rows) else None
    m = re.fullmatch(r"docs\[(\d+)\]", field)
    if m:
        docs, i = node.get("docs", []), int(m.group(1))
        return (docs, i) if i < len(docs) else None
    if field == "docs":
        docs = node.get("docs", [])
        hit = next((v for v in (current, new) if v in docs), None)
        return (docs, docs.index(hit)) if hit is not None else None
    return node, field


def update(node, field, current, new):
    """Move one field from `current` to `new`. Returns "applied", "already" or an error string."""
    where = slot(node, field, current, new)
    if where is None:
        return f"no {field} on this node"
    box, key = where
    have = box.get(key) if isinstance(box, dict) else box[key]
    if have == new:
        return "already"
    if have != current:
        return f"value is {have!r}"
    box[key] = new
    return "applied"


def sentences(obj):
    """Every (container, key) of the Story that holds a sentence: titles, effects, bullets…
    The sources are tree fields, not sentences: sync_sources() updates them. The features are the
    plan's labels (docs/feature-tree.md), which change only in the plan."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str) and k not in ("id", "tree"):
                yield obj, k
            elif k not in ("refs", "sources", "features"):
                yield from sentences(v)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            if isinstance(v, str):
                yield obj, i
            else:
                yield from sentences(v)


def count(story, text):
    return sum(box[k].count(text) for box, k in sentences(story))


def sync_sources(story, x, new):
    """Give the new value of a tree field to every source that quotes it. Returns how many."""
    tree, n = x["file"].split("-")[0], 0
    for c in story["chapters"]:
        for p in c["points"]:
            for key in ("effect", "challenge", "pivot"):
                for s in p.get("sources", {}).get(key, []):
                    r = p["refs"][s["ref"]] if 0 <= s["ref"] < len(p["refs"]) else None
                    if (r and r["tree"] == tree and r["path"] == x["path"] and s["field"] == x["field"]
                            and s["text"] == x["current"]):
                        s["text"] = new
                        n += 1
    return n


def main(report_path):
    items = [x for x in json.loads(pathlib.Path(report_path).read_text(encoding="utf-8"))
             if x["verdict"] in ("wrong", "outdated") and x.get("correct", "").strip()]
    trees = {k: json.loads(v.read_text(encoding="utf-8")) for k, v in TREES.items()}
    story = json.loads(STORY.read_text(encoding="utf-8"))
    renames = {k: {} for k in TREES}
    for x in items:
        if x["file"] in trees and x["field"] == "n":
            renames[x["file"]][tuple(x["path"])] = fix_of(x)
    applied, already, skipped = [], [], []

    # resolve every tree target first, so a rename does not break a later item's path
    targets = [(x, find(trees[x["file"]], x["path"], renames[x["file"]])) for x in items if x["file"] in trees]
    for x, node in targets:
        status = update(node, x["field"], x["current"], fix_of(x)) if node is not None else "node not found"
        if status == "applied":
            applied.append(x)
            sync_sources(story, x, fix_of(x))
        elif status == "already":
            already.append(x)
        else:
            skipped.append((x, status))

    for x in (i for i in items if i["file"] == "story.json"):
        new = fix_of(x)
        if count(story, new) == 1 and count(story, x["current"]) == 0:
            already.append(x)
            continue
        hits = count(story, x["current"])
        if hits != 1:
            skipped.append((x, f"found {hits} times in story.json"))
            continue
        for box, k in sentences(story):
            box[k] = box[k].replace(x["current"], new)
        applied.append(x)

    for k, v in TREES.items():
        v.write_text(json.dumps(trees[k], ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    STORY.write_text(json.dumps(story, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"{len(items)} corrections: applied {len(applied)}, already applied {len(already)}, skipped {len(skipped)}")
    for x in applied:
        where = " / ".join(x.get("path", [])[-2:]) or f"story {x['story']['point']}"
        print(f"  ok   {x['file']:13} {where} [{x['field']}]")
    for x, why in skipped:
        print(f"  SKIP {x['file']:13} {' / '.join(x.get('path', []))} [{x['field']}]: {why}")
    return 1 if skipped else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
