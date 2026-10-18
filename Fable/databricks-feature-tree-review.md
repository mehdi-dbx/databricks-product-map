# Databricks AI & Data Science Feature Tree — Completeness Review

**Review date:** October 17, 2026
**Scope:** Sections 1 through 3.3, plus the visible stub of 3.4. The tree as received is cut off at `3.4 MLflow 3 → Models in`. Sections 3.4 onward (remaining MLflow, generative/agentic AI, Unity Gateway) were not reviewed. No "to verify" markers appear in the received portion, so list 4 confirms the status of the tree's own nodes instead.

**Primary source:** Databricks platform release notes index (`https://docs.databricks.com/aws/en/release-notes/product`, last updated Sep 11, 2026) and the monthly pages under `https://docs.databricks.com/aws/en/release-notes/product/2026/<month>`. Abbreviated below as `RN <month>`.

---

## 1. Missing features

| Feature | What it does | Belongs under | Source |
|---|---|---|---|
| Auto Loader | Incremental file ingestion from cloud storage. Now supports automatic type widening (Public Preview, Mar 25, 2026). | 1.2, before Lakeflow Connect (file-ingestion primitive) | RN March |
| Lakeflow Connect variants | Query-based connectors GA (May 2026); Community connectors Beta (May 2026); MySQL integrated CDC pipeline GA (Oct 15, 2026) — a single pipeline with no separate ingestion gateway. | 1.2 Lakeflow Connect — managed / query-based / community / integrated-CDC variants absent | RN May, RN October |
| Lakeflow Pipelines Editor | Authoring surface for Spark Declarative Pipelines. GA May 2026. | 1.2 Spark Declarative Pipelines (UI surface) | RN May |
| Real-time mode in Spark Declarative Pipelines | Low-latency streaming variant. Public Preview May 2026. | 1.2 Spark Declarative Pipelines (real-time variant) | RN May |
| Declarative Automation Bundles | Infrastructure-as-code / templates surface for jobs, pipelines, connectors. Renamed from Databricks Asset Bundles on Mar 16, 2026. | 3.1 Workspace, or a cross-cutting "access surfaces" node — it is the templates surface for nearly every leaf | RN March |
| Databricks CLI | GA May 2026. | Same as above (CLI surface) | RN May |
| Lakebase Autoscaling vs Provisioned | Since Mar 12, 2026 new Lakebase instances are created as Autoscaling projects (autoscaling compute, scale-to-zero, branching, instant restore). Provisioned instances are being upgraded automatically from June 2026. | 1.3 Lakebase — managed-variant split missing | `docs.databricks.com/aws/en/oltp/upgrade-to-autoscaling` |
| Synced tables / Lakehouse Sync | Synced tables serve lakehouse data through Lakebase. Lakehouse Sync (Lakebase tables → Delta/Iceberg) is Public Preview, Autoscaling only. | 1.3 Lakebase (the bidirectional link LTAP depends on) | `docs.databricks.com/aws/en/oltp/instance` |
| Transactions / multi-table transactions | `BEGIN ATOMIC … END` groups statements across tables; requires catalog commits (Public Preview Mar 9). Transactions GA July 2026. | 1.1 (Delta table feature) or 1.3 | RN March, RN July |
| Catalog commits + external access | Catalog commits GA (May). External writes to managed Delta tables GA and external access to views via Unity REST API GA (Oct 13). | 2.1 (access dimension: external-engine access) | RN May, RN October |
| Governed tags, tag automations, tag propagation | Governed tags GA (April); tag automations Beta (Aug); tag propagation uses lineage to apply a governed tag to derived tables and views (Beta, Oct 12). | 2.1 (policy dimension — ABAC depends on these) | RN April, RN August, RN October |
| Secrets in Unity Catalog | GA Aug 2026; external secrets Beta Sep 2026. | 2.1 | RN August, RN September |
| Access requests | Metastore-level access requests with inherited destination (Public Preview, Jun 22). | 2.1 (access dimension) | RN June |
| Cost dimension for Unity Catalog | Nothing in 2.x covers cost. Usage dashboard GA (Mar 18); Budgets GA (July); system tables (query history GA Sep; configurable retention Beta Sep). | New leaf or leaves under 2.1 (system tables, budgets, usage dashboard) | RN March, RN July, RN September |
| External lineage | Formerly Bring Your Own Lineage. GA Jun 8; Lakeflow Connect pipelines now record source lineage automatically. | 2.1 Lineage (variant) | RN June |
| SecureConnect | Share from storage behind a firewall without allowlisting recipients; also available for clean rooms. Public Preview June; GA Aug 2026. | 2.3 OpenSharing (variant) | RN June, RN August |
| Feature tables | Feature Store has two authoring strategies: Feature Views, and feature tables you populate yourself by writing to a Delta table. Feature tables remain the path for Delta Sharing, third-party online stores, or a GA-only authoring path. | 3.2 (code / self-managed variant alongside Feature Views) | `docs.databricks.com/aws/en/machine-learning/feature-store/` |
| Feature serving (endpoints + automatic lookup) | Feature Serving Endpoints serve features to external applications without a model; Model Serving looks up features from the online store at serving time. | 3.2, after Online Feature Stores | `docs.databricks.com/aws/en/oltp/projects/feature-store` |
| Stream Feature Views | Sub-second fresh features with direct writes from Real-time mode to the Online Feature Store. | 3.2 Feature Views (real-time variant) | Feature Store overview docs |
| Databricks Runtime for Machine Learning | Classic (non-serverless) training compute. DBR 19 ML GA July 2026; DBR 18 ML moved to LTS. | 3.3 (classic variant; 3.3 currently lists only serverless) | RN July |
| AI Runtime CLI (`air`) | Submit and manage distributed training on AI Runtime from a local machine (Beta, Jun 12). Custom Docker images for `air` workloads (Beta, Jun 29). | 3.3 (CLI surface) | RN June |
| Genie Code surfaces | Genie Code CLI — terminal coding agent using the Databricks CLI, model access via Unity Gateway (Beta, Oct 6). Full-page Genie Code GA (Aug); scheduled tasks GA (Sep); Genie Code as a Lakeflow Jobs task Beta (Aug); Genie Code for AI Runtime Public Preview (Aug). | 3.1 Genie Code — UI / CLI / jobs-task surfaces missing | RN October, RN August, RN September |
| Omnigent | Coding-agent meta-harness wrapping agents such as Claude Code and Codex with a web UI, shared sessions, policies, and deployment (Beta, Jun 17). | 3.1 next to Genie Code, or the agentic section | RN June |
| Agentic code converter | Converts T-SQL, Snowflake, Redshift, Oracle, BigQuery, Teradata SQL to Databricks SQL. GA for SQL target Oct 15. | 3.1 (Genie Code-powered) or 1.2 | RN October |
| Workspace "spaces" | "Organize your work with spaces" (Aug 2026). Detail page not opened — **not verified**. | 3.1 Workspace | RN August |
| Lakehouse Replay | Replays sampled read-only serverless workloads against upcoming runtime releases to catch regressions; no setup, not billed (Beta, Jun 10). | Borderline for an AI/DS tree; if kept, 1.4 | RN June |

