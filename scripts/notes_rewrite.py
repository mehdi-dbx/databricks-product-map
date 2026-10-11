#!/usr/bin/env python3
"""Apply rewritten notes back onto the trees, matched by exact node path.

  merge DIR   apply every out-*.json in DIR ({tree, path, note} objects)

Paths are root → node names (see tree_walk.py).
"""
import glob
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from tree_walk import TREES, iter_nodes, load, save  # noqa: E402


def merge(run_dir):
    patches = {}
    for f in sorted(glob.glob(str(pathlib.Path(run_dir) / "out-*.json"))):
        for r in json.loads(pathlib.Path(f).read_text(encoding="utf-8")):
            patches[(r["tree"], tuple(r["path"]))] = r["note"]
    applied = set()
    for name in TREES:
        data = load(name)
        for x in iter_nodes(name, data):
            key = (name, tuple(x["path"]))
            if key in patches:
                x["node"]["note"] = patches[key]
                applied.add(key)
        save(name, data)
    unmatched = set(patches) - applied
    print(f"merged {len(applied)}/{len(patches)} notes | unmatched {len(unmatched)}")
    for u in sorted(unmatched):
        print("  UNMATCHED", u[0], " / ".join(u[1]))
    return 1 if unmatched else 0


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "merge":
        sys.exit(merge(sys.argv[2]))
    print(__doc__)
    sys.exit(2)
