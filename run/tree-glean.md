# Databricks AI Cartography (DAIS 2026 → October 2026)

**Research Date:** October 7, 2026  
**Research Method:** Internal Glean knowledge via `mcp__glean__glean_chat`, `mcp__glean__search`  
**Scope:** FY27 AI product taxonomy, DAIS 2026 announcements, September–October 2026 releases

---

## I. FY27 AI Platform Block

Core ML and AI infrastructure: feature engineering, model training, experiment tracking, serving, and serverless GPU compute.

### Feature Store
- **Description:** Unified, governed repository for ML features. Feature Views, offline/online serving, point-in-time joins, automatic feature lookup at inference.
- **Status:** GA
- **Online Store:** Powered by Lakebase for low-latency serving
- **Key Capability:** Synchronization with Unity Catalog; prevents training/serving skew
- **Source:** [Databricks Feature Store on AWS](https://docs.databricks.com/aws/en/machine-learning/feature-store)

### Model Serving
- **Description:** Managed, serverless REST API endpoints for real-time inference and batch workloads. Supports custom, Foundation, and external models.
- **Status:** GA
- **Serving Modes:** Pay-per-token, provisioned throughput, batch inference via AI Functions
- **Endpoints:** ~300K QPS per endpoint; auto-scales
- **Integration:** Feature Store lookup, AI Search, Unity Gateway governance, rate limits, cost attribution
- **Notable:** Foundation models (Llama, Qwen, Gemini, etc.) available through same platform
- **Source:** [Deploy models using Model Serving on AWS](https://docs.databricks.com/aws/en/machine-learning/model-serving)

### AI Runtime (Serverless GPU Compute)
- **Description:** On-demand NVIDIA GPUs (A10, H100) for training, inference, and custom deep learning without provisioning.
- **Status:** GA
- **Use Cases:** LLM fine-tuning (LoRA, QLoRA), distributed training (DDP, FSDP, DeepSpeed), batch inference (Ray, vLLM), computer vision, recommendations
- **Integration:** Notebooks, Jobs, MLflow, Unity Catalog, Ray, frameworks
- **Key Benefit:** Scale-to-zero, pay-per-minute
- **Source:** [AI Runtime on AWS](https://docs.databricks.com/aws/en/machine-learning/ai-runtime)

### MLflow 3 for GenAI
- **Description:** Unified platform for tracing, evaluation, and production observability of LLM applications and agents.
- **Status:** GA
- **Tracing:** End-to-end spans for agents, RAG, LLMs; 30+ framework auto-instrumentation; OpenTelemetry-compatible; interactive UI with filtering, comparisons
- **Evaluation:** Built-in LLM judges (safety, correctness, relevance, fluency, retrieval quality); custom scorers; offline evaluation; human feedback via Review Apps
- **Monitoring:** Production traffic sampling, quality/safety/latency tracking, dashboard/SQL/AI/BI analysis, alerts
- **Storage:** Recommended Delta table backend in UC for scalability and governance
- **Source:** [MLflow 3 for GenAI on AWS](https://docs.databricks.com/aws/en/mlflow3/genai)

### MLflow Model Registry
- **Description:** Centralized repository and governance for ML models with versioning, stage tracking, and lineage.
- **Status:** GA (foundational component of MLflow 3)
- **Integration:** Unity Catalog permissions, audit logs, cross-workspace sharing
- **Source:** [MLflow on Databricks on AWS](https://docs.databricks.com/aws/en/mlflow)

### AutoML
- **Description:** Automated machine learning for tabular data classification and regression.
- **Status:** GA
- **Integration:** Databricks ML Runtime, Feature Store, MLflow tracking
- **Source:** [Classic ML on AWS](https://docs.databricks.com/aws/en/machine-learning/train-model/automl)

### AI Search (formerly Vector Search)
- **Description:** Managed retrieval service for RAG, agents, recommendations. Vector, keyword (BM25), hybrid, and reranking.
- **Status:** GA
- **Retrieval Modes:** ANN (HNSW + L2), keyword search, hybrid fusion (Reciprocal Rank Fusion), metadata filtering, reranking
- **Sync:** Delta Sync indexes auto-synchronize with source tables
- **Governance:** Unity Catalog, permissions, lineage tracking
- **Sept 2026 Update:** Lakebase-synced table support (Beta), citation generation
- **Source:** [Databricks AI Search on AWS](https://docs.databricks.com/aws/en/ai-search/ai-search)

### MLflow Tracing & Evaluation (Detailed)
- **Tracing Tools:** `@mlflow.trace` decorator, manual span creation, framework auto-instrumentation
- **Evaluation Tools:** `mlflow.genai.evaluate()`, LLM judges, code-based scorers
- **Human Feedback:** Review Apps for expert labeling; can label live chat interactions or existing traces
- **Source:** [Tracing overview on AWS](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/overview)

---

## II. FY27 Agent Bricks Block

Managed, optimized agent platform for building, deploying, evaluating, and governing production AI agents.

### AI Functions (Document Intelligence)
- **Description:** SQL- and pipeline-native AI capabilities for batch transformation of data and documents.
- **Status:** GA
- **Functions:** `ai_parse_document`, `ai_extract`, `ai_classify`, `ai_summarize`, `ai_translate`, `ai_search`, `ai_enrich`, `ai_gen`, `ai_mask`, `ai_query`
- **Execution:** SQL, notebooks, Lakeflow Pipelines, Workflows
- **Oct 2026 Update:** `ai_decide` launched for fast, low-cost decisions (routing, classification, evals); `ai_extract` improved to 2.3× faster with quality boost
- **Source:** [Transform unstructured data using AI Functions on AWS](https://docs.databricks.com/aws/en/large-language-models/ai-functions)

### Knowledge Assistant (Legacy)
- **Description:** Document-grounded chatbot builder using Instructed Retriever; citation-rich answers.
- **Status:** GA, but documented as legacy for new development; **Genie Agents recommended instead**
- **Capabilities:** Managed ingestion, synchronization, SME feedback, examples, endpoint exposure, SDK/API management
- **Source:** [Knowledge Assistant on AWS](https://docs.databricks.com/aws/en/agents/agent-bricks/knowledge-assistant)

### Supervisor Agent (Multi-Agent Orchestration)
- **Description:** Managed multi-agent orchestrator routing requests across specialized agents and tools.
- **Status:** GA (with Beta SDK management surface)
- **Orchestrates:** Genie Agents, Knowledge Assistant endpoints, Model Serving endpoints, UC functions, AI Search, MCP services, custom agents, web search, sandboxed code
- **Auth:** User-scoped access control (users only reach data/tools they're authorized for)
- **Status Note:** Documented as transitioning; **custom Agent Bricks development and Genie Agents recommended for new use cases**
- **Source:** [Multi-Agent Supervisor on AWS](https://docs.databricks.com/aws/en/agents/agent-bricks/multi-agent-supervisor)

### Custom Agents (Code-First Developer Platform)
- **Description:** Full control over orchestration, tools, models, UI, and application behavior. Primary path for developers.
- **Status:** GA (CLI Beta, runtime GA)
- **Frameworks:** LangGraph, Agno, CrewAI, Claude Code SDK, OpenAI Agent SDK
- **Tooling:** Agent Bricks CLI, Agent Server, DurableAgentServer (crash-recoverable, background execution)
- **Runtime:** Managed Databricks infrastructure with automatic scaling
- **Memory & Sessions:** Managed via Lakebase
- **Execution:** Databricks Sandbox for isolated code with scoped UC data access
- **Configuration:** Declarative `agent.toml` for model access, memory, tools, tracing, deployment
- **DAIS 2026 Announcements:**
  - Broader model choice (OpenAI, Anthropic, Gemini, Qwen, Kimi, Grok, etc.)
  - Any agent harness support
  - Richer enterprise context via MCP + UC
  - Managed memory/sessions via Lakebase
  - Document Intelligence as core building block
  - Secure execution via Databricks Sandbox
- **Source:** [Agent Bricks: Data + AI Summit 2026 Blog](https://www.databricks.com/blog/agent-bricks-dais-2026)

### Omnigent (Agent Meta-Harness)
- **Description:** Open-source layer above agent harnesses (Claude, Codex, Cursor, Pi, custom). Composes agents, models, and harnesses with unified control.
- **Status:** Beta
- **Databricks-Managed Version:** Integrates with workspace identity, Unity Gateway, Databricks Sandbox
- **Features:** Stateful policies, permissions, cost limits, logging, sandboxing, shared live sessions (web, terminal, desktop, mobile, APIs)
- **Source:** [Omnigent on Databricks on AWS](https://docs.databricks.com/aws/en/omnigent)

### Agent Bricks CLI & Deployment
- **Description:** Scaffolding, local development, and deployment tooling for agents.
- **Status:** Beta (CLI), GA (runtime)
- **Provisioning:** Model access, memory backends, sessions, tools, tracing, deployment via declarative config
- **Agent Server:** Synchronous/streaming execution; DurableAgentServer for crash recovery and background jobs
- **Source:** Implicit in Agent Bricks documentation

### Agent Evaluation & Monitoring
- **Description:** Systematic evaluation of agent quality, safety, and behavior using traces and LLM judges.
- **Status:** GA (via MLflow Tracing & Evaluation)
- **Integration:** Traces → Review Apps → evaluation datasets → LLM judges → monitoring dashboards
- **Source:** [Evaluate and improve on AWS](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor)

---

## III. FY27 Agentic Data Management Block

AI-powered data management: classification, profiling, quality monitoring, anomaly detection, automated remediation.

### Data Classification
- **Description:** Discovering, labeling, and governance of sensitive, regulated, or business-critical columns.
- **Status:** Part of Agentic Data Management; integrated with UC
- **Governance:** Tagging, access policies, row/column-level controls
- **Source:** Implicit in [AI governance guide on AWS](https://docs.databricks.com/aws/en/ai-gateway/ai-governance)

### Data Profiling / Lakehouse Monitoring
- **Description:** Automated inspection of schemas, distributions, nulls, cardinality, freshness, usage patterns.
- **Status:** GA (as foundational capability supporting quality monitoring and anomaly detection)
- **Output:** Baselines, trust signals, quality metrics
- **Source:** Implicit in Lakehouse Monitoring / governance

### Data-Quality Monitoring
- **Description:** Continuous measurement of table/data quality with AI-driven, automated detection.
- **Status:** GA (integrated with Unity Catalog)
- **Approach:** AI agents monitor, alert, and recommend or execute remediation
- **Source:** Implicit in [Unity Catalog on AWS](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)

### Anomaly Detection
- **Description:** Identification of unusual changes in data, pipeline behavior, or system performance.
- **Status:** GA
- **Example Use:** Genie Code can monitor Lakeflow Pipelines and investigate anomalies
- **Source:** Implicit in Genie Code capabilities

### Automated Remediation & Optimization
- **Description:** Diagnosing failures, proposing fixes, maintaining pipelines, optimizing resources/storage.
- **Status:** Emerging (agentic capabilities expanding)
- **Governance:** Permissions, safeguards, governed execution
- **Source:** Implicit in Agentic Data Management positioning

---

## IV. FY27 AI Products Block

Interactive product-line components (horizontal, overlapping category).

### Interactive Notebooks (Non-AI Training)
- **Description:** Notebook workloads that use interactive compute but not ML Runtime, GPU, Feature Store, or AutoML.
- **Status:** GA
- **Distinction:** Training/AI workloads excluded; counted separately in AI Platform
- **Source:** [FY27 Product Lines Definitions](https://docs.google.com/document/d/150q5aVsnlhA44dol3-XL7LtxOs3K7skIfQNxJyROYxU)

### DBSQL (Interactive SQL)
- **Description:** Interactive SQL editor and querying on Lakehouse data.
- **Status:** GA
- **Included in AI Products:** When used for interactive workloads (not training/serving)
- **Source:** [SQL Warehouses on AWS](https://docs.databricks.com/aws/en/sql/)

### AI/BI Dashboards (Lakeview)
- **Description:** AI-assisted authoring for analytical datasets and interactive visualizations.
- **Status:** GA
- **Features:** Auto-suggestions, filters, sharing, subscriptions, embedding, dashboard-level Genie
- **Public Preview Features:** Dashboard relationships, external embedding
- **GA Features:** Local metric views
- **Source:** [Dashboards on AWS](https://docs.databricks.com/aws/en/dashboards)

### Databricks Apps (Excluding Agents)
- **Description:** Serverless containerized web applications (Streamlit, Gradio, React, FastAPI, Flask). Metric: `apps_excl_agents_dollars`
- **Status:** GA
- **Use Cases:** Interactive dashboards, operational workflows, custom front ends for models/Genie
- **Authorization Models:** App principal (shared resources) or user principal (scoped to user entitlements)
- **Deployment:** UI, CLI, Git, CI/CD; automatic deployments via GitHub Actions
- **Observability:** Telemetry export to UC, production monitoring of agent behavior
- **Source:** [Databricks Apps on AWS](https://docs.databricks.com/aws/en/dev-tools/databricks-apps)

### Predictive Optimization
- **Description:** Automated, ROI-based maintenance for Unity Catalog managed tables (OPTIMIZE, VACUUM, ANALYZE, clustering).
- **Status:** GA
- **Key Insight:** Avoids unnecessary operations and compute costs by analyzing workload patterns
- **Monitoring:** `system.storage.predictive_optimization_operations_history`
- **Source:** [Predictive optimization for Unity Catalog managed tables on AWS](https://docs.databricks.com/aws/en/optimizations/predictive-optimization)

---

## V. Genie / AI/BI Family (Separate Adjacent Category)

Unified AI experience layer for business users and developers.

### Genie One (Unified BI Experience)
- **Description:** Cross-asset discovery, question-answering, dashboard exploration, document creation, AI app access across web, mobile, Slack, Teams, and MCP clients.
- **Status:** GA (with some preview/Beta surfaces)
  - Core GA (web, unified experience)
  - Native mobile: Public Preview
  - macOS desktop app: Beta
  - Account-only user access: Beta
- **Memory:** GA (September 2026) — retains user preferences and reporting conventions
- **MCP Server:** GA (September 2026) — Genie One accessible to Claude, ChatGPT, Cursor, MCP Inspector
- **Pricing Note:** Free for named users through January 31, 2027; service-principal usage billable
- **Source:** [Genie One on AWS](https://docs.databricks.com/aws/en/genie-one/)

### Genie Agents (No-Code Agent Builder)
- **Description:** Domain-specific, governed agents configured with Unity Catalog data, example SQL, business semantics, instructions, and verified answers.
- **Status:** GA (July 2026 onward; previously "Genie Spaces")
- **Features:**
  - Agent mode, management APIs, dashboard integration, iframe embedding, Agent-mode APIs (all GA)
  - Deeper analysis and file reasoning (Sept 2026)
  - File reasoning capabilities expanded (Sept 2026)
- **Pricing:** Free for named users through January 31, 2027
- **Source:** [Genie Agents on AWS](https://docs.databricks.com/aws/en/genie-agents)

### Genie Code (Technical Assistant)
- **Description:** AI co-pilot for notebooks, SQL, pipelines, dashboards, MLflow, and multi-step data/engineering tasks.
- **Status:** GA
- **March 2026 Update:** Renamed from "Databricks Assistant"; expanded autonomous, multi-step capabilities
- **Agent Mode:** GA (March 2026)
- **Preview/Beta Features:** AI Runtime support, web search, Lakeflow Jobs task
- **Sept 2026 Feature:** Intelligent document processing (end-to-end pipelines for parsing, classification, extraction, validation of PDFs, contracts, invoices)
- **Pay-Per-Use Pricing:** Per-user free monthly allowance; usage metered
- **Source:** [Genie Code on AWS](https://docs.databricks.com/aws/en/genie-code)

### AI/BI Dashboards (Also Listed Above)
- **Genie-Level Integration:** Dashboard-level Genie for natural-language queries over visual data
- **Status:** GA
- **Source:** [AI/BI and Genie One release notes 2026](https://docs.databricks.com/aws/en/ai-bi/release-notes/2026)

### Genie Ontology (Business Context Graph)
- **Description:** Continuously learned business-context layer combining Unity Catalog semantics with inferred business understanding.
- **Status:** Public Preview
- **Sept 2026 Update:** Operationalization improvements for use in AI agents
- **Purpose:** Improves grounding and answer quality for Genie One, Genie Agents, and downstream agents
- **Source:** [Introducing Genie One, Genie Ontology, and Genie Agents Blog](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents)

### Genie Spaces (Renamed)
- **Previous Name:** "Genie Spaces"
- **Current Name:** "Genie Agents" (July 2026)
- **Change:** Rename only; core product unchanged
- **Legacy API Names:** Resource names such as `genie_spaces` may still appear in older code
- **Source:** Implicit in Genie Agents documentation

---

## VI. Unity Catalog & Governance Layer

Centralized control plane for data, models, agents, tools, and AI governance.

### Unity Catalog (Asset Governance)
- **Description:** Unified, governed repository for all data and AI assets: tables, volumes, functions, models, agents, MCP services, connections, skills, credentials.
- **Status:** GA (extended for AI assets at DAIS 2026 and beyond)
- **Securable Objects for AI:**
  - Registered ML models
  - Foundation models and external-provider services
  - Agents (governance of model/tool access)
  - SQL/Python UC functions (as tools)
  - MCP Services (external tool providers)
  - Connections (API credentials, OAuth tokens)
  - Skills (instructions and metadata; executable tools governed separately)
- **Governance Mechanisms:** Permissions (GRANT/REVOKE), row/column-level filters, lineage, audit logs, usage tracking
- **Business Semantics:** Domains, business glossaries, Genie Ontology foundation
- **Source:** [Unity Catalog on AWS](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)

### Unity AI Gateway (Traffic & Policy Governance)
- **Announced:** DAIS 2026 (renamed from "AI Gateway" for clarity)
- **Status:** GA (September 2026 documentation update)
- **Description:** Enterprise control plane for AI traffic, routing, policies, cost management, and observability.
- **Governance Model:**
  - **UC governs assets:** permissions on models, agents, tools, connections
  - **Gateway governs runtime:** request routing, rate limits, budgets, service policies, usage attribution
- **Features:**
  - Asset governance (models, MCP services, functions, connections registered as UC securable objects)
  - Agent & tool governance (MCP tools governed via MCP Services; on-behalf-of execution preserves user permissions)
  - Traffic management (routing, rate limits, fallbacks, Smart Routing for model selection)
  - Runtime guardrails (service policies for content/caller-based allow/deny/approval, PII redaction, injection detection, custom rules)
  - Cost controls (attribution by user/team/project/endpoint/model/tags, budgets, usage blocking)
  - Observability (system tables for request tracking, tokens, latency, errors, identity; optional payload logging to Delta tables)
  - Multi-provider control (apply same governance to Databricks-hosted, external, and external-MCP models)
- **September 2026 Update:** Expanded documentation as governance layer for models, agents, MCP services, tools, skills
- **Source:** [Unity Gateway: Governance Layer for Agentic AI Blog](https://www.databricks.com/blog/ai-gateway-governance-layer-agentic-ai)

### MLflow Tracing, Evaluation, and Monitoring
- Already detailed above under **AI Platform Block**

### Review Apps (Human-in-the-Loop Feedback)
- **Description:** Web interface for domain experts to review GenAI traces and provide structured feedback.
- **Workflows:**
  1. Chat UI testing: experts interact with deployed agents and provide immediate feedback
  2. Reviewing traces: experts label existing MLflow traces with feedback (ratings, classifications, expectations)
- **Feedback Storage:** Attached to traces as MLflow assessments
- **Use Case:** Create expert-labeled evaluation datasets for LLM judges and automated scorers
- **Status:** GA
- **Source:** [Enable experts and collaborators to label traces on AWS](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/expert-feedback/label-existing-traces)

---

## VII. Data Foundation & Infrastructure

Lakehouse, data engineering, and transactional layers.

### Lakehouse / Delta Lake
- **Description:** Open data format and unified analytics architecture combining data lake and data warehouse.
- **Status:** GA (foundational)
- **Capabilities:** ACID transactions, schema enforcement, scalable data ingestion (batch and streaming), governed metadata
- **Role in AI:** Provides trusted, fresh data for models, agents, RAG, analytics
- **Source:** [Databricks Lakehouse on AWS](https://www.databricks.com/product/lakehouse)

### Lakeflow (Data Engineering Platform)
- **Components:**
  1. **Lakeflow Connect:** Managed ingestion from databases, SaaS, files, cloud storage, streaming systems
  2. **Lakeflow Pipelines:** Batch and streaming data transformation (SQL/Python)
  3. **Lakeflow Designer:** Visual, no-code canvas + Genie Code natural-language UI for data prep; produces production-ready code
  4. **Lakeflow Jobs:** Orchestration and monitoring for data, analytics, and AI workflows
- **Status:**
  - Connect, Pipelines, Jobs: GA
  - Designer: Public Preview → expanding toward GA
- **AI Integration:** Designer leverages Genie Code for natural-language transformation descriptions; supports AI Functions for data enrichment
- **Sept 2026 Update:** Designer capabilities expanded; Genie Code dashboard authoring became GA
- **Source:** [Data engineering with Databricks on AWS](https://docs.databricks.com/aws/en/data-engineering)

### Lakebase (Serverless PostgreSQL)
- **Description:** Fully managed, serverless PostgreSQL database for transactional applications and AI agents.
- **Status:** GA (announced DAIS 2026; continued expansion)
- **Key Characteristics:**
  - PostgreSQL compatibility and ecosystem
  - Compute/storage separation with autoscaling (scale-to-zero)
  - Database branching for dev/test
  - HA, backups, point-in-time recovery
  - Synchronization with UC tables
  - Primary store for agent memory, application state, low-latency serving
- **Use in AI:** Memory layer for agents, session persistence, transactional state
- **Source:** [Lakebase Postgres on AWS](https://docs.databricks.com/aws/en/oltp/projects)

### Lakebase Search
- **Description:** Native semantic, keyword, and hybrid search inside Lakebase PostgreSQL.
- **Status:** GA (announced September 28, 2026)
- **Search Types:**
  - Vector search via `lakebase_vector` (HNSW index `lakebase_ann`)
  - Keyword/full-text search via `lakebase_text` (BM25 index `lakebase_bm25`)
  - Hybrid search combining semantic similarity and exact-term relevance
  - Configurable tokenization via `lakebase_tokenizer`
- **Advantage:** No separate vector database; agent can write memory, then immediately search it in same Postgres backend
- **Source:** [Lakebase Search on AWS](https://docs.databricks.com/aws/en/oltp/projects/lakebase-search)

### AI Search / Vector Search (Detailed)
- Already detailed above under **AI Platform Block**

---

## VIII. Foundation Models & LLM Access

Multi-provider model access with unified governance.

### Foundation Model APIs
- **Description:** Managed access to hosted models through pay-per-token, priority, or provisioned-throughput pricing.
- **Status:** GA
- **Available Models:**
  - **Anthropic:** Claude Haiku, Sonnet, Fable, Opus
  - **OpenAI:** GPT, GPT Codex, GPT OSS
  - **Google:** Gemini Flash, Gemini Pro, Gemini image generation, Gemma
  - **Meta:** Llama 4 Maverick, Llama 3.3 70B, Llama 3.1 8B
  - **Qwen (Alibaba):** Qwen 3.5, Qwen3-Next, Qwen3-Embedding
  - **xAI:** Grok
  - **Moonshot:** Kimi
  - **Zhipu AI:** GLM
  - **DeepSeek:** DeepSeek V4 Flash, V4 Pro
  - **Thinking Machine Labs:** Inkling
  - **Embeddings:** Qwen3-Embedding-0.6B, GTE-Large-En, BGE-Large-En (Databricks-hosted); OpenAI, Cohere, Google (external)
- **Oct 2026 Updates:** Gemini 2.5 Pro/Flash retired; Gemini 3.1 Pro/Gemini 3.5 Flash recommended
- **Access Modes:**
  - Pay-per-token for experimentation/variable workloads
  - Priority pay-per-token for consistent latency
  - Provisioned throughput for production SLAs
- **Integration:** Unity Gateway, Model Serving, AI Functions, agents
- **Source:** [Databricks Foundation Model APIs on AWS](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis)

### External Model Services
- **Description:** Governed access to models hosted by OpenAI, Anthropic, Google, and other external providers.
- **Status:** GA
- **Governance:** Via Unity Gateway, UC Connections (credentials), rate limits, cost attribution, observability
- **Source:** [Available models in Unity Gateway on AWS](https://docs.databricks.com/aws/en/machine-learning/model-serving/foundation-model-overview)

### Model Fine-Tuning
- **Description:** Post-training, instruction-tuning, and continued pre-training capabilities via Databricks on supported models.
- **Status:** GA (for select models; availability varies)
- **Frameworks:** LoRA, QLoRA, full fine-tuning, RL fine-tuning (where supported)
- **Integration:** AI Runtime GPU compute, MLflow tracking
- **Source:** [Databricks Fine-Tuning on AWS](https://docs.databricks.com/aws/en/machine-learning/model-serving/foundation-models/fine-tuning)

### AI Runtime (Serverless GPU Compute)
- Already detailed above under **AI Platform Block**

---

## IX. Model Interoperability & MCP Integration

Standard interfaces for tools, models, and external systems.

### MCP Integration (Model Context Protocol)
- **Description:** Standard interface for apps to expose tools and data to AI models and agents.
- **Status:** GA (Databricks MCP integrations announced GA September 2026)
- **Databricks Governance:** Assets registered in UC, traffic routed through Gateway, policies enforced, audit logged

### Databricks-Managed MCP Servers
- **Genie One MCP:** Natural-language analytics grounded in Genie Ontology; access to Genie Agents and workspace assets
  - Status: GA (September 2026)
  - Clients: Claude, ChatGPT, Cursor, MCP Inspector, external agents
- **Genie Agent MCP:** Natural-language analytics scoped to a specific Genie Agent
- **AI Search MCP:** Retrieval over unstructured documents
- **Databricks SQL MCP:** Execute SQL; developer/data-engineering workflows
- **Unity Catalog Functions MCP:** Expose SQL/Python UC functions as tools
- **Code Interpreter MCP:** Execute Python through `system.ai.python_exec` function

**Source:** [Managed MCP servers on AWS](https://docs.databricks.com/aws/en/agents/mcp-tools/managed-mcp)

### Databricks-Provided External Connectors
- **Available (GA as of Sept 2026):**
  - Google Drive, Gmail, Google Calendar
  - Microsoft 365 (SharePoint, Teams, Outlook, Calendar)
  - Atlassian (Jira, Confluence)
  - Slack
  - GitHub
  - Glean (Beta)
- **Meta Ads MCP Server:** Announced October 6, 2026; enables governed customer-intelligence workflows for advertising campaigns
- **Authentication:** Per-user OAuth; UC + Gateway govern tool calls, permissions, policies, audit logging
- **Limitations:** Gmail (search/read/draft, no send); GitHub (file/issue/PR writes, private-repo setup required); Glean (search only)

**Source:** [Connect to external tools and sources on AWS](https://docs.databricks.com/aws/en/genie-one/external-sources)

### MCP Services (External MCP Servers)
- **Description:** Register external MCP servers as UC securable objects.
- **Status:** GA
- **Governance:** UC permissions, credentials via UC Connections, traffic routed through Gateway, policies enforced, observability via system tables
- **Source:** [Connect agents to tools with MCP Services on AWS](https://docs.databricks.com/aws/en/agents/mcp-tools/mcp-services)

### Custom MCP Servers
- **Description:** Deploy your own stateless MCP server as a Databricks App.
- **Status:** GA (Databricks Apps GA; custom MCP deployment pattern available)
- **Integration:** Connect to agents or MCP clients
- **Source:** [Use MCP servers in Custom Agents on AWS](https://docs.databricks.com/aws/en/agents/mcp-tools/use-mcp-in-agents)

---

## X. Application Deployment Layer

User-facing AI applications and interfaces.

### Databricks Apps (AI Applications)
- Already detailed above under **AI Products Block**
- **For AI Use:** React frontends, FastAPI backends, Streamlit dashboards, Gradio interfaces connected to Model Serving, agents, Genie, Vector Search
- **Authorization:** App principal (shared) or user principal (scoped to user entitlements)
- **Observability:** Trace export to UC; production monitoring of agent behavior
- **Source:** [Databricks Apps on AWS](https://docs.databricks.com/aws/en/dev-tools/databricks-apps)

### Agent Deployment Patterns
- **Model Serving Endpoint:** Agents deployed as REST API endpoints (real-time inference)
- **Databricks App:** Agents deployed with custom UI/orchestration/workflows
- **Genie Agents:** No-code agents accessible via Genie One and embedded
- **Custom Agent Bricks:** Code-first agents running on Agent Runtime or Model Serving
- **Integration:** Tracing (MLflow), evaluation (LLM judges), monitoring (dashboards/SQL), governance (UC, Gateway)

---

## XI. Research & Enablement Artifacts

Key canonical decks and organizational touchpoints.

### Official Enablement Resources
- **go/AIR/Enablement:** Core AI Enablement portal (internal)
- **L150: Databricks AI:** Technical pitch for "How to Get Started"; covers AI product value props
  - Mentions Mosaic AI research backing (test-time optimization, custom judges, deep research)
  - URL: [L150 Databricks AI](https://docs.google.com/presentation/d/1Om7kpipQNicaBmPFd6zv1TdIvg2_2f-_uJYddu70RKs)
- **Agentic Apps GTM L100 Deck:** Go-to-market messaging for Agent Bricks
- **AI Gateway Enablement Deck:** Governance and Unity Gateway field messaging
- **AI Field SOP (go/ai-field-sop):** Field processes and documentation
- **FY27 Product Lines Definitions:** Internal taxonomy and revenue attribution (referenced throughout)
  - URL: [FY27 Product Lines Definitions](https://docs.google.com/document/d/150q5aVsnlhA44dol3-XL7LtxOs3K7skIfQNxJyROYxU)
- **AI Search Field Enablement Portal:** Dedicated retrieval/RAG resources
- **Genie and AI/BI Field Portal:** Unified BI enablement

### Field Engagement & Solutions
- **[FieldKit] Mosaic AI Agents:** Solution templates for agent deployment
- **AI Dev Kit (go/ai-dev-kit):** Scaffolding and tooling for Databricks agent development; MCP tools and Skills for Claude Code/Cursor
- **Big Book of AgentOps (Sept 2026):** Enterprise guidance for governed, observable AI agents; covers UC, Gateway, MLflow

### Customer Pitch Decks
- **AI Pitch Deck:** Generic GenAI use cases (battery optimization, fraud detection, customer insights)
- **GenAI-CustomerReferences:** Customer case studies and proof points
- **GenAI on Databricks:** General GenAI positioning
- **Databricks Pitch Deck FY27:** Enterprise AI agent ROI messaging; real-world proof

---

## What's NEW Since DAIS 2026 (Internal Framing: Sept–Oct 2026)

### September 2026 Product Developments

1. **Genie Ontology Operationalization** (Sept 1)  
   - Improvements for embedding business context in AI agents
   - Enhanced grounding and answer quality

2. **Expanded Genie Agents** (Sept 2)
   - Deeper analysis capabilities
   - File reasoning enhancements

3. **Big Book of AgentOps** (Sept 2)
   - Enterprise governance and observability playbook
   - Unity Catalog, Gateway, MLflow integration patterns

4. **Adaptive Instructed-Retriever** (Sept 9)
   - Frontier retrieval quality at ~2× lower latency
   - Improved RAG performance

5. **Web Search for Agents** (Sept 17)
   - Research and product direction addressing agent web-search limitations
   - Improved external knowledge access

6. **Genie One MCP Server GA** (Sept 24)
   - Genie accessible to Claude, ChatGPT, Cursor, MCP Inspector
   - Unity Catalog permissions enforced
   - Governed access to Genie analytics from external agents

7. **Genie Code Intelligent Document Processing** (Sept 25)
   - End-to-end PDF/contract/invoice pipelines
   - Parsing, classification, extraction, validation

8. **AI Search Enhancements** (Sept 25)
   - Lakebase synced-table support (Beta)
   - Citation generation for retrieved chunks

9. **Lakebase Search Launch** (Sept 28)
   - Native vector + keyword search in PostgreSQL
   - Hybrid search without separate vector database

10. **Unity Gateway Documentation Expansion** (Sept 29)
    - Comprehensive governance layer positioning
    - Access control, routing, guardrails, observability, cost management

11. **AI Decide Function** (Sept 30)
    - Fast, low-cost decisions: model routing, document classification, agent evaluation
    - Complementary to AI Functions

### October 2026 Product Developments

1. **Improved AI Extract** (Oct 2)
   - 2.3× faster extraction quality without additional cost
   - Checkpoint improvements

2. **Meta Ads MCP Server** (Oct 6)
   - Integration of Meta's Ads MCP
   - Enabled customer-intelligence workflows for advertising

3. **Model Availability Changes** (October)
   - Retired: Gemini 2.5 Pro, Gemini 2.5 Flash
   - Recommended: Gemini 3.1 Pro, Gemini 3.5 Flash

4. **Genie Commercial Update** (October)
   - Genie One and Genie Agents: free for named users through January 31, 2027
   - Service-principal usage remains billable

---

## Key Themes & Positioning (Oct 2026)

**Overarching Narrative:** "Governed platform for the agentic enterprise"

1. **Agent Bricks = Full Production Platform**  
   Model choice, evaluation, multi-agent dev, framework integration, governed deployment

2. **Unity AI Gateway = Enterprise Governance Layer**  
   Runtime policies, routing, budgets, observability, multi-provider control

3. **Genie = AI Coworker Family**  
   One (unified experience), Agents (no-code), Code (technical), Ontology (context)

4. **Omnigent = Meta-Harness Standardization**  
   Composable, controlled, scalable agent coordination

5. **AI Runtime = Serverless ML Compute**  
   On-demand GPUs, cost-effective, integrated with notebooks/jobs/frameworks

6. **MCP = Ecosystem Integration**  
   Databricks-managed servers + external connectors + custom services, all governed

7. **Lakehouse + Lakebase = Data Foundation**  
   Analytics-optimized + transactional-optimized, unified governance

8. **Agentic Data Management = Active Data Ops**  
   Classification, monitoring, remediation, not just rules-based alerting

9. **Field Priorities**  
   Enterprise agent deployment, RAG grounding, safety/governance, cost control

---

## Recognized Canonical Deck Titles & Authors

*Note: Specific author roles/seniority not yet resolved. Will be updated if org-chart data becomes available.*

### Canonical Decks (Quality Signals for Round 2)

- **L150: Databricks AI** — "How to Get Started" technical pitch
  - Mentions Mosaic AI research team contributions
  - Strong field enablement signal

- **FY27 Product Lines Definitions** — Internal product taxonomy and revenue model
  - Reference for all product block definitions
  - Field SOP anchor

- **Databricks Pitch Deck FY27** — Enterprise AI agent ROI messaging
  - Customer proof points, real-world impact

- **Big Book of AgentOps** (Sept 2026) — Enterprise governance playbook
  - Canonical for UC/Gateway/MLflow patterns

- **Agentic Apps GTM L100 Deck** — Go-to-market for Agent Bricks
  - Field messaging anchor

- **Data & AI Governance - Full Deck** — Governance framework reference
  - Referenced in glean_chat for UC governance scope

### Authors / Key Teams (To Resolve)

- **Mosaic AI Research Team** — Test-time optimization, custom judges, agent deep-research workflows
- **Field Engineering AI Leadership** — Field enablement and customer success alignment
- **Product Management (Agents, Genie, Gateway, Lakeflow)** — Specific individuals TBD

---

## Known Limitations & Flagged Uncertainties

1. **Author Resolution:** Specific individuals and titles not yet identified via `mcp__glean__get_person`. Can be resolved in Round 2 with email-based lookups.

2. **Beta/Limited GA Features:** Some capabilities listed as "Beta" or "Public Preview" may have narrower regional/cloud availability. Recommend checking latest regional availability matrix.

3. **Pricing & Commercial Terms:** Free tier for Genie One/Genie Agents explicitly stated as **through January 31, 2027** — subject to change. Service-principal usage always billable.

4. **Model Availability:** Foundation Model APIs availability varies by cloud (AWS, Azure, GCP), region, and workspace configuration. Recommend validating against [Detailed list of models supported by Databricks Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models).

5. **MCP Connectors for Genie Code:** Exact limitations and supported actions (e.g., GitHub write restrictions, Gmail send restrictions) documented in Genie Code MCP docs; confirm before customer recommendation.

6. **Lakebase Availability:** Lakebase and Lakebase Search announced at DAIS 2026; October 2026 status suggests GA, but regional rollout status should be verified.

---

## Summary Statistics

- **Total AI Blocks/Pillars:** 6 main FY27 blocks + Genie family + Governance + Data Foundation + Models + MCP + Apps = **10+ ecosystem layers**
- **Product Count (Rough):** 40+ distinct capabilities/products across the tree
- **DAIS 2026 Announcements:** 8 major themes + 10+ component launches
- **Sept–Oct 2026 Releases:** 15 product/feature developments
- **Canonical Decks:** 8+ identified field resources
- **MCP Integrations:** 7+ Databricks-managed servers + 9+ external connectors + custom MCP pattern
- **Governance Scope:** Data, models, agents, MCP services, functions, connections, skills, credentials

---

## Recommended Next Steps (Round 2)

1. **Resolve Authors:** Use `mcp__glean__get_person` with emails from canonical deck metadata to confirm org roles and seniority.

2. **Drill into Specific Features:** Deep-dive on next-gen features (Omnigent roadmap, Genie Ontology scaling, Lakebase Search production patterns).

3. **Verify Regional/Cloud Availability:** Cross-reference product status against official Databricks regional matrix.

4. **Collect Customer Case Studies:** Mine GenAI-CustomerReferences for proof points and vertical/use-case segmentation.

5. **Field Feedback Loop:** Validate against SSA/SA notes from Q4 2026 customer engagements to identify gaps and real-world priority shifts.

