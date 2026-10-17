# Plan: Expand the explorer from AI + DS to every Databricks platform area

> Status: PLANNED

Created 2026-10-09. Nothing in this plan is built. Decisions D1 to D6 are proposals from the
2026-10-09 discussion. None is validated yet.

Terms: **area** = a top-level area of the Databricks docs. **tree** = one mindmap.
**pillar** = depth 1. **capsule** = depth 2. **leaf** = depth 3 and below.

## 1. Goal

The app started as an explorer of the Databricks AI and Data Science features. The goal is
the same explorer for every area the platform covers: one tree per area, the same panel, the
same quality bar.

## 2. Current state

Checked on 2026-10-09.

| Item | Today |
|---|---|
| Trees | `ai-tree.json`: 11 pillars, 48 capsules, 269 leaves (329 nodes, 3 levels). `ds-tree.json`: 7 pillars, 11 capsules, 307 nodes below them (326 nodes, 4 levels) |
| Other tabs | Story: 11 chapters, 40 points, 59 capsule references by name path. Decks: rendered from `docs/internal-decks.md` |
| Build | `app/build.py` puts both trees, the Story and the Decks into one HTML file (317 KB). Gates: valid JSON, `type` on every d2+ node, every Story reference resolves |
| Node identity | No persistent id. `mindmap.js` numbers nodes at load (`_id++`). Scripts target nodes by name path (`scripts/tree_walk.py`) |
| Shared features | Copied. 8 node names exist in both trees. Feature Store: the AI copy has 4 children and 1 doc link, the DS copy has 8 children and 6 doc links, and the notes differ |
| Navigation | 4 fixed tabs (`navTabs` in `template.html`). Search walks only the open tree (`mindmap.js:272`) |
| Doc links | AI: 47 of 317 d2+ nodes, all capsules. DS: 33 of 318 |
| `since` | Free text that mixes status and dates ("GA", "Beta (Sep 16 2026)") |
| Production | Research agents briefed from the chat (`run/`, `.swarm/`). The code pipeline in `docs/pipeline-design.md` is not built |
| Version control | The project folder is not a git repository |
| Deploy | Databricks App `ai-tree-mindmap`, profile `fevm-agent`, internal only |

## 3. Platform areas

Source: docs.databricks.com home and each area's landing page, fetched 2026-10-09. Paths are
under `https://docs.databricks.com/aws/en`.

The home page lists 11 areas: 8 under "Explore Databricks" and 3 under "Manage Databricks".
Compute and Delta Lake have their own landing page but no card on the home page.

| # | Area | Docs entry | Landing-page sections (abridged) | Already in the trees | Proposed tree |
|---|---|---|---|---|---|
| 1 | AI and machine learning | `/machine-learning/` | Get started · Train classic ML models · Train deep learning models · Deploy and serve models · Monitor and govern ML systems · Productionize ML workflows | AI tree, DS tree | keep `ai`, `ds` |
| 2 | Databricks AI/BI | `/ai-bi/` | AI/BI concepts · BI tools · Genie One · Dashboards · Genie Agents · Unity Catalog semantics · Admin guide · Consumer access | Genie One, Genie Agents, AI/BI Dashboards, Genie Ontology | new `aibi` |
| 3 | Data engineering | `/data-engineering/` | Lakeflow Connect · Lakeflow pipelines · Lakeflow Designer · Lakeflow Jobs · Databricks Runtime for Apache Spark · Structured Streaming | Lakeflow | new `de` |
| 4 | Data warehousing | `/sql/` | Interfaces and tools (SQL editor, dashboards, metric views, alerts, ETL) · Monitor and optimize (query history, query profile, query performance insights) | Lakehouse//RT | new `dw` |
| 5 | OLTP databases (Lakebase) | `/oltp/projects/` | Get started (serve lakehouse data, store Postgres changes in the lakehouse, build applications) · Key features (autoscaling, scale to zero, branches, read replicas, instant restore, HA, DR) · Connect and query | Lakebase, Lakebase Search, LTAP | new `lakebase` |
| 6 | Data sharing | `/data-sharing/` | OpenSharing · Marketplace · Clean Rooms | none | new `sharing` |
| 7 | Develop on Databricks | `/developers/` | Start coding · Build custom apps (Databricks Apps, IDE extensions) · SDKs · Connect (Databricks Connect, SSH tunnel, SQL drivers) · Manage infrastructure (CLI, Declarative Automation Bundles, Terraform, CI/CD) · Collaborate (UDFs, Git folders) | Databricks Apps, Genie App Builder | new `dev` |
| 8 | Data governance with Unity Catalog | `/data-governance/` | Access control · Governed tags · Data discovery · Data and AI lineage · Data classification · Data quality monitoring · Auditing · Data sharing · AI governance with Unity Gateway | Unity Catalog for AI assets, the 2 Agentic Data Management capsules | new `gov` |
| 9 | Security and compliance | `/security/` | Authentication and access control · Networking · Data security and encryption · Secret management · Compliance | none | new `sec` |
| 10 | Administration | `/admin/` | Account administration · Workspace deployment · Workspace settings · Identity management · Compute policies · Governance Hub · System tables · Audit logs · Cost management | none | new `admin` |
| 11 | Data guides | `/guides/` | Task index over the other areas: find and access data, work with data, configure data access, configure workspaces, productionize | none | no tree (D1b) |
| 12 | Compute (no home card) | `/compute/` | Serverless compute · Classic compute · SQL warehouses · Photon · Lakeguard | none | new `compute` (D1c) |
| 13 | Delta Lake (no home card) | `/delta/` | Ingest and convert · Update tables · Incremental and streaming · Table history · Schema · Files and indexing · Settings | Lakehouse / Delta Lake, Predictive Optimization | new `storage` (D1c) |

