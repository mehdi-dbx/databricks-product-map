# Feature tree: integration of the completeness review, pass 2 (sections 4 to 9)

## Findings retained

- Agent deployment: AgentKit (durable execution) and the query interfaces of deployed agents (invocation API, Responses API, SQL).
- Knowledge retrieval: ai_prep_search. Genie Agents added as a context source for custom agents, with a pointer to the Genie section.
- Tools: Databricks Sandbox moves here. It is a tool the agent calls, not a build layer.
- Agent build: "Agent harnesses" dropped, it is a concept. Agent app templates nest under Agent Bricks CLI. Omnigent referenced as the meta-harness option.
- AI Functions: Classification UI and Information Extraction UI nest under ai_classify and ai_extract.
- Lakebase Search removed. No product of that name exists in docs or release notes. The closest capability is ai_search over Lakebase synced tables, an option.
- Unity Catalog for AI assets: model provider services (replaces "Model services"), memory stores, foundation model permissions, AI Functions permissions, ABAC GRANT policies for models and services.
- Unity Gateway monitoring: usage dashboard added. "Audit of gateway calls" removed, the unified trace table is that capability. Unified trace table confirmed as a Unity Gateway feature, marker removed.
- Unity Gateway cost and capacity: rate limits.
- New sub-section Unity Gateway: coding agent governance, with the ug CLI (moved from Developer tools) and centralized coding agent configuration.
- Genie One surfaces: web, desktop (macOS), mobile (iOS, Android), MCP server, web search, account-only user access.
- Genie integrations: "Microsoft 365 Copilot" renamed "Microsoft Copilot Cowork", the name used in the release note.
- Applications: Databricks AppKit and App Spaces under Databricks Apps.
- Genie budgets added as the cost dimension of section 7.
- Prompt Registry moves from the classical ML section to the GenAI section. Section 5 label now names MLflow.
- Databricks Agents SDK removed. It served the Model Serving deployment path, legacy since Oct 5, 2026. Confirmation pending; the tree does not list legacy.
- ResponsesAgent kept with a "to verify" marker.

## Findings rejected

- Priority pay-per-token: a pricing tier, not a capability (guideline 15).
- Genie pricing details (free DBUs, free usage period): commercial terms, not features. The control itself (Genie budgets) is retained.

## Verification status

- Online Feature Stores: GA still not verified.
- Genie Ontology: announced Jun 16, 2026, no docs page or release note found. Marked not verified.
- Genie ZeroOps: docs page exists, no release note. Marked not verified.
- Lakewatch: announced Mar 24, 2026. A third-party recap says GA, nothing authoritative confirms. Status not verified.
- Genie App Builder: docs page says Beta.

## Guideline changes

18 (amended). Scope. Platform operations with no data or AI content are out of the tree. AI-driven operations products stay in (Genie ZeroOps).
19. A name found only in third-party recaps, absent from docs and release notes, is not a leaf until documented.
20. Pricing tiers and commercial terms are not leaves. Cost controls (budgets, caps, rate limits) are.

## Modified sections

Sections 1 to 3 are unchanged except 3.4, which loses Prompt Registry.

```
├── 3. Data science and machine learning
│   ├── ...
│   ├── 3.4 MLflow 3 (ML lifecycle management)
│   │   ├── Experiment tracking
│   │   └── Models in Unity Catalog (model registry)
│   ├── ...
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
```
