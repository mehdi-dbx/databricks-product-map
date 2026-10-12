#!/usr/bin/env python3
"""One small QA sheet per point from preview.json: the final candidates, numbered, with their file name."""
import json, pathlib
from PIL import Image, ImageDraw, ImageFont
RUN = pathlib.Path(__file__).resolve().parent; IMG = RUN.parents[1] / "app/static/img"; OUT = RUN / "qa"; OUT.mkdir(exist_ok=True)
font = ImageFont.load_default(size=15); W, H, C = 400, 225, 3
for pid, cs in json.load(open(RUN / "preview.json")).items():
    rows = -(-len(cs) // C); sheet = Image.new("RGB", (W * C, (H + 22) * rows), "white"); d = ImageDraw.Draw(sheet)
    for k, c in enumerate(cs):
        x, y = (k % C) * W, (k // C) * (H + 22)
        try:
            im = Image.open(IMG / c["file"]).convert("RGB"); im.thumbnail((W - 6, H - 4)); sheet.paste(im, (x + 3, y + 22))
        except Exception: d.text((x + 10, y + 100), "NOT AN IMAGE", fill="red", font=font)
        d.text((x + 4, y + 3), f"#{k+1} {c['file'][:46]}", fill="#c00", font=font)
    sheet.save(OUT / f"{pid}.png")
print("qa sheets:", len(list(OUT.glob('*.png'))))
