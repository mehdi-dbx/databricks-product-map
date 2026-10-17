#!/usr/bin/env python3
"""Check app/src/story.json, the only source of the Story's text, against its plan. It writes nothing.

  python3 scripts/story_check.py
  python3 scripts/story_check.py --diff /tmp/story.before.json   # also list the sentences that changed
  python3 scripts/story_check.py --story COPY.json   # check a copy instead
  python3 scripts/story_check.py --plan PLAN.md      # check against another plan file

Run it after every edit of app/src/story.json, before app/build.py and scripts/story_pdf.py.
The format of the file is described in docs/story-tools.md.

Errors make it exit with 1:
- the plan, docs/feature-tree.md: the story's title, the overview's title, every chapter, every slide
  and every feature (with its children) must be the plan's, in the plan's order and with its exact
  words. The plan's verification markers ("to verify…", "not verified…") never appear in the Story,
  and a slide's title also leaves out the plan's "(see …)" pointers;
- the structure: the keys and their types at each level, the chapters numbered 1, 2, 3… in order,
  and the point ids "<chapter>.<k>", in order;
- a capsule reference (refs) that matches no node of the trees;
- an overview tile whose id is not a point;
- unbalanced ** bold markers in a sentence;
- the sources of a slide (its "sources" key): a source whose ref is not a capsule of the slide or
  whose text no longer equals its tree field (note, solves[i].problem or solves[i].solution of the
  capsule refs[ref]), or an effect, challenge or pivot with no source.

Warnings point at the writing faults that earlier drafts showed (docs/story-editorial-guide.md),
on the effect, challenge and pivot: a digit, a "Label: …" formula, a buzzword, a fragment, a pivot
that only says "addresses this", a sentence close to its own slide's text, and a term repeated from
the line shown just before or after. A warning does not block. Each one is fixed or kept on purpose,
and the choice goes into docs/story-journal.md.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
STORY = ROOT / "app/src/story.json"
PLAN = ROOT / "docs/feature-tree.md"
TREES = {"ai": ROOT / "app/src/ai-tree.json", "ds": ROOT / "app/src/ds-tree.json"}

ADDS = (("effect", "Effect"), ("challenge", "Challenge"), ("pivot", "Pivot"))
FIELD_RE = re.compile(r"solves\[(\d+)\]\.(problem|solution)")
SENT_RE = re.compile(r'(?<=[.!?])\s+(?=[A-Z"“(])')
BUZZWORDS = re.compile(r"\b(seamless|unlock|empower|revolution|game.?chang|journey|leverage|cutting.edge|"
                       r"world.class|effortless|supercharge)", re.I)
SHAPE = {   # level → {key: type}
    "top": {"thread": dict, "overview": list, "chapters": list, "appendix": dict},
    "thread": {"title": str, "overview": str, "opening": list, "closing": list},
    "appendix": {"title": str},
    "feature": {"name": str, "children": list},
    "step": {"name": str, "tiles": list, "points": list},
    "tile": {"label": str, "id": str},
    "chapter": {"num": int, "title": str, "intro": list, "points": list, "handoff": str},
    "point": {"id": str, "title": str, "effect": str, "lead": str, "challenge": str, "pivot": str,
              "bullets": list, "refs": list, "features": list, "sources": dict},
    "ref": {"tree": str, "path": list},
    "sources": {"effect": list, "challenge": list, "pivot": list, "report": str},
    "source": {"ref": int, "field": str, "text": str},
}


def unmarked(text):
    """A plan label without its verification markers: "X (to verify: GA status)" → "X",
    "X (business context layer, not verified: no docs page)" → "X (business context layer)"."""
    def keep(m):
        parts = [p for p in m.group(1).split(", ") if not re.match(r"(to verify|not verified)\b", p)]
        return f" ({', '.join(parts)})" if parts else ""
    return re.sub(r"\s*\(([^()]*)\)", keep, text).strip()


def slide_title(text):
    """A slide's title: the plan's label, without markers and without its "(see …)" pointer."""
    return re.sub(r"\s*\(see [^()]*\)", "", unmarked(text)).strip()


def short(title):
    """The label of an overview tile: the title without its trailing description in parentheses."""
    return re.sub(r"\s*\([^()]*\)$", "", title).strip()


def parse_plan(text):
    """docs/feature-tree.md → {title, overview, appendix, sections[{num, title, points[{id, title, features}]}]}."""
    block = text.split("```")[1].strip("\n").splitlines()
    plan = {"title": block[0].strip(), "overview": "", "appendix": {"title": ""}, "sections": []}
    stack = []
    for line in block[1:]:
        m = re.match(r"^((?:[│ ] {3})*)[├└]── (.*)$", line)
        if not m:
            raise ValueError(f"docs/feature-tree.md: line not understood: {line!r}")
        depth, label = len(m.group(1)) // 4, m.group(2).strip()
        if depth == 0:
            if label.startswith("Overview:"):
                plan["overview"] = label.split(":", 1)[1].strip()
            elif label.startswith("Appendix:"):
                plan["appendix"] = {"title": label.split(":", 1)[1].strip()}
            else:
                num, title = re.match(r"^(\d+)\. (.*)$", label).groups()
                plan["sections"].append({"num": int(num), "title": title, "points": []})
        elif depth == 1:
            pid, title = re.match(r"^(\d+\.\d+) (.*)$", label).groups()
            plan["sections"][-1]["points"].append({"id": pid, "title": slide_title(title), "features": []})
            stack = [plan["sections"][-1]["points"][-1]["features"]]
        else:
            feat = {"name": unmarked(label), "children": []}
            del stack[depth - 1:]
            stack[-1].append(feat)
            stack.append(feat["children"])
    return plan


def plan_errors(story, plan):
    """Every place where the Story leaves the plan: titles, slides and features, in order."""
    out = []
    if story["thread"].get("title") != plan["title"]:
        out.append(f"thread.title is \"{story['thread'].get('title')}\", the plan says \"{plan['title']}\"")
    if story["thread"].get("overview") != plan["overview"]:
        out.append(f"thread.overview is \"{story['thread'].get('overview')}\", the plan says \"{plan['overview']}\"")
    if story.get("appendix") != plan["appendix"]:
        out.append(f"appendix is {story.get('appendix')}, the plan says {plan['appendix']}")
    have = [(c.get("num"), c.get("title")) for c in story["chapters"]]
    want = [(s["num"], s["title"]) for s in plan["sections"]]
    if have != want:
        out.append(f"the chapters are {have}, the plan has {want}")
    for c, s in zip(story["chapters"], plan["sections"]):
        hp = [(p.get("id"), p.get("title")) for p in c.get("points", [])]
        wp = [(p["id"], p["title"]) for p in s["points"]]
        if hp != wp:
            bad = [f"{h} where the plan has {w}" for h, w in zip(hp, wp) if h != w]
            if len(hp) != len(wp):
                bad.append(f"{len(hp)} slides where the plan has {len(wp)}")
            out.append(f"chapter {s['num']}: " + "; ".join(bad))
            continue
        for p, q in zip(c["points"], s["points"]):
            if p.get("features") != q["features"]:
                out.append(f"point {q['id']}: the features differ from the plan")
    return out


def shape(obj, level, where, errors):
    want = SHAPE[level]
    if not isinstance(obj, dict):
        errors.append(f"{where}: expected an object")
        return False
    for k in set(want) - set(obj):
        errors.append(f"{where}: missing key \"{k}\"")
    for k in set(obj) - set(want):
        errors.append(f"{where}: unknown key \"{k}\"")
    for k, t in want.items():
        if k in obj and not isinstance(obj[k], t):
            errors.append(f"{where}.{k}: expected {t.__name__}")
    return all(isinstance(obj.get(k), t) for k, t in want.items())


def strings(obj, where):
    """Every sentence of the file, with where it is. The sources are tree fields, not sentences."""
    if isinstance(obj, str):
        yield where, obj
    elif isinstance(obj, list):
        for i, x in enumerate(obj):
            yield from strings(x, f"{where}[{i}]")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if k not in ("refs", "sources", "features", "id", "num"):
                yield from strings(v, f"{where}.{k}")


def node(trees, ref):
    n = trees.get(ref["tree"])
    if not n or n.get("n") != ref["path"][0]:
        return None
    for name in ref["path"][1:]:
        n = next((c for c in n.get("children", []) if c.get("n") == name), None)
        if n is None:
            return None
    return n


def field_value(n, field):
    if field == "note":
        return n.get("note")
    m = FIELD_RE.fullmatch(field or "")
    if not m:
        return None
    rows, i = n.get("solves", []), int(m.group(1))
    return rows[i][m.group(2)] if i < len(rows) else None


def words(text):
    """Content words, plural folded into singular, so that a reworded sentence still matches."""
    return {w[:-1] if len(w) > 4 and w.endswith("s") else w
            for w in re.findall(r"[a-z]+", text.lower()) if len(w) > 3}


def closeness(a, b):
    """Share of the shorter text's words that the other text also uses."""
    wa, wb = words(a), words(b)
    return len(wa & wb) / max(1, min(len(wa), len(wb)))


