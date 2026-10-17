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
│   ├── 1.3 Transactional and real-time data
│   │   ├── Lakebase (transactional database): LTAP architecture
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
│   │   │   └── Tag propagation
│   │   └── Governance Hub (governance dashboard)
│   ├── 2.3 Observability
│   │   └── Data Quality Monitoring
│   │       ├── Anomaly detection
│   │       └── Health indicators
│   ├── 2.4 Cost and usage
│   │   └── System tables (billing and usage data)
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
│   │       ├── Genie Code pane (in notebooks)
│   │       ├── Full-page Genie Code
│   │       ├── Genie Code CLI
│   │       ├── Scheduled tasks
│   │       └── Lakeflow Jobs task
│   ├── 3.2 Feature engineering in Unity Catalog
│   │   ├── Feature tables
│   │   ├── Feature Views
│   │   │   └── Stream Feature Views
│   │   ├── Online Feature Stores (to verify: GA status)
│   │   └── Feature serving
│   ├── 3.3 Training compute
│   │   ├── Databricks Runtime for Machine Learning (classic compute)
│   │   └── AI Runtime (serverless GPU compute)
│   │       ├── Distributed training (AI Runtime SDK)
│   │       └── AI Runtime CLI
│   ├── 3.4 MLflow 3 (ML lifecycle management)
│   │   ├── Experiment tracking
│   │   └── Models in Unity Catalog (model registry)
│   ├── 3.5 Model Serving (ML models)
│   │   ├── Custom model endpoints
│   │   ├── Endpoint telemetry
│   │   └── Inference tables
│   └── 3.6 Deployment automation
│       ├── Declarative Automation Bundles
│       └── Databricks CLI
├── 4. Agent development
│   ├── 4.1 Model access
│   │   ├── Foundation Model APIs (hosted models)
│   │   │   ├── Pay-per-token
│   │   │   ├── Priority pay-per-token
│   │   │   ├── Provisioned throughput
│   │   │   └── OpenJev (Databricks judge model)
│   │   ├── External model providers
│   │   └── Unity Gateway (model access layer)
│   ├── 4.2 Custom LLMs
│   │   ├── Fine-tuning (on AI Runtime)
│   │   └── Custom LLM serving (on Model Serving)
│   ├── 4.3 Batch inference: AI Functions
│   │   ├── ai_query (general inference)
│   │   ├── ai_classify (classification)
│   │   │   └── Classification UI
│   │   ├── ai_extract (information extraction)
│   │   │   └── Information Extraction UI
│   │   ├── ai_parse_document (document parsing)
│   │   ├── ai_transcribe (audio transcription)
│   │   └── AI Functions REST API
│   ├── 4.4 Knowledge retrieval
│   │   ├── ai_prep_search (chunking and preparation)
│   │   ├── AI Search (vector, hybrid and full-text search)
│   │   ├── ai_search (search SQL function)
│   │   └── Genie Agents as a context source (see AI for business users)
│   ├── 4.5 Tools
│   │   ├── Managed MCP servers
│   │   ├── Managed MCP connectors
│   │   ├── External MCP servers
│   │   ├── Unity Catalog functions
│   │   ├── Skills
│   │   └── Databricks Sandbox (code execution tool)
│   ├── 4.6 Agent build
│   │   ├── Custom agents (code-first agents, any framework)
│   │   ├── AI Bridge (framework integration packages)
│   │   │   ├── databricks-openai
│   │   │   ├── databricks-langchain
│   │   │   ├── databricks-dspy
│   │   │   └── databricks-mcp
│   │   ├── Agent Bricks CLI
│   │   │   └── CLI project templates
│   │   └── Omnigent as meta-harness (see Developer tools)
│   ├── 4.7 Agent deployment
│   │   ├── AgentKit (durable agent server)
│   │   │   └── databricks-agentbricks (SDK package)
│   │   ├── Agent Runtime (on Databricks Apps)
│   │   └── Agent query interfaces
│   │       ├── Invocation API
│   │       ├── Responses API
│   │       └── SQL
│   ├── 4.8 Agent memory
│   │   ├── Managed memory
│   │   ├── Sessions
│   │   └── Memory pipelines
│   └── 4.9 No-code agents: Genie Agents (see AI for business users)
├── 5. Observability and evaluation
│   ├── 5.1 MLflow Tracing
│   │   └── Traces in Unity Catalog
│   ├── 5.2 MLflow evaluation
│   │   ├── LLM judges
│   │   ├── Scorers
│   │   └── Review App (human labeling)
│   ├── 5.3 Prompt Registry (prompt management)
│   └── 5.4 Runtime telemetry
│       ├── Endpoint telemetry (Model Serving)
│       ├── Databricks Apps telemetry
│       ├── Inference tables
│       └── System tables
├── 6. AI governance and security
│   ├── 6.1 Unity Catalog for AI assets
│   │   ├── Models
│   │   ├── Functions
│   │   ├── Model services (hosted model endpoints)
│   │   ├── Model provider services (external providers)
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
│   │   └── Smart routing
│   ├── 6.5 Unity Gateway: coding agent governance
│   │   ├── ug CLI (coding agent connection)
│   │   └── Centralized coding agent configuration
│   └── 6.6 Security and compliance (Databricks AI Security Framework)
│       ├── Databricks Geos (data residency)
│       └── Compliance security profile
├── 7. AI for business users
│   ├── 7.1 Genie One (conversational assistant)
│   │   ├── Web app
│   │   ├── Desktop app (macOS)
│   │   ├── iOS app
│   │   ├── Android app
│   │   ├── Genie One MCP server
│   │   ├── Web search
│   │   └── Account-only user access
│   ├── 7.2 Genie Agents (no-code agents)
│   ├── 7.3 Genie Ontology (business context layer, not verified: no docs page)
│   ├── 7.4 Genie integrations
│   │   ├── Microsoft Teams
│   │   ├── Slack
│   │   ├── Excel
│   │   ├── Google Sheets
│   │   └── Microsoft Copilot Cowork
│   ├── 7.5 AI/BI Dashboards
│   ├── 7.6 Applications
│   │   ├── Databricks Apps (application hosting)
│   │   │   ├── Databricks AppKit (app framework)
│   │   │   └── App Spaces
│   │   └── Genie App Builder (no-code app builder)
│   ├── 7.7 Genie ZeroOps (autonomous pipeline operations, not verified)
│   └── 7.8 Genie budgets (per-user limits)
├── 8. Developer tools
│   ├── 8.1 Omnigent (coding agent harness)
│   └── 8.2 Agentic code converter (SQL migration)
├── 9. Vertical applications
│   ├── 9.1 CustomerLake (customer data platform)
│   └── 9.2 Lakewatch (agentic SIEM)
└── Appendix: capability map by section
```

## Why the feature tree changed from v1 to v2

1. v1 was built from June 2026 material. Its names match the DAIS 2026 recaps and nothing after. Between July and October 2026 Databricks moved several v1 nodes to legacy or removed them:

Supervisor Agent and Knowledge Assistant are legacy since Oct 12, 2026. The Supervisor API reached end of life on Sep 30, 2026.
Foundation Model Fine-tuning was removed on Aug 14, 2026. Fine-tuning now runs on AI Runtime.
Agents deployed on Model Serving, MLflow AgentServer and LongRunningAgentServer are legacy since Oct 5, 2026. Agents run on Agent Runtime (Databricks Apps) with AgentKit.
“Feature Store”, “Model Registry”, “Lakehouse Monitoring” and “Databricks Asset Bundles” are legacy names. Current names: Feature Engineering in Unity Catalog, Models in Unity Catalog, Data Quality Monitoring, Declarative Automation Bundles.

2. v1 presented announcements as shipping products. LTAP is an architecture delivered through Lakebase capabilities, not a feature. CustomerLake and Lakewatch are in Private Preview. AI Dev Kit is a field GitHub project with no docs page. v2 keeps LTAP as a label, keeps the two vertical products in a section named for what they are, and drops AI Dev Kit.

3. v1 had duplicates and gaps. Model Serving appeared twice (4.1, 5.2). Monitoring appeared twice (2.5, 5.3). Agent Bricks, agent memory, Unity Catalog Metrics and Domains, Skills, OpenSharing, Apache Iceberg and the full scope of Unity Gateway (policies, monitoring, cost, coding-agent governance) were absent. v2 was checked in two passes against the monthly release notes from January to October 2026 by a separate verification session, and the remaining open items are marked in the tree (“to verify”, “not verified”).

4. v1 ordered features by product family. v2 orders them by dependency. A node only uses components introduced in earlier nodes. Unity Catalog has its own section before feature engineering, agents or Genie depend on it. Genie Code appears in the data science worfamily in section 7. Unity Gateway appears in agent development as the model access layer, then in governance for its policy, monitoring and cost functions. The reader never meets a proper noun before the node that defines it.

5. v1 mixed classical ML with generative AI. Custom LLM serving and LLM fine-tuning were under data science. In v2 they are in agent development, because the audience evaluates them as part of the generative stack, even though the underlying products (Model Serving, AI Runtime) are shared. A product used in both parts appears in each, scoped to that use.

6. v1 opened with “Why AI stalls before production”. That statement is no longer true for many customers and it frames the deck as a sales pitch. v2 opens with the platform architecture and goes straight to the features.

7. The node titles follow fixed rules. One feature per leaf. No enumeration inside a title; each item is a child node. Every proper noun carries a common noun saying what it is. Titles are labels naming the subject, not questions or hooks. No nodes about the document itself. A label has children; a childless node is a capability. These rules, numbered 1 to 25, were derived from review feedback during the v1 to v2 work and apply to any later edit of the tree.
