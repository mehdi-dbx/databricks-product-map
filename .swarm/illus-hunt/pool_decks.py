#!/usr/bin/env python3
"""Shortlist deck slides for each point (keywords.json against deck-index.jsonl) and download them into dl-verify/."""
import json, pathlib, re, subprocess, time, urllib.request, urllib.error, hashlib
RUN = pathlib.Path(__file__).resolve().parent; CACHE = RUN / "dl-verify"; CACHE.mkdir(exist_ok=True)
QUOTA = "gcp-dev-field-eng-aiapiquota"
kw = json.load(open(RUN / "keywords.json"))
rows = [json.loads(l) for l in open(RUN / "deck-index.jsonl") if '"error"' not in l]
SKIPWORDS = ("agenda", "thank you", "questions?", "q&a", "appendix", "legal", "forward-looking")

def score(r, words):
    t = r["text"].lower()
    if len(t) < 40 or any(s in t[:80] for s in SKIPWORDS): return 0
    hits = sum(t.count(w) for w in words)
    if not hits: return 0
    labels = len(re.findall(r"\b[A-Z][\w/+-]*(?: [\w/+-]+){0,3}\b", r["text"]))   # many short labels = diagram-like
    return hits * 3 + min(labels, 40) / 10 + (2 if r["images"] else 0) - (3 if r["deprecated"] else 0) - (len(t) > 900) * 3

tok, tok_t = None, 0
def token():
    global tok, tok_t
    if time.time() - tok_t > 1800:
        tok = subprocess.check_output(["gcloud", "auth", "application-default", "print-access-token"], text=True).strip(); tok_t = time.time()
    return tok

def thumb(did, oid, dest):
    url = f"https://slides.googleapis.com/v1/presentations/{did}/pages/{oid}/thumbnail?thumbnailProperties.thumbnailSize=LARGE"
    for wait in (0, 20, 40, 80):
        time.sleep(wait)
        try:
            req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token()}", "x-goog-user-project": QUOTA})
            with urllib.request.urlopen(req, timeout=60) as r: cu = json.loads(r.read())["contentUrl"]
            with urllib.request.urlopen(cu, timeout=60) as r: dest.write_bytes(r.read())
            return True
        except urllib.error.HTTPError as e:
            if e.code != 429: return False
        except Exception: pass
    return False

pool = {}
for pid, words in kw.items():
    ranked = sorted((r for r in rows if score(r, words) > 0), key=lambda r: -score(r, words))[:10]
    out = []
    for r in ranked:
        dest = CACHE / f"{r['deck_id']}-{r['slide']}.png"
        if dest.exists() or thumb(r["deck_id"], r["object_id"], dest):
            out.append({"file": str(dest.relative_to(RUN)), "source": f"{r['deck']}, slide {r['slide']}",
                        "url": f"https://docs.google.com/presentation/d/{r['deck_id']}/edit#slide=id.{r['object_id']}",
                        "deprecated": r["deprecated"]})
        time.sleep(1.2)
    pool[pid] = out
    json.dump(pool, open(RUN / "pool-decks.json", "w"), indent=1)
    print(pid, len(out), flush=True)
