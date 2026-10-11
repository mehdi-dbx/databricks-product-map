# Plan — Data Science Ecosystem Tree (2nd tab)

**Created:** 2026-10-07 · Owner: Isaac (orchestrator) · Method: identical to the AI Ecosystem Tree build.

## Decisions (locked)
- **Scope 1(a):** DS = classic Data Science / ML lifecycle. **Overlap with the AI tree is allowed** (MLflow, Feature Store, AutoML, Model Serving reappear here, framed for DS).
- **Tab label:** "Data Science Ecosystem Tree" (verbatim), same title styling as the AI tab (`<em>Tree</em>` in Lava red).

## Target architecture (clean, maintainable)
- Two data files: `app/src/ai-tree.json` (existing) + `app/src/ds-tree.json` (new).
- `build.py` inlines **both** as `const TREES = { ai:…, ds:… }`.
- `mindmap.js` renders the active tree; the two nav tabs swap `DATA` via `loadTree(key)` (re-walk ids, reset filters/panel, render, fitView).
- One self-contained generated HTML (local `ai-tree-mindmap.html` + `app/static/index.html`), deployed to the `fevm-agent` Databricks App.

## Process (mirrors AI exactly)
### Stage 0 — Cartography (3 sub-agents, parallel, live logs)
- Agents: **ds-public** (web), **ds-glean** (internal), **ds-sage** (curated).
- Each: ratisser large → quality filter → write `run/ds-tree-<src>.md` + live log `run/agent-ds-<src>.md`.
- Confidence tags per node: ✅ confirmed (internal/Sage corroborated) vs 🟡 to-verify (public-only).
- Deliverable target: ≥9 pillars, ≥30 products/features (or blocked-with-reason).

### Stage 1 — Merge → `run/DS-TREE.md`
- Orchestrator fuses the 3 source trees into one master cartography (pillars → capsules), dedup, confidence tags, "new since DAIS", canonical decks/authors captured for later.

### Stage 2 — Skeleton → `app/src/ds-tree.json`
- Author the pillar + capsule skeleton (n, s, c, new?, note) from `DS-TREE.md`. No sub-features yet.

### Stage 3 — Drill-down swarm (per-pillar sub-agents, parallel, live logs)
- One agent per pillar group → `run/ds-leaves/<group>.json` fragments.
- Each leaf gets: `children` (mini-capsules, short labels + one-line note), `docs` (real URLs only), `since`, `deck` (Sage/Glean slug or null).
- 🟡 leaves: verify; if unconfirmed → single `⚠ unverified` child, no fabricated features/URLs.
- Terminal leaves inherit parent `docs` for links (render-level, already implemented).

### Stage 4 — Merge → build → verify → deploy
- Merge fragments into `ds-tree.json` (pillar order preserved), `python3 build.py` (JSON fail-fast), verify render once, then grouped deploy.

## Guardrails (/dontstop)
- Do every pillar & capsule, not a sample. Enumerate counts up front; final tally at the end.
- Force agents to the deliverable target; re-run shorts; spot-check for fabrication (hard fail).
- No fake counts; real sources or the item is marked blocked-with-reason.

## Provisional DS pillars (hypothesis — Stage 0 confirms/replaces)
Data prep & EDA · Feature engineering · Notebooks & collaboration · Experiment tracking (MLflow) · AutoML · Distributed/scaled training & compute · MLOps & CI/CD · Model serving & batch inference · DS languages & libraries (Python/R/Spark/Ray) · Visualization & BI for DS · Governance for DS assets.

## Artifacts
- `run/ds-tree-{public,glean,sage}.md`, `run/agent-ds-*.md` (Stage 0)
- `run/DS-TREE.md` (Stage 1)
- `app/src/ds-tree.json` (Stage 2–3)
- `run/ds-leaves/*.json`, `run/agent-dd-ds-*.md` (Stage 3)