The "Already in the trees" column places the existing AI capsules by their doc link, or by
their note when the link is a blog post.

The docs themselves list the same feature in several areas. Dashboards and metric views
appear under both Data warehousing and AI/BI. Data sharing appears under Governance and as
its own area. Unity Catalog, Lakeflow Jobs and Declarative Automation Bundles appear under
AI and machine learning. D2 follows from this.

## 4. Decisions

All proposed, none validated.

### D1: One tree per docs area

- The areas and their names come from the docs (table in §3). Each area gets one tree. Its
  landing-page sections are the first draft of its pillars.
- Reason: the boundaries are Databricks' own, so they need no defence. A feature's doc URL
  tells which area it belongs to.
- Sub-decisions:
  - **D1a.** AI and DS stay as two trees inside area 1 (proposed), or merge.
  - **D1b.** Data guides gets no tree (proposed). It indexes tasks across the other areas.
  - **D1c.** Compute and Delta Lake get their own trees (proposed), or fold into Data
    engineering, Data warehousing and Administration.
  - **D1d.** Order in the app follows the docs grouping: Explore areas, then Manage areas.
- With D1a to D1c as proposed: 13 trees, of which 11 are new.

### D2: A shared feature is stored once

- Every node gets a stable `id`. A node is written in full once, in its home tree. Another
  tree that shows it places a reference stub `{"ref": "<id>"}`. The build replaces the stub
  with a copy of the node and its subtree.
- A second relation, `see`, links related but distinct nodes, or points to a whole tree.
- Rule for choosing between the two:
  - Same feature, same scope → `ref`. Examples: Feature Store (AI ↔ DS), Genie Agents
    (AI ↔ AI/BI), Databricks Apps (AI ↔ Develop).
  - Different scope → separate node + `see`. Examples: "Unity Catalog for AI assets" (AI)
    → `unity-catalog` (Governance). The AI capsule "Lakeflow", which summarizes the whole
    Data engineering area → `see: ["de"]`.
- Home rule: the home tree is the area of the node's primary doc URL. Ties are decided by
  hand and recorded in the area's `AREA-TREE.md`.
- Alternative: keep copies, as the DS plan allowed ("overlap allowed"). Not proposed: the
  copies already drift (Feature Store), and every enrich or verify pass would run once per
  copy.
- Model details: §5.

### D3: Navigation for 13 trees

- A **Platform view**: one map whose first level is the areas and second level their
  pillars. A click on an area or a pillar opens that tree.
- An **area switcher** in the top bar, grouped Explore / Manage, replaces the per-tree tabs.
  Story and Decks stay as tabs.
- **Search across all trees**. Results are listed by area in a dropdown, the same pattern as
  the Story search (`storyResults`). Choosing a result opens its tree and focuses the node.
- In the panel: **"Also in"** chips for shared nodes and **"See also"** chips for `see`
  links. A click switches tree and focuses the node.
- **Deep link** `#<tree>/<id>` opens a node directly.
- Size: one HTML file stays. 317 KB today for about 650 nodes. About 1.2 MB expected at
  about 3,000 nodes with today's density.
- App changes: §6.

### D4: Production: docs seed, research agents, then the pipeline

