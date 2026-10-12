#!/usr/bin/env python3
"""Cross-chapter check: the same deck slide or the same image file used by two candidates."""
import json, pathlib, hashlib, collections, re
ROOT = pathlib.Path(__file__).resolve().parents[2]; IMG = ROOT / "app/static/img"
slides, hashes = collections.defaultdict(list), collections.defaultdict(list)
cands = {}
for f in sorted((ROOT / ".swarm/illus-hunt").glob("cands-ch*.json")):
    for pid, cs in json.load(open(f)).items():
        for x in cs: cands[x["file"]] = (pid, x)
cands.update({c["file"]: (pid, c) for pid, cs in json.load(open(ROOT / "app/src/illustrations.json")).items() for c in cs})
for file, (pid, x) in cands.items():
    m = re.search(r"/presentation/d/([\w-]+)/edit#slide=id\.([\w.-]+)", x.get("url", ""))
    if m: slides[m.groups()].append(f"{pid} {file}")
    if (IMG / file).is_file(): hashes[hashlib.md5((IMG / file).read_bytes()).hexdigest()].append(f"{pid} {file}")
dup = [("same slide url", v) for v in slides.values() if len(v) > 1] + [("identical file", v) for v in hashes.values() if len(v) > 1]
print(f"{len(cands)} candidates;", "duplicates:" if dup else "no duplicate", *dup, sep="\n  ")
