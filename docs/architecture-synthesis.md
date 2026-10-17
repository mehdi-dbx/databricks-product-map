# Synthesis: data model, content flows, storage and platform expansion

> Status: PROPOSED. Reconciles the documents in §1. None of them has been edited.
> §9 lists the changes each one needs once this synthesis is validated.

Created 2026-10-09.

## 1. Sources

| Document | Status | Contributes |
|---|---|---|
| `docs/plan/platform-expansion.md` | planned | Areas, shared nodes (`ref` / `see`), navigation, production stages, phases |
| `docs/data-lifecycle-architecture.md` | proposed | Stable id, provenance, `checked_at`, one patch channel, produce / enrich / verify |
| `docs/lakebase-architecture.md` | proposed | Relational model, export to JSON, Lakebase as system of record |
| `docs/pipeline-design.md` | proposed | Code pipeline: tasks, generate → judge → repair, review, apply, run log |
| `docs/panel-slide-spec.md` | in progress | Node fields, `type`, writing rules |
| `docs/compete-matrix.schema.json` | in use | Matrix structure |
| `docs/story-design.md` | v1 built | Story references by name path, build gate |
| `plan/ds-ecosystem-plan.md` | done | DS process, "overlap allowed" |
| `docs/fable-fact-check-prompt.md`, `docs/fable-fact-check-results.json`, `scripts/apply_fact_check.py` | run 2026-10-09 | First verify run and its applier |
| `scripts/notes_rewrite.py` | in use | Note merge by name path |

## 2. Facts the design must respect

Checked 2026-10-09.

1. The project folder is not a git repository.
2. Workspace `fevm-agent` is the FEVM deployment `agent`.
   - Intent "Customer Demo/Testing".
   - Expires 2026-12-21 (73 days). Extended once, on 2026-09-23.
   - The app runs there. So do the model endpoints the pipeline plans to call.
3. Lakebase synced tables copy Unity Catalog tables into Postgres.
   - Lakebase Change Data Feed goes the other way: it copies Postgres changes into Unity
     Catalog Delta tables that a SQL warehouse can read.
   - Change Data Feed is in Public Preview and needs `REPLICA IDENTITY FULL`.
4. One verify run exists (2026-10-09):
   - 165 claims checked: 103 correct, 31 wrong, 15 outdated, 16 unverifiable.
   - 44 corrections were proposed: the 42 for the trees are in place, and the 2 Story
     corrections went to the Story draft.
   - The 103 confirmations exist only in the results file.
5. Four change formats are in use or designed:
   - `notes_rewrite.py`: `{tree, path, note}`. Overwrites without a check.
   - `apply_fact_check.py`: `{file, path, field, current, correct, verdict, source, why}`.
     Writes only if the field still holds `current`.
   - `pipeline-design.md`: `results.json` / `accepted.json`, by name path.
   - `data-lifecycle-architecture.md`: `{id, field, value, source, pass, ts}`.
6. Every script and the Story target nodes by name path. No node has a persistent id.
7. The `node` table in `lakebase-architecture.md` has no `type`, `solves` or `solves_conf`
   column. Its `tree` column allows only 'ai' or 'ds'.
8. The only live matrix (Unity Gateway) does not match `compete-matrix.schema.json`: it has
   no `feature`, and its groups and capabilities have no `id`. The example file does match.
9. Display, per `mindmap.js`:
   - Never shown: `since`, `solves_conf`, the matrix cell flag `soft`.
   - Shown: `deck` (panel line), `c` and `new` (filters), `matrix` (Landscape tab).
10. `since` mixes status words and dates.

## 3. Decisions added by this synthesis

### S1: The system of record is the JSON files, in git

- The tree files are the system of record, under git. Every table is derived from them and
  can be rebuilt at any time.
- This is the second option of `lakebase-architecture.md` open point 1: JSON is reviewed,
  then loaded. It is also the JSON form that `data-lifecycle-architecture.md` already
  describes: persistent ids, an append-only patch log and a deterministic applier.
