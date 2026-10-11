# Databricks AI Cartography (DAIS 2026 – October 2026)

**Document date:** October 7, 2026  
**Research scope:** Public sources only (databricks.com/blog, product pages, docs, release notes)  
**Coverage:** Major AI announcements from January 2026 through early October 2026, with emphasis on DAIS 2026 (June 16–17) keynotes and subsequent releases.

---

## Executive Summary: AI Pillars

Databricks' AI strategy in 2026 centers on **seven interconnected pillars**:

1. **Agentic AI Platform** — Agent development, orchestration, memory, sandbox execution
2. **Generative AI & LLM Infrastructure** — Model serving, Foundation Model APIs, embedding services
3. **Business AI & Analytics** — Genie One, Genie Agents, Genie Ontology for business users
4. **Developer Productivity** — Genie Code (notebook assistant), Genie App Builder
5. **AI Governance & Security** — Unity Catalog/Gateway, DASF v3.0 framework, observability
6. **Real-time & Transactional AI** — Lakehouse//RT, Lakebase, LTAP architecture
7. **Domain-Specific AI** — CustomerLake (CDP/marketing), Lakewatch (SIEM/security)

---

## 1. AGENTIC AI PLATFORM

**Mission:** Databricks' multi-framework agent development, deployment, memory, and orchestration stack.

### 1.1 Agent Bricks
- **Description:** Developer platform for building custom AI agents with managed memory, tools, tracing, and deployment.
- **Status:** GA (core), with Beta CLI (Sept 29 2026)
- **Key features:** Multi-framework support (Claude, Codex, Cursor, custom), MCP integration, MLflow tracing, DurableAgentServer for state persistence
- **Dates:** Agent Bricks CLI – Beta (Sept 29, 2026)
- **Source:** https://docs.databricks.com/aws/en/generative-ai/agent-framework/build-agents
- **Latest:** Oct 6, 2026 – comprehensive code-first documentation published

### 1.2 Agent Runtime / Databricks Apps
- **Description:** Serverless hosting for agents; scale-to-zero authenticated endpoints with built-in deployment and tracing.
- **Status:** GA (with ongoing Beta features for app builders)
- **Key features:** Authenticated agent endpoints, optional `DurableAgentServer`, MLflow integration, Workspace or Git deployment
- **Dates:** Announced as core DAIS 2026 infrastructure (June 17)
- **Source:** https://docs.databricks.com/aws/en/agents/deploy/agent-runtime

### 1.3 Managed Agent Memory & Sessions
- **Description:** Lakebase-backed long-term memory with semantic search and durable conversation state.
- **Status:** Beta (Sept 16, 2026)
- **Key features:** Cross-session persistence, semantic search over memory, multi-agent compatible, SQL interface
- **Dates:** Sept 16, 2026 – Beta launch
- **Source:** https://docs.databricks.com/aws/en/release-notes/product/2026/september

### 1.4 Omnigent (Multi-Agent Orchestration)
- **Description:** Open-source "meta-harness" for composing agents from different frameworks; managed service on Databricks.
- **Status:** Open-source (Alpha), Managed Omnigent (Beta)
- **Key features:** Framework-agnostic agent composition, portable agent definitions (YAML), shared governance policies, multi-interface access (CLI/browser/mobile)
- **Dates:** Open-source announced June 13, 2026 (Apache 2.0); Managed Beta (current)
- **Source:** https://omnigent.ai, https://docs.databricks.com/aws/en/omnigent/
- **Note:** Managed Omnigent uses CEL policies (not custom Python); Databricks Sandbox execution limitations apply

### 1.5 Databricks Sandbox
- **Description:** Serverless Linux container for AI-generated code execution, tool operation, and coding-agent isolation.
- **Status:** Beta
- **Specs:** 4 vCPU, 8 GB RAM, Python/Node.js/CLI included, persistent `/home/sandbox-agent`, unrestricted outbound network
- **Dates:** Public guidance (current); scoped access via `agentbricks tools add sandbox`
- **Source:** https://developers.databricks.com/docs/agents/sandbox
- **Security note:** Open egress is configurable; assess before running untrusted code

