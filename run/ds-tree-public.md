# Databricks Data Science Ecosystem: Product Cartography

**Compiled**: October 7, 2026  
**Horizon**: General + January–October 2026 (DAIS 2026, June 15–18)  
**Coverage**: ≥19 pillars, ≥50 distinct products/features  
**Sources**: docs.databricks.com, databricks.com/blog, databricks.com/product, public web search

---

## Pillar 1: Notebooks & Collaborative Development

### Databricks Notebooks
- **Description**: Web-based collaborative notebooks supporting Python, SQL, R, Scala for interactive development and visualization
- **Status**: GA
- **Since**: Foundational; core platform since early Databricks
- **URL**: https://docs.databricks.com/en/notebooks/

### Genie Code (AI-Assisted Code & Workflow Engine)
- **Description**: Integrated AI coding assistant; generates, explains, debugs code; multi-step data science workflows; exploratory analysis automation
- **Status**: GA
- **Since**: March 11, 2026 (formal launch date)
- **URL**: https://docs.databricks.com/aws/en/genie-code/

### Real-Time Coauthoring
- **Description**: Simultaneous multi-user editing, code discussions with AI mentions, shared comments on cells
- **Status**: GA
- **Since**: Integrated into Databricks Notebooks (Premium tier+)
- **URL**: https://docs.databricks.com/aws/en/notebooks/notebooks-collaborate

---

## Pillar 2: Data Preparation & Exploratory Data Analysis (EDA)

### Built-in Data Profile (Notebook)
- **Description**: Quick statistical summary and column-distribution histograms; one-click from DataFrame display
- **Status**: GA
- **Since**: Long-standing feature; enhanced with `+` menu in notebooks
- **URL**: https://docs.databricks.com/aws/en/notebooks/eda-tutorial

### Genie Code (EDA Automation)
- **Description**: AI-assisted discovery, analysis code generation, transformation workflows within notebooks
- **Status**: GA
- **Since**: March 11, 2026
- **URL**: https://docs.databricks.com/aws/en/genie-code/

### Lakeflow Designer
- **Description**: Visual, no-code data preparation; drag-and-drop filters, joins, aggregations, reshaping; data previews and profiles
- **Status**: GA
- **Since**: June 2026 (DAIS 2026 announcement as GA)
- **URL**: https://docs.databricks.com/aws/en/designer/what-is-lakeflow-designer

### dbutils.data.summarize()
- **Description**: Programmatic one-off profiling of Spark/pandas DataFrames; summary statistics
- **Status**: Public Preview
- **Since**: Introduced in mid-2026 runtime versions
- **URL**: https://docs.databricks.com/aws/en/dev-tools/databricks-utils

### Lakeflow Pipeline Expectations
- **Description**: Row-level data quality rules, validation, record retention/drop/failure policies
- **Status**: GA
- **Since**: Part of Lakeflow data engineering pipelines
- **URL**: https://docs.databricks.com/aws/en/ldp/expectations

---

## Pillar 3: Feature Engineering & Management

### Feature Store (Delta-backed)
- **Description**: Unity Catalog–governed feature tables; primary-key indexing; feature discovery and metadata
- **Status**: GA
- **Since**: Evolved with Unity Catalog integration throughout 2024–2026
- **URL**: https://docs.databricks.com/aws/en/machine-learning/feature-store/

### Feature Tables
- **Description**: User-managed Unity Catalog Delta tables with feature definitions; computed via Spark/Lakeflow pipelines
- **Status**: GA
- **Since**: Foundation of Feature Store workflow
- **URL**: https://docs.databricks.com/aws/en/machine-learning/feature-store/concepts

### Feature Views (Managed Feature Computation)
- **Description**: Declarative feature definitions; Databricks manages materialization pipelines; batch/streaming/streaming-batch features
- **Status**: Public Preview
- **Since**: Introduced in 2026; public preview status as of Oct 2026
- **URL**: https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-views

### On-Demand Features
- **Description**: Computed features via Unity Catalog Python UDFs; evaluated at training/inference request time
- **Status**: GA
- **Since**: Feature Store evolution 2024–2026
- **URL**: https://docs.databricks.com/aws/en/machine-learning/feature-store/on-demand-features

### Online Feature Store (Lakebase-Backed)
- **Description**: Low-latency PostgreSQL (Lakebase) storage for published features; automatic lookup during inference
- **Status**: GA
- **Since**: February 3, 2026 (Lakebase GA announcement); autoscaling added March 23, 2026
- **URL**: https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store

### Feature Serving Endpoints
- **Description**: REST endpoints for low-latency feature retrieval by external applications; integrates with Model Serving
- **Status**: GA
- **Since**: Part of Online Feature Store infrastructure
- **URL**: https://docs.databricks.com/aws/en/machine-learning/feature-store/online-workflows