Table-format features that may be too granular but reached GA in 2026: Iceberg v3 and managed/foreign Iceberg tables (May), Variant and Variant shredding (July), Parquet v2 (June), type widening (March).

---

## 2. Misplaced features

| Current node | Proposed node | Reason |
|---|---|---|
| 1.4 Data Quality Monitoring | 2.1 (observability dimension of Unity Catalog) | Databricks moved the data quality monitoring documentation from Data guides to the Data governance (Unity Catalog) chapter on Mar 12, 2026 (RN March). The tree's own UC rule asks for an observability dimension and this is it: anomaly-detection alerts in the DQM UI (Beta, Mar 19), health indicators in Catalog Explorer (Public Preview, Mar 13). |
| 1.3 LTAP (leaf) | Overview, or the parent/intro of 1.3 | Databricks' docs state LTAP is "an architecture, not a single feature," delivered through a set of Lakebase capabilities (`docs.databricks.com/aws/en/oltp/projects/ltap-overview`). The one-feature-per-leaf rule fails. Lakebase, synced tables and Lakehouse//RT are the features; LTAP is the frame around them. |
| 2.2 Discover (asset discovery page) | 2.1, or a separate "Discovery" node | Discover is a curated browsing experience across Databricks assets (RN October) — a surface, not a semantic definition. Weak flag: Databricks ships and announces it with domains, so adjacency is defensible. |
| 1.2 Zerobus Ingest (last) | 1.2, adjacent to Lakeflow Connect | Dependency ordering: Zerobus is an ingestion entry point (GA into streaming tables Aug; Public Preview into default storage Sep). Lakeflow Jobs (orchestration) should sit last. |
| 3.3 Serverless GPU (leaf) | Fold into the section title; keep accelerator types or the SDK as leaves | AI Runtime *is* GPU support on serverless compute (RN March), so the leaf duplicates its parent. Concrete sub-features: 1xH100 accelerator (Beta, April) and the AI Runtime SDK (see list 3). |

Ordering inside 3.2 (Feature Views → Online Feature Stores) is correct for author → serve. Online Feature Stores are provisioned as Lakebase Autoscaling projects, so the dependency on 1.3 is satisfied.

---

## 3. Legacy, renamed or removed

