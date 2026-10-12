# Story additions — tools

These tools let the Story carry the three sentences that `docs/story-editorial-guide.md` adds to each point: effect, challenge and pivot. They were built on 2026-10-11.

## Files

| File | Role |
|---|---|
| `docs/story-additions.json` | Holds the sentences and their sources, one item per point. The format is in the guide. The file starts empty. |
| `scripts/apply_story_additions.py` | Checks the sources and copies the sentences into `docs/story-notes.md`. |
| `scripts/story_extract.py` | Reads the added lines into `app/src/story.json` and `docs/story.md`. |
| `app/src/mindmap.js`, `app/src/styles.css` | Show the sentences on the slide. |

## Markup in `docs/story-notes.md`

The sentences are the last lines of the point's block, one line each:

```
**Point 9.1 — Application hosting.** *(Databricks Apps + App Spaces)*
Developers build applications with … (existing text, unchanged)
**Effect:** Data and AI applications run on the platform itself, next to the governed data.
**Challenge:** A data or AI application usually runs on separate infrastructure, …
**Pivot:** Databricks Apps brings these applications onto the platform.
```

Their sources are added at the end of the chapter's Check block:

```
- Additions 9.1 (editorial guide):
  - Effect ← Databricks Apps + App Spaces, solves[0].solution, solves[3].solution
  - Challenge ← Databricks Apps + App Spaces, solves[0].problem, solves[2].problem, solves[3].problem, solves[1].problem
  - Pivot ← Databricks Apps + App Spaces, note
```

## `scripts/apply_story_additions.py`

```
python3 scripts/apply_story_additions.py docs/story-additions.json           # check, then write
python3 scripts/apply_story_additions.py docs/story-additions.json --check   # check only, write nothing
```

An item is refused, and nothing of it is written, if any of these fails:

- The point is in `app/src/story.json`, in the chapter the item names.
- The point cites at least one capsule.
- Each sentence is on one line.
- A sentence that is not empty has at least one source.
- Each source's `ref` is a capsule of the point, and its `field` exists on that capsule.
- Each source's `text` is exactly the content of that field.

When it writes:

- It adds the three lines at the end of the point's block and the source lines at the end of the chapter's Check block.
- It never changes an existing line. The only lines it replaces are the ones it wrote earlier, when their item has changed.
- Run again on the same file, it changes nothing. Such items count as "already applied".
- It prints the applied, already applied and refused items, and any `report` text.
- It exits with code 1 when an item is refused.
- It prints a `WARN` line for each writing fault that earlier drafts showed:
  - a digit;
  - a "Label: …" formula;
  - a buzzword;
  - a fragment instead of a sentence;
  - a pivot that only says "addresses this";
  - a sentence close to the point's own transition or bullets, or to a bullet of chapter 1.

  Warnings do not block the item. Each one is either fixed or kept on purpose, and the reason goes into `docs/story-journal.md`.

## `scripts/story_extract.py`

- It puts the added lines in the point's `effect`, `challenge` and `pivot` fields, and only when they are present. A point without additions keeps exactly the same JSON as before.
- The point text before the added lines still gives the bullets.
- It stops with an error if any text follows an added line, or if a label appears twice in a point.
- `docs/story.md` shows, in this order: title, effect, transition, challenge, pivot, bullets.

## Story tab

Slide order:

1. title;
2. effect (`.seff`, normal text);
3. transition (`.slead`, italic grey);
4. challenge, then pivot (`.sadd`, normal text);
5. bullets;
6. capsule cards.

The Story search covers the three sentences.

## Tests run on 2026-10-11

The tests ran on a copy of the repo, with the three examples of the guide as items:

- `--check` reported 3 items to apply and wrote nothing.
- The first run added 21 lines and changed none.
- A second run changed nothing.
- After one sentence was changed, the run replaced only its line.
- These items were refused, and the file was left untouched:
  - a wrong source text;
  - a sentence with no source;
  - a wrong chapter;
  - a point with no capsule.
- The extractor gave the three points their new fields. The rest of `story.json` stayed identical.
- In the browser:
  - the slides showed the order above;
  - the search found the new sentences;
  - there was no JS error.