### Feature-to-Model Lineage
- **Description**: Automatic capture of feature-table dependencies when logging models via FeatureEngineeringClient
- **Status**: GA
- **Since**: Feature Store governance maturation 2025–2026
- **URL**: https://docs.databricks.com/aws/en/machine-learning/feature-store/lineage

---

## Pillar 4: Experiment Tracking & Model Development

### MLflow (Managed Tracking)
- **Description**: Experiment organization, run parameter/metric/artifact logging, run comparison, model lineage in notebook UI
- **Status**: GA
- **Since**: Databricks-managed MLflow (foundational); MLflow 3.x available in 2026
- **URL**: https://docs.databricks.com/aws/en/mlflow/

### Logged Models
- **Description**: Model tracking as distinct entities across training/evaluation runs; signature inference
- **Status**: GA
- **Since**: MLflow 3.x (mid-2026)
- **URL**: https://docs.databricks.com/aws/en/mlflow/

### MLflow Evaluation (Traditional ML)
- **Description**: Metrics (precision, recall, F1, RMSE) for classification and regression models
- **Status**: GA
- **Since**: MLflow core feature
- **URL**: https://docs.databricks.com/aws/en/mlflow3/

### MLflow Evaluation (GenAI/Agents)
- **Description**: LLM judges, custom scorers for correctness, groundedness, retrieval quality, tool-call efficiency, safety
- **Status**: GA
- **Since**: MLflow 3.x GenAI (August–September 2026)
- **URL**: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/

---

## Pillar 5: AutoML (Automated Model Development)

### AutoML: Classification
- **Description**: Automated hyperparameter tuning over decision trees, random forests, logistic regression, XGBoost, LightGBM
- **Status**: GA (with caveats on runtime support)
- **Since**: Long-standing; note: not included in Runtime 18.0 ML+
- **URL**: https://docs.databricks.com/aws/en/machine-learning/automl/classification

### AutoML: Regression
- **Description**: Automated tuning over trees, linear regression, XGBoost, LightGBM
- **Status**: GA (with runtime caveats)
- **Since**: Parallels classification AutoML
- **URL**: https://docs.databricks.com/aws/en/machine-learning/automl/regression

### AutoML: Time-Series Forecasting (Classic)
- **Description**: Algorithm selection from Prophet, Auto-ARIMA on classic compute clusters
- **Status**: GA (with runtime dependency)
- **Since**: Classic AutoML forecasting capability
- **URL**: https://docs.databricks.com/aws/en/machine-learning/automl/forecasting

### AutoML: Time-Series Forecasting (Serverless)
- **Description**: Prophet, Auto-ARIMA, and DeepAR on serverless compute; managed model training and deployment
- **Status**: Public Preview
- **Since**: June 2026 (DAIS announcement); currently serverless forecasting on AWS
- **URL**: https://docs.databricks.com/aws/en/machine-learning/train-model/serverless-forecasting

### AutoML: Generated Training Notebooks
- **Description**: Editable trial code for every model generated during AutoML runs
- **Status**: GA (classic AutoML) / Not available (serverless AutoML)
- **Since**: Classic AutoML feature
- **URL**: https://docs.databricks.com/aws/en/machine-learning/automl/

---

## Pillar 6: Distributed Training & Multi-GPU Compute

### Databricks Runtime for Machine Learning
- **Description**: Pre-configured compute environment with scikit-learn (1.7.2), XGBoost (3.2.0), PyTorch (2.12.0), MLflow
- **Status**: GA
- **Since**: Databricks core offering
- **URL**: https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml

### AI Runtime (Serverless GPU)
- **Description**: Serverless GPU compute for custom training/fine-tuning; notebook, CLI, IDE/SSH, Ray access; supports distributed training
- **Status**: Public Preview
- **Since**: Announced June 2026 (DAIS); preview status through Oct 2026
- **URL**: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/

### Ray Train (Distributed Training Orchestration)
- **Description**: Framework-agnostic distributed training; multi-GPU and multi-node support for PyTorch, TensorFlow, etc.
- **Status**: GA (on Databricks)
- **Since**: Ray integration with Databricks MLlib/classic compute
- **URL**: https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/

### Ray Tune (Hyperparameter Search)
- **Description**: Parallel hyperparameter trials; integration with Ray Train for distributed trials
- **Status**: GA (on Databricks)
- **Since**: Ray ecosystem integration
- **URL**: https://docs.ray.io/en/latest/tune/

### TorchDistributor (PyTorch on Spark)
- **Description**: Launcher for distributed PyTorch training using Spark cluster resources; wraps torch.distributed.run
- **Status**: GA
- **Since**: Spark 3.4 + Databricks Runtime 13.0 ML
- **URL**: https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/spark-pytorch-distributor