def neighbour_repeats(p):
    """An effect, challenge or pivot that repeats a term of the line shown just before or after it."""
    stop = {"that", "this", "with", "from", "they", "their", "them", "have", "each", "every", "into", "when",
            "what", "which", "where", "than", "then", "more", "most", "other", "also", "same", "only", "both"}
    terms = lambda t: words(t) - stop
    split = lambda t: [x for x in SENT_RE.split(t.strip()) if x] if t else []
    lines = [("Effect", p["effect"])] if p["effect"] else []
    lines += [("lead", x) for x in split(p["lead"])]
    lines += [("Challenge", x) for x in split(p["challenge"])]
    lines += [("Pivot", p["pivot"])] if p["pivot"] else []
    lines += [("bullet", b) for b in p["bullets"]]
    subject, out = terms(p["title"]), []
    for (ka, a), (kb, b) in zip(lines, lines[1:]):
        if ka in ("lead", "bullet") and kb in ("lead", "bullet"):
            continue
        shared = terms(a) & terms(b)
        if not (ka == "Pivot" and kb == "bullet"):
            shared -= subject
        if shared:
            who = ka if ka not in ("lead", "bullet") else kb
            out.append(f"{who} repeats \"{', '.join(sorted(shared))}\" from the neighbouring line")
    return out