---

## 2. GENERATIVE AI & LLM INFRASTRUCTURE

**Mission:** Consistent, governed access to foundation models and model serving.

### 2.1 Foundation Model APIs (pay-per-token)
- **Description:** On-demand access to 20+ model families without provisioned capacity; governed through Unity Gateway.
- **Status:** GA
- **Available families (examples):**
  - OpenAI: GPT-6.1/6/5.6/5.5/5.4, GPT-OSS
  - Anthropic: Claude Sonnet 5.5/5, Opus 5.5/5, Fable, Haiku 4.5
  - Google: Gemini 3.8/3.7/3.6, Gemma 3
  - Meta: Llama 4 Maverick, Llama 3.3, Llama 3.1
  - DeepSeek: V4.1 Flash, V4 (with retirement notice)
  - Others: Alibaba Qwen, GLM, Grok, Kimi, Inkling
- **Tiers:** Standard pay-per-token, Priority (higher cost, consistent latency), Provisioned throughput
- **Pricing model:** DBU per 1M tokens (input/output rates vary); $0.07/DBU baseline example on AWS US-E1
- **Dates:** Ongoing catalog updates; Oct 2 retired Gemini 2.5 Pro/Flash; Oct 6 GLM 5.2 legacy; Nov 5 DeepSeek V4 Flash (0731) retirement scheduled
- **Source:** https://docs.databricks.com/aws/en/machine-learning/model-serving/foundation-model-overview

### 2.2 Mosaic AI Model Serving
- **Description:** Custom ML and foundation-model inference infrastructure; governed through Unity Catalog + Unity Gateway.
- **Status:** GA (legacy endpoint-ACL governance deprecated; unified on Unity Gateway)
- **Key features:** Custom endpoints, pay-per-token endpoints, provisioned throughput, external model provider support
- **Governance evolution:** Legacy "AI Gateway for serving endpoints" now labeled Beta/legacy; all new workloads → Unity Gateway
- **Dates:** Migration guide published Oct 5, 2026
- **Source:** https://docs.databricks.com/aws/en/machine-learning/model-serving

### 2.3 Unity Gateway (AI Gateway for Models & MCP Services)
- **Description:** Centralized routing, access control, rate limits, budgets, and usage monitoring for models and tools.
- **Status:** GA (since April 2026); Service policies remain Beta
- **Key features:** Model routing and fallbacks, cost controls, request/response guardrails (Beta), usage telemetry, integration with Unity Catalog
- **Dates:** GA April 15, 2026; Service policies remain Beta; Oct 5 migration guidance published
- **Source:** https://docs.databricks.com/aws/en/ai-gateway/ai-governance

### 2.4 Service Policies (Guardrails for Models)
- **Description:** Request/response inspection and filtering: built-in rules for PII detection, prompt injection, unsafe content; custom policies supported.
- **Status:** Beta
- **Features:** Separate from route-level access; applies to all model types; customizable via policy UI or API
- **Dates:** Beta (current, announced DAIS 2026)
- **Source:** https://docs.databricks.com/aws/en/ai-gateway/

### 2.5 Unity AI Gateway (Broader AI Governance)
- **Description:** Umbrella term for governance across models, agents, tools, and MCP services under Unity Catalog.
- **Status:** GA
- **Announced:** DAIS 2026 (June 16–17)
- **Scope:** Centralized asset registry, permissions, tracing, and cost visibility for all AI components
- **Source:** https://databricks.com/blog/agent-bricks-dais-2026

---

## 3. BUSINESS AI & ANALYTICS (Genie Suite)

**Mission:** AI-powered analytics and business intelligence for non-technical and technical users.

### 3.1 Genie One (Unified Business AI Interface)
- **Description:** Conversational AI for dashboards, data questions, and business user workflows; previously called "Databricks One."
- **Status:** GA (with ongoing feature releases)
- **Key features:**
  - Natural-language data questions with SQL generation
  - Private user memory (GA Sept 29, 2026): preferences and reporting conventions carry across sessions
  - Connected business tools: Google Drive, Gmail, Calendar; Microsoft 365; Atlassian; Slack; GitHub
  - Public web search: Beta (Sept 3, 2026); external citations
  - Chat downloads, streaming responses, `.txt` uploads (Oct 1, 2026)
  - Personalized sample questions (Oct 1, 2026)