- The skeleton of a new area is seeded from its docs pages by a script, with no model. Names
  come from the official docs.
- Research agents add what the docs miss: previews, announcements, renames, internal names.
  Same method as for AI and DS: public web, Glean and Sage; live logs; ✅ / 🟡 tags.
- From the validated skeleton onward, the code pipeline in `docs/pipeline-design.md`
  produces the content: leaves from the doc pages, notes, type, verify. A human reviews
  before anything is applied.
- The foundations (ids, refs, manifest, gates) and a minimal pipeline are built before the
  pilot area.
- Alternative: build each area the AI/DS way, with chat-briefed agent swarms. Faster to
  start, but it repeats what `pipeline-design.md` was written to replace, at about 5 times
  the volume.
- Stages: §7.

### D5: Content bar for the first version of an area

- Required to publish an area:
  - pillars: `n`, `note`
  - capsules: `id`, `n`, `note`, `type`, `s`, `c`, `docs` (at least 1), `since`, `new`
  - leaves: `id`, `n`, `note`, `type`
- Deferred to later passes, area by area: `solves`, `matrix`, `deck`. The competitors differ
  per area, so each Landscape is its own research:
  - warehousing: Snowflake, BigQuery
  - engineering: Fivetran, dbt, Airflow
  - governance: Collibra, Purview
  - Lakebase: Aurora, Neon
  - BI: Power BI, Tableau
- The Story and Decks tabs stay AI/DS in this plan.
- `since` gets a fixed format on new nodes. Proposed: `YYYY-MM` plus the event, for example
  `2026-06 DAIS`. The status stays in `s`.

### D6: Project framing

- A platform-wide explorer serves the whole field team. It is not an Amadeus deliverable. The
  Story is already generic (decided 2026-10-08).
- To decide:
  - Stay in `Report/AmadeusAI` or move to its own folder.
  - Display title (today "Databricks Ecosystem Trees").
  - App name `ai-tree-mindmap`. A rename creates a new app with a new URL.
- Proposed: its own folder as a git repository, keep the app name, change the title. About
  3,000 nodes edited by scripts and pipeline runs need diffs and rollback, and the folder has
  no git today.

## 5. Data model

### 5.1 Files

```
app/src/
  areas.json        manifest: order, key, title, group, docs entry, file, state (draft | live)
  trees/
    ai.json  ds.json  aibi.json  de.json  dw.json  lakebase.json  sharing.json
    dev.json  gov.json  sec.json  admin.json  compute.json  storage.json
  story.json
  mindmap.js  styles.css  template.html
```

`ai-tree.json` and `ds-tree.json` move to `trees/ai.json` and `trees/ds.json`.

Manifest entry:

```json
{"key": "gov", "title": "Data governance", "group": "Manage",
 "docs": "https://docs.databricks.com/aws/en/data-governance/",
 "file": "trees/gov.json", "state": "draft"}
```

Only `live` areas go into the app. `python3 build.py --drafts` includes drafts for review.

### 5.2 Node

Today's fields, plus `id` and `see`. A home node:

```json
{"id": "unity-catalog", "n": "Unity Catalog", "type": "feature", "note": "…",
 "s": "GA", "c": "ok", "docs": ["https://docs.databricks.com/aws/en/data-governance/unity-catalog/"],
 "since": "…", "children": ["…"]}
```

A reference stub, placed in another tree:

```json
{"ref": "feature-store"}
```

A separate node with a link:

```json
{"id": "uc-for-ai-assets", "n": "Unity Catalog for AI assets", "see": ["unity-catalog"], "…": "…"}
```

### 5.3 Ids

- Lowercase kebab slug, unique across all trees. Leaves: `<parent-id>.<slug>`.
- Assigned once at creation and never regenerated. A rename changes `n`, not `id`. A move to
  another tree keeps the id.
- The 655 existing nodes get ids from one migration script. Its output is reviewed before it
  replaces the files.

### 5.4 Build gates (`app/build.py`)

Kept: valid JSON. `type` on every d2+ node. Story references resolve.

Added:

1. Every node has an `id`. Ids are unique across all trees.
2. Every `ref` resolves to a home node. A stub has no other field. A ref never points to
   another ref. A node appears at most once per tree.
3. Every `see` target resolves, to a node id or a tree key.
4. Every capsule of a `live` area has at least one `docs` URL.
5. Story references resolve by `id`.
6. Every manifest `file` exists, and every tree file is in the manifest.

Build output: `TREES = {key: compiled tree}` with refs expanded and an `alsoIn` list on every
shared node. Also `AREAS = manifest` and `STORY`.