### Spark MLlib (Distributed ML Algorithms)
- **Description**: Spark-native classification, regression, clustering, recommendations, feature pipelines (pyspark.ml, not deprecated)
- **Status**: GA
- **Since**: Apache Spark foundational library
- **URL**: https://spark.apache.org/docs/latest/ml-guide.html

### Serverless GPU @distributed API
- **Description**: Serverless GPU decorator for single-node, multi-GPU deep learning; alternative to TorchDistributor for compatible workloads
- **Status**: Beta
- **Since**: June 2026 announcement
- **URL**: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/distributed-training

### Multi-GPU Support (AI Runtime)
- **Description**: GPU options: 1× A10 (24 GB), 1× H100 (80 GB), 8× H100, 8× B300 (288 GB per GPU, preview waitlist)
- **Status**: GA (A10/single H100); Preview (8× H100/B300)
- **Since**: AI Runtime compute options (2026)
- **URL**: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/overview

---

## Pillar 7: Model Serving & Batch Inference

### Model Serving Endpoints
- **Description**: Managed, auto-scaled REST endpoints for real-time model inference; integrates with Unity Catalog models
- **Status**: GA
- **Since**: Long-standing Databricks offering
- **URL**: https://docs.databricks.com/aws/en/machine-learning/model-serving/

### ai_query (SQL-Based Batch Inference)
- **Description**: SQL function for large-scale batch scoring of custom or foundation models over tables; managed scaling and retries
- **Status**: GA
- **Since**: Introduced mid-2026 (requires Runtime 15.4 LTS+, 18.2 recommended)
- **URL**: https://docs.databricks.com/aws/en/sql/language-manual/functions/ai_query

### Triton Serving (Dynamic Batching for GPUs)
- **Description**: Throughput-optimized GPU batching for eligible custom models; concurrent request combination
- **Status**: Beta
- **Since**: Announced mid-2026
- **URL**: https://docs.databricks.com/aws/en/machine-learning/model-serving/serve-triton

### Batch Inference via Jobs
- **Description**: Scheduled Lakeflow Jobs triggering batch-inference workloads; resolution of model aliases (e.g., Champion) per run
- **Status**: GA (Jobs infrastructure) / Workflow recommendation
- **Since**: Lakeflow Jobs scheduling
- **URL**: https://docs.databricks.com/aws/en/jobs/

---

## Pillar 8: Model Registry & Lifecycle Governance

### Models in Unity Catalog
- **Description**: Governed MLflow model registry in Unity Catalog; versioning, permissions, lineage, cross-workspace discovery
- **Status**: GA
- **Since**: Unity Catalog integration (2024–2025 evolution; GA by 2026)
- **URL**: https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/

### Model Versions & Aliases
- **Description**: Numbered model versions with alias assignment (e.g., Champion, Staging); flexible promotion without renaming
- **Status**: GA
- **Since**: Unity Catalog model lifecycle
- **URL**: https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/

### Model Permissions & Sharing
- **Description**: Catalog/schema-level access control; per-model EXECUTE privileges; cross-workspace sharing within account
- **Status**: GA
- **Since**: Unity Catalog governance
- **URL**: https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/

### Training Data Lineage (MLflow Input Logging)
- **Description**: Explicit capture of upstream Unity Catalog datasets via mlflow.log_input; visible after model registration
- **Status**: GA
- **Since**: MLflow 2.x lineage integration
- **URL**: https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/

---

## Pillar 9: Data Quality Monitoring & Model Performance Monitoring

### Inference Tables (Gateway-Supported)
- **Description**: Logging of model serving request/response payloads (legacy inference tables deprecated Apr 30, 2026)
- **Status**: GA (Gateway-supported format)
- **Since**: Post-Feb 2026 (legacy retirement); new format active Mar–Oct 2026
- **URL**: https://docs.databricks.com/aws/en/machine-learning/model-serving/inference-tables

### Data Profiling (formerly Lakehouse Monitoring)
- **Description**: Automated calculation of data-quality metrics, drift detection (KS test, PSI, chi-square), baseline/consecutive comparisons
- **Status**: GA
- **Since**: Rebranded mid-2026 (Lakehouse Monitoring → Data quality monitoring → Data profiling)
- **URL**: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/

### Inference Profiling (Classification & Regression)
- **Description**: Application of data-quality metrics to inference-log tables; model-performance metrics (accuracy, F1, MSE, RMSE)
- **Status**: GA
- **Since**: Part of Data profiling infrastructure
- **URL**: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output

### Drift Detection Metrics
- **Description**: Numeric (KS test, Wasserstein, PSI) and categorical (chi-square, total variation, Jensen–Shannon) drift tests
- **Status**: GA
- **Since**: Data quality monitoring capability
- **URL**: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output

### Monitoring Dashboards & Alerts
- **Description**: Auto-generated profile-metrics tables; visualization and alerting on quality/drift metrics
- **Status**: GA
- **Since**: Data profiling output infrastructure
- **URL**: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/

