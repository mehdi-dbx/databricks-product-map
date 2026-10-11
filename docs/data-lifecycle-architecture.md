# Data lifecycle architecture — produce, enrich, verify (design, not built)

Status: proposed. Today none of this exists as a reproducible process. The project
was produced ad hoc (inline scripts, no trace) with scattered md. This defines the
machine that would reproduce the dataset and maintain it over time.

## The problem

- Transformations were run inline (classification, population, merges) and not
  saved. The "how" is gone.
- The md are descriptive, not executable.
- There is no stable node identity, no patch channel, no provenance, no freshness
  check. "Future passes" means re-doing work by hand, like the note-fill merge.

## Shared foundation (all three flows depend on it)

Without this, every flow stays manual.

- **Stable node id.** A persistent `id` per node, not the runtime `_id++`. The
  anchor every pass targets. Path-based targeting breaks on rename.
- **Provenance per field.** `source`, which pass set it, when.
- **`checked_at` per field (or per node).** Last time the fact was verified. Without
  it, "is this still valid" is unanswerable.
- **One patch format.** `{id, field, value, source, pass, ts}`. All three flows
  emit patches onto this channel; an idempotent, non-destructive applier merges
  them (does not rewrite the rest of the node). Conflict policy: last-verified wins,
  or explicit.

In JSON this is simulated: persistent ids + an append-only patch log + a
deterministic applier. In a DB it is native: upsert by PK, per-row `updated_at`,
audit table, `CHECK` constraints. The DB makes identity and provenance structural
instead of simulated — see the Lakebase conclusion below.

## Flow 1 — Produce

Builds the skeleton and compiles the Pack.

- raw research → tree structure (nodes, hierarchy)
- classification: every d2+ node gets a `type` (feature / family / primitive /
  concept) — enforced by the build gate in `app/build.py`
- export → `ai-tree.json` / `ds-tree.json` (the Pack) → `build.py` → static HTML

One-shot per run. Deterministic. Each stage a versioned script, not inline.

## Flow 2 — Enrich

Adds or updates content on existing nodes over time, without a full rebuild.

- a pass targets nodes by **stable id** and emits patches (e.g. add `solves`,
  `matrix`, deepen notes, add children)
- the applier merges them idempotently and non-destructively
- every patch carries provenance

This is the channel that makes future passes repeatable instead of hand-merged.

## Flow 3 — Verify

Checks whether existing content is still true, because product facts drift
(Beta→GA, renames, a matrix cell changes, a competitor catches up).

- metadata per field: `source`, `checked_at`, `confidence` (we have fragments: `c`,
  `soft`, `since` — but no `checked_at`)
- a staleness policy: a TTL / cadence; a field not verified in N months is stale and
  flagged
- a re-check pass re-grounds against docs/Glean: confirm → bump `checked_at`; drift
  → patch the value + flag
- a staleness query: "what hasn't been verified since X / what is flagged" — trivial
  in SQL; Genie could answer it

Verify is **not a separate mechanism** — it is a pass that emits patches on the same
channel (confirm = patch `checked_at`; drift = patch value + flag). What makes it a
flow is the metadata (`checked_at`, confidence), not the plumbing.

## Summary

Three flows, one patch channel:

| Flow    | Does                                  | Emits                         |
|---------|---------------------------------------|-------------------------------|
| Produce | skeleton + classify + build           | the Pack                      |
| Enrich  | add/update content on stable ids      | patches                       |
| Verify  | re-check validity, flag drift         | patches (`checked_at` / drift)|

All three need: stable id + provenance + `checked_at`.

## Why Lakebase (conclusion)

Produce alone does not justify a database — the data is small and read-only, JSON is
fine. The justification is **enrich + verify**, which are the real ongoing load and
which need exactly what a DB provides structurally and JSON only simulates:

- **upsert by PK + `updated_at` + audit table** = the patch channel, natively
- **`type text NOT NULL CHECK (type IN (...))`** = typing enforced at write (upstream),
  not caught late at build
- **staleness queries / SQL / Genie** = "what is no longer verified", trivial
- governed by Unity Catalog, on-platform, consistent with the app

Where the DB does **not** apply: the display path stays JSON, generated and served
statically. The app never talks to the database at runtime.

So the switch is justified by maintenance over time, not by storage. The DB makes the
shared foundation (id, provenance, `checked_at`, upsert, constraints) structural
instead of hand-rolled.

## Related

- `lakebase-architecture.md` — the DB-as-source design and the Pack export path.
- `panel-slide-spec.md` — the `type` field + per-type panel templates (produce/classify).
- `compete-matrix.schema.json` — matrix structure enriched/verified per node.