def writing_warnings(p, threshold=0.6):
    out = []
    for key, label in ADDS:
        text = p[key].strip()
        if not text:
            continue
        plain = text.replace("**", "")
        if re.search(r"\d", plain):
            out.append(f"{label} has a digit (fine only inside a product name)")
        if re.match(r"^[A-Z][\w /&-]{0,30}: ", plain):
            out.append(f"{label} starts with a \"Label: …\" formula")
        if BUZZWORDS.search(plain):
            out.append(f"{label} uses a buzzword")
        if len(plain.split()) < 5 and key != "pivot":
            out.append(f"{label} looks like a fragment, not a sentence")
        if re.search(r"\baddress(es)? (this|these|it)\b", plain, re.I):
            out.append(f"{label} only says the product addresses it")
        for own in [p["lead"]] + p["bullets"]:
            if own and closeness(plain, own) >= threshold:
                out.append(f"{label} is close to its own text: {own[:60]}…")
    return out + neighbour_repeats(p)


def sources(p, where, trees, errors):
    """The sources of a slide's effect, challenge and pivot: each one a field of one of its capsules."""
    for key, label in ADDS:
        for si, s in enumerate(p["sources"][key]):
            if not shape(s, "source", f"{where}.sources.{key}[{si}]", errors):
                continue
            if not 0 <= s["ref"] < len(p["refs"]):
                errors.append(f"point {p['id']} sources.{key}: ref {s['ref']} is not a capsule of the point")
                continue
            n = node(trees, p["refs"][s["ref"]])
            if n is not None and field_value(n, s["field"]) != s["text"]:
                errors.append(f"point {p['id']} sources.{key}: {s['field']} of {p['refs'][s['ref']]['path'][-1]} "
                              f"no longer reads \"{s['text'][:50]}…\"")
        if p[key] and not p["sources"][key]:
            errors.append(f"point {p['id']}: the {label.lower()} has no source")


