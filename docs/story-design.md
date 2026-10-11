# Story tab — design (validated first shot, not built)

Status: design validated by Mehdi as a first shot (2026-10-08). Two decisions open (below).

## Principle

A third tab, **Story**, next to the AI and DS trees. It is a continuous narrative read
by scrolling. It is not a slide deck.

The trees are the map. The Story is the guided route through the map.

## Narrative arc

Eleven chapters. Revised after the coverage scan of 2026-10-08, then again to give Governance its own chapter: the first 7-chapter arc
left 4 capsules without a chapter and put 15 capsules in one chapter.

| # | Chapter | Covers |
|---|---------|--------|
| 1 | Challenges | the pain, no capsules |
| 2 | Data and AI foundation | Open table storage with Delta Lake, Ingestion, transformation and table maintenance, Transactional data on the same platform, Real-time analytics on operational data, Data catalog and data quality |
| 3 | Data science lifecycle | Notebooks and data exploration, Feature Store, Experiment tracking and AutoML, Distributed training and GPUs |
| 4 | Model access and governance | Model serving, Foundation models and their lifecycle, Model fine-tuning, External models |
| 5 | Building agents | Batch AI in SQL and pipelines, Retrieval and document question answering, Tool access through MCP, Custom agents, memory and sandbox, Multi-agent orchestration |
| 6 | Evaluating agents | Tracing, Evaluation and prompt versioning, Expert review and labeling |
| 7 | Governance | Unity Catalog for AI assets, Control of AI traffic with Unity Gateway, AI security risks and controls |
| 8 | AI for business users | Natural-language questions on company data, Shared business definitions, No-code assistants built by domain experts, AI-assisted dashboards and spreadsheets, No-code app generation |
| 9 | Developer tools | Application hosting, Coding assistant, Agent development kit and coding-agent harnesses |
| 10 | Domain applications | Customer data application, Security operations application |
| 11 | Production operations | Model registry, Production serving, Monitoring and drift detection, MLOps and CI/CD |

## Capsule coverage (all 59 capsules)

Every d2 capsule of both trees belongs to exactly one chapter. Checked against the
JSON with `scripts/tree_walk.py`: 59 found, 59 placed, 0 duplicates.

| Ch | Tree | Capsule |
|----|------|---------|
| 2 | ai | Lakehouse / Delta Lake |
| 2 | ai | Lakeflow |
| 2 | ai | Predictive Optimization |
| 2 | ai | Lakebase — serverless Postgres |
| 2 | ai | Lakebase Search |
| 2 | ai | Lakehouse//RT |
| 2 | ai | LTAP |
| 2 | ai | Classification / profiling / monitoring |
| 2 | ai | Anomaly detection & remediation |
| 3 | ds | Notebooks & collaboration |
| 3 | ds | Data prep & EDA |
| 3 | ds | DS languages & frameworks |
| 3 | ai | Feature Store |
| 3 | ds | Feature Store |
| 3 | ds | MLflow |
| 3 | ai | AutoML |
| 3 | ds | AutoML |
| 3 | ds | Distributed training & GPU |
| 3 | ai | AI Runtime — serverless GPU |
| 4 | ai | Model Serving |
| 4 | ai | Foundation Model APIs |
| 4 | ai | Model versions |
| 4 | ai | Model lifecycle churn (Oct) |
| 4 | ai | Model fine-tuning |
| 4 | ai | External model services |
| 5 | ai | AI Functions |
| 5 | ai | AI Search (ex-Vector Search) |
| 5 | ai | Knowledge Assistant |
| 5 | ai | Managed MCP servers |
| 5 | ai | External connectors |
| 5 | ai | MCP Services + custom MCP |
| 5 | ai | Custom Agents |
| 5 | ai | Managed memory & sessions |
| 5 | ai | Databricks Sandbox |
| 5 | ai | Supervisor Agent |
| 6 | ai | MLflow 3 for GenAI |
| 6 | ai | Agent evaluation & monitoring |
| 6 | ai | MLflow Prompt Registry |
| 6 | ai | Review Apps |
| 7 | ai | Unity Catalog for AI assets |
| 7 | ai | Unity Gateway |
| 7 | ai | DASF v3.0 |
| 8 | ai | Genie One |
| 8 | ai | Genie Ontology |
| 8 | ai | Genie Agents |
| 8 | ai | AI/BI Dashboards (Lakeview) |
| 8 | ai | Row Zero / Genie ZeroOps |
| 8 | ai | Genie App Builder |
| 9 | ai | Databricks Apps + App Spaces |
| 9 | ai | Genie Code |
| 9 | ai | AI Dev Kit + internal coding agents (Isaac) |
| 9 | ai | Omnigent |
| 10 | ai | CustomerLake |
| 10 | ai | Lakewatch |
| 11 | ai | MLflow Model Registry |
| 11 | ds | Model Registry & governance |
| 11 | ds | Model Serving & batch inference |
| 11 | ds | Monitoring & evaluation |
| 11 | ds | MLOps & CI/CD |