- Reasons:
  - The write path is already file-based: research agents, pipeline review, applier.
  - git gives diff, history and rollback once the folder is a repository (fact 1).
  - The workspace expires on 2026-12-21 (fact 2). A database there as the only master copy
    would go with it.
  - What the database would enforce is covered in files:
    - upsert by key → ids
    - `CHECK` constraints → a JSON Schema checked at write and at build
    - audit table → the change log
- Effect on "Why Lakebase" in `data-lifecycle-architecture.md`: the needs it lists stay.
  They are met in files, and SQL and Genie access comes from a derived copy (S2).
- Alternative: Lakebase as system of record, as designed. It needs:
  - a workspace that does not expire
  - backups
  - an audit table
  - its own review workflow

  It becomes worth it if several people must edit live through SQL or an app.

### S2: SQL and Genie access through a derived copy

- A script exports the JSON and the change log into tables (§4.7), then loads them.
- Proposed target: Unity Catalog Delta tables. A Genie space reads them directly, with no
  preview feature involved.
- Alternative: Lakebase tables, with Change Data Feed to Delta for Genie (Public Preview).
- The app keeps reading the static JSON, as both source documents require.

### S3: One change record, one applier, one log

- Every flow emits the same record (§4.5). One applier applies it.
- Every applied or confirmed record goes to an append-only log.
- Provenance and `checked_at` are read from the log. They are not stored on nodes.

### S4: One machine schema

- `schemas/node.json` (JSON Schema) and the fixed `compete-matrix.schema.json` are the
  machine contract. The applier validates before it writes. The build validates again.
- `panel-slide-spec.md` keeps the intent and the human rules. The prompt files carry the
  writing rules (`pipeline-design.md` open point 6).

## 4. Reconciled design

### 4.1 Identity

- Every node has an `id`, as in plan §5.3:
  - lowercase kebab slug, unique across all trees
  - leaves use `<parent-id>.<slug>`
  - assigned once, never regenerated
- In matrices, competitors, groups and capabilities carry ids. The Unity Gateway matrix gets
  them.
- Story points keep their ids (`7.2`).
- Name paths stay in review files and logs, for reading only.

### 4.2 Node fields

| Field | Level | Required | Shown in the app | Stored in |
|---|---|---|---|---|
| `id` | all | yes | deep links | node |
| `n` | all | yes | name | node |
| `sub` | any | no | subtitle | node |
| `note` | d1 and below | yes | intro sentence | node |
| `type` | d2 and below | yes | picks the panel template | node |
| `s` | capsule | yes | status chip | node |
| `c` | capsule | yes | "Hide to-verify" filter | node |
| `docs` | capsule | at least 1 in live areas | links, inherited by leaves | node |
| `since` | capsule | no | not shown | node, `YYYY-MM` when present |
| `new` | capsule | no | DAIS filter | node |
| `deck` | capsule | no | "Deck ·" line | node |
| `solves` | feature | later pass | problem / solution block | node |
| `solves_conf` | with `solves` | with `solves` | not shown | node |
| `matrix` | feature | later pass | Landscape tab | node, compete schema |
| `see` | any | no | "See also" chips | node |
| `ref` | placement stub | — | — | stub only |
| `children` | non-leaf | — | — | node |
| `alsoIn` | shared nodes | — | "Also in" chips | computed by the build |
| provenance, `checked_at` | per field | — | not shown | change log (§4.6) |

Plan D5 made `since` required. The app never shows it and half of today's values are status
words. Here it is optional, with a fixed format.

### 4.3 Trees and placement

- As in plan §5.1 and §5.2: manifest `areas.json`, one file per tree, a home node per
  feature, `ref` stubs, `see` links.
- Home rule: the home tree is the area of the node's primary doc URL.
- Replaces the "overlap allowed" rule of the DS plan.

### 4.4 Compete matrix

- The matrix stays inside its node (`matrix`), as today and as in `panel-slide-spec.md`. No
  separate `compete-*.json` files.
