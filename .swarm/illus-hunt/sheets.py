#!/usr/bin/env python3
"""Contact sheets: for each point, every pool image and current candidate as numbered tiles, 9 per sheet.

  python3 sheets.py            writes sheets/<point>-<n>.png and sheets/index.json (tile number -> image)
"""
import json, pathlib, re
from PIL import Image, ImageDraw, ImageFont
RUN = pathlib.Path(__file__).resolve().parent; ROOT = RUN.parents[1]; OUT = RUN / "sheets"; OUT.mkdir(exist_ok=True)
docs = json.load(open(RUN / "pool-docs.json")); decks = json.load(open(RUN / "pool-decks.json"))
cands = {}
for f in RUN.glob("cands-ch*.json"):
    for pid, cs in json.load(open(f)).items():
        if re.fullmatch(r"\d+\.\d+", pid): cands.setdefault(pid, []).extend(cs)
W, H, COLS = 600, 340, 3
font = ImageFont.load_default(size=22)
index = {}
for pid in sorted(set(docs) | set(decks) | set(cands), key=lambda p: tuple(map(int, p.split(".")))):
    items, seen = [], set()
    for c in (c for c in cands.get(pid, []) if c.get("file")):
        items.append({"path": str(ROOT / "app/static/img" / c["file"]), "from": "candidate", "file": c["file"], "source": c["source"], "url": c.get("url", "")})
    for e in docs.get(pid, []):
        items.append({"path": str(RUN / e["file"]), "from": "docs", "file": e["file"], "source": e["source"], "url": e["page"]})
    for e in decks.get(pid, []):
        items.append({"path": str(RUN / e["file"]), "from": "deck", "file": e["file"], "source": e["source"], "url": e["url"], "deprecated": e.get("deprecated")})
    items = [i for i in items if not (i["path"] in seen or seen.add(i["path"]))]
    index[pid] = []
    for s in range(0, len(items), 9):
        sheet = Image.new("RGB", (W * COLS, (H + 34) * 3), "white"); d = ImageDraw.Draw(sheet)
        for k, it in enumerate(items[s:s + 9]):
            n = s + k + 1; x, y = (k % COLS) * W, (k // COLS) * (H + 34)
            try:
                im = Image.open(it["path"]).convert("RGB"); im.thumbnail((W - 10, H - 6))
                sheet.paste(im, (x + 5, y + 34))
            except Exception:
                d.text((x + 20, y + 120), "NOT AN IMAGE", fill="red", font=font)
            d.rectangle([x + 2, y + 2, x + W - 2, y + H + 32], outline="#999")
            d.text((x + 8, y + 6), f"#{n} {it['from']}" + (" (deprecated deck)" if it.get("deprecated") else ""), fill="#c00", font=font)
            index[pid].append({"n": n, **it})
        sheet.save(OUT / f"{pid}-{s // 9 + 1}.png")
json.dump(index, open(OUT / "index.json", "w"), indent=1)
print({p: len(v) for p, v in index.items()})
