# DS Capsule Decomposition Log

## Task
Decompose 3 L3 capsules (Monitoring & evaluation, MLOps & CI/CD, DS languages & frameworks) into L4 sub-components using Databricks docs. 

## Guidance per capsule
- **Monitoring**: Drift detection (KS/Wasserstein/PSI numeric, chi-square/TV categorical), Lakehouse Monitoring (snapshot/timeseries/inference profiles), Dashboards & alerts (Lakeview, SQL alerts, channels)
- **MLOps**: Asset Bundles (jobs/pipelines/models/experiments), Lakeflow Jobs (triggers, task types, repair runs), CI/CD (GitHub Actions, Azure DevOps, bundle validate/deploy)
- **Languages**: Keep existing nested children (already present for Python Ecosystem, Deep Learning Frameworks)

## Attempt 1: Research & Decomposition

### Capsule 1: Monitoring & evaluation
- **Inference Tables**: ATOMIC (payload logging, no further decomposition docs found)
- **Data Profiling (Lakehouse Monitoring)**: Decomposing into snapshot/timeseries/inference profiles
- **Drift Detection**: Decomposing into numeric tests (KS, Wasserstein, PSI) and categorical tests (chi-square, TV, JS)
- **Anomaly Detection**: ATOMIC (two internal sub-concepts: freshness, completeness - but no separate configuration needed)
- **Custom Metrics**: Decomposing into aggregate, derived, and drift metric types
- **Monitoring Dashboards & Alerts**: Decomposing into Lakeview dashboards, SQL alerts, notification channels
- **MLflow Evaluation (LLM Judges)**: ATOMIC (8 judges listed, but act as cohesive judge suite - no separate setup)
- **Production Monitoring**: ATOMIC (composed of evaluation on traffic + human feedback, integrated flow)

### Capsule 2: MLOps & CI/CD
- **MLOps Stacks**: ATOMIC (template reference, not a configurable component tree)
- **Declarative Automation Bundles (DABs)**: Decomposing into resource types (jobs, pipelines, models, experiments, endpoints, permissions)
- **Lakeflow Jobs**: ATOMIC (DAG orchestration primitive, triggers handled separately)
- **Job Triggers**: Decomposing into trigger types (cron, Delta, file, model-registry, API-triggered)
- **Lakeflow Pipelines**: Decomposing into SQL and Python declarative modes with policy handling
- **Git Integration & Repos**: ATOMIC (Git primitive, no sub-modes)
- **CI/CD with GitHub Actions & Azure DevOps**: ATOMIC (provider-level orchestration, not decomposable into Databricks components)
- **Terraform Support**: ATOMIC (Provider-level IaC tool)

### Capsule 3: DS languages & frameworks
- **Python Ecosystem**: KEEP existing children (pandas, scikit-learn, XGBoost, LightGBM, statsmodels)
- **R Support**: ATOMIC (single multi-language runtime feature)
- **PySpark**: ATOMIC (core Spark compute engine)
- **Spark MLlib**: ATOMIC (distributed ML library as cohesive unit)
- **Ray**: ATOMIC (distributed computing framework)
- **Deep Learning Frameworks**: KEEP existing children (PyTorch, TensorFlow)
- **pandas API on Spark**: ATOMIC (wrapper layer over Spark DataFrames)
- **Spark NLP**: ATOMIC (third-party community library, single unit)

## Final Results

### Capsule 1: Monitoring & evaluation
**Features that gained L4 children**: 5
- Data Profiling → snapshot/timeseries/inference profiles (3 L4)
- Drift Detection → numeric tests/categorical tests (2 L4)
- Custom Metrics → aggregate/derived/drift (3 L4)
- Monitoring Dashboards & Alerts → Lakeview/SQL alerts/channels (3 L4)
- Total L4 children: 11

**Atomic features (no decomposition)**: 4
- Inference Tables (payload logging feature)
- Anomaly Detection (integrated freshness + completeness)
- MLflow Evaluation (cohesive 8-judge suite)
- Production Monitoring (integrated evaluation + human feedback)

### Capsule 2: MLOps & CI/CD
**Features that gained L4 children**: 3
- Declarative Automation Bundles → jobs/pipelines/models/experiments/endpoints/permissions (6 L4)
- Job Triggers → cron/Delta/file/model-registry/continuous/API (6 L4)
- Lakeflow Pipelines → SQL/Python modes + policies (3 L4)
- Total L4 children: 15

**Atomic features (no decomposition)**: 5
- MLOps Stacks (template reference)
- Lakeflow Jobs (primitive orchestrator)
- Git Integration & Repos (Git primitive)
- CI/CD with GitHub Actions & Azure DevOps (provider-level)
- Terraform Support (provider-level IaC)

### Capsule 3: DS languages & frameworks
**Features that gained L4 children**: 0 (already have nested or are atomic)
- Python Ecosystem: kept existing 5 children (pandas, scikit-learn, XGBoost, LightGBM, statsmodels)
- Deep Learning Frameworks: kept existing 2 children (PyTorch, TensorFlow)
- Total L4 children preserved: 7

**Atomic features (no decomposition)**: 6
- R Support (single language runtime)
- PySpark (core compute engine)
- Spark MLlib (distributed ML library)
- Ray (framework)
- pandas API on Spark (wrapper layer)
- Spark NLP (third-party library)

## Output
✓ JSON output written to `/Users/mehdi.lamrani/code/Report/AmadeusAI/run/ds-deep/members-d.json`
✓ All doc references preserved and grounded
✓ Existing nested children kept (Python Ecosystem, Deep Learning Frameworks)
