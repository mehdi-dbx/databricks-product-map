# Data Science Ecosystem Tree — canonical contract (merge of 3 cartographies)

Merged from `run/ds-tree-public.md` (19 pillars/50+), `run/ds-tree-glean.md` (9/42+), `run/ds-tree-sage.md` (11/48).
Scope **1(a)**: classic DS / ML lifecycle; overlap with the AI tree is allowed (shared bricks reappear, framed for DS). We do NOT re-import the whole GenAI/agents tree — this stays DS-lifecycle-centric.

Confidence: ✅ confirmed (internal Glean / Sage corroborated) · 🟡 to-verify (public-only).

## 11 pillars → capsules (the skeleton the swarm will drill down)

1. **Notebooks & collaborative development** — Databricks Notebooks · Git folders (Repos) · Databricks Assistant (in-notebook) · Notebook visualizations & dashboards
2. **Data prep & EDA** — pandas API on Spark · Spark DataFrames · Data profiling / summary stats · Visualization in notebooks · Databricks SQL for EDA
3. **Feature engineering & Feature Store** — Feature Engineering in Unity Catalog · Feature Store · Feature Views (PuP) · Online Feature Store (Lakebase) · On-demand / point-in-time features
4. **Experiment tracking & model development (MLflow)** — MLflow Tracking · Experiments UI · Autologging · Runs/params/metrics/artifacts · MLflow Models
5. **AutoML** — Databricks AutoML (classification/regression/forecasting) · Glass-box generated notebooks · AutoML API
6. **Distributed training & GPU compute** — ML Runtime (GPU) · Spark MLlib · Ray on Databricks · TorchDistributor · DeepSpeed/Horovod · Serverless GPU (AI Runtime) · Distributed hyperparameter tuning (Hyperopt/Optuna)
7. **Model serving & batch inference** — Mosaic AI Model Serving (real-time) · Batch inference (ai_query / spark_udf) · Provisioned throughput · Serverless serving · Inference tables
8. **Model registry & lifecycle governance** — MLflow Model Registry in Unity Catalog · Versions & aliases (Champion/Challenger) · Model lineage · Deployment gates / webhooks
9. **Monitoring & evaluation** — Lakehouse Monitoring · Inference / quality monitoring · Drift detection · MLflow evaluation (DS metrics)
10. **MLOps & CI/CD** — MLOps Stacks · Databricks Asset Bundles (DABs) · CI/CD (GitHub Actions/Azure DevOps) · Workflows / Jobs for ML · Deployment pipelines
11. **DS languages, libraries & frameworks** — Python (pandas, scikit-learn, XGBoost, LightGBM) · R support · PySpark / Spark MLlib · Deep learning (PyTorch, TensorFlow) · Ray · pandas API on Spark

## Canonical decks / nuggets (for docs/deck fields)
- `dsml-l100200-pitch-deck-godsml` — DSML L100/200 canonical.
- `applied-ai-governance-production-patterns-reference-architecture` — governance.
- `databricks-comprehensive-training-3-days`, `mlops-on-databricks-end-to-end-manufacturing-tutorial`, `databricks-for-data-science-presentation-deck` (Sage).
- Internal: Classic ML L100/L200, Data Quality tech deck (Glean).

## Known gaps flagged by agents
Feature Store deep-dive, real-time serving patterns, author/PM org roles (resolve later via get_person), regional availability, pricing.
