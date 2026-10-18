# Content report — "AI in Production with Databricks" plan v1

Scope: factual review of the plan's nodes against Databricks release notes (Jan–Oct 2026), product documentation and DAIS 2026 recaps. Checked as of October 17, 2026. This report covers content only: what is no longer current, what is missing, what overlaps. Structure, format and status handling are not addressed here.

## 1. Nodes that are no longer current

- **6.5 Supervisor Agent** — Legacy since Oct 12, 2026 (together with Knowledge Assistant). Databricks' current paths: Agent Bricks CLI for agents in code, Genie Agents for no-code. The related Supervisor API (Beta) reached end of life on Sep 30, 2026.
- **4.3 Model fine-tuning** — Foundation Model Fine-tuning was deprecated and scheduled for removal on Aug 14, 2026. Fine-tuning is now a workload on AI Runtime (serverless GPU); custom LLMs are served through Custom Model Serving for LLMs (Beta, May 2026).
- **4.1 / 5.2 Model Serving** — still current for ML models and custom LLMs. Agent deployment on Model Serving, MLflow AgentServer and LongRunningAgentServer moved to legacy on Oct 5, 2026. Current agent path: DurableAgentServer + Agent Runtime on Databricks Apps.
- **3.2 Feature Store** — legacy workspace name. Current: Feature Engineering in Unity Catalog; Feature Views (batch, streaming, request-time) GA Oct 12, 2026; Online Feature Stores backed by Lakebase.
- **5.1 Model Registry** — the workspace registry is legacy; current is Models in Unity Catalog.
- **5.3 Lakehouse Monitoring** — renamed Data Quality Monitoring; documentation moved under Unity Catalog governance (Mar 2026). Same capability as 2.5.
- **5.4 MLOps & CI/CD** — Databricks Asset Bundles renamed Declarative Automation Bundles (Mar 16, 2026).
- **3.4 Distributed training & AI Runtime** — name is current; the `serverless_gpu` package is deprecated in favour of the Databricks AI Runtime SDK (Oct 13, 2026).
- **3.3 MLflow & AutoML** — MLflow 3 is current; no 2026 release-note activity found for AutoML.
- **2.4 Lakehouse//RT & LTAP** — Lakehouse Real-Time is in Beta (Jun 2026). LTAP was presented at DAIS as a coming architecture ("coming soon"; LTAP Writer Library to be open-sourced), not a shipping product.
- **11.1 CustomerLake / 11.2 Lakewatch** — both Private Preview. CustomerLake announced Jun 16, 2026, no GA date. Lakewatch unveiled at RSA Conference 2026; Panther acquisition announced Jun 2026.
- **10.2 AI Dev Kit** — a `databricks-solutions` GitHub project (MCP server with 75+ tools, skills, builder app for external coding agents), not a supported Databricks product. Omnigent is an open-source coding-agent meta-harness with a Databricks-managed version in Beta (Jun 2026).

## 2. Names confirmed current

Genie One (GA, Jun 2026) · Genie Agents (renamed from Genie Spaces, Jul 2026) · Genie Ontology (announced at DAIS; GA not confirmed) · Genie App Builder · Genie Code (renamed from Databricks Assistant, Mar 2026) · Unity Gateway (GA Aug 2026; "Unity AI Gateway" was the DAIS name) · AI Search (renamed from Vector Search, Jun 2026) · Omnigent · Lakebase · Lakeflow · Predictive Optimization · AI Functions · MLflow Tracing · Review Apps · Prompt Registry · Databricks AI Security Framework · AI/BI Dashboards · Databricks Apps.

## 3. Content gaps