- **Pricing caveat:** Free through Jan 31, 2027 for end users; service principals excluded
- **Dates:** Renamed/expanded June 16 DAIS 2026; memory GA Sept 29; web search Beta Sept 3; usability updates Oct 1
- **Source:** https://docs.databricks.com/aws/en/genie-one/

### 3.2 Genie Ontology
- **Description:** Automatic business context layer: metric definitions, terminology, calculations, relationships across enterprise assets.
- **Status:** New / Announced
- **Purpose:** Ground Genie's answers in organizational semantics, not generic SQL generation.
- **Dates:** Announced DAIS 2026 (June 16)
- **Source:** https://databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents

### 3.3 Genie Agents
- **Description:** Domain-specific analytics agents, evolved from Genie Spaces; teams can create reusable agents.
- **Status:** GA
- **Key updates:**
  - Sept 10, 2026: limits increased to **50 data sources** per agent, **200,000 conversations** retention
  - Genie Agent Builder: assist with agent creation
- **Dates:** Announced DAIS 2026 (June 16); limits increased Sept 10, 2026
- **Source:** https://docs.databricks.com/aws/en/genie-one/

### 3.4 Genie Code (Dashboard Authoring & SQL Generation)
- **Description:** AI assistant for dashboard creation and SQL metric-view definition.
- **Status:** Public Preview / GA (with ongoing Beta features)
- **Key features (Oct 2026):**
  - Dashboard materialization on request: Beta (Oct 1)
  - Workspace-image support (Oct 1)
  - Progressive dashboard rendering (Oct 1)
  - Power BI/Tableau migration assistance
- **Dates:** Metric-view features ongoing; Oct 1 materialization feature Beta
- **Source:** https://docs.databricks.com/aws/en/ai-bi/release-notes/2026

---

## 4. DEVELOPER PRODUCTIVITY TOOLS

**Mission:** AI-powered coding, data exploration, and rapid app development.

### 4.1 Genie Code (Notebook Code Assistant)
- **Description:** AI coding assistant in notebooks: generate, explain, fix, optimize, and refactor Python/PySpark/SQL.
- **Status:** GA (launched March 11, 2026; pricing model changed July 8)
- **Key features:**
  - Inline assist (Cmd+I/Ctrl+I), `/explain`, `/fix`, `/doc`, `/optimize`, `/findTables`
  - Agent mode: multi-step across cells with error iteration
  - Unity Catalog metadata integration: find relevant tables, understand columns
  - Keyboard shortcuts and cell-level commands
- **Pricing:** Pay-as-you-go since July 8, 2026 (150 DBU free per user monthly); no longer unlimited free
- **Dates:** Launched March 11, 2026; paywall June (July 8 enforcement); Oct 6 CLI version Beta
- **Source:** https://docs.databricks.com/aws/en/genie-code/

### 4.2 Genie Code CLI (Terminal Agent)
- **Description:** Coding agent for terminal, integrating Databricks data, AI models, and code generation in the shell.
- **Status:** Beta (Oct 6, 2026)
- **Features:** Governed model access via Unity Gateway; multi-step data/code workflow in terminal
- **Dates:** Beta Oct 6, 2026
- **Source:** https://docs.databricks.com/aws/en/release-notes/product/2026/october

### 4.3 Genie App Builder
- **Description:** AI-powered, code-free app creation; generate Databricks Apps from natural-language prompts.
- **Status:** Beta (announced June 16 DAIS 2026; launch Sept 23, 2026)
- **Requirements:** Admin enable "Governed agentic app-building"; App Spaces for governance; supported AWS/Azure regions only
- **Deployment:** Scale-to-zero serverless; free during Beta (pricing TBD)
- **Typical use:** "Build a read-only sales dashboard using `main.analytics.sales` with date/region filters and downloadable tables"
- **Dates:** Announced June 16 (DAIS 2026); Beta launch Sept 23, 2026
- **Source:** https://docs.databricks.com/aws/en/dev-tools/databricks-apps/genie-app-builder

