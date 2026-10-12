#!/usr/bin/env python3
"""Check a chapter's candidates: files, sizes, duplicates, fields, orphans.  usage: verify.py <ch number>"""
import json, pathlib, subprocess, sys, hashlib, collections
ROOT = pathlib.Path(__file__).resolve().parents[2]; IMG = ROOT / "app/static/img"
ch = int(sys.argv[1]); c = json.load(open(ROOT / f".swarm/illus-hunt/cands-ch{ch:02d}.json"))
story = json.load(open(ROOT / "app/src/story.json"))
points = [p["id"] for x in story["chapters"] if x["num"] == ch for p in x["points"]]
listed, hashes, srcs, bad = set(), collections.defaultdict(list), collections.Counter(), []
for pid in points:
    cs = c.get(pid, []); print(f"{pid}: {len(cs)} candidates")
    for x in cs:
        miss = [k for k in ("id", "file", "source", "url", "kind", "why") if not x.get(k)]
        f = IMG / x.get("file", "?"); listed.add(f.name)
        if miss: bad.append(f"{pid} {x.get('file')}: missing {miss}")
        if not f.is_file(): bad.append(f"{pid} {x.get('file')}: file missing"); continue
        out = subprocess.run(["sips", "-g", "pixelWidth", str(f)], capture_output=True, text=True).stdout.split()
        w = int(out[-1]) if out and out[-1].isdigit() else 0
        if w < 600: bad.append(f"{pid} {f.name}: " + (f"only {w}px wide" if w else "not an image"))
        hashes[hashlib.md5(f.read_bytes()).hexdigest()].append(f.name); srcs[x["source"]] += 1
        print(f"   {f.name:52} {w:5}px  {x['kind']:10} {x['source'][:58]}")
extra = set(c) - set(points)
if extra: bad.append(f"points outside the chapter: {sorted(extra)}")
bad += [f"identical files: {v}" for v in hashes.values() if len(v) > 1]
bad += [f"same deck slide twice: {s}" for s, n in srcs.items() if n > 1 and "slide" in s]
orph = [f.name for f in IMG.glob(f"p{ch}.*") if f.name not in listed]
if orph: bad.append(f"orphan files in img/: {orph}")
print("PROBLEMS:" if bad else "OK", *bad, sep="\n  ")