### 5.5 Migration of AI and DS

1. Assign ids (script, reviewed).
2. Resolve the 8 duplicated names one at a time. Same feature: merge into one home node and
   place a `ref` in the other tree. Different scope: keep both and add `see`. Proposed for
   Feature Store and AutoML: merge, with DS as home, since the DS copies are the richer ones.
3. Move Story references from name path to id. `app/src/story.json` holds ids, and
   `scripts/story_check.py` and the build gate check them.
4. The AI capsules that belong to another area (§3) stay in the AI tree until that area is
   built. Then each moves to its home tree with the same id, and the AI tree keeps a `ref` or
   a `see` (rule in D2).

### 5.6 Later move to Lakebase

The model maps onto the tables in `docs/lakebase-architecture.md`:
- `node` keeps its home `tree` and `parent_id`.
- Two tables are added: `placement` (tree, parent_id, ordinal, node_id) and `see` (node_id,
  target).

Nothing in this plan depends on that move.

## 6. App changes

| File | Change |
|---|---|
| `template.html` | Top bar: Platform, area switcher (Explore / Manage), Story, Decks. Title per D6 |
| `mindmap.js` | Load `AREAS`. `loadTree(key)` for any area. Platform view built from the manifest and each tree's pillars. Search dropdown across all trees. "Also in" and "See also" chips in the panel. Hash deep links. The Story "see in tree" link opens a node by id |
| `styles.css` | Switcher, chips, Platform view |
| `build.py` | Manifest, ids, refs, `see`, gates (§5.4) |
| `app.py` | No change |

Platform view, two options:
- a generated tree that reuses the mindmap renderer and looks like the rest of the app
  (proposed)
- a card grid, simpler to build

## 7. Production of one area

The same stages for every area. `<a>` is the area key. Working files go under `run/<a>/`.

| # | Stage | Done by | Output | Check |
|---|---|---|---|---|
| 0 | Docs seed: read the area landing page and its section pages, extract sections and feature pages with their URLs | script, no model | `run/<a>/seed.json` | none |
| 1 | Cartography: public web (blog, DAIS, release notes), Glean, Sage. Live logs. ✅ / 🟡 per node | 3 research agents | `run/<a>/tree-{public,glean,sage}.json` and `.md`, `agent-*.md` | structure checked by script |
| 2 | Merge: seed + 3 sources into pillars and capsules. Dedup by doc URL, then by name. Mark features that already exist in another tree (`ref` or `see`) | script, then orchestrator resolves flagged conflicts | `run/<a>/skeleton.json`, `AREA-TREE.md` (review view) | **Mehdi validates the skeleton** |
| 3 | Skeleton: write `trees/<a>.json` with `id`, `type`, `n`, draft `note`, `s`, `c`, `docs`, `since`, `new`. Manifest state `draft` | script from `skeleton.json` | tree file | build gates |
| 4 | Leaves: children of each capsule, from its doc pages | pipeline task `children` | `runs/<run-id>/results.json`, `review.md` | judge, then human accept |
| 5 | Content: notes, type, verify | pipeline tasks `note`, `type`, `verify` | same | judge, then human accept |
| 6 | Tally: counts per depth, field presence, link check (HTTP 200), open 🟡 items, refs | script | `run/<a>/TALLY.md` | numbers come from the files, never from agent reports |
| 7 | Publish: state `live`, build, render check, deploy | orchestrator | app | Mehdi |

- `children` is a new pipeline task. The tasks in `pipeline-design.md` are `note`, `solves`
  and `type`, plus the verify flow.
- `children` uses the capsule's doc URLs as its sources and may only list items present in
  those pages.
- Items found only by the research agents enter as 🟡 with their source.

## 8. Phases

| Phase | Content | Done when |
|---|---|---|
| P0 Foundations | D6 folder and git. Manifest, `trees/`, ids on the 655 nodes, `ref` and `see`, gates §5.4. Duplicates resolved. Story references by id | Build passes. Compiled `TREES.ai` and `TREES.ds` equal today's files except for the added ids and the merged duplicates. Every duplicate has a recorded decision |
| P1 App navigation | §6: switcher, Platform view, search across trees, chips, deep links | Works with AI, DS and one empty draft area |
| P2 Minimal pipeline | `pipeline-design.md` with tasks `children`, `note`, `type`, `verify`. Review file. Apply by id | One verify run over AI and DS produces a review file. The pipeline's open points 1, 2 and 4 are settled |
| P3 Pilot area | Stages 0 to 7 on one area | Area live. Tally meets §9. Retro written |
| P4 Adjust | Fix the method from the pilot retro, once, in one update to this plan | Updated plan validated |
| P5 Other areas | Waves (below) | Each area live with its tally |
| P6 Enrichment | Per area: `solves`, Landscape and `matrix`, deck hunt, Story and Decks scope | Separate plans |