### 4.4 Databricks Apps & App Spaces
- **Description:** Serverless application hosting and governance for custom enterprise apps.
- **Status:** GA (App Spaces with governance; Genie App Builder Beta)
- **Key features:**
  - Serverless runtime: scale-to-zero, default 30-min idle timeout
  - Governance layer (App Spaces): control authorization, roles, permitted resource access
  - Deployment: Git-backed or workspace folder (CLI/UI)
  - Framework support: Python, Node.js
- **Dates:** App Spaces announced June 16 (DAIS 2026); ongoing feature releases
- **Source:** https://docs.databricks.com/aws/en/dev-tools/databricks-apps/

---

## 5. AI GOVERNANCE, SECURITY & OBSERVABILITY

**Mission:** Unified control, auditing, and risk mitigation across all AI systems.

### 5.1 Unity Catalog for AI Assets
- **Description:** Centralized registry for models, model services, agents, functions, MCP services, and connections; ownership and permissions.
- **Status:** GA
- **Key features:**
  - Three-level namespace (catalog.schema.asset)
  - Version and alias support (e.g., `Champion`, `staging`, `production`)
  - Cross-workspace discovery for registered models
  - Integration with MLflow for model lineage and metadata
  - Row-level access control (RLAC) and attribute-based access control (ABAC)
- **Dates:** Ongoing; expanded scope for agents announced DAIS 2026 (April 15 announcement, June keynote)
- **Source:** https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/

### 5.2 MLflow Tracing & Observability
- **Description:** End-to-end execution tracing for agents, RAG, and LLM applications; captures model calls, tool invocations, latency, tokens, cost.
- **Status:** GA (MLflow 3.x)
- **Key features:**
  - Automatic tracing in Agent Bricks, Agent Runtime, and manual instrumentation
  - Token count and cost attribution
  - Tool-call tracing for agents
  - OpenTelemetry compatibility
- **Dates:** MLflow 3.x current standard; ongoing integrations
- **Source:** https://docs.databricks.com/aws/en/mlflow3/genai/

### 5.3 MLflow Evaluation & Scorers
- **Description:** Structured evaluation for LLM and agent outputs using built-in LLM judges, custom scorers, and deterministic checks.
- **Status:** GA (mlflow.genai.evaluate)
- **Built-in scorers (8):**
  - Correctness, RelevanceToQuery, Safety (general)
  - RetrievalRelevance, RetrievalGroundedness, RetrievalSufficiency (RAG-specific)
  - Guidelines (custom rules)
  - Token count, cost (system metrics)
- **Workflow:** Evaluation datasets → traced application → scorers → per-example feedback
- **Dates:** Current standard (legacy Agent Evaluation deprecated)
- **Source:** https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/

### 5.4 MLflow Prompt Registry
- **Description:** Centralized, versioned storage for prompts with immutable versions and mutable aliases (staging/production).
- **Status:** GA (MLflow 3.x)
- **Features:** Prompt versioning, promotion workflows, configuration co-storage
- **Dates:** GA (MLflow 3.x standard)
- **Source:** https://mlflow.org/docs/latest/genai/prompt-registry/

### 5.5 Databricks AI Security Framework (DASF) v3.0
- **Description:** Comprehensive risk taxonomy and control framework for AI systems; includes new Agentic AI extension.
- **Status:** Published / Announced
- **Key metrics:**
  - **97 risks** (vs. 62 in v2.0)
  - **73 controls** (vs. 67 in v2.0)
  - **Agentic AI Extension:** 35 new risks, 6 new controls, 13 system components
- **Agentic risk areas:** Agent core (reasoning/memory), MCP servers (tool interfaces), MCP clients (tool execution/data)
- **Top control families:**
  - Least-privilege tool access (Unity Catalog permissions, scoped data access)
  - Human oversight for high-stakes actions
  - Sandboxing and isolation
  - Gateway guardrails (PII, injection detection)
  - Agentic observability and tracing