- Schema changes:
  - `feature` and `featurePath` become optional. They are only needed for a standalone file.
  - `legend` becomes optional, with one shared default legend in `schemas/legend.json`.
    This answers `lakebase-architecture.md` open point 3.
  - Group and capability `id` stay required.
- Cells flagged `soft` become verify targets.

### 4.5 Change record

```json
{
  "id": "unity-gateway",
  "field": "note",
  "current": "text before",
  "value": "text after",
  "verdict": "new | wrong | outdated | correct | unverifiable",
  "source": "https://docs.databricks.com/aws/en/ai-gateway/",
  "why": "one sentence",
  "pass": "verify.factcheck@1",
  "run": "2026-10-09-factcheck",
  "ts": "2026-10-09T08:40:00Z",
  "path": ["Databricks AI", "Governance for AI", "Unity Gateway"]
}
```

- `id` targets the node. `path` is only for the people reading the review.
- `field` uses the addressing of `apply_fact_check.py`:
  - a node field
  - `solves[i].problem` or `solves[i].solution`
  - `docs[i]`
  - matrix cells: `matrix.<capability-id>.<competitor-id>.<status|note>`
- `current`, from `apply_fact_check.py`: the applier writes only if the field still holds it.
- `verdict: correct` writes nothing. The record is logged and dates the check.
- `verdict: new` creates a field (`current` empty).
  - A new node: `field: "node"`, the node as `value`, plus `parent` and `ordinal`.
  - A placement: `field: "ref"`, plus `tree`, `parent` and `ordinal`.
- Story records carry `{"story": "7.2", "part": "…", "bullet": n}` instead of `id`. They are
  applied to `app/src/story.json`, as today.

### 4.6 Applier and log

- One applier, generalized from `apply_fact_check.py`. It replaces that script and the
  `merge` command of `notes_rewrite.py`.
- For each record:
  1. Find the node by id.
  2. Compare with `current`.
  3. Write.
  4. Validate the node against the schema.
  5. Append the record to `data/changes.jsonl`.
- Result per record: applied, already applied, or skipped with a reason. The exit code is
  non-zero when anything is skipped, as today.
- One git commit per applied run. The message is the run id.
- Read from the log:
  - **Provenance** of a field: its last record (source, pass, run, ts).
  - **`checked_at`** of a field: the `ts` of its last record with verdict correct, wrong,
    outdated or new.
  - **Stale**: `checked_at` older than the policy (proposed: 3 months).
- Bootstrap, once the ids exist: the 2026-10-09 fact-check (165 items) is converted into
  records.
  - The 103 confirmations date their fields to 2026-10-09.
  - The 44 applied corrections are recorded.
  - The 16 unverifiable items are logged and listed for the next verify run.

### 4.7 Tables (derived copy)

This is the model from `lakebase-architecture.md`, with fixes:

- `node`: `id` (text PK), `home_tree`, `home_parent_id`, `ordinal`, `n`, `sub`, `note`,
  `type` (`CHECK`), `s`, `c`, `since`, `new`, `deck`, `solves_conf`
- `node_doc`: `node_id`, `ordinal`, `url`
- `solves_row`: `node_id`, `ordinal`, `axis`, `problem`, `solution`
- `placement`: `tree`, `parent_id`, `ordinal`, `node_id` (one row per `ref`)
- `see`: `node_id`, `target`
- Matrix tables as designed: `matrix`, `competitor`, `matrix_group`, `capability`, `cell`,
  `verdict`. Plus a `legend` reference table.
- `change`: the log, one row per record
- View `field_check`: `id`, `field`, `checked_at`, `source`, computed from `change`
- `area`: the manifest

The round-trip test from `lakebase-architecture.md` stays: JSON → tables → JSON gives
identical output.

### 4.8 Flows and tools

