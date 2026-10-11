# Agent H6 Findings: Classic DS/ML Lifecycle Decks on Databricks

## KEPT DECKS (4 total)

### 1. Data Science With Databricks
- **Link:** https://docs.google.com/presentation/d/1Hkh7g4iiNK4kQ41WHLC59TJxi_BP37DgvuL_ZnYMS8A
- **Summary:** Comprehensive pitch deck covering the full ML lifecycle on Databricks. Covers data platform (Delta Lake, Unity Catalog), end-to-end ML workflows (data collection through monitoring), Feature Store with online/offline serving, AutoML (glass-box), MLflow tracking & experiment management, Model Registry in UC, Model Serving with A/B testing support, Lakehouse Monitoring for data/model quality, Databricks Assistant, CI/CD via Asset Bundles, and Project Genie for democratized AI. Dense technical reference with architecture diagrams.
- **Date:** Sept 2025
- **Author(s):** Rohit Dashora, Sr. Delivery Solutions Architect
- **Audience:** Data scientists, ML engineers, enterprise architects
- **Level:** L100-L300 (pitch-to-technical)
- **Why it's a nugget:** CANONICAL end-to-end DSML lifecycle reference on Databricks. Covers all sub-themes: data prep/EDA (Feature Store section), MLflow tracking, AutoML, model serving, deployment patterns, governance (UC), and monitoring. Most comprehensive single source.

### 2. ML-in-Production-EN
- **Link:** https://docs.google.com/presentation/d/1xSVnUxXShOzwSJfOx3UHWkzvaKGx0_dpOV0mB3lf0sM
- **Summary:** Production-focused course deck on MLOps lifecycle. Covers MLOps definition (DevOps + DataOps + ModelOps), Feature Store with online/offline skew solutions, Delta Lake fundamentals, MLflow autologging and experiment tracking, model management with Model Registry, three deployment paradigms (deploy code/model/hybrid), Model Serving infrastructure, Lakehouse Monitoring for drift detection, and comprehensive CI/CD/testing strategies. Includes practical A/B testing framework and rollout strategies (shadow, rolling, blue-green, canary).
- **Date:** Feb 2025
- **Author(s):** Unknown (internal Databricks course material)
- **Audience:** ML engineers, MLOps practitioners
- **Level:** L200-L300 (technical-deep)
- **Why it's a nugget:** AUTHORITATIVE MLOps deployment reference. Strong on: Feature Store architecture, model registry workflows, deployment pattern trade-offs, monitoring/drift types, and A/B testing. Complements broader decks with deep MLOps specifics.

### 3. M1 - Data Preparation for Machine Learning
- **Link:** https://docs.google.com/presentation/d/1xRcGl_zGYL9T2FSnjU8VUBn5E-qd92qNaWqGqdgbIPo
- **Summary:** Official Databricks Academy L100 course module on data preparation for ML. Covers Databricks Data Intelligence Platform overview, Delta Lake features (ACID, time travel, schema evolution), Unity Catalog governance for ML assets, data ingestion/bronze-silver-gold architecture, EDA with built-in profiling tools, feature engineering, data preprocessing (missing data, encoding, standardization), and Feature Store integration. Includes labs for hands-on learning.
- **Date:** Feb 2025
- **Author(s):** Databricks Academy
- **Audience:** Data scientists, ML practitioners (foundational)
- **Level:** L100-L200 (introductory-intermediate)
- **Why it's a nugget:** OFFICIAL foundational curriculum on data prep lifecycle. Only deck focusing deeply on data quality, EDA tooling, and feature engineering workflows. Essential for data-centric ML best practices.

### 4. MLOps on Databricks
- **Link:** https://docs.google.com/presentation/d/1NXAQNb2ZRcPxHM9WzLnW-hZixnd-BxLqCmgTrcOTrQo
- **Summary:** Comprehensive MLOps architecture guide accompanying Big Book of MLOps V2. Covers MLOps fundamentals (why it matters, risk/efficiency), ML system components (data/code/models in dev/staging/prod), ML deployment patterns (deploy code vs. deploy model tradeoffs), Unity Catalog design decisions for ML (catalog/schema/table organization), Model Serving serverless deployment, Lakehouse Monitoring unified platform, and reference architecture. Includes design guidance for multi-environment governance.
- **Date:** Jan 2025
- **Author(s):** Salman Ali (with Databricks MLOps team)
- **Audience:** ML architects, MLOps engineers, enterprise teams
- **Level:** L200-L300 (architecture-strategic)
- **Why it's a nugget:** ARCHITECTURE & GOVERNANCE reference. Only deck with: deploy code vs. deploy model comparison, UC schema design patterns (bronze/silver/gold), environment semantics, and reference architecture for prod-ready MLOps. Essential for enterprise deployments.

---

## Coverage Summary

### Sub-themes Addressed:
- **Data Prep/EDA:** ✓ (M1 primary, DS-with-Databricks supplement)
- **Feature Store for DS:** ✓ (All 4 decks, strongest in ML-in-Production & M1)
- **MLflow Experiment Tracking:** ✓ (DS-with-Databricks, ML-in-Production, MLOps)
- **AutoML:** ✓ (DS-with-Databricks primary)
- **Distributed Training & GPU:** ✓ (DS-with-Databricks mentions ML Runtime)
- **Model Serving & Batch Inference:** ✓ (All 4, strongest in DS-with-Databricks & ML-in-Production)
- **Model Registry & Governance:** ✓ (All 4, strongest in ML-in-Production & MLOps)
- **Monitoring/Evaluation:** ✓ (All 4, Lakehouse Monitoring in all)
- **MLOps & CI/CD:** ✓ (All 4, strongest in ML-in-Production & MLOps)
- **Asset Bundles, MLOps Stacks:** ✓ (DS-with-Databricks & MLOps)

### Quality Assessment:
- All 4 are: Dense, complete, customer-facing, recent (Jan-Sept 2025), authored by recognized Databricks/team members
- No fragments or shallow one-pagers
- No GenAI focus (classic DSML only, as required)
- No stale content (all 2025 or recent 2024)
- No obvious duplicates

### Recommendation Ranking:
1. **Data Science With Databricks** — Most comprehensive entry point
2. **MLOps on Databricks** — Architecture & governance blueprint
3. **ML-in-Production-EN** — Deep MLOps/deployment specifics
4. **M1 - Data Preparation** — Foundational data lifecycle (academy-grade)

---

## Rejected/Not Pursued:
- GenAI-focused decks (intentionally filtered out per theme)
- Older decks (2023-early 2024) with potentially stale product features
- Customer-specific decks (e.g., Ahold Delhaize, Gucci) — valuable case studies but not canonical reference decks
- Additional MLOps variants (Kari Ross, Will Block decks 2023) — superseded by Salman Ali 2025 version
- One-slide references in Slack (not dense enough for this bar)

---

**Tally:** 4 kept | 0 shallow/stale rejected | 0 sub-theme gaps (all covered) | Hunt complete.