| Node in tree | Current name / replacement | Date | Source |
|---|---|---|---|
| 3.3 Serverless GPU (SDK side) | Databricks AI Runtime SDK (`databricks-sdk-air`) replaces the deprecated `serverless_gpu` package from GPU environment version 6. `gpus`/`gpu_type` renamed to `num_accelerators`/`accelerator_type`; old names end in version 7. | Oct 13, 2026 | RN October |
| 1.3 Lakebase | Lakebase Provisioned is the original offering; Lakebase Autoscaling is the current version and receives new feature development. | Default since Mar 12, 2026 | `docs.databricks.com/aws/en/oltp/instance` |
| 1.3 Lakehouse//RT | Not renamed, but canonical doc name is Lakehouse Real-Time (Lakehouse//RT): a serverless SQL warehouse type for sub-second reads. Beta. | Jun 30, 2026 | RN June |
| 2.3 OpenSharing | Correct — Delta Sharing became OpenSharing following the open-source release. Some later release notes still say "Delta Sharing." | Jun 10, 2026 | RN June |
| 2.1 Lineage | "Bring Your Own Lineage" is now External lineage. | Jun 8, 2026 | RN June |
| 3.1 Genie Code | Correct — Databricks Assistant became Genie Code; Agent mode GA (Mar 11). Chat/Agent mode selector removed Jun 29; Genie Code runs only in Agent mode. | Mar 11 / Jun 29, 2026 | RN March, RN June |
| 3.2 (implicit) | Workspace Feature Store is deprecated; the current product is Feature Store in Unity Catalog. | — | Feature Store overview docs |
| 3.2 Feature Views (API lineage) | `create_pipeline` is deprecated for Feature Views; use the materialized features API. Beta-era Feature Views need migration via `Feature.clone()`. | SDK 0.16.0 | `docs.databricks.com/aws/en/release-notes/feature-store/databricks-feature-store` |
| 2.3 Marketplace | Solution Accelerators are no longer a separate listing type; now categorized as apps or notebooks. | Jun 25, 2026 | RN June |
| (not in received portion) Databricks Asset Bundles | Declarative Automation Bundles | Mar 16, 2026 | RN March |

---

## 4. Status confirmation for tree nodes

No "to verify" markers were found in the received portion. Statuses of the tree's own nodes:

| Node | Confirmed status | Source |
|---|---|---|
| Lakeflow Designer | GA Jun 16, 2026 | RN June |
| Lakehouse//RT | Beta Jun 30, 2026 | RN June |
| LTAP | Announced at DAIS Jun 16, 2026; Lakebase is its foundation; architecture, not a feature | Databricks newsroom (`databricks.com/company/newsroom/press-releases/databricks-launches-ltap-first-lake-transactionalanalytical`) |
| Zerobus Ingest | GA into streaming tables (Aug); Public Preview into default storage (Sep) | RN index |
| RBAC | GA Aug 2026 | RN index |
| ABAC | GA April 2026; cross-engine ABAC GA Oct 1 | RN April, RN October |
| Data classification | GA April 2026 | RN index |
| Governance Hub | Beta July 2026; Tags page Beta Aug | RN index |
| Metric views | Window measures GA Oct 6; parameters Public Preview June | RN October, RN June |
| Domains, Discover | Both GA Oct 8, 2026 | RN October |
| Pages | Beta Aug 2026 | RN index |
| Clean Rooms | Shared output, JAR workloads, identity-resolution packaged rooms all GA Oct 13 | RN October |
| Feature Views | GA Oct 12 for batch, streaming and request-time data; compliance-profile workspaces mid-November | RN October |
| Online Feature Stores | Documented as current; GA status **not verified** (no 2026 release note found) | Feature Store docs |
| AI Runtime | Public Preview for single-node (Mar 19); distributed training API still Beta | RN March |
| Genie Code | Agent mode GA Mar 11; CLI Beta Oct 6 | RN March, RN October |

---

## Expected impact on the truncated sections (3.4 onward)

- Vector Search is now AI Search (Jun 1, 2026).
- AI Gateway (Beta, Feb) became Unity Gateway; GA Aug 2026.
- Genie Spaces became Genie Agents (July 2026).
- Knowledge Assistant and Supervisor Agent are legacy as of Oct 12, 2026 — Agent Bricks CLI for code, Genie Agents for no-code.
- MLflow `AgentServer`, `LongRunningAgentServer` and agents deployed to Model Serving are legacy (Oct 5, 2026), replaced by `DurableAgentServer` and Agent Runtime on Databricks Apps.
- MLflow trace storage in Unity Catalog GA (July); unified trace table Beta (Aug); managed agent memory and sessions Beta (Sep); agent memory pipelines Beta (Oct).