Pilot, proposed: **Data governance**. Most other areas will point to its nodes (Unity
Catalog), so building it first gives the later areas their `ref` and `see` targets. It also
tests both relations on real content: the 2 Agentic Data Management capsules (`ref`) and
"Unity Catalog for AI assets" (`see`). Alternative: AI/BI, which is smaller.

Waves, proposed:
- Wave 1, areas that already have AI capsules: AI/BI, Data engineering, Lakebase, Develop.
- Wave 2: Data warehousing, Data sharing, Compute, Delta Lake.
- Wave 3: Security and compliance, Administration.

## 9. Quality bar to publish an area

- Every docs landing-page section of the area maps to a pillar or a capsule, or is dropped
  with a written reason.
- Every capsule has at least one doc URL that answers HTTP 200.
  - Prefer docs.databricks.com.
  - A blog or press URL only for features with `s` = Announced or `c` = verify.
- No invented feature or URL. A 🟡 item that stays uncorroborated gets one "⚠ unverified"
  child with its source, as in the DS plan.
- Every node has an `id`. Every d2+ node has a `type`.
- Notes pass the judge rubric built from the writing rules in `panel-slide-spec.md`.
- Capsules have 3 to 8 children, as in today's trees.
- All counts in `TALLY.md` are computed from the files.

## 10. Estimates

- 11 new trees with D1a to D1c as proposed.
- Docs sections suggest 3 to 9 pillars per new area.
- 150 to 300 nodes per new area gives 1,700 to 3,300 new nodes, about 2,300 to 4,000 in
  total. Today's trees are about 330 nodes each.
- HTML: about 1 to 1.6 MB.
- Human checkpoints per area: skeleton (stage 2), pipeline review files (stages 4 and 5),
  publish (stage 7). `pipeline-design.md` allows accepting everything above a judge score,
  which limits line-by-line review.

## 11. Links to the other designs

- `docs/data-lifecycle-architecture.md`:
  - P0 builds its stable ids.
  - P2 writes the run id and date on applied changes, the start of provenance and
    `checked_at`.
- `docs/pipeline-design.md`:
  - P2 builds it, with `children` added.
  - Its open point 3 (stable ids) is settled by P0.
  - Its open points 1 (model endpoint), 2 (Glean from code) and 4 (review format) are
    settled in P2.
- `docs/panel-slide-spec.md`: the writing rules are unchanged. `id`, `ref` and `see` are added
  to its node schema section.
- `docs/story-design.md`: references move from name path to id. Story content is unchanged.
- `docs/lakebase-architecture.md`: out of scope. The model stays compatible (§5.6).
- `plan/ds-ecosystem-plan.md`: D2 replaces its "overlap allowed" rule.

## 12. Risks

| Risk | Mitigation |
|---|---|
| Wrong product names or invented features from public web sources | Names seeded from the docs (stage 0). ✅ needs internal corroboration. No URL without HTTP 200 |
| Agents report more than they did | Tally computed from the files (stage 6) |
| Disputes over which area a feature belongs to | Home rule = area of the primary doc URL. Ties decided by hand and recorded in `AREA-TREE.md` |
| Review load at about 5 times today's volume | Skeleton review is the main human checkpoint. Accept above a judge score in the pipeline |
| Product changes (renames, Beta to GA) | Fixed `since` format, the verify task, `checked_at` |
| Glean cannot be called from code | Internal corroboration stays with the research agents (stage 1). The pipeline uses doc pages only |
| Trees too large to read | Pillars bounded by the docs sections. 3 to 8 children per capsule |

## 13. Open questions for Mehdi

1. D1a to D1d: AI and DS as two trees, no Data guides tree, Compute and Delta Lake as
   trees, Explore / Manage order.
2. D2: the `ref` / `see` model. Feature Store and AutoML homed in DS.
3. D3: Platform view as a generated tree or a card grid.
4. D4: foundations and pipeline before the pilot, or the pilot first with the current method.
5. D5: `since` format.
6. D6: folder, git, title, app name.
7. Pilot area: Data governance (proposed) or AI/BI.
8. Pipeline open points: model endpoint, Glean from code, review format.
