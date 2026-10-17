# Story — source file and tools

The Story lives in one file, `app/src/story.json`, edited by hand: its text, and the sources of each slide's effect, challenge and pivot. Its structure follows the plan, `docs/feature-tree.md`. Everything else is built from it.

## Files

| File | Role |
|---|---|
| `docs/feature-tree.md` | The plan: the story's title, the overview, the chapters, the slides, their features and the appendix, and why v2 replaced v1. It changes only on request. |
| `app/src/story.json` | The only source of the Story: titles, effects, transitions, challenges, pivots, bullets, features, chapter intros, overview, appendix, and the sources of the effects, challenges and pivots. |
| `scripts/story_check.py` | Checks `story.json` against the plan and the trees, and writes nothing. `app/build.py` runs it and stops on any error. |
| `app/build.py` | Builds the app, whose Story tab reads `story.json`. It leaves the sources out of the app. |
| `scripts/story_pdf.py` | Builds the PDF, `AI-and-Data-Science-on-Databricks.pdf`, and its copy in `app/static`. |
| `scripts/apply_fact_check.py` | Applies a fact-check report to the trees and to the sentences of `story.json`. A corrected tree field also updates the sources that quote it. |
| `docs/archive/` | The former sources and the docs of the v1 chapter 1. No script reads them. |

## After an edit

1. `python3 scripts/story_check.py`
2. `python3 app/build.py`
3. `python3 scripts/story_pdf.py`

## Format of `app/src/story.json`

The file has four keys: `thread`, `overview`, `chapters` and `appendix`. Every key is always present. An empty field stays `""` or `[]`.

- **`thread`**:
  - `title`: the story's title, the plan's root;
  - `overview`: the overview's title, "Databricks platform architecture";
  - `opening` and `closing`: lists of sentences. The plan has neither, so both stay `[]`.
- **`overview`**: the first slide, one block per chapter, in order:
  - `name`: the chapter's title;
  - `tiles`: the chapter's slides, each `{"label": …, "id": "<slide id>"}`. The label is the slide's title without its trailing description in parentheses. A click on a tile opens its slide;
  - `points`: a few words each. They stay `[]`.
- **`chapters`**, in the plan's order:
  - `num`: 1, 2, 3… in the order of the list;
  - `title`: the plan's;
  - `intro`: a list of sentences (`docs/story-cement.md`);
  - `points`: the slides;
  - `handoff`: `""` (`docs/story-cement.md`).
- **`points`**, in the plan's order:
  - `id`: the plan's, `"<chapter num>.<position>"`;
  - `title`: the plan's label, without its markers and its "(see …)" pointer (`docs/story-editorial-guide.md`, "Title");
  - `effect`: one sentence, the line under the title;
  - `lead`: the transition, one string that may hold several sentences;
  - `challenge`: one string of several sentences, shown in the "Challenges" box;
  - `pivot`: one sentence that starts with the product's name in bold;
  - `bullets`: a list, one sentence each;
  - `refs`: the capsules shown as cards, each `{"tree": "ai" or "ds", "path": [the names from the tree's root to the capsule]}`;
  - `features`: the slide's features in the plan, each `{"name": …, "children": [features]}`, without the plan's markers. The appendix shows them, and the Story search covers them;
  - `sources`: what the effect, challenge and pivot rest on. See "Sources" below. The app and the PDF do not show it.
- **`appendix`**: `{"title": …}`, the plan's "capability map by section". The app and the PDF build the map from the slides' features.

Rules for the text:

- Bold is written `**…**`, in any sentence. Every `**` must be closed.
- A string that holds several sentences (`lead`, `challenge`) shows one sentence per bullet. It is split after ".", "!" or "?" when a space and a capital letter, a quote or a parenthesis follow.
- The rules for writing are in `docs/story-editorial-guide.md` (the slides) and `docs/story-cement.md` (the chapter intros).

Example of a slide, shortened:

```json
{
  "id": "7.6",
  "title": "Applications",
  "effect": "Data and AI applications run on the platform itself, next to the governed data.",
  "lead": "When the same question comes back every week, it is worth turning into a small application.",
  "challenge": "Usually each one runs on separate infrastructure, with its own identity management and secrets. It sits apart from the governed data. Access control and audit trails are hard to put in place.",
  "pivot": "**Databricks Apps** now hosts them itself.",
  "bullets": ["Developers build applications with the **frameworks they already use**, such as Streamlit, Gradio, React or FastAPI, and deploy them.", "…"],
  "refs": [{"tree": "ai", "path": ["Databricks AI", "Developer productivity", "Databricks Apps + App Spaces"]},
           {"tree": "ai", "path": ["Databricks AI", "Genie / AI.BI family", "Genie App Builder"]}],
  "features": [{"name": "Databricks Apps (application hosting)", "children": [{"name": "Databricks AppKit (app framework)", "children": []}, {"name": "App Spaces", "children": []}]},
               {"name": "Genie App Builder (no-code app builder)", "children": []}],
  "sources": {
    "effect": [{"ref": 0, "field": "solves[0].solution", "text": "**Serverless Databricks Apps** eliminate external hosting costs and complexity"}],
    "challenge": [{"ref": 0, "field": "solves[0].problem", "text": "Apps require **separate infrastructure** outside Databricks platform"}],
    "pivot": [{"ref": 0, "field": "note", "text": "Databricks Apps hosts interactive data and AI apps on Databricks, governed by Unity Catalog."}],
    "report": ""
  }
}
```

**When the plan changes**, on request, `story.json` follows it: chapters, slide ids, titles and features. Then update `app/src/illustrations.json` and `illustration-picks.json`, which are keyed by slide id. The check catches every difference with the plan, but not the illustrations.

## Sources

Each slide's `sources` has four keys, always present:

- `effect`, `challenge`, `pivot`: a list of sources each, `{"ref": …, "field": …, "text": …}`.
  - `ref` is the position of the capsule in the slide's `refs`.
  - `field` is `note`, `solves[i].problem` or `solves[i].solution`.
  - `text` is the field's exact value. It is not a sentence of the Story: the search, the diff and the fact-check of sentences skip it.
- `report`: why a sentence is missing, for example when no capsule has `solves` rows. Otherwise `""`.

A new or rewritten effect, challenge or pivot gets its sources here.

## `scripts/story_check.py`

It stops with errors, and exit code 1, on:

- a story title, overview title, appendix, chapter, slide id, slide title or feature that differs from the plan, or is not in the plan's order;
- a verification marker of the plan ("to verify", "not verified") in any sentence;
- a missing, unknown or mistyped key, chapters out of order, or a point id that does not follow its chapter and position;
- a capsule reference that matches no tree node;
- an overview tile whose id is not a slide;
- an unclosed `**`;
- a source whose `ref` is not a capsule of the slide, or whose `text` no longer equals the tree field;
- an effect, challenge or pivot with no source.

It prints a `WARN` line for each writing fault seen in earlier drafts, on the effect, challenge and pivot:

- a digit;
- a "Label: …" formula;
- a buzzword;
- a fragment instead of a sentence;
- a pivot that only says "addresses this";
- a sentence close to its slide's transition or bullets;
- a term repeated from the neighbouring line. Terms of the slide's title are allowed, except between the pivot and the first bullet.

Warnings do not block. Each one is either fixed or kept on purpose, and the reason goes into `docs/story-journal.md`.

Options: `--story` checks a copy, `--plan` checks against another plan file, `--diff OLD` lists the sentences that changed.

## Story tab

Slide order:

1. title;
2. effect (`.seff`, brand blue, smaller than the bullets);
3. transition (`.slead`, italic grey);
4. challenge (`.sadd.schal`, grey, upright, the size of the effect), inside a box labelled "Challenges" (`.schbox`: blue border, transparent, as wide as its text, no hover);
5. pivot (`.sadd`, normal text, the product's name in bold);
6. bullets, with their `**…**` keywords in bold;
7. capsule cards.

- A transition or a challenge of two or more sentences shows as a list, one sentence per bullet (`.slist`, with a small black dot).
- The overview is the first slide: the story's title, the overview's title and one block per chapter. "Overview" is the first entry of the chapter list.
- The appendix is the last section, "Appendix" in the chapter list: every slide with its features. A slide's title links to the slide.
- The Story search covers every sentence and every feature, and ignores the asterisks.

## PDF

`scripts/story_pdf.py` describes its layout in its docstring: 16:9, one slide per page, the overview as the cover, a dark opener per chapter, and the appendix on the last pages.
