# Databricks AI Tree — unified cartography (DAIS 2026 → 7 Oct 2026)

**Built:** 2026-10-07 by merging 3 source agents (public web · internal Glean · Sage catalog).
**Purpose:** master map of everything Databricks does in AI. Drives the round-2 doc hunt.

## Confidence legend
- ✅ **Confirmed** — corroborated by internal Glean and/or a curated Sage asset (reliable).
- 🟡 **To verify** — public-web-only or single-source; plausible but not cross-checked (possible naming drift / hallucination). Must be validated before any customer use.
- Status: **GA · Public Preview (PuP) · Beta · Private Preview · Announced · Legacy/Retired**

---

## PILLAR 1 — AI Platform / ML lifecycle (Mosaic AI)
Core ML & GenAI infra: features → training → tracking → serving.

- ✅ **Feature Store** (GA) — governed features; online store on **Lakebase**; UC-synced. [glean+public]
- ✅ **Model Serving** (GA) — serverless endpoints (custom / foundation / external); pay-per-token, provisioned throughput, batch. Governed by Unity Gateway. [glean+public]
- ✅ **AI Runtime — serverless GPU** (GA per glean / "previewed" per public 🟡 on exact status) — A10/H100, LoRA/QLoRA fine-tune, distributed training, vLLM/Ray batch. [glean+public]
- ✅ **MLflow 3 for GenAI** (GA) — tracing (OpenTelemetry, 30+ frameworks), evaluation (built-in LLM judges + custom scorers), production monitoring, Delta/UC backend. [glean+public+sage]
- ✅ **MLflow Model Registry** (GA) — versioning, aliases (Champion/staging/prod), UC lineage. [glean+public]
- ✅ **MLflow Prompt Registry** (GA) — versioned prompts, staging/prod aliases. [public]
- ✅ **AutoML** (GA) — tabular classification/regression. [glean+public]
- ✅ **AI Search** (ex-Vector Search) (GA) — vector + BM25 keyword + hybrid (RRF) + reranking; Delta Sync; UC-governed; citations; Lakebase-synced tables (Beta). [glean+public]
- ✅ **Model fine-tuning** (GA, varies by model) — LoRA/QLoRA/full/RL where supported. [glean+public]

## PILLAR 2 — Foundation Models & LLM access
- ✅ **Foundation Model APIs** (GA) — multi-provider (Anthropic, OpenAI, Google, Meta, Qwen, xAI Grok, Moonshot Kimi, Zhipu GLM, DeepSeek, …); pay-per-token / priority / provisioned throughput. [glean+public]
  - 🟡 *Exact model version numbers* (e.g. "GPT-6.1", "Gemini 3.8", "Claude Sonnet 5.5", "DeepSeek V4") — public-only, **verify against the live supported-models matrix**; naming almost certainly drifted.
- ✅ **External model services** (GA) — governed access to externally hosted models via UC Connections + Gateway. [glean+public]
- 🟡 **Model lifecycle churn (Oct)** — Gemini 2.5 retirement, GLM legacy, DeepSeek retirement schedule — public-only dates, verify. [public]

## PILLAR 3 — Agents / Agent Bricks
Production platform to build, deploy, evaluate, govern agents.

- ✅ **AI Functions** (GA) — `ai_parse_document`, `ai_extract`, `ai_classify`, `ai_summarize`, `ai_translate`, `ai_gen`, `ai_mask`, `ai_query` + **`ai_decide`** (Beta, Sept 30) + `ai_extract` 2.3× faster (Oct 2). [glean+public]
- ✅ **Custom Agents** (GA; CLI Beta) — code-first; LangGraph/Agno/CrewAI/Claude Code SDK/OpenAI SDK; Agent Server + **DurableAgentServer** (crash-recoverable); declarative config (`agent.toml`). [glean+public]
- ✅ **Managed memory & sessions** (Beta, Sept 16) — Lakebase-backed, cross-session, semantic search. [glean+public]
- ✅ **Databricks Sandbox** (Beta) — isolated serverless code execution, scoped UC access. [glean+public]
- ✅ **Supervisor Agent** (GA, **legacy** — Custom Agents/Genie Agents preferred) — multi-agent orchestration, user-scoped auth. [glean+public]
- ✅ **Knowledge Assistant** (GA, **legacy** — Genie Agents preferred) — document-grounded chatbot, Instructed Retriever, citations. [glean]
- ✅ **Omnigent** (Beta; OSS Apache-2.0) — agent *meta-harness* composing Claude/Codex/Cursor/custom; managed version integrates workspace identity + Gateway + Sandbox (CEL policies). [glean+public]
- ✅ **Agent evaluation & monitoring** (GA via MLflow) — traces → Review Apps → datasets → LLM judges → dashboards. [glean+public+sage]