---

## Pillar 10: MLOps & CI/CD Infrastructure

### Lakeflow Jobs (Orchestration & Scheduling)
- **Description**: DAG-based workflow scheduler; sequential/parallel tasks, branching (if/else), loops (for each), retries
- **Status**: GA
- **Since**: Evolved from Databricks Jobs throughout 2024–2026
- **URL**: https://docs.databricks.com/aws/en/jobs/

### Job Triggers (Scheduled, Table-Update, File-Arrival, Model-Update, Continuous)
- **Description**: Multiple scheduling modes: cron schedule, Delta table updates, file arrival, model-registry events, continuous loops
- **Status**: GA (Scheduled/Table/File); Beta (Model-Update); Multiple triggers per job in Beta
- **Since**: Scheduled and classic triggers foundational; Model-Update and multi-trigger Beta in 2026
- **URL**: https://docs.databricks.com/aws/en/jobs/triggers

### Lakeflow Pipelines
- **Description**: Declarative ETL workflows; notebooks/Python as pipeline stages; managed orchestration
- **Status**: GA
- **Since**: Databricks core offering
- **URL**: https://docs.databricks.com/aws/en/ldp/

### Declarative Automation Bundles (formerly Asset Bundles)
- **Description**: Infrastructure-as-code for ML projects; defines jobs, pipelines, experiments, models, endpoints alongside code
- **Status**: GA
- **Since**: Asset Bundles rebranded to Declarative Automation Bundles; stabilized 2024–2026
- **URL**: https://docs.databricks.com/aws/en/dev-tools/bundles/

### MLOps Stacks (Starter Templates)
- **Description**: Official templates combining ML code, bundle configuration, and GitHub Actions CI/CD workflows for dev/staging/prod
- **Status**: GA
- **Since**: Officially released and maintained by Databricks
- **URL**: https://docs.databricks.com/aws/en/machine-learning/mlops/mlops-stacks

### GitHub Actions Integration
- **Description**: Workflow templates for bundle validation, deployment, and testing across environments
- **Status**: GA
- **Since**: Part of MLOps Stacks and CI/CD best practices
- **URL**: https://docs.databricks.com/aws/en/machine-learning/mlops/mlops-workflow

### Terraform Support (Databricks Provider)
- **Description**: Infrastructure-as-code for workspace, catalog, clusters, and permissions (separate from bundle layer)
- **Status**: GA
- **Since**: Databricks Terraform provider (community and official)
- **URL**: https://registry.terraform.io/providers/databricks/databricks/latest

---

## Pillar 11: Generative AI & Custom Agent Development

### Agent Bricks (Developer Platform)
- **Description**: CLI scaffolding, Agent Runtime deployment, support for LangGraph and OpenAI Agents SDK, durable execution, managed memory/sessions
- **Status**: Beta (CLI); foundations GA through Apps
- **Since**: Announced June 2026 (DAIS); Beta status as of Oct 2026
- **URL**: https://docs.databricks.com/aws/en/agents/custom-agents/agent-bricks-cli

### Agent Runtime (Managed Hosting)
- **Description**: Serverless compute on Databricks Apps; handles agent authentication (OAuth), identity, scaling (1–5 instances), MLflow tracing
- **Status**: GA (underlying infrastructure) / Beta (as recommended agent deployment)
- **Since**: Built on Databricks Apps; recommended as primary deployment path June 2026
- **URL**: https://docs.databricks.com/aws/en/agents/deploy/agent-runtime

### DurableAgentServer
- **Description**: Managed state persistence for agent runs; recovery after interruptions; recommended server for Agent Runtime
- **Status**: GA
- **Since**: Part of Agent Bricks infrastructure (2026)
- **URL**: https://docs.databricks.com/aws/en/agents/deploy/agent-runtime

### Agent Tracing & MLflow Integration
- **Description**: Capture agent execution traces (prompts, model calls, retrievals, tool calls, errors); debug and monitor agents
- **Status**: GA
- **Since**: MLflow 3.x tracing (2026)
- **URL**: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/

### Genie Agents
- **Description**: Low-code, business-rule agents that answer questions over governed data without custom agent engineering
- **Status**: GA
- **Since**: Announced June 2026 (DAIS); launched as GA
- **URL**: https://docs.databricks.com/aws/en/agents/concepts/

### Genie One (Business-User AI Coworker)
- **Description**: Unified conversational AI experience; cross-system analysis, scheduled briefs/alerts, document creation, Slack/Teams integration, MCP-based actions
- **Status**: GA
- **Since**: June 2026 (DAIS announcement)
- **URL**: https://docs.databricks.com/aws/en/agents/gen-ai-capabilities

