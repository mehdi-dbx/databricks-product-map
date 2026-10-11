#!/usr/bin/env python3
"""Traverse the ecosystem trees and yield every node with its location.

Each item: {"tree", "path", "depth", "node"} where `path` is the list of names
from the root to the node. The path is how other scripts target a node.

Usage:
  python3 scripts/tree_walk.py            # print a count per tree and depth
"""
import json
import pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
TREES = {"ai-tree.json": ROOT / "app/src/ai-tree.json", "ds-tree.json": ROOT / "app/src/ds-tree.json"}


def load(tree_name):
    return json.loads(TREES[tree_name].read_text(encoding="utf-8"))


def save(tree_name, data):
    TREES[tree_name].write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def iter_nodes(tree_name, data=None):
    """Yield every node of one tree, depth-first, root included (depth 0)."""
    data = data if data is not None else load(tree_name)

    def walk(n, depth, path):
        p = path + [n.get("n", "?")]
        yield {"tree": tree_name, "path": p, "depth": depth, "node": n}
        for c in n.get("children", []):
            yield from walk(c, depth + 1, p)

    yield from walk(data, 0, [])


def iter_all():
    for name in TREES:
        yield from iter_nodes(name)


if __name__ == "__main__":
    for name in TREES:
        c = Counter(x["depth"] for x in iter_nodes(name))
        print(name, dict(sorted(c.items())), "total", sum(c.values()))