- **Agent Bricks** is absent from the plan. Since Mar 27, 2026 it is the umbrella for all Databricks AI capabilities; since DAIS it is code-first: any harness (LangGraph, CrewAI, Claude Code SDK, …), Agent Bricks CLI (Beta Sep 2026), Databricks Sandbox, plus Classification and Information Extraction UIs (Public Preview Mar 2026).
- **Agent memory and sessions** — managed memory (Beta Jun 2026), memory and sessions (Beta Sep 2026), memory pipelines (Beta Oct 2026), all backed by Lakebase.
- **Unity Gateway scope** — "AI traffic control" (8.2) covers a fraction. Current scope: single governed entry for Databricks-hosted and external models (any provider, incl. bring-your-own Claude enterprise subscription and Amazon Bedrock Mantle), MCP servers and connectors, agents and skills; service policies incl. LLM-as-a-judge with OpenJev, sensitive-data block/redact, external partner guardrails, request tags; FinOps: usage, budgets, provider cost caps and discounts, smart routing, provisioned throughput; governance of external coding agents via the `ug` CLI. API, SDKs, CLI and Terraform GA Sep 2026.
- **Semantic / context layer** — Unity Catalog Metrics (metric views), Domains and Discover page (GA Oct 2026), Pages for business concepts (Beta Aug 2026). Genie Ontology alone does not carry the DAIS "Context" theme.
- **Skills** — Unity Catalog Skills (Beta Aug 2026), Unity Gateway Skills API (Beta Oct 2026), workspace skills for Genie Code.
- **Open formats** — 2.1 names Delta only. Apache Iceberg v3 and managed Iceberg tables are GA (May 2026); external writes to managed Delta tables GA (Oct 2026).
- **Sharing and collaboration** — OpenSharing (renamed from Delta Sharing, Jun 2026), Clean Rooms, third-party apps from Marketplace (Jun 2026). Genie Agents can be shared externally via OpenSharing (Beta).
- **Document intelligence** within 6.1 — ai_parse_document (GA), ai_extract / ai_classify v2 (GA Jun 2026), ai_transcribe (Beta), AI Functions REST API (GA Aug 2026).
- **AI Search additions** — ai_search SQL function (Beta Aug 2026), Lakebase Search (Beta), High QPS (GA Jul 2026).
- **MCP governance** — MCP servers and managed connectors are governed through Unity Gateway (Beta Aug 2026); Genie One MCP server GA (Sep 2026).
- **Tracing additions** — MLflow traces stored in Unity Catalog (GA Jul 2026); unified trace table across all AI activity, including coding agents (Beta Aug–Sep 2026).
- **Unity Catalog governance additions** — ABAC GA (cross-engine GA Oct 2026), RBAC GA (Aug 2026), Governance Hub (Beta Jul 2026), Data Classification GA, governed tags with propagation (Beta Oct 2026), model services as a UC securable (Beta Jun 2026).
- **Genie distribution** — Teams, Slack, Microsoft 365 Copilot, Excel Add-in (GA Sep 2026), Google Sheets, Power Platform connector, Genie One macOS app (Beta), Genie One web search (Beta).
- **Genie ZeroOps** — autonomous pipeline operations with human review, Private Preview.
- **Genie Code additions** — Genie Code CLI (Beta Oct 2026), scheduled tasks (GA Sep 2026), Lakeflow Jobs task, agentic code converter (GA Oct 2026).
- **Lakeflow detail** — Connect (100+ connectors), Spark Declarative Pipelines (real-time mode Public Preview), Lakeflow Designer (GA Jun 2026), Zerobus Ingest (GA).

## 4. Overlaps within v1

- 4.1 and 5.2 describe the same capability (Model Serving).
- 2.5 and 5.3 describe the same capability (data quality monitoring).
- 3.3, 5.1, 7.1 and 7.2 are all MLflow 3 / Unity Catalog.
- 4.2 Foundation models and 4.4 External models are both accessed through Unity Gateway.
- 8.2 Unity Gateway and 6.3 MCP overlap (MCP governance lives in the gateway).

## 5. Availability not confirmed by this review

Genie Ontology GA · Genie App Builder status (likely the "Build governed data and AI apps without code (Beta)" release note, Sep 2026) · App Spaces and Serverless Micro Apps · Databricks Sandbox · Online Feature Stores · AutoML · current DASF version · Catalog Federation.

## 6. Proposed node structure (reference)

```
AI in Production with Databricks
├── Overview — Choice, Context, Control
├── 1. Challenges
│   ├── 1.1 Choice gap
│   ├── 1.2 Context gap
│   └── 1.3 Control gap
├── 2. Agentic data foundation
│   ├── 2.1 Open storage w/ Delta Lake 
│   ├── 2.2 Lakeflow
│   ├── 2.3 Lakebase
│   ├── 2.4 Lakehouse//RT & LTAP
│   ├── 2.5 Predictive Optimization & Data Quality Monitoring
│   └── 2.6 OpenSharing, Clean Rooms & Marketplace
├── 3. Context layer
│   ├── 3.1 Unity Catalog Metrics
│   ├── 3.2 Genie Ontology
│   ├── 3.3 Domains, Discover & Pages
│   └── 3.4 Skills
├── 4. Control layer
│   ├── 4.1 Unity Catalog for AI assets
│   ├── 4.2 Unity Gateway — governed front door
│   ├── 4.3 Unity Gateway — policies & guardrails
│   ├── 4.4 Unity Gateway — AI FinOps
│   └── 4.5 Security & compliance
├── 5. Data Science & ML
│   ├── 5.1 Notebooks & Genie Code
│   ├── 5.2 Feature Engineering in Unity Catalog
│   ├── 5.3 MLflow 3 & Models in Unity Catalog
│   ├── 5.4 AI Runtime
│   ├── 5.5 Model Serving
│   └── 5.6 Declarative Automation Bundles & CI/CD
├── 6. Agent Bricks
│   ├── 6.1 AI Functions & document intelligence
│   ├── 6.2 AI Search
│   ├── 6.3 Tools via MCP
│   ├── 6.4 Code-first agents
│   ├── 6.5 Agent memory & sessions
│   └── 6.6 No-code agents with Genie Agents
├── 7. Evaluate & observe
│   ├── 7.1 MLflow Tracing
│   ├── 7.2 Agent evaluation & Prompt Registry
│   └── 7.3 Runtime telemetry
├── 8. AI for business users
│   ├── 8.1 Genie One
│   ├── 8.2 Genie Agents
│   ├── 8.3 Genie everywhere (Teams, Slack, Excel, Sheets)
│   ├── 8.4 AI/BI Dashboards
│   ├── 8.5 Databricks Apps & Genie App Builder
│   └── 8.6 Genie ZeroOps
├── 9. Developer experience
│   ├── 9.1 Genie Code & Genie Code CLI
│   ├── 9.2 Omnigent
│   └── 9.3 Bring your own coding agent
├── 10. Where this leads
│   ├── 10.1 CustomerLake
│   └── 10.2 Lakewatch
└── Closing
```