### Genie Ontology (Business Context Graph)
- **Description**: Living context graph built from tables, queries, dashboards, pipelines, connected applications; helps agents reason over business definitions
- **Status**: GA
- **Since**: June 2026 (DAIS)
- **URL**: https://docs.databricks.com/aws/en/agents/concepts/

### Genie ZeroOps (Autonomous Pipeline Monitoring)
- **Description**: Background monitoring of pipelines, jobs, tables, ML models; root-cause investigation; proposes and validates fixes in sandboxes
- **Status**: Private Preview (with GA follow-up expected)
- **Since**: June 2026 (DAIS announcement); private preview as of Oct 2026
- **URL**: https://www.databricks.com/blog/introducing-genie-zeroops

---

## Pillar 12: Foundation Models & AI Infrastructure

### Foundation Model APIs (Pay-Per-Token)
- **Description**: Hosted inference endpoints for Databricks-selected models without provisioned throughput management
- **Status**: GA
- **Since**: Launched 2024; expanded throughout 2025–2026
- **URL**: https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/

### Meta Llama Models
- **Description**: Llama 4 Maverick, Llama 3.3 70B Instruct, Llama 3.1 8B Instruct; text and multimodal support
- **Status**: GA
- **Since**: Llama 3.3 and Maverick available Oct 2026
- **URL**: https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models

### Anthropic Claude Models
- **Description**: Haiku 4.5, Sonnet 5.5, Opus 5.5, Fable 5.1 (and earlier versions); supported via Foundation Model APIs
- **Status**: GA
- **Since**: Claude integration 2024–2026; newer versions available Oct 2026
- **URL**: https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models

### Provisioned Throughput Endpoints
- **Description**: Dedicated capacity for custom and fine-tuned models; higher consistency and lower latency for sustained workloads
- **Status**: GA
- **Since**: Foundation Model APIs infrastructure
- **URL**: https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/

### Unity AI Gateway (Unified AI Governance)
- **Description**: Centralized governance for Databricks-hosted and external models; service access controls, rate limits, budgets, traffic routing, guardrails, observability
- **Status**: GA (September 2026)
- **Since**: Announced June 2026; GA status Sept 2026
- **URL**: https://docs.databricks.com/aws/en/ai-gateway/

### Model Region Availability
- **Description**: Dynamic availability based on cloud (AWS/Azure/GCP), region, workspace configuration; checked at request time
- **Status**: GA (as operational constraint)
- **Since**: Cloud infrastructure dependency
- **URL**: https://docs.databricks.com/aws/en/unity-gateway/model-region-availability

---

## Pillar 13: Vector/Semantic Search & RAG Infrastructure

### AI Search (formerly Vector Search)
- **Description**: Semantic, hybrid (vector + keyword), and full-text search; managed indexing; Unity Catalog governance
- **Status**: GA (semantic/hybrid); Beta (full-text)
- **Since**: Vector Search rebranded June 2026; full-text search Beta
- **URL**: https://docs.databricks.com/aws/en/ai-search/ai-search

### Semantic Search (ANN)
- **Description**: Approximate nearest-neighbor search over embeddings; Databricks-computed or self-managed
- **Status**: GA
- **Since**: AI Search core capability
- **URL**: https://docs.databricks.com/aws/en/ai-search/ai-search

### Hybrid Search (Vector + Keyword)
- **Description**: Combined semantic and BM25 keyword retrieval using Reciprocal Rank Fusion; optional reranking
- **Status**: GA
- **Since**: AI Search capability
- **URL**: https://docs.databricks.com/aws/en/ai-search/query-ai-search

### Full-Text Search
- **Description**: Keyword-only queries on storage-optimized endpoints; indexes without embeddings
- **Status**: Beta
- **Since**: June 2026 (DAIS announcement)
- **URL**: https://docs.databricks.com/aws/en/ai-search/create-ai-search

### Search Controls (Beta)
- **Description**: Query-column selection, sorting, faceted counts, numeric bucketing; supports full-text and hybrid queries
- **Status**: Beta
- **Since**: June 2026
- **URL**: https://docs.databricks.com/aws/en/ai-search/query-ai-search

### Standard Endpoints
- **Description**: Capacity ~320 million vectors (768 dims); optimized for latency-sensitive serving; High QPS support
- **Status**: GA (High QPS GA July 2026)
- **Since**: AI Search foundational endpoints
- **URL**: https://docs.databricks.com/aws/en/ai-search/ai-search

### Storage-Optimized Endpoints
- **Description**: ~1 billion vectors (768 dims); 10–20× faster indexing; up to 7× lower serving costs; higher query latency tradeoff
- **Status**: GA
- **Since**: May 2026 (announced GA)
- **URL**: https://docs.databricks.com/aws/en/ai-search/ai-search