## PILLAR 4 — Governance for AI
- ✅ **Unity Catalog for AI assets** (GA) — governs tables, models, foundation/external models, **agents, UC functions (tools), MCP services, connections, skills, credentials**; RLAC/ABAC, lineage, audit. [glean+public]
- ✅ **Unity AI Gateway** (GA; renamed from "AI Gateway") — runtime control plane: routing/fallbacks/Smart Routing, rate limits, budgets & cost attribution, guardrails (PII, injection) via **Service Policies (Beta)**, observability via system tables, multi-provider. [glean+public+sage]
- ✅ **Review Apps** (GA) — human-in-the-loop labeling of traces/chat for eval datasets. [glean]
- ✅ **DASF v3.0 — Databricks AI Security Framework** (published Mar 2026) — 97 risks / 73 controls; **Agentic extension** (35 risks, 6 controls, 13 components). [public]

## PILLAR 5 — Genie / AI/BI family
- ✅ **Genie One** (GA; mobile PuP, macOS Beta) — unified cross-asset BI assistant; **memory GA (Sept)**, **MCP server GA (Sept)**; free for named users through **Jan 31 2027**. (Public note: formerly surfaced as "Databricks One".) [glean+public+sage]
- ✅ **Genie Agents** (GA; ex-**Genie Spaces**, renamed Jul 2026) — no-code domain agents on UC data; file reasoning; **limits ↑ 50 sources / 200k conversations (Sept 10)**. [glean+public]
- ✅ **Genie Code** (GA; ex-"Databricks Assistant", Mar 2026) — notebook/SQL/pipeline/dashboard assistant, agent mode, intelligent document processing; **pay-as-you-go (150 DBU free/user/mo since Jul 8)**; **Genie Code CLI (Beta, Oct 6)**. [glean+public+sage]
- ✅ **AI/BI Dashboards (Lakeview)** (GA) — AI-assisted authoring, dashboard-level Genie, metric views. [glean+public+sage]
- ✅ **Genie Ontology** (Public Preview) — learned business-context layer grounding Genie answers. [glean+public]
- ✅ **Genie App Builder** (Beta, Sept 23) — NL → Databricks App; needs admin "governed agentic app-building" + App Spaces. [public]

## PILLAR 6 — Developer productivity
- ✅ Genie Code / Genie Code CLI / Genie App Builder (see Pillar 5).
- ✅ **Databricks Apps + App Spaces** (GA) — serverless Streamlit/Gradio/React/FastAPI; app- vs user-principal auth; UC telemetry; App Spaces governance (DAIS 2026). [glean+public+sage]
- ✅ **AI Dev Kit (`go/ai-dev-kit`) + internal coding agents ("Isaac")** — scaffolding, UC-governed MCPs; internal proof point (25× spend growth, $400/mo baseline). [glean+sage]

## PILLAR 7 — MCP integration
- ✅ **Databricks-managed MCP servers** (GA Sept) — Genie One, Genie Agent, AI Search, Databricks SQL, UC Functions, Code Interpreter. [glean+public]
- ✅ **External connectors** (GA Sept 10) — Google Workspace, Microsoft 365, Atlassian, Slack, GitHub; **Glean (search-only, Beta)**; **Meta Ads (Oct 6)**. Per-user OAuth, UC+Gateway governed. (Limits: Gmail no-send, GitHub write caveats.) [glean+public]
- ✅ **MCP Services** (GA) — register external MCP servers as UC securables. **Custom MCP** as a Databricks App (GA pattern). [glean]

## PILLAR 8 — Data foundation for AI
- ✅ **Lakehouse / Delta Lake** (GA) — open ACID format; trusted data for AI. [glean+public]
- ✅ **Lakeflow** — Connect / Pipelines / Jobs (GA) + **Designer** (Public Preview, NL via Genie Code). [glean+public]
- ✅ **Lakebase — serverless Postgres** (GA, since Jan 2026) — agent memory/state, online feature store, branching, HA; UC-synced. [glean+public]
- ✅ **Lakebase Search** (GA, Sept 28) — vector + BM25 + hybrid inside Postgres, no separate vector DB. [glean+public]
- ✅ **Predictive Optimization** (GA) — ROI-based OPTIMIZE/VACUUM/ANALYZE/clustering on UC managed tables. [glean]

## PILLAR 9 — Agentic Data Management  *(internal FY27 taxonomy block)*
- ✅ Data classification · profiling / Lakehouse Monitoring · data-quality monitoring · anomaly detection · automated remediation — AI-driven, UC-integrated; remediation still **emerging**. [glean]

