#!/usr/bin/env python3
"""Render the Story as a PDF deck, one 16:9 page per slide.

  python3 scripts/story_pdf.py                      # writes AI-and-Data-Science-on-Databricks.pdf, and a copy
                                                    # in app/static that the app serves
  python3 scripts/story_pdf.py --html /tmp/s.html   # also keeps the HTML it prints

Reads app/src/story.json and the two trees (for the capsule cards).

- The deck follows the plan, docs/feature-tree.md: the overview (the platform architecture) first,
  then every chapter, then the appendix.
- Each chapter opens on a dark page: the previous chapter's handoff when there is one, then the
  chapter's title, its intro and the list of its slides. An intro's last bullet that is a question
  is not shown.
- Each slide keeps the app's order: title, effect, transition, challenges, pivot, bullets, cards.
  A capsule present in both trees gets one card.
  The cards keep the name, the status, the note and the doc links, as in the app. They drop "See in
  tree" and the tree tag, which only make sense there.
  Illustrations are left out: they are still candidates.
- A slide without challenges puts its bullets on the left and its cards on the right.
- The closing, when there is one, follows the last chapter.
- The appendix ends the deck: the capability map, every slide of every chapter with its features
  from the plan, over as many pages as APPENDIX_PAGES sets.
- Every page carries the Databricks logo top left and the Amadeus logo top right (assets/logos).
- The fonts are static DM Sans and DM Mono, embedded as TrueType. They are downloaded once from
  google/fonts into ~/.cache/story_pdf.
- Every page is fitted. When a slide's body overflows, its font size goes down step by step. The
  header keeps its size, so titles sit at the same place on every slide. The script fails if a
  page still overflows at the smallest size.
"""
import base64
import html
import json
import re
import shutil
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
STORY = ROOT / "app/src/story.json"
TREES = {k: ROOT / f"app/src/{k}-tree.json" for k in ("ai", "ds")}
OUT = ROOT / "AI-and-Data-Science-on-Databricks.pdf"
APP_COPY = ROOT / "app/static" / OUT.name   # served by the app at /AI-and-Data-Science-on-Databricks.pdf
APPENDIX_PAGES = [(1, 2, 3), (4, 5), (6, 7, 8, 9)]   # the chapters on each page of the appendix
LOGOS = ROOT / "assets/logos"   # databricks.svg (databricks.com header), amadeus.svg (2023 logo)
FONT_DIR = Path.home() / ".cache/story_pdf"
FONT_SRC = "https://github.com/google/fonts/raw/main/ofl/"
VAR_FONTS = {"sans": "dmsans/DMSans%5Bopsz%2Cwght%5D.ttf", "sans-italic": "dmsans/DMSans-Italic%5Bopsz%2Cwght%5D.ttf"}
MONO_FONTS = {400: "dmmono/DMMono-Regular.ttf", 500: "dmmono/DMMono-Medium.ttf"}
# static DM Sans instances: (source, weight, style, optical size). Text weights use the 14 pt design,
# title weights the 36 pt one, as the browser picks for those sizes.
SANS = [("sans", 400, "normal", 14), ("sans", 500, "normal", 14), ("sans", 600, "normal", 14),
        ("sans", 700, "normal", 14), ("sans", 800, "normal", 36), ("sans", 900, "normal", 36),
        ("sans-italic", 400, "italic", 14)]

SLABEL = {"PrivPreview": "PPR"}   # same chip labels as the app (mindmap.js)
MON = (r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|"
       r"Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)")
DATE_RE = re.compile(r"\b" + MON + r"\b|\b20\d\d\b", re.I)
TRAIL_DATE_RE = re.compile(r"\s+(?:through|until|as of)\s+" + MON + r"\b.*$", re.I)
SENT_RE = re.compile(r'(?<=[.!?])\s+(?=[A-Z"“(])')
MIN_BODY_PX = 12.5   # smallest body font size a slide may be fitted down to


def fetch(rel):
    path = FONT_DIR / Path(rel).name.replace("%5B", "[").replace("%5D", "]").replace("%2C", ",")
    if not path.exists():
        FONT_DIR.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(FONT_SRC + rel) as r:
            path.write_bytes(r.read())
    return path