| Flow | Today | Reconciled |
|---|---|---|
| Produce | Agents briefed from the chat | Docs seed script, research agents and merge script give `skeleton.json`. Then human validation, then records (`verdict: new`), then the applier |
| Enrich | Agents, then `notes_rewrite.py merge` | Pipeline task (generate → judge → repair), then `review.md`, then accepted records, then the applier |
| Verify against docs | not built | Pipeline task `verify`: fetches the node's doc URLs, judges each claim against them, emits records |
| Verify on the open web | `fable-fact-check-prompt.md` run by hand in a model with web search, then `apply_fact_check.py` | Same prompt, versioned in `prompts/`, with output already in record form. Run periodically, through the same applier |

### 4.9 Where quality is checked

| Check | Where | What a failure stops |
|---|---|---|
| Schema: fields, enums, `type` | applier and build | the write, the build |
| Unique ids; `ref`, `see`, manifest and Story references resolve | build | the build |
| At least 1 doc link per capsule in live areas | build | the build |
| Content rules: writing, grounding | pipeline judge | the record: repair, then review |
| Facts against docs or the web | verify runs | nothing; they produce records for review |
| Coverage and counts per area | tally script | publishing the area |
| Human review | skeleton per area, `review.md` per run, publishing | — |

## 5. Conflicts resolved

| # | Conflict | Between | Resolution |
|---|---|---|---|
| 1 | Targeting nodes by name path or by stable id | scripts, Story, pipeline / lifecycle, plan | Id. Path for reading only |
| 2 | Four change formats | fact 5 | One record (§4.5) |
| 3 | Overwrite or compare-and-set | `notes_rewrite.py` / `apply_fact_check.py` | Compare-and-set |
| 4 | Confirmations not kept | lifecycle / applier | Logged. They date `checked_at` |
| 5 | Where provenance and `checked_at` live | lifecycle (per field) / plan (not specified) | Read from the change log |
| 6 | System of record | Lakebase doc / pipeline, plan | JSON in git (S1) |
| 7 | git assumed but absent | Lakebase doc open point 1 | `git init` (R0) |
| 8 | Genie path; synced tables described backwards | Lakebase doc open point 2 | Delta export (S2), or Lakebase Change Data Feed |
| 9 | `type` `CHECK` but no `type` column | lifecycle / Lakebase doc | Column added (§4.7) |
| 10 | `solves` and `solves_conf` missing from the tables | Lakebase doc / data | `solves_row` table, `solves_conf` column |
| 11 | `tree` limited to 'ai' / 'ds', one parent per node | Lakebase doc / plan D2 | `home_tree` + `placement` + `see` |
| 12 | `compete-*.json` files or a matrix inside the node | Lakebase doc / data, spec | Inside the node |
| 13 | Live matrix does not match the schema | data / schema | `feature` and `legend` optional; ids added |
| 14 | One legend per matrix or a shared legend | schema / Lakebase doc open point 3 | Shared default, optional override |
| 15 | `soft` listed as node metadata | lifecycle / schema | Matrix-cell flag, and a verify target |
| 16 | `since` required but never shown | plan D5 / app | Optional, fixed format |
| 17 | Types checked at build only, or at write | `build.py` / lifecycle | The applier checks too (S4) |
| 18 | Rules in the spec or in the prompts | pipeline open point 6 | Schema = machine contract, prompts = writing rules, spec = intent |
| 19 | Overlap allowed, or one shared node | DS plan / plan D2 | One shared node |
| 20 | Verify only through the pipeline, or the open-web fact-check | pipeline / 2026-10-09 run | Two verify modes, same record |

## 6. Merged roadmap

