# Story pains

> **Archived on 2026-10-17.** The Story follows the plan in `docs/feature-tree.md` (v2), which has no "Challenges" chapter: it opens with the platform architecture and goes straight to the features. This file describes chapter 1 of v1. No script reads it.

Generated from `app/src/story.json` and the trees, for `docs/story-starting-situation.md`. For each chapter, the capsules its points cite and the pains each one solves: the `problem` of its `solves` rows, word for word (bold markers removed).
Counts: 11 chapters, 40 points, 59 capsule references, 258 pains, 10 capsule references without pains (2.5 Classification / profiling / monitoring, 3.1 Notebooks & collaboration, 3.1 Data prep & EDA, 3.1 DS languages & frameworks, 4.2 Model versions, 4.2 Model lifecycle churn (Oct), 5.3 External connectors, 7.3 DASF v3.0, 11.3 Monitoring & evaluation, 11.4 MLOps & CI/CD).


## 1. Challenges

No capsule: this chapter states the starting situation.

## 2. Data and AI foundation

**2.1 · Lakehouse / Delta Lake** (ai)
- [0] Data corruption mid-stream
- [1] Enforcement breaks on change
- [2] Separate stores for batch/stream
- [3] Proprietary or complex formats
- [4] Transactional inconsistency

**2.2 · Lakeflow** (ai)
- [0] Manual connector code
- [1] Pipeline orchestration complex
- [2] SQL/Python required for ETL
- [3] Workflows hardcoded manually
- [4] Job dependencies manual

**2.2 · Predictive Optimization** (ai)
- [0] Manual OPTIMIZE scheduling
- [1] Clustering keys hand-tuned
- [2] Maintenance overtunes tables
- [3] Only UC managed eligible
- [4] Maintenance job overhead

**2.3 · Lakebase — serverless Postgres** (ai)
- [0] Session memory external to DB
- [1] Online/offline mismatch
- [2] App data ungoverned
- [3] Prod data in test env
- [4] Single-point failure

**2.3 · Lakebase Search** (ai)
- [0] Semantic or keyword separately
- [1] Separate vector DB required
- [2] Merging results manually
- [3] Vector data replicated elsewhere

**2.4 · Lakehouse//RT** (ai)
- [0] BI and dashboard queries slow (seconds)
- [1] Copied serving data stale vs operational source
- [2] Separate OLAP warehouse + operational copy
- [3] Dashboard users bottleneck shared warehouse
- [4] Limited analytical SQL supported

**2.4 · LTAP** (ai)
- [0] Replication pipelines needed between operational DB and warehouse
- [1] Eventual consistency lag between operational and analytical
- [2] Maintain two systems (Postgres + Warehouse)
- [3] Data duplication and replication overhead
- [4] Stale operational data in analytics

**2.5 · Classification / profiling / monitoring** (ai)
- no pains in the tree

**2.5 · Anomaly detection & remediation** (ai)
- [0] Data freshness invisible
- [1] Deep profiling schemas slow
- [2] Repairs manual and risky
- [3] No notification channels
- [4] Repair policies undocumented

## 3. Data science lifecycle

**3.1 · Notebooks & collaboration** (ds)
- no pains in the tree

**3.1 · Data prep & EDA** (ds)
- no pains in the tree

**3.1 · DS languages & frameworks** (ds)
- no pains in the tree

**3.2 · Feature Store** (ai)
- [0] features computed differently at training vs inference
- [1] features scattered across systems
- [2] features recreated per project
- [3] manual feature lookups costly
- [4] training data point-in-time errors common

**3.2 · Feature Store** (ds)
- [0] Features computed differently at training vs inference cause skew in production
- [1] Teams duplicate features across projects wasting resources
- [2] No visibility into feature origins and dependencies
- [3] Ungoverned access to features across teams
- [4] Apps must handle complex client-side feature lookup logic
- [5] Offline features become stale between batch updates

