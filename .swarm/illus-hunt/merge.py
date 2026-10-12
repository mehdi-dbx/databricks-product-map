#!/usr/bin/env python3
"""Merge the judges' final selections (final-ch*.json) into app/src/illustrations.json.

- keeps the first test candidates (seeds) already validated
- one image file per point: an image used by several points is kept in the first point only
- each file must be a real image of at least 600 px; wider than 1800 px is shrunk in place
- deck candidates: the URL is rebuilt from the deck title and slide number (deck-index.jsonl), and
  the image must be byte-identical to a fresh thumbnail of that slide, else it is reported
- image files in app/static/img/ that no point lists are moved to .swarm/illus-hunt/rejected/
  usage: merge.py [--write]
"""
import json, pathlib, re, sys, hashlib, subprocess, shutil
RUN = pathlib.Path(__file__).resolve().parent; ROOT = RUN.parents[1]; IMG = ROOT / "app/static/img"
CACHE = RUN / "dl-verify"
SEEDS = {"3.1": ["ds-lifecycle-slide14"], "6.2": ["mlflow-eval-hero", "mlflow-eval-1", "mlflow-eval-custom-judge"], "6.3": ["mlflow-eval-feedback"]}
index = [json.loads(l) for l in open(RUN / "deck-index.jsonl") if '"error"' not in l]
norm = lambda s: re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
decks = {}
for r in index: decks.setdefault(norm(r["deck"]), r["deck_id"])
slide_oid = {(r["deck_id"], r["slide"]): r["object_id"] for r in index}
md5 = lambda f: hashlib.md5(f.read_bytes()).hexdigest()

def deck_of(source):
    m = re.match(r"(.+?),?\s+slides?\s+(\d+)\b", source)
    if not m: return None
    t, n = norm(m.group(1)), int(m.group(2))
    hits = {d for k, d in decks.items() if k == t} or {d for k, d in decks.items() if t in k or k in t}
    return (hits.pop(), n) if len(hits) == 1 else ("?", n)

def width(f):
    out = subprocess.run(["sips", "-g", "pixelWidth", str(f)], capture_output=True, text=True).stdout.split()
    return int(out[-1]) if out and out[-1].isdigit() else 0

old = json.load(open(ROOT / "app/src/illustrations.json"))
seeds = {p: [c for c in old.get(p, []) if c["id"] in ids] for p, ids in SEEDS.items()}
out, report, seen = {}, [], {}
for p, cs in seeds.items():
    for c in cs: seen[md5(IMG / c["file"])] = p
    out[p] = list(cs)
key = lambda p: tuple(int(i) for i in p.split("."))
DROPS = [l.split("\t")[0] for l in open(RUN / "drops.txt") if l.strip() and not l.startswith("#")]
finals = {}
for f in sorted(RUN.glob("final-ch*.json")) + sorted(RUN.glob("gap-*.json")):
    for p, cs in json.load(open(f)).items():
        if re.fullmatch(r"\d+\.\d+", p): finals.setdefault(p, []).extend(cs)
for p in sorted(finals, key=key):
    for x in finals[p]:
        f = IMG / str(x.get("file"))
        if any(str(x.get("file")).startswith(d) for d in DROPS): continue
        if not f.is_file(): report.append(f"{p} {x.get('file')}: file missing — dropped"); continue
        w = width(f)
        if w < 600: report.append(f"{p} {f.name}: " + ("not an image" if not w else f"{w}px") + " — dropped"); continue
        h = md5(f)
        if h in seen: report.append(f"{p} {f.name}: same image as in {seen[h]} — dropped"); continue
        if w > 1800: subprocess.run(["sips", "-Z", "1800", str(f)], capture_output=True); h = md5(f)
        seen[h] = p
        c = {k: x[k] for k in ("id", "file", "source", "url", "kind", "why") if x.get(k)}
        c["id"] = f.stem
        d = deck_of(x.get("source", "")) if " slide" in x.get("source", "") else None
        if d:
            did, n = d
            if did == "?" or (did, n) not in slide_oid:
                report.append(f"{p} {f.name}: deck slide not resolved for '{x.get('source')}'")
            else:
                c["url"] = f"https://docs.google.com/presentation/d/{did}/edit#slide=id.{slide_oid[(did, n)]}"
                t = CACHE / f"{did}-{n}.png"
                if not t.exists():
                    subprocess.run(["python3", str(RUN / "gslides.py"), "thumb", did, str(n), str(t)], capture_output=True)
                if t.exists() and md5(t) != h:
                    report.append(f"{p} {f.name}: not the slide it names ({x.get('source')})")
        out.setdefault(p, []).append(c)
out = {p: out[p] for p in sorted(out, key=key)}
listed = {c["file"] for cs in out.values() for c in cs}
orphans = [f for f in IMG.iterdir() if f.is_file() and f.name not in listed]
counts = {p: len(v) for p, v in out.items()}
print(sum(counts.values()), "candidates on", len(out), "points"); print(counts)
print("below 4:", {p: n for p, n in counts.items() if n < 4})
print(len(orphans), "unlisted image files"); print(*report, sep="\n")
json.dump(out, open(RUN / "preview.json", "w"), indent=1, ensure_ascii=False)
if "--write" in sys.argv:
    (ROOT / "app/src/illustrations.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    rej = RUN / "rejected"; rej.mkdir(exist_ok=True)
    for f in orphans: shutil.move(str(f), rej / f.name)
    print("wrote app/src/illustrations.json; moved unlisted files to .swarm/illus-hunt/rejected/")
