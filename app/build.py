#!/usr/bin/env python3
"""Build the self-contained AI Ecosystem Tree HTML from the parts in src/.

Single source of truth lives in src/:
  - ai-tree.json   the data (the only file to edit to change the tree)
  - styles.css     all CSS
  - mindmap.js     layout + render + interactions (uses the global DATA)
  - template.html  shell with {{STYLES}} and {{SCRIPT}} placeholders

Edit those, then run:  python3 build.py

Outputs (both GENERATED — do not edit by hand):
  - static/index.html         served by the Databricks App (app.py)
  - ../ai-tree-mindmap.html   open directly in a browser (file://)
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "src"

ai_text = (SRC / "ai-tree.json").read_text(encoding="utf-8").strip()
ds_text = (SRC / "ds-tree.json").read_text(encoding="utf-8").strip()
ai_data = json.loads(ai_text)  # fail fast if not valid JSON
ds_data = json.loads(ds_text)

# ---- schema gate: every d2+ node MUST carry a valid `type` (deterministic, not doc-only) ----
VALID_TYPES = {"feature", "family", "primitive", "concept"}


def validate_types(root, tree_name):
    bad = []

    def walk(n, depth, path):
        p = path + [n.get("n", "?")]
        if depth >= 2:
            t = n.get("type")
            if t not in VALID_TYPES:
                bad.append((" / ".join(p), t))
        for c in n.get("children", []):
            walk(c, depth + 1, p)

    walk(root, 0, [])
    if bad:
        lines = "\n".join(f"  - {path}  (type={t!r})" for path, t in bad[:40])
        more = "" if len(bad) <= 40 else f"\n  … and {len(bad) - 40} more"
        raise SystemExit(
            f"BUILD FAILED — {len(bad)} node(s) in {tree_name} missing a valid `type` "
            f"(must be one of {sorted(VALID_TYPES)}):\n{lines}{more}\n"
            f"See docs/panel-slide-spec.md — every d2+ node must be classified at population time."
        )


validate_types(ai_data, "ai-tree.json")
validate_types(ds_data, "ds-tree.json")

# ---- story: every capsule the Story cites must exist in the trees ----
story_text = (SRC / "story.json").read_text(encoding="utf-8").strip()
story_data = json.loads(story_text)


def tree_paths(root):
    paths = set()

    def walk(n, path):
        p = path + (n.get("n", "?"),)
        paths.add(p)
        for c in n.get("children", []):
            walk(c, p)

    walk(root, ())
    return paths


known = {"ai": tree_paths(ai_data), "ds": tree_paths(ds_data)}
missing = [(p["id"], " / ".join(r["path"]))
           for ch in story_data["chapters"] for p in ch["points"] for r in p["refs"]
           if tuple(r["path"]) not in known.get(r["tree"], set())]
if missing:
    lines = "\n".join(f"  - point {i}: {path}" for i, path in missing)
    raise SystemExit(f"BUILD FAILED — {len(missing)} Story reference(s) point to no tree node:\n{lines}\n"
                     f"Regenerate with: python3 scripts/story_extract.py")

# ---- decks tab: docs/internal-decks.md rendered to HTML at build time ----
import html as _html  # noqa: E402
import re as _re  # noqa: E402


def _inline(text):
    """Escape, then apply links [text](url), **bold**, *italic* and `code`."""
    out, i = [], 0
    while i < len(text):
        j = text.find("](", i)
        if j < 0:
            out.append(_html.escape(text[i:]))
            break
        depth, k = 0, j - 1                # the link text may itself contain [brackets]
        while k >= i:
            if text[k] == "]":
                depth += 1
            elif text[k] == "[":
                if depth == 0:
                    break
                depth -= 1
            k -= 1
        end = text.find(")", j + 2)
        if k < i or end < 0:
            out.append(_html.escape(text[i:j + 2]))
            i = j + 2
            continue
        out.append(_html.escape(text[i:k]))
        label, url = text[k + 1:j], text[j + 2:end]
        out.append(f'<a href="{_html.escape(url, quote=True)}" target="_blank" rel="noopener">{_html.escape(label)}</a>')
        i = end + 1
    s = "".join(out)
    s = _re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = _re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    return _re.sub(r"`([^`]+)`", r"<code>\1</code>", s)


def _cells(row):
    parts = _re.split(r"(?<!\\)\|", row.strip().strip("|"))
    return [_inline(c.strip().replace("\\|", "|")) for c in parts]


_COLW = {"Theme": "10rem", "Deck": "20rem", "Reference (not a deck)": "20rem", "Owner": "11rem",
         "Created": "6.5rem", "Updated": "6.5rem", "Level": "6.5rem", "Size": "5.5rem", "Pages": "4.5rem", "Where": "8rem"}


def md_to_html(md):
    """Small markdown renderer for the subset internal-decks.md uses."""
    html_out, lines, i = [], md.splitlines(), 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.strip() == "<!-- md-only -->":
            j = i + 1                    # notes for the md reader, not rendered in the app
            while j < len(lines) and lines[j].strip() != "<!-- /md-only -->":
                j += 1
            if j == len(lines):
                raise SystemExit(f"BUILD FAILED — internal-decks.md line {i + 1}: <!-- md-only --> is never closed")
            i = j + 1
            continue
        h = _re.match(r"^(#{1,3})\s+(.*)$", line)
        if h:
            n = len(h.group(1))
            html_out.append(f"<h{n}>{_inline(h.group(2))}</h{n}>")
            i += 1
        elif line.startswith("|"):
            block = []
            while i < len(lines) and lines[i].startswith("|"):
                block.append(lines[i])
                i += 1
            head, body = block[0], [r for r in block[1:] if not _re.match(r"^\|[\s:|-]+\|$", r)]
            names = [_re.sub(r"<[^>]+>", "", c) for c in _cells(head)]
            # same width for the same column in every table, so the sections line up
            cols = "".join(f'<col style="width:{_COLW[n]}">' if n in _COLW else "<col>" for n in names)
            html_out.append(f"<div class=\"dtable\"><table><colgroup>{cols}</colgroup><thead><tr>" +
                            "".join(f"<th>{c}</th>" for c in _cells(head)) + "</tr></thead><tbody>" +
                            "".join("<tr>" + "".join(f"<td>{c}</td>" for c in _cells(r)) + "</tr>" for r in body) +
                            "</tbody></table></div>")
        elif line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(lines[i][2:])
                i += 1
            html_out.append("<ul>" + "".join(f"<li>{_inline(x)}</li>" for x in items) + "</ul>")
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not _re.match(r"^(#|\||- |<!--)", lines[i]):
                para.append(lines[i].strip())
                i += 1
            html_out.append(f"<p>{_inline(' '.join(para))}</p>")
    return "\n".join(html_out)


decks_html = md_to_html((HERE.parent / "docs" / "internal-decks.md").read_text(encoding="utf-8"))

css = (SRC / "styles.css").read_text(encoding="utf-8")
js = (SRC / "mindmap.js").read_text(encoding="utf-8")
template = (SRC / "template.html").read_text(encoding="utf-8")

banner = "<!-- AUTO-GENERATED from app/src/ by app/build.py — edit the sources, then run build.py -->\n"
script = f'const TREES = {{ "ai": {ai_text}, "ds": {ds_text} }};\nconst STORY = {story_text};\n\n{js}'
html = banner + template.replace("{{STYLES}}", css).replace("{{DECKS}}", decks_html).replace("{{SCRIPT}}", script)

outputs = [HERE / "static" / "index.html", HERE.parent / "ai-tree-mindmap.html"]
for out in outputs:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out}  ({len(html):,} bytes)")
