# Data Science Capsules Deep Drill-Down (agent-ds-deep-b)
**Started:** 2026-10-07  
**Task:** Substantiate 3 DS capsules (MLflow, AutoML, Distributed training & GPU) with real docs URLs + 4-8 sub-features each.

---

## ATTEMPT 1: MLflow Search & Documentation Mining

**Query 1:** MLflow tracking autologging experiments evaluation model registry  
**Status:** ✓ COMPLETE

**Query 2:** AutoML classification regression forecasting serverless  
**Status:** ✓ COMPLETE

**Query 3:** Distributed training Ray Train TorchDistributor DeepSpeed GPU  
**Status:** ✓ COMPLETE

**Query 4:** MLflow prompt registry traces LLM judges custom scorers  
**Status:** ✓ COMPLETE

**Query 5:** AutoML glass-box SHAP feature selection data prep  
**Status:** ✓ COMPLETE

**Query 6:** Spark MLlib DeepSpeed multi-GPU  
**Status:** ✓ COMPLETE

**Query 7:** Ray Tune hyperparameter distributed trials  
**Status:** ✓ COMPLETE

**Query 8:** AI Runtime serverless GPU H100 A10 fine-tuning  
**Status:** ✓ COMPLETE

---

## FINDINGS LOG

### MLflow (8 sub-features)
- [x] Tracking: params/metrics/artifacts/runs; https://docs.databricks.com/aws/en/mlflow/tracking
- [x] Autologging: framework-specific capture (sklearn, XGBoost, TF, PyTorch, LightGBM); https://docs.databricks.com/gcp/en/mlflow/databricks-autologging
- [x] Experiments UI: organization, comparison, visualization; https://docs.databricks.com/aws/en/mlflow/experiments
- [x] Logged Models: first-class entities (v3.x); https://docs.databricks.com/aws/en/mlflow/logged-model
- [x] LLM Evaluation (judges): correctness, safety, groundedness, relevance; https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges
- [x] Custom Scorers: code-based deterministic checks; https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers
- [x] Prompt Registry: versioning, aliases, config co-storage; https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry
- [x] MLflow Traces: LLM calls, retrievals, tools, sub-agents; https://docs.databricks.com/aws/en/mlflow3/genai/tracing/overview

### AutoML (8 sub-features)
- [x] Classification: trees, forests, LR, XGBoost, LightGBM; https://docs.databricks.com/aws/en/machine-learning/automl/classification
- [x] Regression: trees, linear, XGBoost, LightGBM; https://docs.databricks.com/aws/en/machine-learning/automl/regression
- [x] Forecasting (classic): Prophet, Auto-ARIMA; https://docs.databricks.com/aws/en/machine-learning/automl/forecasting
- [x] Forecasting (serverless): Prophet, Auto-ARIMA, DeepAR; https://docs.databricks.com/aws/en/machine-learning/train-model/serverless-forecasting
- [x] Glass-box notebooks: editable trial code; https://docs.databricks.com/aws/en/machine-learning/automl/
- [x] SHAP Explainability: feature importance; https://docs.databricks.com/aws/en/machine-learning/automl/
- [x] Data Preparation: column selection, imputation, splits; https://docs.databricks.com/aws/en/machine-learning/automl/classification-data-prep
- [x] AutoML Python API: programmatic configuration; https://docs.databricks.com/aws/en/machine-learning/automl/automl-api-reference

### Distributed training & GPU (8 sub-features)
- [x] ML Runtime GPU: PyTorch 2.12.0, scikit-learn 1.7.2 pre-installed; https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml
- [x] AI Runtime (serverless GPU): 1×A10, 1×H100, 8×H100; https://docs.databricks.com/aws/en/machine-learning/ai-runtime/quickstart
- [x] Ray Train: framework-agnostic distributed orchestration; https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/
- [x] Ray Tune: distributed HPO with ASHA early stopping; https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/
- [x] TorchDistributor: Spark-based PyTorch launcher; https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/spark-pytorch-distributor
- [x] Spark MLlib: distributed classical ML (pyspark.ml); https://docs.databricks.com/aws/en/machine-learning/train-model/mllib
- [x] DeepSpeed: ZeRO sharding, optimizer partitioning; https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/deepspeed
- [x] @distributed API: serverless single-node DDP/FSDP; https://docs.databricks.com/aws/en/machine-learning/ai-runtime/distributed-training

---

## RETRIES & BACKOFFS
None needed; all searches yielded real, substantiated documentation.

**FINAL STATUS: SUCCESS - 24/24 sub-features substantiated with real URLs**
