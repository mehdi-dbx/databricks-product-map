# Data architecture — Lakebase as source of truth (design, not yet built)

Status: proposed, under discussion. Nothing migrated yet.

## Goal

Make the project robust, scalable, and enrichable. Today the data is a single
JSON "Pack" (`ai-tree.json`, `ds-tree.json`, `compete-*.json`), edited by hand or
by agent swarms and built into static HTML. We want to:

- consult the data easily via **SQL and Genie**
- **maintain and update** it as a database, not a hand-edited file
- keep the UI fast: the JSON Pack is still **generated** and handed to the app for
  display, so the app never talks to the database at runtime.

## Architecture

Lakebase is the system of record. The JSON Pack becomes a compiled, read-only
build artifact derived from it.

```
Lakebase (Postgres, source of truth — editable, SQL/Genie queryable)
    │  export (recursive query → nested JSON)
    ▼
ai-tree.json / ds-tree.json / compete-*.json   (the generated Pack)
    │  build.py
    ▼
app/static/index.html → Databricks App
```

Properties:

- The app stays static-JSON at display time. No DB dependency, no runtime latency,
  no new failure mode on the presentation path.
- Authoring, querying and maintenance move to Lakebase.
- The Pack is a cache/read-model, regenerated on change.

## Relational model (storage-agnostic; same whether JSON today or Lakebase later)

The tree is hierarchical, so `node` is an adjacency list. Compete matrices reuse
the structure already defined in `compete-matrix.schema.json`.

Tables:

- **node** — `id`, `tree` ('ai' | 'ds'), `parent_id` (nullable, self-FK),
  `ordinal`, `name`, `sub`, `status`, `confidence`, `note`, `since`, `deck`,
  `new` (bool). Depth is derived, not stored.
- **node_doc** — `node_id` (FK), `url`, `ordinal`.
- **matrix** — `id`, `node_id` (FK, the feature this matrix belongs to),
  `home_competitor_id`, `updated`, `sources`.
- **competitor** — `id`, `matrix_id` (FK), `name`, `home` (bool), `segment`,
  `vendor`.
- **matrix_group** — `id`, `matrix_id` (FK), `label`, `ordinal`.
- **capability** — `id`, `group_id` (FK), `label`, `ordinal`.
- **cell** — `capability_id` (FK), `competitor_id` (FK), `status`, `note`,
  `emphasis` (bool), `soft` (bool).
- **verdict** — `matrix_id` (FK), `dimension`, `home_text`, `field_text`,
  `winner` ('home' | 'field' | 'parity').

Legend and segment definitions can live in small reference tables or as a JSON
column on `matrix`, to be decided when we write the DDL.

## Export step

A script reads the tables and rebuilds the nested JSON Pack:

- recurse on `parent_id` to assemble each tree, ordered by `ordinal`
- aggregate `node_doc` into each node's `docs`
- assemble matrices from `matrix` / `competitor` / `matrix_group` / `capability` /
  `cell` / `verdict`

Easiest in Python at build time: fetch flat rows, build the nesting in memory,
write the JSON files, then run the existing `build.py` unchanged (plus one upstream
step).

## Open points to settle before building

1. **Write / review workflow.** This decides the robustness we are after. Today
   enrichment goes through files in git, so every change has a diff, a PR, and a
   rollback. Postgres does not give PR-style review for free. Two options:
   - agent swarms write to the database directly (fast, but the git audit trail is
     lost unless we add one)
   - swarms keep producing JSON, which is reviewed, then loaded into the database
     (keeps the audit trail, adds a load step)
2. **Genie path.** Genie answers over Unity-Catalog-governed tables through a SQL
   warehouse. Lakebase has UC integration and a synced-tables mechanism to Delta;
   we must confirm which one to wire so a Genie space sees these tables. Direct SQL
   on Postgres works immediately regardless.
3. **Legend/segments storage** — reference tables vs JSON column on `matrix`.

## Recommended first step

Build the backbone first, migrate nothing:

1. Write the target Postgres DDL.
2. Write the export script and run it against the current JSON to prove the model
   round-trips on real data (JSON → tables → JSON, identical output).

Lakebase provisioning and the Genie wiring come after the model is proven, once the
UC path is verified.

## Related

- `compete-matrix.schema.json` — the matrix structure, already a first step toward
  this relational model.
- `panel-slide-spec.md` — the panel/mini-slide design the Pack feeds.
- `app/build.py` — the current build; gains one upstream export step.
