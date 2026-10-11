# DS Capsules Deep Drill-Down Log

## Target Capsules
1. **Monitoring & evaluation**
2. **MLOps & CI/CD**
3. **DS languages & frameworks**

## Attempt 1: Initial Research (Oct 7, 2026)

### Capsule 1: Monitoring & evaluation

**Attempt 1.1 - Search Lakehouse Monitoring**
- Query: Lakehouse Monitoring data quality metrics drift detection
- Status: PENDING

**Attempt 1.2 - Search MLflow evaluation**
- Query: MLflow evaluation LLM judges scorers
- Status: PENDING

**Attempt 1.3 - Search inference profiling**
- Query: inference profiling model performance monitoring
- Status: PENDING

### Capsule 2: MLOps & CI/CD

**Attempt 2.1 - Search MLOps Stacks**
- Query: Databricks MLOps Stacks asset bundles DABs
- Status: PENDING

**Attempt 2.2 - Search Lakeflow Jobs**
- Query: Lakeflow Jobs workflows orchestration
- Status: PENDING

**Attempt 2.3 - Search CI/CD**
- Query: Databricks CI/CD GitHub Actions Azure DevOps
- Status: PENDING

### Capsule 3: DS languages & frameworks

**Attempt 3.1 - Search Python libraries**
- Query: Databricks Python ecosystem pandas scikit-learn XGBoost
- Status: PENDING

**Attempt 3.2 - Search Ray distributed**
- Query: Databricks Ray training tuning
- Status: PENDING

**Attempt 3.3 - Search PyTorch TensorFlow**
- Query: Databricks PyTorch deep learning frameworks
- Status: PENDING

## RESULTS - Attempt 1 Complete

### Capsule 1: Monitoring & evaluation ✓
- **Sub-features:** 8 (all with substantive notes)
- **Docs URLs:** 14 across capsule + children
- **Key features documented:**
  - Inference Tables (AI Gateway payload logging)
  - Data Profiling (quality metrics, snapshot/timeseries)
  - Drift Detection (KS test, Wasserstein, PSI, chi-square)
  - Anomaly Detection (freshness, completeness patterns)
  - Custom Metrics (aggregate, derived, drift types)
  - Monitoring Dashboards & Alerts (Lakeview + SQL alerts)
  - MLflow Evaluation (8 LLM judges)
  - Production Monitoring (sampled traffic + human feedback)

### Capsule 2: MLOps & CI/CD ✓
- **Sub-features:** 8 (all with substantive notes)
- **Docs URLs:** 18 across capsule + children
- **Key features documented:**
  - MLOps Stacks (reference templates + CI/CD workflows)
  - Declarative Automation Bundles (YAML IaC for ML)
  - Lakeflow Jobs (DAG orchestration, 1000 tasks)
  - Job Triggers (cron, Delta, file, model-registry, multi-trigger Beta)
  - Lakeflow Pipelines (declarative ETL + expectations)
  - Git Integration (Git Folders rebranded from Repos)
  - CI/CD with GitHub Actions & Azure DevOps
  - Terraform Support (account + workspace IaC)

### Capsule 3: DS languages & frameworks ✓
- **Sub-features:** 8 (+ 7 nested children for Python & Deep Learning)
- **Docs URLs:** 12 across capsule + children
- **Key features documented:**
  - Python Ecosystem (pandas 2.3.3, scikit-learn 1.7.2, XGBoost 3.2.0, LightGBM 4.6.0, statsmodels)
  - R Support (multi-language notebooks, SparkR deprecated, sparklyr recommended)
  - PySpark (distributed DataFrames, serverless/standard/dedicated support)
  - Spark MLlib (pyspark.ml distributed ML, collaborative filtering)
  - Ray (distributed training + hyperparameter tuning)
  - Deep Learning Frameworks (PyTorch 2.12.0 GA; TensorFlow legacy on Runtime 17.3 LTS)
  - pandas API on Spark (koalas evolution)
  - Spark NLP (community library by John Snow Labs)
- **Nested children preserved:**
  - Python Ecosystem: pandas, scikit-learn, XGBoost, LightGBM, statsmodels
  - Deep Learning: PyTorch, TensorFlow

## Status: COMPLETE ✓
All 3 capsules with ≥8 sub-features, all substantive notes grounded in docs.databricks.com.
Output: `/Users/mehdi.lamrani/code/Report/AmadeusAI/run/ds-deep/d.json` (validated).
