# Feature tree: integration of the completeness review

## Coverage of the review

The verification session received only the beginning of the tree. The text stops at "3.4 MLflow 3 → Models in". Sections 3.4 to 9 were not reviewed. Two items reported as missing (Declarative Automation Bundles, Databricks CLI) are in 3.6, which the reviewer could not see. For the second pass, send the tree as an attached file rather than pasted into the prompt, and split the verification in two runs: sections 1 to 3, then 4 to 9.

## Findings retained

- Lakeflow Connect variants: managed, query-based, community connectors, Auto Loader. Lakeflow Pipelines Editor. Real-time mode for pipelines.
- Lakebase: synced tables and Lakehouse Sync. LTAP becomes the label of the sub-section, not a leaf.
- Multi-table transactions under table formats.
- Unity Catalog: external lineage, access requests, external engine access (catalog commits, Unity REST API), secrets, governed tags and tag propagation, SecureConnect. Two missing dimensions added: observability (Data Quality Monitoring moves here) and cost (system tables, usage dashboard, budgets).
- Discover moves to catalog access, out of semantic definitions.
- Feature engineering: feature tables, Stream Feature Views, feature serving.
- Training compute: Databricks Runtime for Machine Learning next to AI Runtime. AI Runtime SDK and CLI added. The Serverless GPU node is removed; it duplicated its parent.
- Genie Code surfaces grouped under Genie Code. Genie Code CLI leaves section 8.
- Agentic code converter added to section 8.
- Zerobus Ingest moves next to Lakeflow Connect. Lakeflow Jobs moves last.
- Online Feature Stores: GA status not verified, marked.

## Findings rejected

- Lakehouse Replay and workspace spaces: platform operations, out of scope.
- Type widening, Variant shredding, Parquet v2, Iceberg v3: format details, not capabilities to evaluate.
- Lakebase Provisioned as a leaf: legacy offering, the tree does not list legacy.
- Reclassification of Solution Accelerators on Marketplace: not a capability.

## Guidelines added

15. Granularity. A leaf is a capability a technical decision-maker evaluates. Options, formats and versions are not leaves.
16. Architectures and concepts are labels, not leaves. LTAP names a sub-section; Lakebase and Lakehouse//RT are its leaves.
17. A product's surfaces stay under the product. No surface of a product listed elsewhere appears in a tools section.
18. Scope. Platform operations with no data or AI content are out of the tree.

## Modified sections

Sections 4 to 7 and 9 are unchanged.

```
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
│   │   ├── Models in Unity Catalog (model registry)
│   │   └── Prompt Registry
│   ├── 3.5 Model Serving (ML models)
│   └── 3.6 Deployment automation
│       ├── Declarative Automation Bundles
│       └── Databricks CLI
├── 8. Developer tools
│   ├── 8.1 Omnigent (coding agent harness)
│   ├── 8.2 Agentic code converter (SQL migration)
│   └── 8.3 External coding agents
│       ├── ug CLI (Unity Gateway connection)
│       └── AI Dev Kit (community toolkit)
```