## PILLAR 10 — Real-time & transactional AI  🟡 *(public-only — verify names/status)*
- 🟡 **Lakehouse//RT** (Beta) — serverless low-latency SQL ("Reyden" engine) on Delta/Iceberg; read-only. [public]
- 🟡 **LTAP** (Announced / vision) — Lake Transactional-Analytical Processing unifying Lakebase + lakehouse. [public]

## PILLAR 11 — Domain-specific AI  🟡 *(public-only — verify names/status)*
- 🟡 **CustomerLake** (Private Preview) — agentic CDP (Customer 360, identity resolution, campaign agents). [public]
- 🟡 **Lakewatch** (Private Preview) — agentic SIEM; linked to **Panther** acquisition. [public]
- 🟡 Other public-only M&A/items: **Row Zero** (governed spreadsheets into Genie), **Genie ZeroOps** (ML auto-remediation) — single-source, verify. [public]

---

## What's NEW since DAIS 2026 (deltas, Sept–Oct 2026)
**DAIS 2026 (Jun 16–17) themes:** Agent Bricks → full production platform (any model, any harness, MCP+UC, managed memory); Unity AI Gateway as governance layer; Genie One/Agents/Ontology; Omnigent; AI Runtime; agent-native data (Lakebase + Search).

**Sept:** MCP connectors GA (10) · Genie Agents limits ↑ (10) · managed memory Beta (16) · Gateway API/dev tools GA (16) · Genie App Builder Beta (23) · Lakebase Search GA (28) · Agent Bricks CLI Beta (29) · Genie One memory GA (29) · `ai_decide` Beta (30). *(🟡 public-only: Row Zero acq 24.)*
**Oct (1–7):** Genie One usability GA (1) · Genie Code dashboard materialization Beta (1) · `ai_extract` 2.3× (2) · Gateway migration guide (5) · Agent Bricks code-first docs (6) · Genie Code CLI Beta (6) · Meta Ads MCP (6). *(🟡 public-only: Gemini 2.5 retirement, GLM legacy.)*

---

## Canonical decks & authors — for round-2 doc hunt
Quality signals already spotted (slugs/URLs in `tree-sage.md` and `tree-glean.md`):

**Gold / canonical decks (Sage, customer-facing):**
- `dsml-l100200-pitch-deck-godsml` — **Data Science & ML L100/200** (canonical Mosaic AI/MLflow story).
- `genie-battlecard` — **Genie competitive battlecard** (vs Snowflake/MSFT/Google/Amazon).
- `ai-governance-on-databricks-overview-l100-pitch-deck` + `data-ai-governance-full-deck` (L400) + `data-ai-governance-customer-facing-deck`.
- `unity-ai-gateway-product-deck-l200`.
- `eval-flywheel-databricks-genai-agent-demo` — end-to-end agent + MLflow eval (Gold codebase).
- `ai-transformation-a-databricks-point-of-view-generic-whitepaper` — parent exec whitepaper (7-Eleven/Coles/AGL instances).
- `aibi-foundation-delivery-and-resources-guide`, `genie-foundations-delivery-and-resources` — delivery frameworks.
- `mosaic-ai-security-overview`, `databricks-ai-features-security-architecture`.

**Internal canonical (Glean):**
- **L150: Databricks AI** (`go/AIR/Enablement`) — technical "how to get started" pitch.
- **FY27 Product Lines Definitions** — authoritative AI taxonomy.
- **Big Book of AgentOps** (Sept 2026) — governance/observability playbook.
- **Agentic Apps GTM L100 Deck**; **AI Gateway Enablement Deck**; **Databricks Pitch Deck FY27**.

**Authors / teams — ⚠️ NOT yet resolved** (round-2 action: `mcp__glean__get_person`): Mosaic AI Research team; Agents/Genie/Gateway/Lakeflow PM owners; FE AI leadership. Sage GitHub owners seen: RohitDashora, archana986, bhavink, josh-melton-db, dhavalbagadia05, pponnaDB.

**Content gaps flagged by Sage (thin field enablement):** Vector Search/RAG, Agent Bricks how-to, AI Functions quickstarts, Omnigent, MLflow-at-scale.

---

## Open verification queue (before customer use)
1. Foundation model exact version names/numbers (public drift).
2. Pillar 10/11 names & status: Lakehouse//RT / Reyden, LTAP, CustomerLake, Lakewatch/Panther, Row Zero, Genie ZeroOps.
3. AI Runtime exact GA vs preview status.
4. Regional/cloud availability for Lakebase, Genie App Builder, Beta features.
5. Resolve canonical-deck authors + org roles.
