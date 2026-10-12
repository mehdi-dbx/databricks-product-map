#!/usr/bin/env python3
"""For the short points: every pool image (docs + deck) not already kept anywhere, as small numbered tiles."""
import json, pathlib, hashlib, sys
from PIL import Image, ImageDraw, ImageFont
RUN = pathlib.Path(__file__).resolve().parent; IMG = RUN.parents[1] / "app/static/img"; OUT = RUN / "fill"; OUT.mkdir(exist_ok=True)
md5 = lambda f: hashlib.md5(f.read_bytes()).hexdigest()
prev = json.load(open(RUN / "preview.json"))
used = {md5(IMG / c["file"]) for cs in prev.values() for c in cs if (IMG / c["file"]).exists()}
docs = json.load(open(RUN / "pool-docs.json")); decks = json.load(open(RUN / "pool-decks.json"))
font = ImageFont.load_default(size=15); W, H, C = 400, 225, 4
index = {}
for pid in sys.argv[1:]:
    items = [dict(e, url=e["page"]) for e in docs.get(pid, [])] + [e for e in decks.get(pid, []) if not e.get("deprecated")]
    items = [e for e in items if (RUN / e["file"]).exists() and md5(RUN / e["file"]) not in used]
    seen, uniq = set(), []
    for e in items:
        h = md5(RUN / e["file"])
        if h not in seen: seen.add(h); uniq.append(e)
    index[pid] = uniq
    rows = max(1, -(-len(uniq) // C)); sheet = Image.new("RGB", (W * C, (H + 20) * rows), "white"); d = ImageDraw.Draw(sheet)
    for k, e in enumerate(uniq):
        x, y = (k % C) * W, (k // C) * (H + 20)
        try: im = Image.open(RUN / e["file"]).convert("RGB"); im.thumbnail((W - 6, H - 4)); sheet.paste(im, (x + 3, y + 20))
        except Exception: d.text((x + 10, y + 100), "NOT AN IMAGE", fill="red", font=font)
        d.text((x + 4, y + 2), f"#{k+1} {e['source'][:44]}", fill="#c00", font=font)
    sheet.save(OUT / f"{pid}.png")
json.dump(index, open(OUT / "index.json", "w"), indent=1)
print({p: len(v) for p, v in index.items()})