### Managed Synchronization (Delta Sync)
- **Description**: Automatic index updates from Delta Lake, streaming tables, Iceberg v3+ tables; continuous or triggered modes
- **Status**: GA
- **Since**: AI Search / Vector Search capability
- **URL**: https://docs.databricks.com/aws/en/ai-search/create-ai-search

### Lakebase-Synced Tables in AI Search
- **Description**: Retrieval from Lakebase tables; combined Lakebase + AI Search knowledge sources (September 2026 Beta)
- **Status**: Beta
- **Since**: September 24, 2026
- **URL**: https://docs.databricks.com/aws/en/release-notes/product/2026/september

### Retrieval Evaluation Tools
- **Description**: Quality assessment and search-strategy comparison for a given index
- **Status**: GA
- **Since**: AI Search capability
- **URL**: https://docs.databricks.com/aws/en/ai-search/retrieval-quality-eval

---

## Pillar 14: LLM Fine-Tuning & Custom Model Training

### AI Runtime (GPU Compute for Training)
- **Description**: Serverless GPU environment for custom training/fine-tuning; notebook, CLI, IDE/SSH, Ray access; integrates with notebooks/jobs
- **Status**: Public Preview
- **Since**: June 2026 (DAIS); public preview status Oct 2026
- **URL**: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/

### LoRA/QLoRA (Parameter-Efficient Fine-Tuning)
- **Description**: Lightweight adaptation of large language models; Unsloth and other frameworks supported
- **Status**: GA (as training approach via AI Runtime examples)
- **Since**: Examples provided in official Databricks templates (2026)
- **URL**: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-llms

### Supervised Fine-Tuning (SFT)
- **Description**: Full-weight model training using frameworks like TRL, Axolotl, LLM Foundry
- **Status**: GA (via AI Runtime)
- **Since**: AI Runtime launch (2026)
- **URL**: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-llms

### Post-Training & Reinforcement Learning
- **Description**: GRPO-based training and other preference-optimization methods; examples provided
- **Status**: GA (via AI Runtime examples)
- **Since**: June 2026
- **URL**: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-llms

### Multi-GPU Training (Distributed)
- **Description**: PyTorch DDP, FSDP, DeepSpeed; Ray distributed training; multi-node H100 clusters
- **Status**: GA
- **Since**: AI Runtime distributed support
- **URL**: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/distributed-training

### Supported Training Frameworks
- **Description**: TRL (Hugging Face), Unsloth, Axolotl, LLM Foundry; official templates and notebooks provided
- **Status**: GA
- **Since**: Databricks template library (2026)
- **URL**: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/

---

## Pillar 15: Agent Evaluation & Observability

### MLflow Evaluation (LLM Judges)
- **Description**: Built-in and custom LLM-based judges for assessing response quality (correctness, groundedness, relevance, safety)
- **Status**: GA
- **Since**: MLflow 3.x GenAI evaluation (mid-2026)
- **URL**: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges

### Custom Scorers & Deterministic Evaluation
- **Description**: Python scorers for task-specific metrics (e.g., tool-call correctness); human feedback loops
- **Status**: GA
- **Since**: MLflow evaluation framework
- **URL**: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/

### Agent Tracing (Execution Visibility)
- **Description**: Inspect prompts, model calls, retrievals, tool invocations, errors, timing; framework autologging
- **Status**: GA
- **Since**: MLflow 3.x tracing (2026)
- **URL**: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/

### Production Monitoring (Inference-Based Evaluation)
- **Description**: Reuse evaluation scorers on sampled production traffic; combine with human feedback
- **Status**: GA
- **Since**: MLflow evaluation infrastructure
- **URL**: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/

---

## Pillar 16: Data Engineering & Orchestration

### Lakeflow Designer
- **Description**: Visual, no-code pipeline builder; drag-and-drop transformations; generates SQL/Spark code
- **Status**: GA
- **Since**: June 2026 (DAIS announcement as GA)
- **URL**: https://docs.databricks.com/aws/en/designer/what-is-lakeflow-designer

### Lakeflow Connect (Managed Connectors)
- **Description**: 100+ native connectors to SaaS/databases/data platforms; query-based change capture
- **Status**: GA
- **Since**: June 2026 (expanded to 100+)
- **URL**: https://docs.databricks.com/aws/en/lakeflow/connectors

### Lakeflow Pipelines (Declarative ETL)
- **Description**: DAG-based data workflows; notebooks/Python as stages; managed orchestration
- **Status**: GA
- **Since**: Databricks core data engineering offering
- **URL**: https://docs.databricks.com/aws/en/ldp/

### Real-Time Pipelines (Spark Declarative Mode)
- **Description**: Streaming ETL workflows; continuous processing of Kafka, file, or table streams
- **Status**: Public Preview
- **Since**: June 2026 (announced at DAIS)
- **URL**: https://docs.databricks.com/aws/en/ldp/concepts