| Step | Content | Replaces | Done when |
|---|---|---|---|
| R0 Repository | Own folder (plan D6), `git init`, first commit of the current state | — | Repository holds today's state |
| R1 Contracts | Ids on the 655 nodes. `schemas/node.json`. Matrix schema fix and ids. Change record. Applier and log. Fact-check bootstrap | Lifecycle shared foundation; the ids in plan P0; `apply_fact_check.py`; `notes_rewrite.py merge` | Build passes. Log holds the 165 records of 2026-10-09. `checked_at` is set on the 103 confirmed fields |
| R2 Several trees | Manifest, `trees/`, `ref` / `see`, the 8 duplicates, Story by id, gates | Rest of plan P0 | Compiled AI and DS trees equal today's, apart from the ids and merged duplicates |
| R3 Navigation | Plan P1 | — | As in the plan |
| R4 Pipeline | Tasks `children`, `note`, `type`, `verify`. `prompts/`, including the fact-check prompt. `review.md`. Uses the R1 applier | `pipeline-design.md`; plan P2 | One docs-verify run over AI and DS produces records and a review file |
| R5 Pilot area | Plan P3 | — | As in the plan |
| R6 Adjust | Plan P4 | — | As in the plan |
| R7 Other areas | Plan P5 | — | As in the plan |
| R8 Enrichment | Plan P6 | — | As in the plan |
| S Tables and Genie | Export script, DDL, load, round-trip test, Genie space | First step of the Lakebase doc | Round-trip output identical. Genie answers "which fields were not checked since X" |

S can start any time after R1, and not before: without ids and the log, the tables have no
keys and no `checked_at`.

## 7. Open decisions

Added by this synthesis:
1. S1: system of record, JSON in git (proposed) or Lakebase.
2. S2: table target, Delta (proposed) or Lakebase.
3. Staleness policy (proposed: 3 months).
4. Location of the log (proposed: `data/changes.jsonl`).
5. Deck data lives in two places: `deck` on 10 AI capsules, and `docs/internal-decks.md`.
   Unify in R8 or keep both.
6. Workspace: extend `agent` before 2026-12-21, or move the app and the pipeline to a
   workspace that does not expire.

From the plan: D1a to D1d, D2 (home of Feature Store and AutoML), D3, D4, D6, pilot area.

From the pipeline:
- Model endpoints for the generator and the judge.
- Whether a model with web search can be called from code, for the open-web verify.
- Glean from code.
- Review format.
- Where runs execute.

## 8. Risks

| Risk | Effect | Mitigation |
|---|---|---|
| Workspace expiry on 2026-12-21 | App offline. Pipeline loses its model endpoints | Extension before expiry, or a workspace that does not expire. Data stays safe in git (S1) |
| Change Data Feed changes while in Public Preview | Genie path breaks | S2 defaults to the Delta export, with no preview dependency |
| Records that address by index (`solves[i]`, `docs[i]`) | Wrong row if rows are reordered | The `current` check skips the record |
| Log size | Thousands of records per area | JSONL. Split per area if needed |

## 9. Changes each source document needs (after validation)

| Document | Change |
|---|---|
| `docs/lakebase-architecture.md` | l.8: the data files are `ai-tree.json`, `ds-tree.json`, `story.json`; there is no `compete-*.json`. l.45-47: `node` table per §4.7. l.79: there is no git today. l.86-88: synced tables go from Unity Catalog to Postgres; Genie path per S2. Status of Lakebase per S1. Add where the database runs and the workspace expiry |
| `docs/data-lifecycle-architecture.md` | l.3: one verify run exists (2026-10-09). l.24: record per §4.5. l.61-62: `soft` is a matrix-cell flag; add `solves_conf`. l.65: confirmations are logged. "Why Lakebase": per S1 |
| `docs/pipeline-design.md` | Apply by id. `results.json` / `accepted.json` become records. Add task `children`. Two verify modes. Open point 3 settled. Review = `review.md` + one git commit per run |
| `docs/compete-matrix.schema.json` | `feature`, `featurePath` and `legend` optional. Shared legend file |
| `docs/panel-slide-spec.md` | Node schema: add `id`, `ref`, `see`. Point to `schemas/node.json` |
| `docs/story-design.md` | References by id |
| `plan/ds-ecosystem-plan.md` | "Overlap allowed" superseded by plan D2 |
| `docs/plan/platform-expansion.md` | §5.6 replaced by §4.7 here. P0 split into R1 and R2. D5: `since` optional. Add the open-web verify mode. Provenance read from the log |
