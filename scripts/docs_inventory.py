#!/usr/bin/env python3
"""Inventory of the Databricks documentation (AWS, English).

Reads the docs sitemap, fetches every page and keeps what each page says about itself:
title, sidebar label, description, breadcrumb, release status and last-updated date.
URLs that robots.txt disallows (the archive) are listed as skipped and not fetched.

- `area` is the first item of the page breadcrumb. A section's own page belongs to its
  section. A top-level page (nothing above it in the breadcrumb, no page below it) has none.
- `status` is the release state (Beta, Public Preview, GA, Legacy, ...) declared by the
  note at the top of the page, before its first section. Such a note links to the release
  types page or has a release state as heading. The state is the first one named by its
  links, else by its text, else by its heading.
- `mentions` are the release states linked from the rest of the page, usually for a
  sub-feature.

Usage:
  python3 -I scripts/docs_inventory.py [--cache DIR] [--workers N]
    writes run/docs-inventory/pages.json    (one line per page, so two scans diff page by page)
    writes run/docs-inventory/INVENTORY.md  (pages grouped by area)
  --cache DIR  stores each fetched page in DIR and reads it from there on later runs
"""
import argparse
import datetime
import gzip
import hashlib
import http.client
import json
import pathlib
import re
import sys
import threading
import time
import urllib.parse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "run/docs-inventory"
HOST = "docs.databricks.com"
BASE = "/aws/en/"
UA = "Mozilla/5.0 (compatible; docs-inventory)"
RELEASE_TYPES = "/release-notes/release-types"
STATES = {"public preview": "Public Preview", "private preview": "Private Preview", "beta": "Beta",
          "experimental": "Experimental", "generally available": "GA", "legacy": "Legacy",
          "deprecated": "Deprecated", "preview": "Preview"}
STATE_RX = re.compile(r"\b(" + "|".join(STATES) + r")\b", re.I)
ORDER = ["Experimental", "Private Preview", "Beta", "Public Preview", "Preview", "GA", "Legacy", "Deprecated"]
KEYS = ("path", "section", "area", "title", "label", "status", "mentions", "updated", "crumbs",
        "description", "http", "moved_to")
TOP = "Top-level pages"

_local = threading.local()


def clean(s):
    return " ".join(s.replace("​", "").split())


def state(text):
    """The first release state named in a text."""
    m = STATE_RX.search(text)
    return STATES[m.group(1).lower()] if m else None


def link_state(text):
    """The release state named by the whole text of a link ("Beta", "generally available (GA)").
    A link such as "Databricks preview releases" names none."""
    return STATES.get(re.sub(r"\s*\(ga\)$", "", text.lower()))