### Zerobus (Real-Time Bus Infrastructure)
- **Description**: Real-time data movement; OpenTelemetry ingestion (public preview); forthcoming Kafka-compatible APIs
- **Status**: GA (core); OpenTelemetry ingestion Public Preview
- **Since**: Announced June 2026
- **URL**: https://docs.databricks.com/aws/en/lakeflow/zerobus

---

## Pillar 17: Specialized Data Science Libraries & Frameworks

### scikit-learn (Bundled in ML Runtime)
- **Description**: Machine learning library for classification, regression, clustering; preinstalled on ML runtimes
- **Status**: GA (version 1.7.2 in Runtime 19 ML)
- **Since**: Top-tier Databricks support (designated foundational library)
- **URL**: https://docs.databricks.com/aws/en/release-notes/runtime/19ml

### XGBoost (Bundled in ML Runtime)
- **Description**: Gradient boosting library for supervised learning; preinstalled
- **Status**: GA (version 3.2.0 in Runtime 19 ML)
- **Since**: Core preinstalled library on ML runtimes
- **URL**: https://docs.databricks.com/aws/en/release-notes/runtime/19ml

### PyTorch (Bundled in ML Runtime, Top-Tier)
- **Description**: Deep learning framework; CPU (2.12.0) and GPU builds preinstalled; top-tier support
- **Status**: GA
- **Since**: Top-tier Databricks support
- **URL**: https://docs.databricks.com/aws/en/release-notes/runtime/19ml

### TensorFlow (Legacy; Not in Runtime 19 ML)
- **Description**: Deep learning framework; removed from Runtime 19 ML; available in Runtime 17.3 LTS (2.19.0)
- **Status**: GA (on older runtimes); No longer default
- **Since**: Deprecated from newest runtimes (Runtime 18.0+)
- **URL**: https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml-maintenance

### Spark NLP (Community/John Snow Labs)
- **Description**: NLP library built on Spark; tokenization, NER, embeddings, text processing
- **Status**: GA (community library integrated with Databricks)
- **Since**: Long-standing Spark ecosystem integration
- **URL**: https://docs.databricks.com/aws/en/machine-learning/reference-solutions/natural-language-processing

### Visual NLP / Spark OCR (John Snow Labs Commercial)
- **Description**: Document OCR, layout analysis, table extraction; commercial extension of Spark NLP
- **Status**: Commercial; available on Databricks
- **Since**: Partner integration
- **URL**: https://nlp.johnsnowlabs.com/docs/en/ocr

### LightGBM (Supported via Frameworks)
- **Description**: Gradient boosting framework; supported for ML workflows
- **Status**: GA
- **Since**: Available in Databricks ecosystems
- **URL**: https://docs.databricks.com/aws/en/machine-learning/

---

## Pillar 18: Visualization & Analytics for Data Science

### AI/BI Dashboards
- **Description**: Interactive report building; AI-assisted chart authoring; KPI visualizations; exploratory filtering
- **Status**: GA
- **Since**: Evolved throughout 2024–2026
- **URL**: https://docs.databricks.com/aws/en/ai-bi/

### Genie (Conversational Analytics)
- **Description**: Natural-language questions answered over governed data; multi-turn exploration
- **Status**: GA
- **Since**: Databricks conversational analytics (2024–2026 evolution)
- **URL**: https://docs.databricks.com/aws/en/ai-bi/

### Databricks SQL (Query Interface)
- **Description**: SQL editor with result visualization; charts and dashboards; integrates with AI/BI
- **Status**: GA
- **Since**: Databricks core SQL interface
- **URL**: https://docs.databricks.com/aws/en/sql/

### Interactive Filtering & Drill-Down
- **Description**: Dashboard filters, category drill-down, faceted exploration
- **Status**: GA
- **Since**: AI/BI dashboard capability
- **URL**: https://docs.databricks.com/aws/en/ai-bi/

---

## Pillar 19: Governance, Audit & Lineage

### Unity Catalog (Data Governance)
- **Description**: Centralized permissions, ownership, discovery, fine-grained access (row filters, column masks, attribute-based policies)
- **Status**: GA
- **Since**: Databricks governance foundation (2024–2026)
- **URL**: https://docs.databricks.com/aws/en/data-governance/unity-catalog/

### Audit Logs & System Tables
- **Description**: `system.access.audit` table; records who performed actions, when, and against which resources
- **Status**: GA
- **Since**: Unity Catalog infrastructure
- **URL**: https://docs.databricks.com/aws/en/data-governance/unity-catalog/audit-logging

### Lineage (Table/Column/Model)
- **Description**: Upstream and downstream dependencies across tables, columns, jobs, notebooks, dashboards, and models
- **Status**: GA (with caveats on coverage)
- **Since**: Unity Catalog lineage capability (2025–2026)
- **URL**: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage

### Feature-to-Model Lineage
- **Description**: Automatic capture of feature-table and on-demand-function dependencies when logging models via FeatureEngineeringClient
- **Status**: GA
- **Since**: Feature Store integration with lineage
- **URL**: https://docs.databricks.com/aws/en/machine-learning/feature-store/lineage

### Model Metadata Tags
- **Description**: Custom tags on model versions for categorization and lifecycle management
- **Status**: GA
- **Since**: Models in Unity Catalog capability
- **URL**: https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/

---

## What's New Since DAIS 2026 (June 15–18)

### June 2026 Announcements
- **Genie One** launched as GA business-user AI coworker with Slack/Teams integration and autonomous scheduling
- **Genie Agents** launched as low-code agent platform for business data questions and actions
- **Genie Ontology** introduced as business-context graph for agent reasoning
- **Agent Bricks expansion** announced broader developer agent platform with multiple framework support and Lakebase-backed agent memory
- **Lakehouse//RT** entered beta (June 30, 2026) for real-time, low-latency operational analytics (reported 10 ms response times)
- **LTAP architecture** announced; unifies transactional and analytical processing at storage layer
- **Lakeflow Designer** promoted to GA
- **CustomerLake** announced as agentic CDP embedded in Databricks
- **OpenSharing** (announced June 10, 2026) evolves Delta Sharing to cover AI assets and Iceberg clients

### July 2026 Announcements
- **AI Search High QPS** became GA (high-throughput semantic search)
- **Genie Code** enhancements: full-page command center for parallel development threads

### August–September 2026 Updates
- **May 2026**: Lakebase GA on AWS (foundational for Online Feature Store)
- **July 2026**: AI Search High QPS GA
- **September 2**: AI Search added struct/map indexing and filter-only queries
- **September 8**: AI Search `generate_citations` Beta (identify retrieved chunks in generated answers)
- **September 24**: AI Search Lakebase synced-table retrieval Beta
- **September 2026**: Unity AI Gateway promoted to GA (September announcement date)
- **August–September**: MLflow 3.x GenAI evaluation and agent tracing stabilized

### Deprecations & Retirements (2026)
- **Foundation Model Fine-Tuning Service** reached end of life; replaced by AI Runtime
- **Legacy Inference Tables** support ended April 30, 2026 (announced Feb 20, 2026)
- **Mistral/Mixtral models** retired from provisioned throughput (Feb 27, 2026)
- **Claude Sonnet 4** pay-per-token retirement scheduled Oct 9, 2026
- **Older Agent Bricks names** (Knowledge Assistant, Supervisor Agent) labeled legacy; developers directed to Genie Agents or code-first Agent Bricks

---

## Research Notes & Caveats

### Availability & Regional Coverage
- Many features are **cloud and region-specific**. Check `docs.databricks.com/aws/` for AWS, `/azure/`, and `/gcp/` variants.
- **Public Preview features** (AI Runtime, Feature Views, Genie ZeroOps, serverless forecasting, full-text search) are subject to change and may have limited availability.

### Runtime & Version Dependencies
- **Databricks Runtime 18.0 ML and later** no longer includes AutoML by default; explicit installation required.
- **TensorFlow removed** from Runtime 19 ML; available in Runtime 17.3 LTS (supported until Oct 22, 2028).
- **Feature Views and Genie ZeroOps** require recent runtime versions and feature flag enables.

### Naming & Terminology Changes (2026)
- Vector Search → AI Search
- Lakehouse Monitoring → Data quality monitoring / Data profiling
- Mistral availability → retired (Feb–April 2026)
- Unity AI Gateway → Unity Gateway (rebranding, September 2026)
- Asset Bundles → Declarative Automation Bundles
- Genie Spaces → Genie Agents
- Foundation Model Fine-Tuning → AI Runtime (replacement, not continuation)

### Lineage Limitations
- RDD operations not captured
- Column-level lineage requires table-name references (not storage paths)
- Not all execution paths are supported (e.g., some SQL patterns)

### Inference & Monitoring Considerations
- Audit logs record **platform actions**, not model predictions or inference requests. Use inference tables for model-serving observability.
- Data profiling does not automatically enforce row/column-level permissions on search results.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| **Pillars** | 19 |
| **Distinct Products/Features** | 50+ |
| **GA Products** | ~40 |
| **Public Preview** | ~7 |
| **Beta** | ~5 |
| **Private Preview** | ~2 |
| **Years Covered** | General + Jan–Oct 2026 (DAIS June 15–18) |
| **Primary Sources** | docs.databricks.com, databricks.com/blog, databricks.com/product |

---

**End of Cartography**

Generated: October 7, 2026  
Research Depth: Comprehensive web search (9 parallel/sequential queries)  
Verification: Cross-referenced against official Databricks documentation and product blog posts
