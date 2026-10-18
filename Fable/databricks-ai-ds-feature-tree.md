# AI and Data Science on Databricks: feature tree

```
AI and Data Science on Databricks
├── Overview: Databricks platform architecture
├── 1. Data storage and movement
│   ├── 1.1 Table formats
│   │   ├── Delta Lake
│   │   ├── Apache Iceberg
│   │   └── Multi-table transactions
│   ├── 1.2 Ingestion and pipelines
│   │   ├── Lakeflow Connect (ingestion connectors)
│   │   │   ├── Managed connectors
│   │   │   ├── Query-based connectors
│   │   │   ├── Community connectors
│   │   │   └── Auto Loader (file ingestion)
│   │   ├── Zerobus Ingest (event ingestion)
│   │   ├── Spark Declarative Pipelines (pipeline framework)
│   │   │   ├── Lakeflow Pipelines Editor (authoring UI)
│   │   │   └── Real-time mode
│   │   ├── Lakeflow Designer (visual pipeline builder)
│   │   └── Lakeflow Jobs (orchestration)
│   ├── 1.3 Transactional and real-time data: LTAP architecture
│   │   ├── Lakebase (transactional database)
│   │   │   ├── Synced tables (lakehouse to Lakebase)
│   │   │   └── Lakehouse Sync (Lakebase to lakehouse)
│   │   └── Lakehouse//RT (real-time analytics)
│   └── 1.4 Table maintenance
│       └── Predictive Optimization
├── 2. Unity Catalog
│   ├── 2.1 Catalog and access
│   │   ├── Catalog
│   │   ├── Discover (asset discovery)
│   │   ├── Lineage
│   │   │   └── External lineage
│   │   ├── Role-based access control
│   │   ├── Attribute-based access control
│   │   ├── Access requests
│   │   ├── External engine access
│   │   │   ├── Catalog commits
│   │   │   └── Unity REST API
│   │   └── Secrets
│   ├── 2.2 Policy and classification
│   │   ├── Data classification
│   │   ├── Governed tags
│   │   ├── Tag propagation
│   │   └── Governance Hub (governance dashboard)
│   ├── 2.3 Observability
│   │   ├── Data Quality Monitoring
│   │   ├── Anomaly detection
│   │   └── Health indicators
│   ├── 2.4 Cost and usage
│   │   ├── System tables
│   │   ├── Usage dashboard
│   │   └── Budgets
│   ├── 2.5 Semantic definitions
│   │   ├── Metrics (metric views)
│   │   ├── Domains (business domains)
│   │   └── Pages (business concept pages)
│   └── 2.6 Data sharing
│       ├── OpenSharing (sharing protocol)
│       │   └── SecureConnect (sharing behind a firewall)
│       ├── Clean Rooms
│       └── Marketplace
├── 3. Data science and machine learning
│   ├── 3.1 Workspace
│   │   ├── Notebooks
│   │   └── Genie Code (coding assistant)
│   │       ├── Notebook assistant
│   │       ├── Full-page Genie Code
│   │       ├── Genie Code CLI
│   │       ├── Scheduled tasks
│   │       └── Lakeflow Jobs task
│   ├── 3.2 Feature engineering in Unity Catalog
│   │   ├── Feature tables
│   │   ├── Feature Views
│   │   ├── Stream Feature Views
│   │   ├── Online Feature Stores (to verify: GA status)
│   │   └── Feature serving
│   ├── 3.3 Training compute
│   │   ├── Databricks Runtime for Machine Learning (classic compute)
│   │   └── AI Runtime (serverless GPU compute)
│   │       ├── Distributed training
│   │       ├── AI Runtime SDK
│   │       └── AI Runtime CLI
│   ├── 3.4 MLflow 3 (ML lifecycle management)
│   │   ├── Experiment tracking
│   │   └── Models in Unity Catalog (model registry)
│   ├── 3.5 Model Serving (ML models)
│   └── 3.6 Deployment automation
│       ├── Declarative Automation Bundles
│       └── Databricks CLI
├── 4. Agent development: Agent Bricks
│   ├── 4.1 Agent Bricks (scope)
│   ├── 4.2 Model access
│   │   ├── Foundation Model APIs (hosted models)
│   │   ├── External model providers
│   │   └── Unity Gateway (model access layer)
│   ├── 4.3 Custom LLMs
│   │   ├── Fine-tuning (on AI Runtime)
│   │   └── Custom LLM serving (on Model Serving)
│   ├── 4.4 Batch inference: AI Functions
│   │   ├── ai_query (general inference)
│   │   ├── ai_classify (classification)
│   │   │   └── Classification UI
│   │   ├── ai_extract (information extraction)
│   │   │   └── Information Extraction UI
│   │   ├── ai_parse_document (document parsing)
│   │   ├── ai_transcribe (audio transcription)
│   │   └── AI Functions REST API
│   ├── 4.5 Knowledge retrieval
│   │   ├── ai_prep_search (chunking and preparation)
│   │   ├── AI Search (vector, hybrid and full-text search)
│   │   ├── ai_search (search SQL function)
│   │   └── Genie Agents as a context source (see AI for business users)
│   ├── 4.6 Tools
│   │   ├── Managed MCP servers
│   │   ├── Managed MCP connectors
│   │   ├── External MCP servers
│   │   ├── Unity Catalog functions
│   │   ├── Skills
│   │   └── Databricks Sandbox (code execution tool)
│   ├── 4.7 Agent build
│   │   ├── Custom agents (code-first agents, any framework)
│   │   ├── AI Bridge (framework integration packages)
│   │   │   ├── databricks-openai
│   │   │   ├── databricks-langchain
│   │   │   └── databricks-dspy
│   │   ├── ResponsesAgent (MLflow agent interface, to verify: current or legacy)
│   │   ├── Agent Bricks CLI
│   │   │   └── Agent app templates
│   │   └── Omnigent as meta-harness (see Developer tools)
│   ├── 4.8 Agent deployment
│   │   ├── Agent Server
│   │   ├── AgentKit (durable execution)
│   │   ├── Agent Runtime (on Databricks Apps)
│   │   └── Agent query interfaces
│   │       ├── Invocation API
│   │       ├── Responses API
│   │       └── SQL
│   ├── 4.9 Agent memory
│   │   ├── Managed memory
│   │   ├── Sessions
│   │   └── Memory pipelines
│   └── 4.10 No-code agents: Genie Agents (see AI for business users)
├── 5. GenAI observability and evaluation: MLflow
│   ├── 5.1 MLflow Tracing
│   │   └── Traces in Unity Catalog
│   ├── 5.2 Evaluation
│   │   ├── LLM judges
│   │   ├── OpenJev (judge model)
│   │   ├── Scorers
│   │   └── Review App (human labeling)
│   ├── 5.3 Prompt Registry (prompt management)
│   └── 5.4 Runtime telemetry
│       ├── Model Serving telemetry
│       ├── Databricks Apps telemetry
│       ├── Inference tables
│       └── System tables
├── 6. AI governance and security
│   ├── 6.1 Unity Catalog for AI assets
│   │   ├── Models
│   │   ├── Functions
│   │   ├── Model provider services
│   │   ├── Memory stores
│   │   ├── Skills
│   │   ├── Traces
│   │   ├── Foundation model permissions
│   │   ├── AI Functions permissions
│   │   └── ABAC GRANT policies for models and services
│   ├── 6.2 Unity Gateway: policies
│   │   ├── Service policies
│   │   ├── LLM-as-a-judge policies
│   │   ├── Sensitive data redaction
│   │   ├── Partner guardrails
│   │   └── Request tags (attribution)
│   ├── 6.3 Unity Gateway: monitoring
│   │   ├── Inference tables (request and response logging)
│   │   ├── Usage tracking
│   │   ├── Usage dashboard
│   │   └── Unified trace table
│   ├── 6.4 Unity Gateway: cost and capacity
│   │   ├── Budgets
│   │   ├── Cost caps
│   │   ├── Rate limits
│   │   ├── Smart routing
│   │   └── Provisioned throughput
│   ├── 6.5 Unity Gateway: coding agent governance
│   │   ├── ug CLI (coding agent connection)
│   │   └── Centralized coding agent configuration
│   └── 6.6 Security and compliance
│       ├── Databricks AI Security Framework
│       ├── Databricks Geos (data residency)
│       └── Compliance security profile
├── 7. AI for business users: Genie
│   ├── 7.1 Genie product family
│   ├── 7.2 Genie One (conversational assistant)
│   │   ├── Web app
│   │   ├── Desktop app (macOS)
│   │   ├── iOS app
│   │   ├── Android app
│   │   ├── Genie One MCP server
│   │   ├── Web search
│   │   └── Account-only user access
│   ├── 7.3 Genie Agents (no-code agents)
│   ├── 7.4 Genie Ontology (business context layer, not verified: no docs page)
│   ├── 7.5 Genie integrations
│   │   ├── Microsoft Teams
│   │   ├── Slack
│   │   ├── Excel
│   │   ├── Google Sheets
│   │   └── Microsoft Copilot Cowork
│   ├── 7.6 AI/BI Dashboards
│   ├── 7.7 Applications
│   │   ├── Databricks Apps (application hosting)
│   │   │   ├── Databricks AppKit (app framework)
│   │   │   └── App Spaces
│   │   └── Genie App Builder (no-code app builder)
│   ├── 7.8 Genie ZeroOps (autonomous pipeline operations, not verified)
│   └── 7.9 Genie budgets (per-user limits)
├── 8. Developer tools
│   ├── 8.1 Omnigent (coding agent harness)
│   ├── 8.2 Agentic code converter (SQL migration)
│   └── 8.3 AI Dev Kit (community toolkit for external coding agents)
├── 9. Vertical applications
│   ├── 9.1 CustomerLake (customer data platform)
│   └── 9.2 Lakewatch (security lakehouse)
└── Appendix: capability map by section
```
