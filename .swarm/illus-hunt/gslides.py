#!/usr/bin/env python3
"""Google Slides helpers for the illustration hunt.

  python3 gslides.py index  > deck-index.jsonl     text of every slide of every deck in docs/internal-decks.md
  python3 gslides.py thumb <deck_id> <slide_no> <out.png>   download one slide as a 1600 px PNG
"""
import json, re, subprocess, sys, urllib.request, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
QUOTA = "gcp-dev-field-eng-aiapiquota"
# copies replaced by their original (see the Deprecated section of internal-decks.md)
SKIP = {"1Hkh7g4iiNK4kQ41WHLC59TJxi_BP37DgvuL_ZnYMS8A", "15kie8V3Nv-Ekm81ernaHwD_MQCGrohTjsMx3RyW4GLA"}


def get(url, raw=False):
    tok = subprocess.check_output(["gcloud", "auth", "application-default", "print-access-token"], text=True).strip()
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {tok}", "x-goog-user-project": QUOTA})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    return data if raw else json.loads(data)


def decks():
    """(deck title, id, deprecated?) for each Google Slides link in internal-decks.md."""
    out, seen, deprecated = [], set(), False
    for line in (ROOT / "docs/internal-decks.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("## Deprecated"):
            deprecated = True
        for title, did in re.findall(r"\[([^\]]+(?:\][^\]]*)?)\]\(https://docs\.google\.com/presentation/d/([\w-]+)", line):
            if did not in seen and did not in SKIP:
                seen.add(did)
                out.append((title, did, deprecated))
    return out


def texts(el):
    """All text in a page element, including groups and tables."""
    if "shape" in el:
        for te in el["shape"].get("text", {}).get("textElements", []):
            if "textRun" in te:
                yield te["textRun"]["content"]
    for c in el.get("elementGroup", {}).get("children", []):
        yield from texts(c)
    for row in el.get("table", {}).get("tableRows", []):
        for cell in row.get("tableCells", []):
            for te in cell.get("text", {}).get("textElements", []):
                if "textRun" in te:
                    yield te["textRun"]["content"]


def index():
    for title, did, dep in decks():
        try:
            p = get(f"https://slides.googleapis.com/v1/presentations/{did}")
        except Exception as e:
            print(json.dumps({"deck": title, "deck_id": did, "error": str(e)}), flush=True)
            continue
        for i, s in enumerate(p.get("slides", []), 1):
            t = " ".join(" ".join(" ".join(texts(el)) for el in s.get("pageElements", [])).split())
            n_img = sum(1 for el in s.get("pageElements", []) if "image" in el)
            print(json.dumps({"deck": p.get("title", title), "deck_id": did, "deprecated": dep, "slide": i,
                              "object_id": s["objectId"], "images": n_img, "text": t}, ensure_ascii=False), flush=True)


def thumb(did, slide_no, out):
    p = get(f"https://slides.googleapis.com/v1/presentations/{did}?fields=slides(objectId)")
    oid = p["slides"][int(slide_no) - 1]["objectId"]
    t = get(f"https://slides.googleapis.com/v1/presentations/{did}/pages/{oid}/thumbnail?thumbnailProperties.thumbnailSize=LARGE")
    with urllib.request.urlopen(t["contentUrl"], timeout=120) as r:
        pathlib.Path(out).write_bytes(r.read())
    print(out)


if __name__ == "__main__":
    {"index": lambda: index(), "thumb": lambda: thumb(*sys.argv[2:5])}[sys.argv[1]]()