def font_faces():
    """@font-face rules with static fonts as data URIs.

    Chromium embeds a variable font, such as the DM Sans that Google Fonts serves, as Type 3 fonts,
    which some PDF viewers render blurred. Static instances embed as TrueType."""
    from fontTools.ttLib import TTFont
    from fontTools.varLib.instancer import instantiateVariableFont
    rules = []
    for src, wght, style, opsz in SANS:
        out = FONT_DIR / f"DMSans-{style}-{wght}-{opsz}.ttf"
        if not out.exists():
            instantiateVariableFont(TTFont(fetch(VAR_FONTS[src])), {"wght": wght, "opsz": opsz},
                                    updateFontNames=True).save(out)
        rules.append(("DM Sans", wght, style, out))
    rules += [("DM Mono", w, "normal", fetch(rel)) for w, rel in MONO_FONTS.items()]
    return "".join(
        f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};"
        f"src:url(data:font/ttf;base64,{base64.b64encode(f.read_bytes()).decode()}) format('truetype');}}\n"
        for fam, w, st, f in rules)


def esc(s):
    return html.escape(s or "", quote=False)


def md(s):
    """Text with **bold**, as in the app (mdBold)."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", esc(s))


def dn(s):
    """Display name without dates, as in the app."""
    s = re.sub(r"\s*\(([^()]*)\)", lambda m: "" if DATE_RE.search(m.group(1)) else m.group(0), s or "")
    return TRAIL_DATE_RE.sub("", s).strip()


def sentences(t):
    return SENT_RE.split(t) if t else []


def chain(trees, ref):
    n = trees[ref["tree"]]
    if n.get("n") != ref["path"][0]:
        return []
    out = [n]
    for name in ref["path"][1:]:
        n = next((c for c in n.get("children", []) if c.get("n") == name), None)
        if n is None:
            return []
        out.append(n)
    return out


def ul(items, cls):
    return f'<ul class="{cls}">' + "".join(f"<li>{md(x)}</li>" for x in items) + "</ul>" if items else ""


def logo(name, white=False):
    """A logo as a data URI; the white variant goes on the dark pages."""
    svg = (LOGOS / f"{name}.svg").read_text(encoding="utf-8")
    if white:
        svg = svg.replace('fill="#000"', 'fill="#fff"').replace("fill:#000835", "fill:#fff")
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


def doc_label(u):
    """A doc link's label: the last segment of its path, as in the app, cut at a word. Release
    notes keep the last two segments after "release-notes" ("release notes 2026 september")."""
    x = urlparse(u)
    seg = [s for s in x.path.split("/") if s]
    if "release-notes" in seg:
        words = " ".join(["release notes"] + seg[seg.index("release-notes") + 1:][-2:])
    else:
        words = seg[-1] if seg else (x.hostname or "link")
    words = re.sub(r"[-_]", " ", words)
    return words if len(words) <= 32 else words[:32].rsplit(" ", 1)[0] + "…"


def card(trees, ref):
    ch = chain(trees, ref)
    if not ch:
        raise SystemExit(f"capsule not found: {ref}")
    n = ch[-1]
    docs = next((x["docs"] for x in reversed(ch) if x.get("docs")), [])
    labels = {}
    for u in docs:                     # one link per label: "feature-store" and "feature-store/" are one
        labels.setdefault(doc_label(u), u)
    links = "".join(f'<a href="{esc(u)}">↗ {esc(lab)}</a>' for lab, u in labels.items())
    chip = f'<span class="chip s-{esc(n["s"])}">{esc(SLABEL.get(n["s"], n["s"]))}</span>' if n.get("s") else ""
    return (f'<div class="cap"><div class="nm"><span>{esc(dn(n["n"]))}</span>{chip}</div>'
            f'<div class="note">{esc(n.get("note", ""))}</div>'
            + (f'<div class="docs">{links}</div>' if links else "") + "</div>")


def unique_refs(trees, refs):
    """One card per name: a capsule present in both trees (Feature Store, AutoML) shows once."""
    seen, out = set(), []
    for r in refs:
        name = dn(chain(trees, r)[-1]["n"]) if chain(trees, r) else repr(r)
        if name not in seen:
            seen.add(name); out.append(r)
    return out


def flat(features):
    """A feature's children, and theirs, on one line."""
    return " · ".join(f["name"] + (f" ({flat(f['children'])})" if f["children"] else "") for f in features)