- **Dates:** DASF v3.0 announced March 20, 2026; companion guidance March 11, 2026
- **Source:** https://databricks.com/blog/agentic-ai-security-new-risks-and-controls-databricks-ai-security-framework-dasf-v30

### 5.6 MCP Connectors (Managed Integration)
- **Description:** Databricks-provided MCP connectors for external tools; governed through Unity Catalog and Unity Gateway.
- **Status:** GA (Sept 10, 2026)
- **Available connectors:** Google Workspace, Microsoft 365, Atlassian, Slack, GitHub
- **Governance:** Centrally managed access, permissions, and audit trail
- **Dates:** GA Sept 10, 2026
- **Source:** https://docs.databricks.com/aws/en/ai-bi/release-notes/2026

---

## 6. REAL-TIME & TRANSACTIONAL AI

**Mission:** Combine transactional consistency and analytical performance for AI applications.

### 6.1 Lakehouse//RT (Real-Time Analytical Warehouse)
- **Description:** Serverless SQL engine (Reyden) for millisecond-latency, high-concurrency read queries directly on Delta/Iceberg tables.
- **Status:** Beta (announced June 16 DAIS 2026)
- **Performance claims (vendor-reported):**
  - 10 ms latency on small datasets
  - Sub-100 ms at 12,000 QPS on analytical benchmarks
  - Up to 16× better performance vs. traditional real-time stacks
- **Scope:** SELECT queries only (read-only); direct governance through Unity Catalog
- **Dates:** Announced June 16, 2026 (DAIS); Beta (current)
- **Source:** https://databricks.com/blog/introducing-lakehousert-real-time-performance-unified-lakehouse

### 6.2 Lakebase (Serverless PostgreSQL)
- **Description:** Fully managed, serverless Postgres with compute-storage separation, autoscaling, scale-to-zero, and lakehouse integration.
- **Status:** GA (announced GA Jan 22, 2026; ongoing feature releases)
- **GA features (by date):**
  - Core: GA (Jan 22)
  - High availability: GA (March 2)
  - Management APIs: GA (Aug 14)
  - Genie Code integration: Available (Aug 24)
  - Lakebase Search (vector + BM25): GA Sept 28, 2026
- **AI use cases:**
  - Agent memory and state (conversation context, checkpoints)
  - RAG and retrieval: vector + keyword search (Lakebase Search)
  - Online feature store: low-latency feature lookups
  - Application data: transactional consistency for AI-backed systems
- **Dates:** GA Jan 22, 2026; Lakebase Search GA Sept 28, 2026
- **Source:** https://docs.databricks.com/aws/en/oltp/, https://databricks.com/blog/lakebase-search-state-art-full-text-and-vector-search-postgres

### 6.3 LTAP Architecture (Lake Transactional-Analytical Processing)
- **Description:** Proposed unified architecture combining Lakebase (transactional Postgres) and lakehouse analytics (Delta/Iceberg) over one storage layer.
- **Status:** Announced / Architectural Vision
- **Goal:** Eliminate separate copies and synchronization pipelines
- **Dates:** Announced June 16, 2026 (DAIS); availability depends on cloud/region
- **Source:** https://databricks.com/company/newsroom/press-releases/databricks-launches-ltap-first-lake-transactionalanalytical

---

## 7. MACHINE LEARNING LIFECYCLE

**Mission:** End-to-end ML governance: from feature engineering to inference.

### 7.1 Feature Store (Unity Catalog Integration)
- **Description:** Governed feature layer connecting data prep, model training, and production inference.
- **Status:** GA (with Public Preview for Feature Views)
- **Key elements:**
  - **Feature Views** (Public Preview): declarative, Databricks-managed computation
  - **Feature tables:** user-managed pipeline ownership
  - **Online Feature Store:** Lakebase-powered for real-time lookup
  - **Unity Catalog:** centralized feature governance and discovery
- **Deprecated:** Workspace Feature Store (legacy)
- **Dates:** Public Preview for Feature Views (current); ongoing
- **Source:** https://docs.databricks.com/aws/en/machine-learning/feature-store

