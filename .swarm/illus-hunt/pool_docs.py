#!/usr/bin/env python3
"""Download the images of the docs pages picked for each point (docs-pages.json) into pool/."""
import json, re, pathlib, hashlib, subprocess, urllib.request, concurrent.futures as cf
RUN = pathlib.Path(__file__).resolve().parent
POOL = RUN / "pool"; CACHE = RUN / "dl-docs"; POOL.mkdir(exist_ok=True); CACHE.mkdir(exist_ok=True)
SKIP = ("archive/", "error-messages/", "sql/language-manual", "release-notes", "dev-tools/cli/reference")
picks = {p: [x for x in v if not x.startswith(SKIP)][:12] for p, v in json.load(open(RUN / "docs-pages.json")).items()}

def fetch(url, dest):
    if not dest.exists():
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r: dest.write_bytes(r.read())
    return dest

def page_images(path):
    try:
        html = fetch(f"https://docs.databricks.com/aws/en/{path}", CACHE / (hashlib.md5(path.encode()).hexdigest() + ".html")).read_text(errors="ignore")
    except Exception: return []
    return list(dict.fromkeys(re.findall(r"/aws/en/assets/images/[^\"' >]+\.(?:png|jpg|jpeg|gif|webp|svg)", html)))

def width(f):
    out = subprocess.run(["sips", "-g", "pixelWidth", str(f)], capture_output=True, text=True).stdout.split()
    return int(out[-1]) if out and out[-1].isdigit() else 0

def get_img(rel):
    dest = CACHE / pathlib.Path(rel).name
    try: return fetch("https://docs.databricks.com" + rel, dest)
    except Exception: return None

pool = {}
with cf.ThreadPoolExecutor(8) as ex:
    pages = {pg for v in picks.values() for pg in v}
    imgs_of = dict(zip(pages, ex.map(page_images, pages)))
    rels = {r for v in imgs_of.values() for r in v}
    files = dict(zip(rels, ex.map(get_img, rels)))
for pid, pgs in picks.items():
    seen, out = set(), []
    for pg in pgs:
        for rel in imgs_of[pg]:
            f = files.get(rel)
            if not f or f.suffix == ".svg" or width(f) < 600: continue
            h = hashlib.md5(f.read_bytes()).hexdigest()
            if h in seen: continue
            seen.add(h); out.append({"file": str(f.relative_to(RUN)), "page": f"https://docs.databricks.com/aws/en/{pg}", "source": f"docs.databricks.com/{pg}"})
    pool[pid] = out
json.dump(pool, open(RUN / "pool-docs.json", "w"), indent=1)
print({p: len(v) for p, v in pool.items()}); print(sum(len(v) for v in pool.values()), "docs images")