def appendix_page(story, nums):
    blocks = []
    for c in story["chapters"]:
        if c["num"] not in nums:
            continue
        pts = "".join(
            f'<div class="ap-pt"><div class="ap-t"><span>{esc(p["id"])}</span>{esc(p["title"])}</div>'
            + ("<ul class=\"ap-f\">" + "".join(
                f'<li>{esc(f["name"])}' + (f'<span class="ap-c">{esc(flat(f["children"]))}</span>' if f["children"] else "")
                + "</li>" for f in p["features"]) + "</ul>" if p["features"] else "")
            + "</div>" for p in c["points"])
        blocks.append(f'<div class="ap-sec"><div class="ap-h"><span class="kn">{c["num"]:02d}</span>{esc(c["title"])}</div>{pts}</div>')
    return f'<div class="head"><h2 class="t">{esc(story["appendix"]["title"][:1].upper() + story["appendix"]["title"][1:])}</h2></div>' \
           f'<div class="main fit"><div class="ap">{"".join(blocks)}</div></div>'


def build(story, trees):
    title = story["thread"]["title"]
    chapters = story["chapters"]
    anchor = {p["id"]: f"s-{p['id']}" for c in chapters for p in c["points"]}
    pages = []

    # overview, the first page
    steps = "".join(
        '<div class="ov-step"><div class="ov-card">'
        f'<div class="ov-h"><span class="ov-n">{i}</span><span class="ov-name">{esc(b["name"])}</span></div>'
        '<div class="ov-tiles">' + "".join(
            f'<a class="tile" href="#{anchor[t["id"]]}">{esc(t["label"])}</a>' for t in b["tiles"]) + "</div></div>"
        + (ul(b["points"], "ov-pts") if b["points"] else "") + "</div>"
        for i, b in enumerate(story["overview"], 1))
    pages.append(("dark cover", "overview", "",
                  f'<div class="kick">Overview</div><h1 class="ct">{esc(title)}</h1>'
                  f'<p class="sub">{esc(story["thread"].get("overview", ""))}</p>'
                  f'<div class="ov-path" style="grid-template-columns:repeat({len(story["overview"])},minmax(0,1fr))">{steps}</div>'))

    # each opener starts with the previous chapter's handoff, when there is one
    question = ""
    for k, c in enumerate(chapters, 1):
        intro = list(c.get("intro") or [])
        if intro and intro[-1].endswith("?"):
            intro.pop()
        toc = "".join(f'<a class="tile" href="#{anchor[p["id"]]}">{esc(p["title"])}</a>' for p in c["points"])
        pages.append(("dark chap", f"chapter {k}", "",
                      f'<div class="kick">Chapter {k:02d}</div>'
                      + (f'<p class="q">{md(question)}</p>' if question else "")
                      + f'<h1 class="dt">{esc(c["title"])}</h1>'
                      f'<div class="cols fit"><div>{ul(intro, "intro")}</div>'
                      f'<div class="toc"><div class="lbl">In this chapter</div>{toc}</div></div>'))
        question = c.get("handoff", "")
        for p in c["points"]:
            chal = sentences(p.get("challenge"))
            sol = (f'<p class="piv">{md(p["pivot"])}</p>' if p.get("pivot") else "") + ul(p["bullets"], "bul")
            cards = "".join(dict.fromkeys(card(trees, r) for r in unique_refs(trees, p["refs"])))
            if chal:
                body = (f'<div class="body"><div class="chal"><div class="lbl">Challenges</div>{ul(chal, "chl")}</div>'
                        f'<div class="sol">{sol}</div></div>')
                caps = f'<div class="caps">{cards}</div>' if cards else ""
            else:
                body = f'<div class="body solo"><div class="sol">{sol}</div><div class="caps side">{cards}</div></div>'
                caps = ""
            pages.append(("slide", p["id"], f'<div class="kick"><span class="kn">{k:02d}</span>{esc(c["title"])}</div>',
                          f'<div class="head"><h2 class="t">{esc(p["title"])}</h2>'
                          + (f'<p class="eff">{md(p["effect"])}</p>' if p.get("effect") else "")
                          + (f'<p class="lead">{md(p["lead"])}</p>' if p.get("lead") else "")
                          + f'</div><div class="main fit">{body}{caps}</div>'))

    closing = story["thread"].get("closing") or []
    if closing:
        pages.append(("dark close", "closing", "",
                      f'<div class="kick">Closing</div><h1 class="dt">{esc(title)}</h1><div class="fit">{ul(closing, "intro two")}</div>'))

    for i, nums in enumerate(APPENDIX_PAGES, 1):
        pages.append(("slide appx", f"appendix {i}", f'<div class="kick">Appendix</div>', appendix_page(story, nums)))
    missing = {c["num"] for c in chapters} - {n for nums in APPENDIX_PAGES for n in nums}
    if missing:
        raise SystemExit(f"APPENDIX_PAGES leaves out chapters {sorted(missing)}")

    total = len(pages)
    out = []
    light = (logo("databricks"), logo("amadeus"))
    dark = (logo("databricks", True), logo("amadeus", True))
    for i, (cls, pid, kick, inner) in enumerate(pages, 1):
        dbx, ama = dark if "dark" in cls else light
        brand = (f'<div class="brand"><img class="lg-dbx" src="{dbx}" alt="Databricks">'
                 + (f'<span class="sep"></span>{kick}' if kick else "")
                 + f'<img class="lg-ama" src="{ama}" alt="Amadeus"></div>')
        foot = "" if i == 1 else f'<div class="foot"><span>{esc(title)}</span><span>{i} / {total}</span></div>'
        sid = f' id="{anchor[pid]}"' if pid in anchor else ""
        out.append(f'<section class="pg {cls}"{sid} data-id="{esc(pid)}">{brand}{inner}{foot}</section>')
    return HEAD.replace("{title}", esc(title)).replace("{fonts}", font_faces()) + "".join(out) + "</body></html>"


HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<style>
{fonts}@page{size:1280px 720px;margin:0;}
*{box-sizing:border-box;margin:0;padding:0;}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{font-family:'DM Sans',sans-serif;color:#1B3139;-webkit-font-smoothing:antialiased;}
a{color:inherit;text-decoration:none;}
b{font-weight:700;}
ul{list-style:none;}
.pg{position:relative;width:1280px;height:720px;overflow:hidden;break-after:page;font-size:16px;}
.pg:last-child{break-after:auto;}
.foot{position:absolute;left:68px;right:64px;bottom:26px;display:flex;justify-content:space-between;
  font-family:'DM Mono',monospace;font-size:10px;letter-spacing:0.14em;text-transform:uppercase;color:#a3b0b5;}
.kick{font-family:'DM Mono',monospace;font-size:11.5px;font-weight:500;letter-spacing:0.16em;text-transform:uppercase;}

/* light slides */
.slide{background:#fff;padding:82px 68px 64px 72px;display:flex;flex-direction:column;}
.slide::before{content:"";position:absolute;left:0;top:0;bottom:0;width:6px;background:#FF3621;}
.brand{position:absolute;top:30px;left:72px;right:64px;display:flex;align-items:center;gap:16px;}
.dark .brand{left:68px;} .cover .brand{left:56px;right:56px;}
.lg-dbx{display:block;height:19px;} .lg-ama{display:block;height:14px;margin-left:auto;}
.brand .sep{width:1px;height:16px;background:#DCE0E2;}
.brand .kick{display:flex;align-items:center;gap:12px;color:#8a9aa1;}
.brand .kick .kn{color:#FF3621;}
.t{font-size:38px;font-weight:800;letter-spacing:-0.012em;line-height:1.1;color:#2272B4;text-wrap:balance;}
.eff{font-size:21px;font-weight:500;line-height:1.35;color:#2272B4;margin-top:9px;text-wrap:pretty;}
.lead{font-size:17px;font-style:italic;line-height:1.45;color:#5A6F77;margin-top:16px;max-width:1040px;text-wrap:pretty;}
.main{flex:1;min-height:0;display:flex;flex-direction:column;margin-top:26px;font-size:17.5px;}
.body{display:grid;grid-template-columns:5fr 7fr;column-gap:40px;align-items:start;}
.body.solo{grid-template-columns:7fr 5fr;column-gap:56px;}
.solo .bul li{font-size:1.18em;}
.solo .bul li+li{margin-top:0.8em;}
.caps.side{margin:0;padding:0;border:0;flex-direction:column;gap:0.85em;}
.caps.side .cap{flex:none;}
.chal{border:1px solid rgba(34,114,180,0.55);border-radius:14px;padding:16px 22px 15px;}
.lbl{font-size:11.5px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#5A6F77;margin-bottom:9px;}
.chl li,.bul li,.intro li,.ov-pts li{position:relative;padding-left:1.15em;text-wrap:pretty;}
.chl li{font-size:0.94em;line-height:1.45;color:#76888F;}
.chl li+li{margin-top:0.45em;}
.chl li::before{content:"";position:absolute;left:0.1em;top:0.62em;width:0.36em;height:0.36em;border-radius:50%;background:#1B3139;opacity:0.6;}
.piv{font-size:1.12em;line-height:1.42;margin-bottom:0.75em;text-wrap:pretty;}
.bul li{font-size:1.02em;line-height:1.45;}
.bul li+li{margin-top:0.55em;}
.bul li::before{content:"";position:absolute;left:0.1em;top:0.6em;width:0.4em;height:0.4em;border-radius:50%;background:#FF3621;opacity:0.65;}
.caps{margin-top:1.7em;padding-top:1.1em;border-top:1px dashed #DCE0E2;display:flex;gap:1em;}
.cap{flex:0 1 calc((100% - 2em)/3);border:1px solid rgba(255,54,33,0.5);border-radius:12px;padding:0.62em 0.9em 0.7em;}
.cap .nm{display:flex;align-items:center;gap:0.5em;font-weight:700;font-size:0.88em;line-height:1.25;}
.chip{flex:none;font-family:'DM Mono',monospace;font-size:0.66em;font-weight:500;letter-spacing:0.05em;text-transform:uppercase;padding:0.12em 0.6em;border-radius:100px;color:#fff;}
.s-GA{background:#1B3139;} .s-PuP{background:#2272B4;} .s-Beta{background:#B06A00;} .s-PrivPreview{background:#8a9aa1;}
.s-Announced{background:#9aa3a7;} .s-Legacy{background:#a05a5a;}
.cap .note{font-size:0.77em;line-height:1.38;color:#5A6F77;margin-top:0.32em;text-wrap:pretty;}
.cap .docs{display:flex;flex-wrap:wrap;gap:0.15em 1.1em;margin-top:0.42em;font-size:0.72em;line-height:1.35;}
.cap .docs a{color:#2272B4;white-space:nowrap;}

/* dark pages: overview, chapter openers, closing */
.dark{background:linear-gradient(135deg,#26404a 0%,#15272e 100%);color:#fff;padding:52px 68px 64px;}
.dark::before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 92% -25%,rgba(255,54,33,0.24),transparent 55%);}
.dark>*:not(.foot):not(.brand){position:relative;}
.dark .kick{color:#FF3621;margin-bottom:14px;}
.dark .foot{color:rgba(255,255,255,0.42);}
.tile{display:block;font-weight:600;line-height:1.22;color:#fff;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.16);border-radius:999px;}
.intro li{color:rgba(255,255,255,0.82);font-size:1.18em;line-height:1.48;}
.intro li+li{margin-top:0.5em;}
.intro li b{color:#fff;}
.intro li::before,.ov-pts li::before{content:"";position:absolute;left:0.05em;top:0.6em;width:0.4em;height:0.4em;border-radius:50%;background:#FF3621;}

.cover{padding:78px 56px 40px;}
.ct{font-size:44px;font-weight:900;letter-spacing:-0.015em;line-height:1.08;margin-bottom:24px;}
.sub{font-size:19px;font-weight:500;color:rgba(255,255,255,0.7);margin:-14px 0 26px;}
.ov-path{display:grid;grid-template-rows:auto auto;column-gap:12px;row-gap:12px;}
.ov-step{display:grid;grid-template-rows:subgrid;grid-row:span 2;min-width:0;}
.ov-card{position:relative;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.13);border-top:3px solid #FF3621;border-radius:12px;padding:11px 8px 11px;}
.ov-step:not(:last-child) .ov-card::after{content:"";position:absolute;right:-10px;top:17px;width:7px;height:7px;border-top:2px solid #FF3621;border-right:2px solid #FF3621;transform:rotate(45deg);}
.ov-h{display:flex;align-items:flex-start;gap:6px;min-height:52px;margin-bottom:8px;}
.ov-n{flex:none;display:inline-flex;align-items:center;justify-content:center;width:21px;height:21px;border-radius:50%;background:#FF3621;font-family:'DM Mono',monospace;font-size:10.5px;font-weight:500;}
.ov-name{font-size:10.5px;font-weight:800;letter-spacing:0.02em;text-transform:uppercase;line-height:1.15;}
.ov-tiles{display:flex;flex-direction:column;gap:4px;}
.ov-tiles .tile{font-size:11px;padding:4px 8px;border-radius:8px;width:100%;}
.ov-pts{display:flex;flex-direction:column;gap:4px;padding:0 3px;}
.ov-pts li{font-size:11.5px;line-height:1.35;color:rgba(255,255,255,0.8);padding-left:1.05em;}
.ov-pts li::before{width:0.45em;height:0.45em;top:0.5em;}

.chap,.close{display:flex;flex-direction:column;justify-content:center;padding-top:84px;padding-bottom:84px;}
.q{font-size:19px;font-style:italic;line-height:1.4;color:rgba(255,255,255,0.62);max-width:900px;margin-bottom:12px;text-wrap:balance;}
.dt{font-size:54px;font-weight:900;letter-spacing:-0.018em;line-height:1.04;text-wrap:balance;}
.cols{display:grid;grid-template-columns:7fr 4fr;column-gap:64px;align-items:start;margin-top:36px;}
.toc{display:flex;flex-direction:column;gap:8px;}
.toc .lbl{color:#FF3621;font-family:'DM Mono',monospace;font-weight:500;letter-spacing:0.16em;margin-bottom:4px;}
.toc .tile{font-size:15px;padding:9px 18px;}
.close .dt{margin-bottom:40px;}
.close .intro li{font-size:1.18em;}
.intro.two{columns:2;column-gap:56px;}
.intro.two li{break-inside:avoid;}

/* appendix: the capability map */
.appx .main{margin-top:20px;font-size:13.25px;}
.ap{columns:4;column-gap:28px;}
.ap-sec{margin-bottom:1.1em;}
.ap-h{break-after:avoid;}
.ap-h{display:flex;align-items:baseline;gap:0.6em;font-weight:800;font-size:1.08em;color:#1B3139;text-transform:uppercase;letter-spacing:0.03em;
  padding-bottom:0.35em;margin-bottom:0.5em;border-bottom:2px solid #FF3621;}
.ap-h .kn{font-family:'DM Mono',monospace;font-weight:500;color:#FF3621;}
.ap-pt{break-inside:avoid;margin-bottom:0.55em;}
.ap-t{font-weight:700;color:#2272B4;line-height:1.3;}
.ap-t span{font-family:'DM Mono',monospace;font-weight:500;font-size:0.86em;color:#8a9aa1;margin-right:0.5em;}
.ap-f li{position:relative;padding-left:0.95em;line-height:1.35;color:#1B3139;margin-top:0.12em;}
.ap-f li::before{content:"";position:absolute;left:0.1em;top:0.58em;width:0.3em;height:0.3em;border-radius:50%;background:#FF3621;opacity:0.65;}
.ap-c{display:block;font-size:0.9em;color:#76888F;line-height:1.35;}
</style></head><body>"""

FIT_JS = """(minPx) => {
  const out = [];
  for (const pg of document.querySelectorAll('.pg')) {
    const fit = pg.querySelector('.fit'), box = pg.getBoundingClientRect();
    const limit = box.bottom - 52;   // the footer zone
    const over = () => [...pg.querySelectorAll('li,p,h1,h2,.cap,.tile,.chal,.ov-card,.lbl')].some(e => {
      const r = e.getBoundingClientRect();
      return r.bottom > limit + 0.5 || r.top < box.top - 0.5 || r.right > box.right - 30 + 0.5; });
    const start = fit ? parseFloat(getComputedStyle(fit).fontSize) : 16;
    let px = start;
    while (fit && over() && px > minPx) { px -= 0.25; fit.style.fontSize = px + 'px'; }
    out.push({id: pg.dataset.id, px, start, over: over()});
  }
  return out;
}"""


def main(argv):
    keep_html = argv[argv.index("--html") + 1] if "--html" in argv else None
    story = json.loads(STORY.read_text(encoding="utf-8"))
    trees = {k: json.loads(v.read_text(encoding="utf-8")) for k, v in TREES.items()}
    doc = build(story, trees)
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        page.set_content(doc, wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        if not page.evaluate("document.fonts.check('16px \"DM Sans\"') && document.fonts.check('12px \"DM Mono\"')"):
            raise SystemExit("the DM Sans and DM Mono fonts did not load")
        fits = page.evaluate(FIT_JS, MIN_BODY_PX)
        if keep_html:
            Path(keep_html).write_text(page.content(), encoding="utf-8")
        page.pdf(path=str(OUT), width="1280px", height="720px", print_background=True, prefer_css_page_size=True)
        browser.close()
    shutil.copyfile(OUT, APP_COPY)
    bad = [f["id"] for f in fits if f["over"]]
    fitted = [f"{f['id']} ({f['start']:g} → {f['px']:g}px)" for f in fits if f["px"] < f["start"] and not f["over"]]
    print(f"wrote {OUT.relative_to(ROOT)}: {len(fits)} pages")
    print("fitted down:", ", ".join(fitted) or "none")
    if bad:
        raise SystemExit(f"still overflowing at {MIN_BODY_PX}px: {', '.join(bad)}")


if __name__ == "__main__":
    main(sys.argv[1:])