### 7.2 Databricks AI Runtime
- **Description:** Serverless GPU compute for model training and inference; includes agent infrastructure.
- **Status:** Announced / Previewed
- **Features:** Managed GPU clusters, integrated with Databricks Apps for agent hosting
- **Dates:** Announced DAIS 2026 (June 17)
- **Source:** https://youtube.com/watch?v=sn9My5Pj0mE (DAIS Day 2 keynote, timestamp 1:37:07)

### 7.3 Genie Code for ML
- **Description:** AI assistant for machine learning workflows in notebooks.
- **Status:** Announced / GA via Genie Code
- **Features:** Code generation for model development, experiment tracking, hyperparameter tuning
- **Dates:** Announced DAIS 2026 (June 17)
- **Source:** https://youtube.com/watch?v=sn9My5Pj0mE (DAIS Day 2 keynote, timestamp 1:37:07)

### 7.4 Genie ZeroOps for ML
- **Description:** Background agent monitoring and auto-remediation for ML pipelines: proposes fixes for failing jobs, models, and data issues.
- **Status:** Announced / Previewed
- **Goal:** Reduce manual DevOps for ML workflows
- **Dates:** Announced DAIS 2026 (June 17)
- **Source:** https://databricks.com/blog/introducing-genie-zeroops

---

## 8. DATA RETRIEVAL & SEARCH FOR AI

**Mission:** Hybrid retrieval infrastructure for RAG and agent search.

### 8.1 Databricks AI Search (formerly Vector Search)
- **Description:** Hybrid retrieval combining semantic vectors, BM25 keyword search, and rank fusion for RAG.
- **Status:** GA (renamed/refreshed Oct 2026)
- **Retrieval modes:**
  - Semantic (vector similarity): finds related meaning
  - Keyword (BM25): finds lexical matches, product names, identifiers
  - Hybrid (RRF): merges both rankings; max 200 results
  - Full-text (Beta): explicit search across selected columns
- **Optional reranking:** second-pass ranking to improve result ordering
- **Index types:**
  - Delta Sync: auto-sync from source table
  - Direct Vector Access: application-managed
- **Endpoint types:** Standard (in-memory), Storage-optimized (separate compute/storage)
- **Dates:** Renamed/refreshed current; full-text search Beta
- **Source:** https://docs.databricks.com/aws/en/ai-search/

---

## 9. DOMAIN-SPECIFIC AI PLATFORMS

**Mission:** Industry-specific AI applications built on Databricks.

### 9.1 CustomerLake (Agentic CDP)
- **Description:** Native customer data platform with AI agents for profile resolution, audience segmentation, and personalized engagement.
- **Status:** Private Preview (announced June 16 DAIS 2026)
- **Key components:**
  - Customer 360: unified profiles from behavior, transactions, engagement, operations data
  - Identity resolution: deterministic + probabilistic + agent-assisted matching
  - Audience segmentation: natural-language Genie-based exploration
  - Profile Agents and Campaign Agents: continuous agentic engagement ("infinity campaigns")
  - Reverse ETL and activation ecosystem: Adobe, Meta, Braze, Iterable, LiveRamp, The Trade Desk, others
- **Data foundation:** Built on Databricks lakehouse (Unity Catalog governance, Lakeflow ingestion)
- **Dates:** Private Preview June 16, 2026 (DAIS); no public GA date announced
- **Source:** https://databricks.com/blog/introducing-customerlake-agentic-cdp

### 9.2 Lakewatch (Agentic SIEM)
- **Description:** Security lakehouse with AI agents for threat detection, investigation, and SOC automation.
- **Status:** Private Preview (announced March 24, 2026)
- **Key capabilities:**
  - Cross-source correlation: security events + business context + IT logs
  - Standardized telemetry (OCSF): normalize logs for multi-source correlation
  - AI-assisted threat hunting: natural-language Genie queries on security data
  - Detection engineering: automate rule authoring, normalization, triage (detection-as-code)
  - Agent-assisted investigation: context gathering, alert triage, summarization
  - Long-term historical analysis: petabyte-scale retention in cloud storage
