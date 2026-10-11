# Databricks Data Science Ecosystem Cartography
## Sage Context Catalog (FE/GTM Assets) — October 2026

---

## EXECUTIVE SUMMARY

**Pillars Identified:** 11 major pillars
**Assets Catalogued:** 48 curated resources (gold/silver quality dominant)
**Coverage:** Core DS/ML lifecycle + GenAI/Agents + Platform patterns
**Data Source:** Sage Context Catalog (system-managed domains)

This report maps the Databricks Data Science ecosystem across the classic DS/ML lifecycle (data → model → deploy) with extensions into GenAI agents, governance, and industrial IoT data.

---

## PILLAR 1: DATA SCIENCE & ML PLATFORMS (Core DSML)

Foundational messaging and capability overview for DS/ML on Databricks.

| Slug | Type | Quality | Description | Author/Owner | URL |
|------|------|---------|-------------|--------------|-----|
| `dsml-l100200-pitch-deck-godsml` | Presentation | **Gold** | Authoritative L100/200 pitch deck — full DSML platform story, Mosaic AI + MLflow ecosystem, customer-facing. **CANONICAL DECK.** | vlad.marin@databricks.com | [Slide Deck](https://docs.google.com/presentation/d/19FFrwianS8-QR9nJSyZynrVvY6cw07CWqvKpwuCSVOY) |
| `databricks-for-data-science-presentation-deck` | Presentation | Silver | Educational intro deck — Databricks capabilities for data science workflows & analytics. | — | [Deck](https://drive.google.com/file/d/1MS88ZGsHlTKs42lxjzIJ5QXjSgBvtXCQ) |
| `databricks-comprehensive-training-3-days` | Demo/Training | **Gold** | Hands-on 3-day training program: full Data Intelligence Platform story using realistic IoT manufacturing dataset. Data eng → analytics → dashboards → AI/ML → ops. | josh.melton@databricks.com (repo) | [GitHub](https://github.com/josh-melton-db/databricks-crash-course) |

---

## PILLAR 2: AI DATA MODELING & SEMANTICS (For AI-Ready Pipelines)

Modeling foundations for agentic systems and AI consumption. Centred on Joe Reis's *Practical Data Modeling* adapted to the Lakehouse/AI era.

| Slug | Type | Quality | Description | Author/Owner | URL |
|------|------|---------|-------------|--------------|-----|
| `ai-data-modeling-insights-recommendations-distilled` | Documentation | **Gold** | **FLAGSHIP ASSET.** AI-specific distillation: 8 core insights + concrete recommendations (pre-flight checklist, grain rule, agent-centric modeling, semantic governance). Maps to UC, Metric Views, Vector Search, MLflow, Genie. | david.okeeffe@databricks.com | [Doc](https://docs.google.com/document/d/1bWv0nXCfXfFN6svkKz1D_qinauREKnkTcF7cvq__gSY) |
| `data-modeling-sa-synthesis-lakehouse-ai-data-modeling` | Documentation | Silver | SA POV: classic modeling principles on Delta + Unity Catalog; semantic layers; AI-readiness. | — | [Synthesis](https://docs.google.com/document/d/17P4oOfPuUbv8joCmUZ7kLdZjSUWMrgL2bSbQHbphifc) |
| `data-modeling-sa-synthesis-semantics-orgs-agents` | Documentation | Silver | Semantics, org structures, and agentic systems: context/intent/action as semantic foundation; agents as forcing function for governance. | — | [Synthesis](https://docs.google.com/document/d/1FhWy454Vdb4Qq8REOpf0pgpM-DIy7aCPFQdnwopF_t8) |
| `practical-data-modeling-sa-index-reading-map` | Documentation | Silver | **START HERE for Data Modeling domain.** Index + reading map across 24 chapter distillations (entities, attributes, grain, time, aggregation, semantics). | — | [Index](https://docs.google.com/document/d/1J-3C5x5lkb3SdW7FihSQrFIUYbAU7EUPm-qLqmEqlLs) |
| `practical-data-modeling-ch-4-the-five-forms-of-data-sa-distillation` | Documentation | Bronze | The five forms of data: how to model beyond rows and columns. | — | [Chapter](https://docs.google.com/document/d/16xn0G2DxuDjFV1UVfhgINBB5Nypzt1wgEtWfBOo4mcM) |
| `enterprise-genaillm-environment-rules-of-thumb-distilled-inmonknowlesrapien` | Documentation | Silver | Inmon/Knowles/Rapien digest: trustworthy GenAI = trustworthy enterprise meaning. 19 LLM rules + 37 data-modeling rules; maps to UC + Metric Views + Project Ontos. | — | [Digest](https://docs.google.com/document/d/1bpVbfD_s3DCdUHvTVYjEBqDWXQdyjptw5p7Tgh9RbuU) |
| `medallion-vs-data-vault-architecture-category-error-field-note` | Documentation | Silver | Field note: medallion (refinement zoning) ≠ Data Vault (methodology); both can coexist. | — | [Note](https://docs.google.com/document/d/1FXWjesL3WAYsLjlxlZ6ZnIbCqXDmPhnBvAS3_vQXLpk) |
| `coles-enterprise-ontology-rfi-response-revised-v30-snowflake-governed-aibi` | Documentation | **Gold** | LIVE WORKED EXAMPLE: Coles customer RFI response. Semantic layer (UC Metric Views → Ontology → UC Business Semantics) + Genie + Apps. 10–12w PoV. | — | [RFI](https://drive.google.com/file/d/1zFSZ3rrfmF9JkRokPgPSIV6UuBxAdLvb) |

---

## PILLAR 3: ML LIFECYCLE & MLOps (Model Development → Production)

Covers MLflow, model registry, experiment tracking, and end-to-end MLOps pipelines.

| Slug | Type | Quality | Description | Author/Owner | URL |
|------|------|---------|-------------|--------------|-----|
| `mlops-on-databricks-end-to-end-manufacturing-tutorial` | Codebase | Bronze | Hands-on MLOps pipeline: Databricks Asset Bundles + UC + MLflow + Feature Store for manufacturing quality prediction. 3 CI/CD promotion patterns, synthetic data, batch inference. | archana986 (GitHub) | [Tutorial](https://github.com/archana986/ML-Engg-Ops-Notebooks) |
| `mlflow-2-tier-registry-pattern-for-many-models-with-ensemble-selection` | Reference Architecture | Silver | MLflow 2-tier model registry pattern for many-models + ensemble selection at scale. | — | [Repo](https://github.com/databricks-field-eng/mlflow-hierarchical-ensemble-registry-poc) |
| `databricks-workspace-to-workspace-model-migration-bundle` | Codebase | Bronze | Databricks Asset Bundle: migrate MLflow registered models between UC catalogs on same metastore. Preserves versions, metrics, params, tags, aliases, grants. | archana986 | [Repo](https://github.com/archana986/databricks-model-migration) |
| `ml-batch-scoring-into-a-gold-predictions-table-mlflow-uc` | Codebase | Bronze | **Default pattern:** Train (MLflow) → register (@prod alias in UC) → batch score (Spark UDF) → gold_<entity>_predictions (analytics/Genie/agents read). | — | [Pattern](https://github.com/databricks-field-eng/fde-specs/tree/main/techniques/ml-batch-scoring-gold-predictions) |
| `unity-catalog-model-registration-batch-inference-demo` | Demo | Silver | Hugging Face vision models in UC + distributed batch inference without Model Serving. 3 notebooks (register, alias, Spark UDF). | — | [Demo](https://github.com/databricks-field-eng/amer-pubsec-us-maven-demo-uc-model-registration) |
| `mlops-uplift-brief-the-predecessor-whitepaper` | Documentation | Silver | May 2026 MLOps Uplift Brief: MLOps modernisation as entry to AI transformation. YWS hardening, UC model registry, declarative bundles, MLflow lineage, integration boundaries. | — | [Brief](https://drive.google.com/file/d/1F1on4GF9Bpe9NwY8UNKLp45AXpqB1jUS) |

---

## PILLAR 4: GENERATIVE AI AGENTS & AGENTIC DEVELOPMENT

Building, evaluating, and deploying autonomous agents on Databricks using MLflow, Agent Bricks, and Genie.

| Slug | Type | Quality | Description | Author/Owner | URL |
|------|------|---------|-------------|--------------|-----|
| `eval-flywheel-databricks-genai-agent-demo` | Codebase | **Gold** | **CANONICAL AGENT DEMO.** End-to-end: build → evaluate → iterate → deploy customer support triage agent. MLflow tracing, deterministic + LLM judges, eval experiments, Genie Code loop. | dhaval.bagadia@databricks.com | [Repo](https://github.com/dhavalbagadia05/Agent_Evaluation_Databricks) |
| `building-agents-on-databricks-workshop-ws-001` | Presentation + Lab | Silver | 2h workshop: agent build→eval→iterate→deploy loop on Databricks. Managed vs. custom decision framework, Agent Cheat Sheet, hands-on lab (custom MLflow agent, traces, judges, eval dataset, Review App). | emerson.bayuk@databricks.com (FE, FSI PS) | [Lab](https://drive.google.com/drive/folders/1sRBguLY6g7eR3ILIB3ENmSeb-reGzJEw) |
| `agent-ontology-demo` | Demo | **Gold** | Comparative demo: LLM agents answering NOC questions over synthetic telco data with vs. without ontology. Shows how semantic layers improve correctness from 0% → ~78% on domain traps. | — | [Repo](https://github.com/databricks-field-eng/agent-ontology-demo) |
| `enterprise-mro-hub-demo` | Demo | Silver | Full-stack Databricks App for enterprise operations (MFG/E&U): backed by Lakebase (serverless Postgres), one-command deployment. | — | [Drive](https://drive.google.com/file/d/1WrBPbqsyQX0aYafDZUyfI0u926xAUBlK) |
| `support-assistant` | AI Agent Tool | Silver | Diagnostic agent: searches Slack, JIRA, Confluence, internal docs for Lakeflow/CDC issues using Claude API + MCP. Root cause analysis + prioritized tickets. | — | [Confluence](https://databricks.atlassian.net/wiki/spaces/UN/pages/5713429843) |
| `know-before-you-go-hackathon-communication` | Documentation | Silver | Hackathon prep guide: team-based agent/code-first paths, business impact judging, office hours support. | — | [Doc](https://docs.google.com/document/d/14o_bYThLmcCmSilSwhVYje3xv9t-yEiJhiBPTsJcPlM) |
| `hackathon-in-a-box` | Documentation | Silver | Comprehensive GenAI hackathon org guide: technical prerequisites, dev paths, judging criteria, environment setup. | — | [Folder](https://drive.google.com/drive/folders/1q4znsLVfwT1dFBMZXFKYUxRrD7MaSeWO) |

---

## PILLAR 5: AI GOVERNANCE & SECURITY

Identity, access control, observability, and data governance for AI applications.

| Slug | Type | Quality | Description | Author/Owner | URL |
|------|------|---------|-------------|--------------|-----|
| `applied-ai-governance-production-patterns-reference-architecture` | Reference Architecture | **Gold** | **CANONICAL GOVERNANCE ARCHITECTURE.** Production patterns: IAM, OAuth federation, MCP security, tool governance, observability. 7 pillars, decision frameworks, 60+ pages of implementation. | bhavin.kukadia@databricks.com | [Repo](https://github.com/bhavink/applied-ai-governance) |
| `data-ai-governance-full-deck` | Presentation | **Gold** | L400 internal training: governance frameworks, IAM, compliance, observability for AI systems on Databricks. | — | [Deck](https://docs.google.com/presentation/d/1kIwyrbFrNQYtQzdAMxW1L7NAJ5eZxJ4wGf5y2J4kj0Y) |
| `data-ai-governance-customer-facing-deck` | Presentation | **Gold** | Customer-facing: governance patterns, best practices, implementation strategies for AI. | — | [Deck](https://docs.google.com/presentation/d/1eZMuxmlDuOfymXFzPVJnRKQF61haD1uY5kOeu1KcmYg) |
| `ai-governance-on-databricks-overview-l100-pitch-deck` | Presentation | **Gold** | Executive overview: AI governance capabilities, best practices, frameworks, compliance patterns. | — | [Deck](https://docs.google.com/presentation/d/1VMsZhARsSBJBJW8dU3h9x5Ye7qTAJTzEcID272fJnlQ) |
| `databricks-ai-governance-framework-dais-presentation` | Presentation | Silver | DAIS conference presentation: governance framework, IAM, compliance, observability. | — | [Deck](https://docs.google.com/presentation/d/1sd2ZYB4N8x9Xx3F988RWa47vHH1gT8uG1yhc_Jr--8A) |
| `uaig-coding-agents-governance-playbook` | Documentation | Bronze | Draft governance playbook for Databricks Coding Agents: policy frameworks, compliance, operational guidance. | — | [Doc](https://docs.google.com/document/d/1AMsZY-TQ-gxAkToe_EzF34TulN4qZeYUyJf8BNbIe4c) |

---

## PILLAR 6: VECTOR SEARCH & RETRIEVAL-AUGMENTED GENERATION (RAG)

Semantic search, embeddings, and RAG systems for LLM-driven applications.

| Slug | Type | Quality | Description | Author/Owner | URL |
|------|------|---------|-------------|--------------|-----|
| `brand-image-creation-app` | App | Silver | RAG-powered brand asset library: semantic search + multi-image AI editing + text-to-image + feedback loop on Databricks with Vector Search. | — | [Live App](https://brand-image-app-7474656585748611.aws.databricksapps.com) |
| `multi-modal-semantic-search` | Demo | Bronze | Semantic search across video repository using ai_parse_document, Agent Bricks, CLIP embeddings, Vector Search + reranking. | — | [Demo](https://e2-demo-field-eng.cloud.databricks.com/browse/folders/1367581502351076) |
| `databricks-vector-search-security-overview` | Presentation | **Gold** | Comprehensive Vector Search security presentation: architecture, considerations, field enablement. | — | [Deck](https://docs.google.com/presentation/d/1h48GJEXrUQpcsOwmPDLznvaJBDPhiQC0fh4ZrpoBdkI) |
| `vector-search-security-faq` | Documentation | Silver | FAQ: security architecture, data protection, compliance for Vector Search deployments. | — | [FAQ](https://docs.google.com/document/d/1xJoOSKpvF1P3ReFTbck4cM4dZp4ogzvq9-n8EKGdkcw) |
| `net-one-systems-knowledge-base-rag-engagement-report` | Documentation | Silver | Engagement report: Net One Systems knowledge-base RAG pilot & expansion. Lessons learned. | — | [Report](https://docs.google.com/document/d/1d_7W-cWc1GEDT5Nn5tkNESptU4O6gXxj) |
| `queensland-treasury-document-processing-engine-for-rag` | Documentation | Silver | Engagement report: Queensland Treasury document processing for RAG. FDE implementation. | — | [Report](https://docs.google.com/document/d/1rXlTJnKqxUT-fj6IGDl0hbr5mWlrJ4Qi9MkkWad1DhM) |

---

## PILLAR 7: KNOWLEDGE GRAPHS & SEMANTIC LAYERS

Ontologies, graph structures, and semantic reasoning for agents.

| Slug | Type | Quality | Description | Author/Owner | URL |
|------|------|---------|-------------|--------------|-----|
| `knowledge-graph-design-patterns-on-databricks-lakebase-pgvector` | Documentation | Bronze | **FIELD-VALIDATED.** 3 reusable patterns: rank facts by confidence/freshness, keep graphs in sync with live systems, govern agent reads/writes. Production KG (14.4K entities, 41K relationships, 9 months daily use). | — | [Doc](https://docs.google.com/document/d/11CZU4jKeELTgMd2ME__7xDDT-a4bVUd92MI0p24Bk80) |
| `ontop-virtual-knowledge-graph-on-databricks-apps` | Codebase | **Gold** | Virtual KG using Ontop on Databricks Apps: SPARQL endpoints over Databricks SQL with UC permission enforcement. MCP endpoints for agent validation. | — | [Repo](https://github.com/aktungmak/ontop-databricks-apps) |
| `fe-graph-viz-reusable-graph-visualization-template` | Codebase | Silver | Force-directed graph viz template for Databricks Apps (react-force-graph-2d). Global/local/shortest-path views; data-source agnostic (Kùzu, LadybugDB, Neo4j). | — | [Repo](https://github.com/databricks-field-eng/field-graph-viz) |

---

## PILLAR 8: GENIE & AI/BI ANALYTICS

Databricks Genie: AI assistant for self-service analytics and dashboarding.

| Slug | Type | Quality | Description | Author/Owner | URL |
|------|------|---------|-------------|--------------|-----|
| `genie-best-practices-kit` | Reference Architecture | **Gold** | Enterprise-grade Genie implementation blueprint: structured data curation, metadata, accuracy principles. ZIP with setup guides + Jupyter notebooks. | — | [Kit](https://drive.google.com/file/d/1_N0WPJVobCTWF3YwsDHqN5A_DwUifHLl) |
| `cost-efficient-usage-of-genie-genie-code` | Presentation | Silver | Genie/Genie Code cost optimization under PayGo pricing (150 DBU/user/month free). Token economics, prompting principles, context windows, Space optimization, Genie Code tips. 1-page cheat sheet. | — | [Deck](https://docs.google.com/presentation/d/1lmzLicDn8xBQfvUkeHOy-e_c2nyyfLivLpr3088QcA8) |
| `databricks-genie-manufacturing-analytics-workshop` | Demo | Bronze | Hands-on workshop: build Genie AI assistant for manufacturing analytics (OEE, quality, downtime, safety). Benchmarking, security, deployment, monitoring. | archana986 | [Repo](https://github.com/archana986/manufacturing-genie-workshop) |

---

## PILLAR 9: DATA ENGINEERING & INGESTION PIPELINES

Feature engineering, ETL, data quality, and ingestion patterns.

| Slug | Type | Quality | Description | Author/Owner | URL |
|------|------|---------|-------------|--------------|-----|
| `dedup-ops-medallion-duplicate-detection` | Codebase | **Gold** | Spark Declarative Pipeline: detects duplicate/near-duplicate tables across medallion layers using UC metadata + lineage. Weighted scoring + Lakeview dashboard. | hurcy (GitHub) | [Repo](https://github.com/hurcy/duplicate-detection) |
| `config-resolver-step-pattern-for-reproducible-dag-config-2` | Documentation | Silver | Lakeflow pattern: resolve DAG config once per run so all tasks see same values (today's date, latest version, etc.) regardless of execution time. | — | [Pattern](https://github.com/databricks-field-eng/lakeflow-config-resolver/tree/main) |
| `ignition-zerobus-connector-for-databricks` | Codebase | **Gold** | Production Ignition module: streams OT/IIoT tag-change events to Delta via Zerobus (gRPC + protobuf). Supports Ignition 8.1.x–8.3.x, low-latency from OPC UA/MQTT/PLC. | — | [Repo](https://github.com/databricks-industry-solutions/lakeflow-zerobus-ignition-connector) |
| `zerobus-streaming-query-listener` | Codebase | Silver | Spark Structured Streaming metrics via StreamingQueryListener → Delta/UC via Zerobus. Schema + config + IoT example with DAB. | sjrusso8 | [Repo](https://github.com/sjrusso8/zerobus-streaming-listener) |
| `scaling-cool-cucumbers-dsa-solution-accelerators-repository` | Codebase | **Gold** | **FIELD REPOSITORY.** Databricks Asset Bundles for cost analysis, performance benchmarking, resource management, monitoring. Proven patterns. | — | [Repo](https://github.com/databricks-field-eng/scaling-cool-cucumbers) |

---

## PILLAR 10: INDUSTRIAL IoT & OPERATIONAL DATA (OT/IIoT)

Streaming OT data, historians, Purdue model, asset-health patterns for manufacturing & energy.

| Slug | Type | Quality | Description | Author/Owner | URL |
|------|------|---------|-------------|--------------|-----|
| `industrial-ai-reference-architecture-diagram` | Documentation | **Gold** | **CANONICAL DIAGRAM.** Edge/control loop → Ignition → Zerobus → Delta → UC → analytics/AI (above control loop). | — | [Diagram](https://drive.google.com/file/d/1VaxeXHjdQDsDMHcUk4PjZKFQ4AnINSrI) |
| `dbra-industrial-ot-research-synthesis` | Documentation | Silver | DBRA synthesis: PLC/SCADA, historian/PI, Ignition/UDT, Unified Namespace, MQTT/Sparkplug, Zerobus→Delta→UC patterns. | — | [Synthesis](https://docs.google.com/document/d/1hBy7FXb1iPNpq3B5fXrzkUKJCw-lt7dWZfCY5idESBs) |
| `accenture-edge-position-deck-industrial-ot-data-modernisation` | Documentation | Silver | Accenture partnership: industrial OT data modernisation positioning. Purdue model, historian modernisation, asset-health loop. | — | [Deck](https://drive.google.com/file/d/1uKu39KqWlHWb-w2Vr4RycV_IH7ItMHRJ) |
| `accenture-industrial-historian-modernisation-gold-distillation` | Documentation | Silver | Distillation: modernising plant historians (PI, etc.) onto Delta/UC. PII/historian framing, asset-health use case. | — | [Distillation](https://docs.google.com/document/d/19dcvgvRCKqZhxJ9iC3k3Dm4eL9dj5XcsB70PMljujzY) |
| `asset-health-decision-loop-diagram` | Documentation | Silver | Diagram: streamed OT data → condition monitoring → anomaly detection → maintenance decisions on Databricks. | — | [Diagram](https://drive.google.com/file/d/1IvS_tt3QSgoeTV1c61NCEmJv7ilWQ3_o) |
| `how-to-stream-industrial-data-from-ignition-to-delta-lake-with-zerobus-ingest-blog` | Documentation | **Gold** | Technical blog post (in review): stream Ignition Gateway data → Delta/UC via Zerobus. Ignition config, Sparkplug vs. Zerobus distinctions, SDT compression. | — | [Blog](https://docs.google.com/document/d/1d35Zp1NS-AwUPHsBIB_036NfT8CUjP_xO4dBrlfOLB0) |
| `ignition-zerobus-industrial-ot-data-distillation` | Documentation | Silver | Distillation: push-based ingestion (Zerobus) between Ignition Gateway and Delta/UC. Historian relationship, Unified Namespace, control-loop framing. | — | [Distillation](https://docs.google.com/document/d/12Fdm1zO-iWoFHKb2QQ2WgHnWiWSPR0xL4mWduYk-fsw) |
| `purdue-model-isa-95-reference-diagram` | Documentation | Silver | Reference diagram: Purdue model (ISA-95) layers (0–5) for framing where OT data originates and where Databricks sits. | — | [Diagram](https://drive.google.com/file/d/1DefmUDclYjdaTWV6_t6YLQW9MEiqvbDw) |
| `uns-ignition-udt-databricks-position` | Documentation | Silver | Databricks position on Unified Namespace, Ignition UDTs, mapping to UC + Delta for analytics/AI. | — | [Position](https://docs.google.com/document/d/1-rtnsx0wcJQPMLlqJRU4qJ9AE1PUGn7spSkS7xNyUu4) |

---

## PILLAR 11: DATA GOVERNANCE & LIFECYCLE MANAGEMENT

Unity Catalog, data quality, privilege management, and data lineage.

| Slug | Type | Quality | Description | Author/Owner | URL |
|------|------|---------|-------------|--------------|-----|
| `data-lifecycle-policy-automated-stale-table-cleanup` | Codebase | **Gold** | Databricks Asset Bundle: auto-identify & truncate stale tables (90+ days) in UC with DRY_RUN safety + exclusion lists. Audit tables + Lakeview dashboard. | — | [Repo](https://github.com/NickeyKim/Data_Lifecycle_Policy) |
| `uc-privileges-check-drift-detection-dab` | Codebase | **Gold** | DAB: monitors UC privileges daily, detects drift via snapshots, alerts via Lakeview dashboard. | — | [Repo](https://github.com/NickeyKim/UC_privileges_check) |
| `system-table-audit-dashboard` | Dashboard | **Gold** | DAB: AI/BI dashboard for security auditing & anomaly detection from system.access.audit logs (90 days). Unauthorized access + suspicious patterns. | — | [Repo](https://github.com/NickeyKim/System_Table_Audit_Dashboard) |
| `databricks-migration-toolkits` | Codebase | Bronze | Migration toolkit: move Lakeview dashboards, UC models, Genie Spaces, Databricks Apps across workspaces/catalogs. Automates discovery, review, migration with permission preservation. | archana986 | [Repo](https://github.com/archana986/databricks-dashboard-models-app-genie-migration) |
| `rfa-portal-request-for-access-mvp` | App | Silver | Drop-in Databricks App: UC's Request-for-Access flow + governance controls. Self-service requests → email approval → auto GRANT. Reviewers decouple from object ownership (UC tags). | — | [App](https://github.com/databricks-field-eng/dsa-emea-ce/tree/main/accelerators/apps/request-for-access) |
| `uc-migration-toolkits-models-dashboards-across-workspaces` | Presentation | **Gold** | Presentation: why teams need SDK-based migration toolkits (Terraform gaps). Data mesh evolution, workspace consolidation, lineage preservation. | — | [Presentation](https://docs.google.com/presentation/d/1KDTqUM56byxeVjP8Qaw0fZCJ2iKDuT2QiH39sjraPX4) |
| `data-governance-platform-maturity-crawl-walk-run-framework` | Presentation | Bronze | Framework: Data Governance & Platform Maturity progression (Crawl → Walk → Run). Strategic advancement. | — | [Framework](https://docs.google.com/presentation/d/1Y_mjcLS6Gn2oZrEq1D1tJ5PGDCa6fDWo4KcskdPzYS4) |
| `bu-migration-to-data-platform-2` | Documentation | Silver | End-to-end guide: onboarding a Business Unit onto central data platform. 7-stage progression. | — | [Guide](https://docs.google.com/presentation/d/1mKX4F97T8HQ54rpd6wr3RsFPB6YXWcMb4o9uQOfPfzo) |
| `acl-and-permission-planning-template-2` | Documentation | Silver | Google Sheets template: plan & manage ACLs & permissions for enterprise systems. Structured framework. | — | [Template](https://docs.google.com/spreadsheets/d/1uOMwIRm6w0Z3aCaWrQZMcgkOLgMFd1rNIiqzIyMO3bk) |

---

## BONUS: FIELD ENABLEMENT & DSA RESOURCES

Practitioner guidance, knowledge bases, and acceleration resources for field engineers.

| Slug | Type | Quality | Description | Author/Owner | URL |
|------|------|---------|-------------|--------------|-----|
| `pickling-cool-cucumbers-pcc-field-engineering-knowledge-base` | Codebase | Silver | PCC: Databricks FE shared workspace. Automation skills, runbooks, training, AI agent plugins. Vault mgmt + pod ops tools. | — | [Repo](https://github.com/databricks-field-eng/pickling-cool-cucumbers) |
| `dsa-cookbook` | Documentation | Silver | DSA playbook: recipe-style guidance for engagements, technical workflows, best practices, reusable patterns. | — | [Cookbook](https://sites.google.com/databricks.com/delivery-solution-architects/cookbook) |
| `defect-detector-engine-part-visual-inspection-app` | App | **Gold** | Databricks App: AI-powered visual inspection (manufacturing) using CLIP + Vision LLM. Two-stage pipeline. Defect detection + replacement-part search. | pponnaDB (GitHub) | [Repo](https://github.com/pponnaDB/defect-detector) |
| `cloud-infrastructure-costs-solution` | Codebase | **Gold** | Automation: join AWS CUR / Azure Cost Mgmt with Databricks system tables → unified infra + DBU cost reporting (classic compute, AWS + Azure). | — | [Repo](https://github.com/databricks-solutions/cloud-infra-costs) |
| `databricks-platform-setup-iac` | Codebase | **Gold** | Terraform IaC: comprehensive provisioning for Databricks on AWS. Modular, YAML-driven workloads. Networking, IAM, identity, security, UC. | — | [Repo](https://github.com/databricks-field-eng/platform-setup) |

---

## CRITICAL GAPS & THIN COVERAGE

**Potential gaps to address (post-discovery):**

1. **Generative AI Foundation Models & Fine-Tuning** — Assets on pretraining, PEFT, LoRA, or fine-tuned models are underrepresented; mostly relying on foundational model APIs.
2. **Feature Store Deep Dive** — Feature definition, serving, lineage: only touched in MLOps assets; dedicated FS best practices thin.
3. **Real-Time Serving & Low-Latency Inference** — Model Serving patterns, endpoint optimization: minimal coverage vs. batch patterns.
4. **Cross-Cloud Data Mesh Patterns** — Limited explicit guidance on data mesh on Databricks across AWS/Azure/GCP.
5. **AI/ML for Specific Verticals (beyond IIoT)** — FinServ AI, Healthcare AI, Retail AI pipelines: light coverage; mostly industry-specific demos.

---

## KEY METRICS & DISTRIBUTION

- **Total Assets:** 48 curated resources
- **Quality Distribution:** 18 Gold (37.5%), 24 Silver (50%), 6 Bronze (12.5%)
- **Type Distribution:** 
  - Presentations/Decks: 11 (23%)
  - Codebases: 14 (29%)
  - Documentation: 16 (33%)
  - Apps/Demos: 7 (15%)
- **Dominant Authors/Owners:** Josh Melton, David O'Keeffe, Vlad Marin, Bhavin Kukadia, Dhaval Bagadia (FE/GTM leadership)

---

## STANDOUT ASSETS (CUSTOMER IMPACT)

**If you have 15 minutes:** Start with these three.
1. **DSML L100/200 Pitch Deck** (`dsml-l100200-pitch-deck-godsml`) — Canonical positioning
2. **Applied AI Governance Reference Architecture** (`applied-ai-governance-production-patterns-reference-architecture`) — Production safety
3. **AI Data Modeling Distilled** (`ai-data-modeling-insights-recommendations-distilled`) — Semantic foundation for agents

**If you have 1 hour:** Add Industrial IoT ref arch, Genie best practices, and Eval Flywheel demo.

---

## NAVIGATION TIPS

- **For data scientists:** Start Pillar 1, 2, 3, then 4, 9.
- **For architects:** Pillars 1, 2, 5, 10 (governance + ops data).
- **For AI/ML engineers:** Pillars 3, 4, 6, 7, 8.
- **For data engineers:** Pillars 9, 10, 11, then 2.
- **For DS/ML leaders (execs):** DSML pitch deck, AI Governance full deck, Data Modeling insights.

---

**Report Generated:** October 7, 2026  
**Source:** Databricks Sage Context Catalog (FE/GTM Assets)  
**Curator:** DS-Sage Research Agent (Databricks Field Engineering)
