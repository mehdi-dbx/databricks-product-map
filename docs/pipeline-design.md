# Content pipeline — design (for validation, not built)

Status: proposed. Nothing in this document is built yet.

## Goal

All content work on the trees runs from code in this repo. A run must not depend on
a chat session. The chat is neither the orchestrator nor the memory of the process.

Today the opposite is true. Classification, note-fill, solves, the note rewrite and
the deck hunt were driven from the chat: agents briefed by hand, inline scripts,
corrections re-briefed by hand. The only reusable pieces are `app/build.py`,
`scripts/tree_walk.py` and `scripts/notes_rewrite.py merge`.

## Principles

- One entry point runs a task end to end: `python -m pipeline <task> [options]`.
- Prompts are versioned files in `prompts/`. To change behaviour, edit a file.
- The code calls the model directly and asks for structured output (a JSON schema).
  The code parses the output and retries when it is invalid.
- Quality is judged by a model with a written rubric, not by regex.
- A human reviews before anything is applied to the trees.
- Every model call is logged with the prompt version, the input and the output.
- Steps are idempotent. Re-running a task on the same input gives the same result,
  or skips nodes already done.

## Repository layout

```
pipeline/
  __main__.py        entry point, task dispatch
  tasks.py           task definitions (see below)
  llm.py             model call, JSON schema output, retries
  sources.py         fetch source text for a node (doc URLs)
  review.py          build the review file, read accepted items
  apply.py           merge accepted items into the trees by node path
  runlog.py          append-only log per run
prompts/
  note.generate.md   rewrite or write a note
  note.judge.md      rubric to judge a note
  solves.generate.md problem/solution block
  solves.judge.md    rubric for solves
schemas/
  note.json          {note}
  judge.json         {score, verdict, reason}
  solves.json        {solves: [{axis, problem, solution}]}
runs/<run-id>/
  log.jsonl          every model call
  results.json       generated + judged items
  review.md          diff for human review
  accepted.json      items the human accepted
```

`scripts/tree_walk.py` becomes `pipeline/` traversal. `scripts/notes_rewrite.py merge`
becomes `pipeline/apply.py`.

## Task definition

A task is data, not code. Each task declares:

- **selector** — which nodes it targets (tree, depth, type, missing field, or all).
- **field** — the node field it writes (`note`, `solves`, `type`, later `matrix`).
- **generate prompt + schema** — how to produce the field.
- **judge prompt + schema** — how to grade the result.
- **sources** — whether the node's doc URLs are fetched and passed to the model.
- **max repairs** — how many judge → rewrite rounds before giving up.

First tasks: `note`, `solves`, `type`. `matrix` comes later with the Landscape project.

## Run flow

```
select nodes
  → fetch sources (if the task needs them)
  → generate (model, prompt file, schema)
  → judge (model, rubric file, schema)
  → if verdict = fail: rewrite with the judge's reason, judge again (max N)
  → write results.json + review.md
  → human marks accepted items (accepted.json)
  → apply accepted items to the trees by node path
  → build
```

A **verify** run is the same flow with the generate step skipped. It judges the
current content of every selected node and lists the ones that fail. This is Flow 3
in `data-lifecycle-architecture.md`.

## Model access

The code calls a Databricks model serving endpoint through the Databricks SDK, with the
`fevm-agent` profile. The endpoint name is a setting. No SQL warehouse, table or job
is needed for a local run.

Not verified yet: which Foundation Model endpoints are available on `fevm-agent`.

## Sources for research tasks

Tasks that need facts (solves, notes on new features) get their sources from code.
The code fetches the node's `docs` URLs and turns the HTML into text. It passes the
relevant excerpt to the model with an instruction to use only that text. The judge
checks the output against the same excerpt.

Not verified yet: whether Glean can be called from code. If it cannot, internal
sources stay out of automated runs.

## Review

`review.md` lists each item with the old value, the new value, the judge's score and
reason, and the sources used. You accept items by listing them in `accepted.json`
(by node path), or accept everything above a score. Nothing reaches the trees without
this step.

## Provenance

`runs/<run-id>/log.jsonl` keeps every call. The applied changes record the run id,
the prompt version and the date. This gives the `checked_at` and source data that
`data-lifecycle-architecture.md` asks for.

## What this replaces

- chat-briefed agent swarms and their `.swarm/` journals
- inline scripts run from the chat
- corrections re-briefed by hand
- the regex linter (deleted)

## Open points

1. **Model endpoint** — which model to use for generation and for judging, and whether
   the judge should be a different model from the generator.
2. **Glean from code** — available or not. This decides whether internal sources can
   feed automated runs.
3. **Stable node ids** — apply and provenance target nodes by path today. A rename
   breaks the link. `data-lifecycle-architecture.md` lists stable ids as a prerequisite.
4. **Review format** — markdown diff, or a small HTML page with accept/reject buttons.
5. **Where runs execute** — local only for now. A Databricks job later if runs must be
   scheduled (verify on a cadence).
6. **Prompt files and the spec** — the rules in `panel-slide-spec.md` move into the
   prompt files, which become the version that runs. The spec keeps the intent and
   links to the prompts.

## Out of scope for now

The Lakebase move (`lakebase-architecture.md`). The pipeline works on the JSON files.
It can switch to a table later without changing the task model.

## Related

- `data-lifecycle-architecture.md` — the produce / enrich / verify flows this implements.
- `panel-slide-spec.md` — the content rules the prompts will carry.
- `lakebase-architecture.md` — the later storage move.
