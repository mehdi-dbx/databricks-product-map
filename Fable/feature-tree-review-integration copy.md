
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