**3.3 · MLflow** (ds)
- [0] Experiments are not reproducible without tracked parameters and code versions
- [1] Teams work in isolation with scattered metrics and results
- [2] No visibility into models across workspaces
- [3] Manual version management creates inconsistency and confusion
- [4] Agent/LLM behavior is opaque with no intermediate step visibility
- [5] Untracked resource usage leads to unexpected costs

**3.3 · AutoML** (ai)
- [0] manual testing multiple algorithms tedious
- [1] hyperparameter search time-consuming
- [2] manual data cleaning and prep needed
- [3] model selections opaque to teams
- [4] ML iteration slow and manual

**3.3 · AutoML** (ds)
- [0] Data scientists manually search through algorithms causing delays
- [1] Hyperparameter optimization is tedious and often incomplete
- [2] Manual experimentation is slow delaying model deployment
- [3] AutoML results are black boxes without visibility into how models work
- [4] Feature importance is unclear limiting model interpretability
- [5] Limited to specific problem types requiring multiple tools

**3.4 · Distributed training & GPU** (ds)
- [0] Data/models exceeding single-machine memory cannot train locally
- [1] Distributed training code is complex and difficult to write correctly
- [2] Inter-node communication causes performance degradation at scale
- [3] Single-machine training has limited throughput and speed
- [4] Manual GPU provisioning and cluster configuration is error-prone

**3.4 · AI Runtime — serverless GPU** (ai)
- [0] GPU scarcity delays training
- [1] overprovisioned GPUs idle
- [2] data pipeline optimization manual
- [3] multi-GPU setup complex
- [4] GPU usage and training visibility poor

## 4. Model access and governance

**4.1 · Model Serving** (ai)
- [0] multiple serving systems per provider
- [1] manual infrastructure provisioning
- [2] fragmented model access control
- [3] separate queries for features and models
- [4] idle compute wastes spend

**4.2 · Foundation Model APIs** (ai)
- [0] Vendor lock-in to single model provider
- [1] Unpredictable token spend growth
- [2] Unavailable endpoints during peak usage
- [3] Fragmented testing across providers
- [4] Expensive pay-per-token for production

**4.2 · Model versions** (ai)
- no pains in the tree

**4.2 · Model lifecycle churn (Oct)** (ai)
- no pains in the tree

**4.3 · Model fine-tuning** (ai)
- [0] full fine-tune requires large GPU memory
- [1] fine-tuning expensive with full GPU
- [2] model adaptation slow with full training
- [3] one approach for all use cases
- [4] fine-tuned models isolated from serving

**4.4 · External model services** (ai)
- [0] API keys scattered across code and team members
- [1] Ungoverned external API calls bypass security
- [2] Blind to external model spending
- [3] Imbalanced load across providers
- [4] External model access unaudited

## 5. Production operations

**5.1 · MLflow Model Registry** (ai)
- [0] model versions untracked over time
- [1] manual stage transitions error-prone
- [2] model origin and ancestors unclear
- [3] model changes and decisions undocumented
- [4] promotion workflows manual and slow

**5.1 · Model Registry & governance** (ds)
- [0] No cross-workspace visibility means models are repeatedly recreated
- [1] Inflexible stage promotion creates deployment bottlenecks
- [2] Lost lineage between models and training data complicates debugging
- [3] Scattered permissions across teams creates security gaps
- [4] Teams duplicate model efforts due to lack of discoverability
- [5] No audit trail for regulatory compliance and debugging

**5.2 · Model Serving & batch inference** (ds)
- [0] Models scattered across multiple serving platforms creates operational chaos
- [1] Manual endpoint scaling and management is time-consuming and reactive
- [2] No central visibility or control over deployed models
- [3] Low query throughput limits production workload capacity
- [4] High overhead latency degrades end-user experience
- [5] Over-provisioned infrastructure drives unnecessary costs

**5.3 · Monitoring & evaluation** (ds)
- no pains in the tree

**5.4 · MLOps & CI/CD** (ds)
- no pains in the tree
## 6. Building agents

**6.1 · AI Functions** (ai)
- [0] external AI services require data export
- [1] model output is unstructured for downstream use
- [2] manual batch splitting and parallelization
- [3] data leaves workspace for inference
- [4] build separate OCR, NLP, JSON pipelines