def get(path):
    """GET one path on HOST. Reuses the thread's connection, follows redirects on HOST and
    retries network errors, 429 and 5xx. Returns (HTTP status or None, final path or URL, text)."""
    status, tries, hops = None, 0, 0
    while tries < 5:
        try:
            conn = _local.conn = getattr(_local, "conn", None) or http.client.HTTPSConnection(HOST, timeout=30)
            conn.request("GET", path, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
            r = conn.getresponse()
            body = r.read()
        except (OSError, http.client.HTTPException):
            _local.conn = None
            time.sleep(tries)
            tries += 1
            continue
        status = r.status
        if status in (301, 302, 307, 308) and hops < 5:
            loc = urllib.parse.urlsplit(urllib.parse.urljoin(f"https://{HOST}{path}", r.getheader("Location", "")))
            if loc.netloc != HOST:
                return status, loc.geturl(), ""
            path, hops = loc.path, hops + 1
            continue
        if status == 429 or status >= 500:
            time.sleep(2 ** tries)
            tries += 1
            continue
        if r.getheader("Content-Encoding") == "gzip":
            body = gzip.decompress(body)
        return status, path, body.decode("utf-8", "replace")
    return status, path, ""


def fetch(path, cache):
    """get(path), read from the cache when the page is there."""
    f = cache / (hashlib.sha1(path.encode()).hexdigest() + ".json.gz") if cache else None
    if f and f.exists():
        return tuple(json.loads(gzip.decompress(f.read_bytes())))
    got = get(path)
    if f and got[0] == 200:
        f.write_bytes(gzip.compress(json.dumps(got).encode()))
    return got


def robots():
    """Allow and Disallow rules of the `User-agent: *` group, as (length, is_allow, regex)."""
    status, _, text = get("/robots.txt")
    if status != 200:
        sys.exit(f"robots.txt: HTTP {status}")
    rules, ours = [], False
    for line in text.splitlines():
        key, _, value = line.split("#")[0].partition(":")
        key, value = key.strip().lower(), value.strip()
        if key == "user-agent":
            ours = value == "*"
        elif ours and key in ("allow", "disallow") and value:
            rx = re.escape(value).replace(r"\*", ".*")
            rules.append((len(value), key == "allow", re.compile(rx[:-2] + "$" if rx.endswith(r"\$") else rx)))
    return rules


def allowed(path, rules):
    """RFC 9309: the longest matching rule decides, and Allow wins a tie."""
    hits = [(n, allow) for n, allow, rx in rules if rx.match(path)]
    return max(hits)[1] if hits else True


class Page(HTMLParser):
    """Fields of one docs page. The HTML is minified and omits optional end tags (li, p),
    so the parser keys on start tags and on the end tags that are always present."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = self.h1 = self.description = self.updated = None
        self.crumbs = []          # [label, href, active], home first
        self.status, self.mentions = None, []
        self._field = None        # "title" or "h1" while its text is read
        self._text = []
        self._nav = False         # inside the breadcrumb
        self._section = False     # first h2 after the title reached
        self._depth = 0           # div depth inside a note (admonition), 0 outside
        self._head = 0            # depth of the note heading while inside it
        self._note = {"head": [], "body": [], "links": []}
        self._link = None         # text of the release-types link being read

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class") or ""
        if tag == "meta" and a.get("name") == "description":
            self.description = a.get("content")
        elif tag == "time" and a.get("itemprop") == "dateModified":
            self.updated = (a.get("datetime") or "")[:10] or None
        elif tag == "nav" and a.get("aria-label") == "Breadcrumbs":
            self._nav = True
        elif tag == "li" and self._nav:
            self.crumbs.append(["", None, "breadcrumbs__item--active" in cls])
        elif tag == "a" and self._nav and self.crumbs:
            self.crumbs[-1][1] = a.get("href")
        elif tag in ("title", "h1") and getattr(self, tag) is None and self._field is None:
            self._field, self._text = tag, []
        elif tag == "h2" and self.h1 is not None:
            self._section = True
        if tag == "div" and (self._depth or "theme-admonition" in cls):
            if not self._depth:
                self._note = {"head": [], "body": [], "links": []}
            self._depth += 1
            if "admonitionHeading" in cls:
                self._head = self._depth
        if tag == "a" and self.h1 is not None and RELEASE_TYPES in (a.get("href") or ""):
            self._link = []

    def handle_data(self, data):
        if self._field:
            self._text.append(data)
        if self._nav and self.crumbs:
            self.crumbs[-1][0] += data
        if self._link is not None:
            self._link.append(data)
        if self._depth:
            self._note["head" if self._head else "body"].append(data)

    def handle_endtag(self, tag):
        if tag == self._field:
            setattr(self, tag, clean("".join(self._text)))
            self._field = None
        elif tag == "nav" and self._nav:
            self._nav = False
        elif tag == "a" and self._link is not None:
            label, self._link = clean("".join(self._link)), None
            if self._depth:
                self._note["links"].append(label)
            elif link_state(label):
                self.mentions.append(link_state(label))
        elif tag == "div" and self._depth:
            if self._depth == self._head:
                self._head = 0
            self._depth -= 1
            if not self._depth:
                self._end_note()

    def _end_note(self):
        head, body = clean("".join(self._note["head"])), clean("".join(self._note["body"]))
        links = [s for s in map(link_state, self._note["links"]) if s]
        if self.status is None and not self._section and (self._note["links"] or state(head)):
            self.status = links[0] if links else state(body) or state(head)
            if self.status:
                return
        self.mentions += links


def rel(href):
    return href[len(BASE):] if href and href.startswith(BASE) else href


def record(path, http, final, html):
    """One inventory row. A page that did not answer 200 keeps path, section, http and moved_to."""
    rec = {"path": rel(path), "section": rel(path).split("/")[0]}
    if http == 200:
        p = Page()
        p.feed(html)
        p.close()
        crumbs = [[clean(n), rel(h), active] for n, h, active in p.crumbs]
        crumbs = [c for c in crumbs if c[0]]                          # the home link is an icon
        label = crumbs.pop()[0] if crumbs and crumbs[-1][2] else None  # the page itself
        title = p.h1 or (p.title or "").removesuffix(" | Databricks on AWS")
        rec.update(title=title, label=label or title, status=p.status,
                   mentions=sorted(set(p.mentions), key=ORDER.index), updated=p.updated,
                   crumbs=[c[:2] for c in crumbs], description=p.description)
    rec["http"] = http
    if final != path:
        rec["moved_to"] = rel(final)
    return rec


def with_areas(pages):
    """The rows with their `area`, fields in KEYS order."""
    roots = {p["crumbs"][0][1]: p["crumbs"][0][0] for p in pages if p.get("crumbs") and p["crumbs"][0][1]}
    for p in pages:
        if p["http"] == 200:
            p["area"] = p["crumbs"][0][0] if p["crumbs"] else roots.get(p["path"])
    return [{k: p[k] for k in KEYS if k in p} for p in pages]


def write_json(pages, skipped, today):
    def rows(xs):
        return ",\n".join("  " + json.dumps(x, ensure_ascii=False) for x in xs)

    (OUT / "pages.json").write_text(
        f'{{"source": "https://{HOST}{BASE}sitemap.xml", "fetched": "{today}",\n'
        f' "skipped": [\n{rows(skipped)}\n ],\n "pages": [\n{rows(pages)}\n ]}}\n', encoding="utf-8")


def write_md(pages, skipped, today):
    ok = [p for p in pages if p["http"] == 200]
    bad = [p for p in pages if p["http"] != 200]
    groups = defaultdict(list)
    for p in ok:
        groups[p["area"]].append(p)
    order = sorted((a for a in groups if a), key=lambda a: (-len(groups[a]), a)) + ([None] if None in groups else [])
    types = [s for s in ORDER if any(p["status"] == s for p in ok)]
    day, n = Counter(p["updated"] for p in ok).most_common(1)[0]
    out = ["# Databricks docs inventory (AWS, English)", "",
           f"Source: https://{HOST}{BASE}sitemap.xml, fetched {today}, by `scripts/docs_inventory.py`. "
           "Data: `pages.json`.", "",
           f"{len(pages) + len(skipped)} sitemap URLs: {len(ok)} pages read, {len(bad)} not HTTP 200, "
           f"{len(skipped)} skipped by robots.txt.", "",
           "- Area: first item of the page breadcrumb. A section's own page belongs to its section. "
           f"{TOP}: nothing above them in the breadcrumb and no page below them.",
           "- Status: release state declared by the note at the top of the page, before its first section.",
           f"- Updated: the page's last-updated date. Most common: {day} ({n} pages).", "",
           "## Areas", "",
           "| Area | Pages | " + "".join(f"{t} | " for t in types) + "URL sections |",
           "|---|---:|" + "---:|" * len(types) + "---|"]
    for a in order:
        ps = groups[a]
        st = Counter(p["status"] for p in ps)
        secs = ", ".join(f"`{s}`" for s, _ in Counter(p["section"] for p in ps).most_common(3))
        cell = (a or TOP).replace("|", "\\|")
        out.append(f"| {cell} | {len(ps)} | " + "".join(f"{st[t] or ''} | " for t in types) + f"{secs} |")
    for a in order:
        out += ["", f"## {a or TOP} ({len(groups[a])})", ""]
        for p in sorted(groups[a], key=lambda p: [c[0].lower() for c in p["crumbs"][1:]] + [p["label"].lower()]):
            trail = " › ".join([c[0] for c in p["crumbs"][1:]] + [p["label"]])
            extra = "".join(f" · {x}" for x in (p["updated"], p["status"] and f"**{p['status']}**") if x)
            out.append(f"- {trail} — [`{p['path'] or '/'}`](https://{HOST}{BASE}{p['path']}){extra}")
    if bad or skipped:
        out += ["", "## Not read", ""]
        out += [f"- `{p['path']}` — HTTP {p['http']}" + (f" → `{p['moved_to']}`" if "moved_to" in p else "") for p in bad]
        out += [f"- `{s['path']}` — {s['reason']}" for s in skipped]
    (OUT / "INVENTORY.md").write_text("\n".join(out) + "\n", encoding="utf-8")


def tally(pages, skipped):
    ok = [p for p in pages if p["http"] == 200]

    def has(k):
        return sum(bool(p[k]) for p in ok)

    st = Counter(p["status"] for p in ok if p["status"])
    print(f"sitemap URLs {len(pages) + len(skipped)}: fetched {len(pages)}, skipped {len(skipped)} "
          f"{dict(Counter(s['reason'] for s in skipped))}")
    print(f"HTTP {dict(Counter(p['http'] for p in pages))}, moved {sum('moved_to' in p for p in pages)}")
    print(f"pages read {len(ok)}: breadcrumb {has('crumbs')}, updated {has('updated')}, "
          f"description {has('description')}, mentions {has('mentions')}")
    print(f"status {has('status')}: " + ", ".join(f"{s} {st[s]}" for s in ORDER if st[s]))
    print(f"areas {len({p['area'] for p in ok if p['area']})}, {TOP.lower()} {sum(not p['area'] for p in ok)}")


def main():
    ap = argparse.ArgumentParser(description="Inventory of the Databricks documentation (AWS, English).")
    ap.add_argument("--cache", type=pathlib.Path, help="directory that keeps the fetched pages")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()
    if args.cache:
        args.cache.mkdir(parents=True, exist_ok=True)

    rules = robots()
    status, _, xml = get(BASE + "sitemap.xml")
    if status != 200:
        sys.exit(f"sitemap.xml: HTTP {status}")
    paths, skipped = [], []
    for p in sorted({urllib.parse.urlsplit(u).path for u in re.findall(r"<loc>(.*?)</loc>", xml)}):
        if not p.startswith(BASE):
            skipped.append({"path": p, "reason": "outside " + BASE})
        elif not allowed(p, rules):
            skipped.append({"path": rel(p), "reason": "robots.txt"})
        else:
            paths.append(p)
    print(f"sitemap: {len(paths)} pages to read, {len(skipped)} skipped, {args.workers} workers", file=sys.stderr)

    pages = []
    with ThreadPoolExecutor(args.workers) as pool:
        for i, rec in enumerate(pool.map(lambda p: record(p, *fetch(p, args.cache)), paths), 1):
            pages.append(rec)
            if i % 500 == 0 or i == len(paths):
                print(f"  {i}/{len(paths)}", file=sys.stderr, flush=True)
    pages = with_areas(pages)

    today = datetime.date.today()
    OUT.mkdir(parents=True, exist_ok=True)
    write_json(pages, skipped, today)
    write_md(pages, skipped, today)
    tally(pages, skipped)
    print(f"wrote {OUT.relative_to(ROOT)}/pages.json, INVENTORY.md")


if __name__ == "__main__":
    main()