## 7. Sources used

Release notes
- Index (all 2026 months): https://docs.databricks.com/aws/en/release-notes/product
- October 2026: https://docs.databricks.com/aws/en/release-notes/product/2026/october
- March 2026: https://docs.databricks.com/aws/en/release-notes/product/2026/march
- What's coming (Azure, incl. Supervisor API EOL): https://learn.microsoft.com/en-us/azure/databricks/release-notes/whats-coming

Product documentation
- Agents on Databricks (Agent Bricks): https://docs.databricks.com/aws/en/agents
- Agent Bricks CLI: https://docs.databricks.com/aws/en/agents/custom-agents/agent-bricks-cli
- Agent Runtime / Agent Server: https://docs.databricks.com/aws/en/agents/deploy/agent-runtime · https://docs.databricks.com/aws/en/agents/deploy/agent-server
- Legacy agent offerings: https://docs.databricks.com/aws/en/agents/legacy
- Agent memory pipelines: https://docs.databricks.com/aws/en/agents/agent-memory/memory-pipelines
- Supervisor API (deprecated): https://learn.microsoft.com/en-sg/azure/databricks/agents/custom-agents/supervisor-api-app
- Foundation Model Fine-tuning (deprecated): https://docs.databricks.com/aws/en/large-language-models/foundation-model-training/index.html
- Feature Views: https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-views
- AI Runtime: https://docs.databricks.com/aws/en/machine-learning/ai-runtime
- Unity Gateway model providers: https://docs.databricks.com/aws/en/ai-gateway/model-provider-services
- Unity Gateway Skills API: https://docs.databricks.com/aws/en/ai-gateway/skill-reference
- MCP servers via Unity Gateway: https://docs.databricks.com/aws/en/ai-gateway/register-mcp-service
- Service policies: https://docs.databricks.com/aws/en/data-governance/unity-catalog/service-policies/external-policies
- Data Quality Monitoring: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring
- Metric views / Domains / Discover: https://docs.databricks.com/aws/en/uc-semantics/metric-views · https://docs.databricks.com/aws/en/uc-semantics/domains · https://docs.databricks.com/aws/en/discover/discover-page
- Genie Agents: https://docs.databricks.com/aws/en/genie-agents
- Genie Code / CLI: https://docs.databricks.com/aws/en/genie-code · https://docs.databricks.com/aws/en/genie-code/genie-code-cli
- Omnigent: https://docs.databricks.com/gcp/en/omnigent/
- Declarative Automation Bundles rename: https://docs.databricks.com/aws/en/dev-tools/bundles/faqs#rename
- AI Dev Kit: github.com/databricks-solutions/ai-dev-kit

Newsroom
- Lakewatch: https://www.databricks.com/company/newsroom/press-releases/databricks-enters-security-market-launch-lakewatch-new-agentic-siem
- CustomerLake: https://www.databricks.com/company/newsroom/press-releases/databricks-enters-marketing-industry-customerlake-agentic-customer

DAIS 2026 recaps (secondary)
- https://github.com/amit10may/databricks-ai-summit-2026
- https://bricksnotes.com/databricks-summit-2026
- https://qubika.com/blog/everything-databricks-announced-dais-data-ai-summit-2026/
- https://datapao.com/databricks-data-ai-summit-2026/
- https://atlan.com/know/ai-agent/databricks/databricks-data-ai-summit-2026-announcements/
- https://www.flexera.com/blog/perspectives/databricks-data-ai-summit-2026-recap-genie-one-ltap-lakehouse-rt-and-every-major-launche/
- https://www.constellationr.com/insights/news/databricks-targets-transactional-data-customer-data-use-cases-context-ai-agent