**6.2 · AI Search (ex-Vector Search)** (ai)
- [0] manual embedding and index management
- [1] single-mode search (vector only)
- [2] vector indices slow to maintain at scale
- [3] embeddings uncontrolled and opaque
- [4] search latency grows with scale

**6.2 · Knowledge Assistant** (ai)
- [0] traditional RAG hallucinations misground
- [1] generic retrieval misses document intent
- [2] sources missing or false
- [3] complex RAG engineering required
- [4] no way to refine retriever behavior

**6.3 · Managed MCP servers** (ai)
- [0] Custom connectors per tool
- [1] Credential sprawl across agents
- [2] Agent access uncontrolled
- [3] Building server infrastructure
- [4] Agents infer context
- [5] Tool usage hidden

**6.3 · External connectors** (ai)
- no pains in the tree

**6.3 · MCP Services + custom MCP** (ai)
- [0] No native integrations available
- [1] Where to host MCP server
- [2] Ungoverned tool exposure
- [3] Build from scratch each time
- [4] REST APIs not toolified

**6.4 · Custom Agents** (ai)
- [0] fixed orchestration patterns
- [1] predetermined framework choice
- [2] limited integrations to external systems
- [3] manual session and memory management
- [4] external deployment and monitoring tools
- [5] fixed model selection

**6.4 · Managed memory & sessions** (ai)
- [0] no memory across separate conversations
- [1] users repeat instructions in each session
- [2] agents start fresh each conversation
- [3] siloed memory per agent
- [4] limited conversation context window

**6.4 · Databricks Sandbox** (ai)
- [0] untrusted AI-generated code poses risk
- [1] code has unrestricted access to data
- [2] manual cluster setup required
- [3] cluster startup time blocks execution
- [4] open inbound connections to sandbox

**6.5 · Supervisor Agent** (ai)
- [0] manual routing between agents
- [1] single agent insufficient for complex tasks
- [2] fragmented tool ecosystems
- [3] disconnected responses from subagents
- [4] bypass user data access controls

## 7. Evaluating agents

**7.1 · MLflow 3 for GenAI** (ai)
- [0] agentic chains opaque to operators
- [1] LLM quality hard to measure consistently
- [2] blind production agents and models
- [3] LLM spend opaque per request
- [4] failures hard to isolate in chains

**7.2 · Agent evaluation & monitoring** (ai)
- [0] no metrics on response quality
- [1] manual review of traces
- [2] blind to production agent quality
- [3] slow iteration without clear signals
- [4] can't compare agent versions

**7.2 · MLflow Prompt Registry** (ai)
- [0] prompt changes untracked over time
- [1] staging/prod prompts diverge
- [2] prompts scattered across notebooks
- [3] prompt access uncontrolled
- [4] model outputs hard to replicate

**7.3 · Review Apps** (ai)
- [0] Agent quality subjective without ground truth
- [1] Manual spreadsheet labeling disconnected from traces
- [2] Testing without feedback loop or expert input
- [3] LLM judges misaligned with expert expectations
- [4] Eval criteria drift across labeling sessions

## 8. Governance

**8.1 · Unity Catalog for AI assets** (ai)
- [0] AI models, agents, functions ungoverned individually
- [1] Inconsistent permission enforcement across assets
- [2] Unknown dependencies between models and data
- [3] Unaudited access to production AI assets
- [4] External credentials scattered and unmanaged

**8.2 · Unity Gateway** (ai)
- [0] self-managed per provider
- [1] no central view of who calls what
- [2] spend grows unchecked
- [3] no guardrails on prompts and responses
- [4] no audit for compliance

**8.3 · DASF v3.0** (ai)
- no pains in the tree

## 9. AI for business users

**9.1 · Genie One** (ai)
- [0] Business users blocked by technical Databricks interface
- [1] Analyst dependency for every data question
- [2] Hard to find relevant dashboards, agents, or data assets
- [3] Generic AI answers lack grounding in authoritative data
- [4] Insights remain disconnected from business workflows and apps
- [5] Cross-workspace data access requires manual control