def features_shape(items, where, errors):
    for i, f in enumerate(items):
        if shape(f, "feature", f"{where}[{i}]", errors):
            features_shape(f["children"], f"{where}[{i}].children", errors)


def check(story, trees, plan=None):
    errors, warns = [], []
    if not shape(story, "top", "story", errors):
        return errors, warns
    shape(story["thread"], "thread", "thread", errors)
    shape(story["appendix"], "appendix", "appendix", errors)
    points = {}
    for ci, c in enumerate(story["chapters"]):
        where = f"chapters[{ci}]"
        if not shape(c, "chapter", where, errors):
            continue
        if c["num"] != ci + 1:
            errors.append(f"{where}: num is {c['num']}, expected {ci + 1}")
        for pi, p in enumerate(c["points"]):
            pw = f"{where}.points[{pi}]"
            if not shape(p, "point", pw, errors):
                continue
            if p["id"] != f"{c['num']}.{pi + 1}":
                errors.append(f"{pw}: id is \"{p['id']}\", expected \"{c['num']}.{pi + 1}\"")
            if p["id"] in points:
                errors.append(f"{pw}: id \"{p['id']}\" is used twice")
            points[p["id"]] = (c["num"], p)
            for ri, r in enumerate(p["refs"]):
                if shape(r, "ref", f"{pw}.refs[{ri}]", errors) and node(trees, r) is None:
                    errors.append(f"point {p['id']}: capsule not found: {r['tree']} / {' / '.join(r['path'])}")
            features_shape(p["features"], f"{pw}.features", errors)
            if shape(p["sources"], "sources", f"{pw}.sources", errors):
                sources(p, pw, trees, errors)
    for si, s in enumerate(story["overview"]):
        if shape(s, "step", f"overview[{si}]", errors):
            for ti, t in enumerate(s["tiles"]):
                if shape(t, "tile", f"overview[{si}].tiles[{ti}]", errors) and t["id"] not in points:
                    errors.append(f"overview[{si}].tiles[{ti}]: \"{t['label']}\" points to {t['id']}, which is no point")
    for where, text in strings(story, "story"):
        if text.count("**") % 2:
            errors.append(f"{where}: unbalanced ** in \"{text[:60]}…\"")

    for pid, (num, p) in points.items():
        warns += [f"{pid}: {w}" for w in writing_warnings(p)]
    if plan is not None and not errors:
        errors += [f"plan: {e}" for e in plan_errors(story, plan)]
    for where, text in strings(story, "story"):
        if re.search(r"\b(to verify|not verified)\b", text, re.I):
            errors.append(f"{where}: a verification marker is shown: \"{text[:60]}…\"")
    return errors, warns


def diff(old, new):
    """The sentences that differ between two versions of the file, by place."""
    a, b = dict(strings(old, "story")), dict(strings(new, "story"))
    out = [f"  - {k}: {a[k]}\n  + {k}: {b[k]}" for k in a if k in b and a[k] != b[k]]
    out += [f"  - {k}: {a[k]}" for k in a if k not in b]
    out += [f"  + {k}: {b[k]}" for k in b if k not in a]
    return out


def arg(argv, name, default):
    return pathlib.Path(argv[argv.index(name) + 1]) if name in argv else default


def main(argv):
    story = json.loads(arg(argv, "--story", STORY).read_text(encoding="utf-8"))
    trees = {k: json.loads(v.read_text(encoding="utf-8")) for k, v in TREES.items()}
    plan = parse_plan(arg(argv, "--plan", PLAN).read_text(encoding="utf-8"))
    errors, warns = check(story, trees, plan)
    for w in warns:
        print(f"  WARN {w}")
    for e in errors:
        print(f"  ERROR {e}")
    if "--diff" in argv:
        changes = diff(json.loads(arg(argv, "--diff", None).read_text(encoding="utf-8")), story)
        print("\n".join(changes) if changes else "  no sentence changed")
    n = sum(len(c["points"]) for c in story.get("chapters", []) if isinstance(c, dict) and isinstance(c.get("points"), list))
    print(f"story.json: {len(story.get('chapters', []))} chapters, {n} points, {len(errors)} errors, {len(warns)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
