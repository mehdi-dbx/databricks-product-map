# Deep Drill-Down: Model Serving & Model Registry (2 Capsules)

## Task
Deep doc-grounded drill-down on 2 Databricks DATA SCIENCE capsules:
1. Model Serving & batch inference
2. Model Registry & governance

Rules: REAL docs.databricks.com URLs only. ≥1 per capsule. 4-8 sub-features per capsule. Substantive notes. Log ATTEMPT/RESULT per search.

---

## Progress Log

### Capsule 1: Model Serving & batch inference

**ATTEMPT 1**: Search Databricks docs for Model Serving real-time endpoints, serverless, provisioned throughput patterns.
**RESULT**: Found https://docs.databricks.com/aws/en/machine-learning/model-serving main page. Real features:
- Real-time REST endpoints (>25K QPS, <50ms latency)
- Serverless auto-scaling compute
- Batch inference via ai_query (SQL function)
- Batch inference via Spark UDFs (custom code)
- Provisioned throughput for foundation models
- Triton serving (GPU batching, Beta)
- Foundation model hosting (Llama, Mistral, Qwen, Gemini)
- Custom models (Express deployments, MLflow-registered)

**ATTEMPT 2**: Search for feature-specific pages.
**RESULT**: Found:
- Express deployments: https://docs.databricks.com/aws/en/machine-learning/model-serving/express-deployments
- Triton serving: https://docs.databricks.com/aws/en/machine-learning/model-serving/serve-triton
- Feature serving: https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving
- Inference tables: https://docs.databricks.com/aws/en/machine-learning/model-serving/inference-tables
- Traffic splitting: https://docs.databricks.com/aws/en/machine-learning/model-serving/serve-multiple-models-to-serving-endpoint

**COUNT**: 8 substantive sub-features documented with real URLs. All grounded in GA or Beta features.

### Capsule 2: Model Registry & governance

**ATTEMPT 1**: Search for Model Registry, UC governance, versioning patterns.
**RESULT**: Found https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/ main page. Real features:
- Model versioning (immutable history, signatures required)
- Aliases (Champion, staging, prod promotion)
- Unity Catalog governance (permissions, auditing)
- Training data lineage (mlflow.log_input tracking)
- Model lineage visualization (Catalog Explorer)
- Tags & metadata management
- Cross-workspace sharing (UC metastore-based)

**ATTEMPT 2**: Search for governance-specific features.
**RESULT**: Found:
- Deployment jobs with approvals: https://docs.databricks.com/aws/en/mlflow/deployment-job (Public Preview)
- Webhooks (legacy): https://docs.databricks.com/aws/en/mlflow/model-registry-webhooks
- Permissions reference: https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects
- Lineage: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage

**COUNT**: 8 substantive sub-features documented with real URLs. 7 GA, 1 Public Preview (deployment jobs).

---

## Final Output

**JSON file**: `/Users/mehdi.lamrani/code/Report/AmadeusAI/run/ds-deep/c.json`

**Validation**: JSON structure validates and parses correctly.

### Capsule 1: Model Serving & batch inference
- **Sub-features**: 8
- **Substantive notes**: 8 (all grounded in docs)
- **URLs**: 2 main + referenced in notes
- **Status**: 7 GA, 1 Beta (Triton)

### Capsule 2: Model Registry & governance
- **Sub-features**: 8
- **Substantive notes**: 8 (all grounded in docs)
- **URLs**: 2 main + referenced in notes
- **Status**: 7 GA, 1 PuP (deployment jobs)

**Total**: 16 substantive sub-features across 2 capsules. All ≥4 features per capsule. No features <4. All documented with real docs.databricks.com URLs.