Chapter sizes: 0 · 9 · 10 · 6 · 10 · 4 · 3 · 6 · 4 · 2 · 5 = 59. Governance became its own chapter (7) on 2026-10-08; later chapters moved to 8–11.

Feature Store and AutoML exist in both trees. Both copies sit in chapter 3.
When story.json is built, this table becomes its node references.

## Chapter content

- A short narrative text, written once.
- Capsule cards for the nodes the chapter covers. The cards are pulled from the tree
  JSON (name, status, note, without/with pairs). There is no copy of tree content: when
  a capsule changes in the tree, the Story shows the change.
- A "see in tree" link on each card. It switches to the tree tab and focuses the node
  (same behaviour as the Focus button).

## Visual

A sticky mini-map of the pillars on the side. The pillars of the current chapter light
up as the reader scrolls.

## Data

`app/src/story.json`:

- chapters: id, title, narrative text, list of node references
- a node reference = tree + path (root → node names), same convention as the pipeline

The build fails if a reference does not resolve to a node.

## Decisions

1. **Angle: generic.** The story is a generic Databricks story, with no claims about
   Amadeus (decided by Mehdi, 2026-10-08).
2. **Length: accepted as is.** The proto-story is about 2,100 words, presented while
   scrolling. No further cut is needed (decided by Mehdi, 2026-10-08).

The working draft is `protostory.md`. The readable story is `story.md`, generated from
it by `scripts/story_extract.py`. The check lines are dropped. Each link sentence
becomes the first sentence of the next point, so the text flows from point to point.

## Build plan

What the Story tab is, as described to Mehdi on 2026-10-08.

**v1 built on 2026-10-08, local only.** Everything below is in v1 except the pillar
mini-map. v1 has a chapter rail instead, which lights up the chapter being read. The
points render as slides: title, transition line, one bullet per sentence.
`scripts/story_extract.py` writes `story.json`, and `app/build.py` embeds it and fails
on any reference that does not resolve to a tree node.

**What the user sees, in a third tab next to the two trees:**
- The story, chapter by chapter, read by scrolling. The text is the one in `story.md`,
  generated from `protostory.md` by `scripts/story_extract.py`.
- In each point, the capsules it cites, shown as small cards (name, status, note). The
  cards are pulled from the trees, so a change to a capsule in a tree shows in the
  Story.
- On each card, a "see in tree" link. It switches to the tree tab and centers on the
  capsule, like the Focus button.
- On the side, the list of pillars. The pillars of the chapter being read light up.

**What it touches in the code:**
- A new data file, `app/src/story.json`: chapters, point texts, and capsule references
  (tree + path).
- The tab rendering in `mindmap.js`, `styles.css` and `template.html`.
- A check in `build.py` that every capsule referenced by the Story exists in the trees.

## Related

- `panel-slide-spec.md` — capsule content shown in the cards.
- `pipeline-design.md` — the narrative text can later be generated and judged by the
  pipeline like any other field.