- **Vendor claims:** up to 80% lower TCO vs. incumbent SIEMs (requires validation)
- **Panther acquisition:** Databricks completed acquisition Aug 11, 2026, bringing Panther's detection capabilities and 100+ prebuilt connectors
- **Dates:** Private Preview March 24, 2026; Panther acquisition announced June 16, completed Aug 11
- **Source:** https://databricks.com/blog/databricks-enters-security-market-launch-lakewatch-new-agentic-siem

---

## 10. NEW UTILITY & EMERGING FEATURES (Recent)

### 10.1 ai_decide (Structured Decision AI Function)
- **Description:** New AI Function for structured, probabilistic decisions through SQL or REST; returns choices, probabilities, scores.
- **Status:** Beta (announced Sept 30, 2026)
- **Use cases:** Classification, model routing, agent evaluation
- **Dates:** Beta Sept 30, 2026
- **Source:** https://databricks.com/blog/introducing-aidecide-make-fast-decisions-your-governed-data

### 10.2 Row Zero Acquisition
- **Description:** Databricks announced acquisition of Row Zero to integrate live, governed spreadsheets into Genie.
- **Status:** Acquisition announced Sept 24, 2026 (integration timeline TBD)
- **Purpose:** Bring familiar spreadsheet workflows into governed Databricks environment
- **Dates:** Announced Sept 24, 2026
- **Source:** https://databricks.com/company/newsroom/press-releases/databricks-acquires-row-zero-bringing-live-governed-spreadsheets

---

## WHAT'S NEW SINCE DAIS 2026 (June 16–17 → October 7)

### September 2026

| Date | Announcement | Status → Current |
|---|---|---|
| Sept 3 | Genie One public-web search | Beta ✓ |
| Sept 10 | MCP connectors (Google/Microsoft/Atlassian/Slack/GitHub) | GA ✓ |
| Sept 10 | Genie Agents limits increase (50 sources, 200k conversations) | GA ✓ |
| Sept 16 | Managed agent memory & sessions | Beta ✓ |
| Sept 16 | Unity Gateway API & developer tools | GA ✓ |
| Sept 22 | Coding-agent governance (CLI `ug` integration) | GA ✓ |
| Sept 23 | Genie App Builder | Beta ✓ |
| Sept 24 | Row Zero acquisition announcement | Acquisition announced |
| Sept 28 | Lakebase Search (vector + BM25) | GA (AWS, Azure) ✓ |
| Sept 29 | Agent Bricks CLI | Beta ✓ |
| Sept 29 | Genie One memory | GA ✓ |
| Sept 30 | ai_decide (structured decisions) | Beta ✓ |

### October 2026 (to date: Oct 1–7)

| Date | Announcement | Status → Current |
|---|---|---|
| Oct 1 | Genie One usability (uploads, streaming, downloads, sample questions) | GA ✓ |
| Oct 1 | Genie Code dashboard materialization | Beta ✓ |
| Oct 2 | OpenJev (Qwen3.5 4B) on Unity Gateway | GA ✓ |
| Oct 2 | Gemini 2.5 Pro/Flash retirement (effective date) | Retired |
| Oct 5 | Unity Gateway migration guide published | Documentation ✓ |
| Oct 6 | Agent Bricks documentation (code-first, DurableAgentServer, crash recovery) | Documentation ✓ |
| Oct 6 | Genie Code CLI | Beta ✓ |
| Oct 6 | GLM 5.2 becomes legacy | Lifecycle |
| Nov 5 (scheduled) | DeepSeek V4 Flash (0731) retirement | Future |

---

## PRODUCT AVAILABILITY LEGEND

| Status | Meaning |
|---|---|
| **GA** | Generally Available; production-ready for all supported regions |
| **Public Preview** | Available for opt-in; broadly supported but ongoing feature work |
| **Beta** | Limited availability; features may change; feedback welcomed |
| **Private Preview** | Invitation-only; development-stage |
| **Announced** | Publicly disclosed; launch date not yet set |
| **Deprecated** | No longer recommended; recommend alternative |
| **Retired** | Service no longer available |

---

## CROSS-PRODUCT INTEGRATION MATRIX