**9.2 · Genie Ontology** (ai)
- [0] Metrics defined differently across dashboards, queries, and teams
- [1] Genie may choose obsolete or draft definitions over trusted sources
- [2] Business definitions fragmented across dashboards, SQL, docs, chat, tickets
- [3] AI answers lack grounding in authoritative business definitions
- [4] Only critical metrics are formally defined; long tail of context is scattered
- [5] Ontology snippets may leak access to data users cannot see

**9.3 · Genie Agents** (ai)
- [0] Dashboards answer only predefined questions
- [1] Metrics defined inconsistently across teams and dashboards
- [2] Complex "why" and "what-if" analysis fragmented across tools
- [3] Business knowledge trapped with subject-matter experts
- [4] Analytics isolated from business applications and workflows
- [5] AI answers raise data access and compliance concerns

**9.4 · AI/BI Dashboards (Lakeview)** (ai)
- [0] Dashboard authoring slow with manual SQL and visualization configuration
- [1] High SQL barrier for dashboard creation
- [2] Authors struggle to choose the right chart type and configuration
- [3] Joining tables and creating calculated metrics is error-prone and slow
- [4] Troubleshooting and refining dashboards requires specialist skills
- [5] Self-service BI blocked by specialist dependency

**9.4 · Row Zero / Genie ZeroOps** (ai)
- [0] Analysis disconnected from governed data source
- [1] Manual scenario modeling and calculations in spreadsheets
- [2] Manual fix validation and approval for operational changes
- [3] Spreadsheet analysis ungoverned and unaudited
- [4] Slow manual spreadsheet-based analytics workflows

**9.5 · Genie App Builder** (ai)
- [0] App development slow with traditional coding workflows
- [1] App building requires software engineering or Streamlit/React expertise
- [2] Rapid agentic app-building risks uncontrolled deployment and resource use
- [3] App modifications require developer involvement and redeployment cycles
- [4] Apps built outside native Databricks platform lack seamless data access

**9.6 · Databricks Apps + App Spaces** (ai)
- [0] Apps require separate infrastructure outside Databricks platform
- [1] App-level access control and audit trails difficult to implement
- [2] Apps require separate identity management and secrets handling
- [3] Apps isolated from governed data lake
- [4] Locked into single framework or complex multi-stack management
- [5] Apps difficult to move across workspaces and environments

## 10. Developer tools

**10.1 · Genie Code** (ai)
- [0] Writing SQL and pipelines slow and repetitive
- [1] Developers must context-switch between notebook, SQL, pipeline, dashboard tools
- [2] Boilerplate code writing blocks rapid iteration
- [3] Non-expert developers struggle with SQL and pipeline optimization
- [4] No clear pricing or budget controls for coding assistance
- [5] Coding assistant not accessible from command line or CI/CD workflows

**10.2 · AI Dev Kit + internal coding agents (Isaac)** (ai)
- [0] MCPs used by agents create vendor lock-in and uncontrolled integrations
- [1] Developers must manually scaffold agents and MCP configurations
- [2] Agent spending grows uncontrolled without visibility or budgeting
- [3] Building production-grade agents time-consuming and error-prone
- [4] Agent-MCP integrations lack audit and compliance tracking

**10.2 · Omnigent** (ai)
- [0] each agent harness isolated ecosystem
- [1] rewrite code to change agents
- [2] manual copying of content between tools
- [3] no centralized control mechanism
- [4] agents operate in isolation

## 11. Domain applications

**11.1 · CustomerLake** (ai)
- [0] Customer data fragmented across systems
- [1] Duplicate customer records create fragmentation
- [2] Manual audience segmentation and activation
- [3] Customer data ungoverned with no lineage
- [4] Batch profile lookups delay personalization

**11.2 · Lakewatch** (ai)
- [0] Security telemetry siloed in separate SIEM vendors
- [1] Manual threat hunting and incident triage
- [2] Logs deleted for cost; limited retention capacity
- [3] Detections scattered across tools; hard to version and test
- [4] Slow log searches across large datasets
- [5] Heterogeneous log formats from diverse sources

