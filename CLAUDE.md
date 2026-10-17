# Working on this repository

An internal Databricks field app, `ai-tree-mindmap`. It has four tabs: AI Ecosystem Tree, Data Science Tree, Data & AI Story and Decks. It is internal only and is never shared with customers.

## Build and deploy

- Build: `python3 app/build.py` writes `app/static/index.html` and `ai-tree-mindmap.html` from `app/src/` and `docs/internal-decks.md`.
- Story PDF: `python3 scripts/story_pdf.py` writes `AI-and-Data-Science-on-Databricks.pdf`, one 16:9 page per slide, and a copy in `app/static` that the deployed app serves at `/AI-and-Data-Science-on-Databricks.pdf`.
- Deploy only when asked:
  - `databricks sync app /Workspace/Users/mehdi.lamrani@databricks.com/ai-tree-mindmap --profile fevm-agent --full`
  - then `databricks apps deploy ai-tree-mindmap --source-code-path /Workspace/Users/mehdi.lamrani@databricks.com/ai-tree-mindmap --profile fevm-agent`
- GitHub: `mehdi-dbx/databricks-product-map`, a private repo.
  - Commit and push only when asked.
  - To push, switch to the `mehdi-dbx` gh account, then switch back to `mehdi-lamrani_data`.

## The Story

- **Plan:** `docs/feature-tree.md`, version 2 of 2026-10-17. It sets the chapters, the slides, their titles and their features. Respect it word for word, and change it only on request. The check fails when the Story leaves it.
- **Source:** `app/src/story.json`, the only file of the Story. It is edited by hand. Each slide holds its text and, in `sources`, the tree fields that its effect, challenge and pivot rest on. Its format is in `docs/story-tools.md`.
- **After an edit:** `python3 scripts/story_check.py`, then `python3 app/build.py`, then `python3 scripts/story_pdf.py`. The build stops if the check finds an error.
- **The slides:** `docs/story-editorial-guide.md`, the rules, the process and how to delegate.
- **The chapter intros:** `docs/story-cement.md`.
- **Archive:** `docs/archive/` holds `story-notes.md`, the source until 2026-10-16, and the docs of the v1 chapter 1, which the plan dropped. No script reads them.
- **Decisions:** log every one, with its reason, in `docs/story-journal.md`.

## Rules for any change

- **Act only on an explicit request.** A critique or a remark is not a request. Before acting, say in French, in one line, what you are about to do.
- **Never rewrite validated text.** A new direction adds to the existing work. Keep wording, bullets and titles exactly as they are, unless a change is explicitly asked for.
- **Invent nothing.** No concept, role, option, field or fact that neither the user nor the repository states. An analogy with earlier work creates nothing.
- **No confirmation request on what is already settled, and no "open decisions" sections.** Ask only when a choice is really open and changes what gets built.
- **Before delivering a doc, reread it line by line.** Cut everything that does not serve the planned work: analogies, history, generic rules.
- **Docs and app content are in English. The chat is in French and terse.**
  - Docs never name people. They do not quote the chat: they sum up the decisions.
  - A doc that instructs Claude is in the imperative, with its inputs and its conduct.
  - One file per purpose.
- **Rules that matter go into these files and into scripts.** Memory between sessions is not reliable.
- **Two sessions must not edit the same files.** For parallel work, use a git worktree.