| Product | Depends on / Integrates with | Notes |
|---|---|---|
| **Agent Bricks** | MLflow (tracing), Unity Catalog (governance), Sandbox (execution), Agent Runtime | Full-stack agent development |
| **Genie One** | Unity Catalog (data), Foundation Model APIs, MCP connectors, external integrations | Business-user analytics |
| **Genie Code** | Foundation Model APIs, Databricks notebooks, Unity Catalog (metadata) | Developer productivity |
| **MLflow Evaluation** | Foundation Model APIs (judges), traces, evaluation datasets | Quality gates for GenAI |
| **Lakebase** | Lakehouse (storage sync), Feature Store (online serving), Agent memory (state) | Transactional foundation |
| **Feature Store** | Unity Catalog (governance), MLflow (model lineage), Lakebase (online store) | ML lifecycle |
| **CustomerLake** | Lakebase (data), Unity Catalog (governance), Agent infrastructure (Profile/Campaign Agents) | Marketing AI |
| **Lakewatch** | Lakehouse (security data), Unity Catalog (governance), Genie (threat hunting) | Security AI |
| **Omnigent** | Multiple agent frameworks, Unity Gateway (governance), Databricks Sandbox (execution) | Multi-agent orchestration |

---

## KEY DATES & MILESTONES (2026)

| Date | Milestone |
|---|---|
| Jan 22 | Lakebase GA |
| March 2 | Lakebase high availability |
| March 11 | DASF v3.0 companion guidance (agentic controls) |
| March 20 | DASF v3.0 published (97 risks, 73 controls) |
| March 24 | Lakewatch private preview launch |
| April 15 | Unity Gateway GA / AI Gateway unified governance |
| June 13 | Omnigent open-source (Apache 2.0) |
| June 16–17 | **DAIS 2026 keynotes**: 10 major AI announcements |
| July 8 | Genie Code pricing model change (pay-as-you-go) |
| Aug 11 | Panther acquisition completed |
| Aug 14 | Lakebase management APIs GA |
| Aug 24 | Genie Code integrated in Lakebase projects |
| Sept 10 | MCP connectors GA; Genie Agents limits increased |
| Sept 28 | Lakebase Search GA (Sept 28, 2026) |
| Sept 29 | Agent Bricks CLI Beta; Genie One memory GA |
| Oct 6 | Genie Code CLI Beta; agent documentation refresh |
| **Oct 7** | **Research snapshot date** |
| Nov 5 | DeepSeek V4 Flash (0731) retirement (scheduled) |

---

## GAPS & UNCERTAINTIES (As of Oct 7, 2026)

1. **Lakewatch GA date:** Still in private preview; no public GA announcement as of Oct 7.
2. **CustomerLake GA date:** Announced June 16 as private preview; no public GA date disclosed.
3. **LTAP status:** Architectural vision announced; availability depends on cloud/region; specific rollout plan not published.
4. **App Spaces production roadmap:** GA for governance; feature roadmap beyond current GA unclear.
5. **Lakehouse//RT scale limits:** Beta product; specific concurrent-query and table-size limits not publicly documented.
6. **Service policy enforcement:** Currently Beta; no commitment to timeline for general availability.
7. **Omnigent managed service limitations:** CEL policies only; no custom Python policies; Databricks Sandbox egress controls incompatible.

---

## SOURCES SUMMARY

| Source Type | Examples |
|---|---|
| Official announcements | databricks.com/company/newsroom/press-releases |
| Product blogs | databricks.com/blog |
| Product pages | databricks.com/product/* |
| Official documentation | docs.databricks.com |
| Developer guides | developers.databricks.com |
| Release notes | docs.databricks.com/.../release-notes |
| Keynote recordings | youtube.com (DAIS 2026 videos) |

---

## RESEARCH METADATA

- **Document compiled:** Oct 7, 2026
- **Research method:** Public-source web search + official Databricks documentation
- **Coverage:** January 2026 – October 7, 2026
- **Total distinct products/features documented:** 50+
- **Total search queries executed:** 19
- **Confidence level:** High (all sources official Databricks channels)
- **Next update recommended:** After next Databricks quarterly announcement or major product release
