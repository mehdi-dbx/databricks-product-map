# Agent H5 — Best Internal Decks/Docs
## Data foundation + Real-time + Domain-specific

**Hunt date:** 2026-10-08 | **Sources scanned:** Google Drive, Confluence | **Quality filter applied:** Dense, complete, customer-facing, recognized author, recent (2025-2026) | **Coverage themes:** Lakehouse/Delta Lake, Lakeflow, Lakebase, real-time/LTAP, data governance & agentic management

---

## TOP TIER — Ranked by density & coverage

### 1. Lakeflow Connect: Simple Ingestion Connectors (Tech Deck)
- **Link:** [1xiUXDS6x6aHv547-daQKBhvoOidHy_eVxdC8qdiHQxs](https://docs.google.com/presentation/d/1xiUXDS6x6aHv547-daQKBhvoOidHy_eVxdC8qdiHQxs)
- **Summary:** 55-slide technical deep-dive into Lakeflow data ingestion connectors (SaaS, databases, real-time, files). Covers architecture (managed ingestion pipelines, CDC, schema evolution), source-specific implementations (Salesforce, SQL Server, Workday, SFTP, GA4, query-based), performance benchmarks, monitoring, and Enzyme optimization. End-to-end medallion architecture integration with Unity Catalog governance.
- **Date:** Updated Nov 2025 (content through Jul 2025)
- **Author(s):** Chad Macumber (Solutions Architect)
- **Audience:** Data engineers, architects, technical sales engineers
- **Level:** L200 (technical)
- **Why it's a nugget:** Only comprehensive single-source reference for Lakeflow Connect (delta-tracked changes, cost models, incremental refresh strategies, database gateway architecture). Enzyme coverage unique in deck collection.

### 2. Agent on the Lakehouse MVP — SSA Program
- **Link:** [Confluence 6925255078](https://databricks.atlassian.net/wiki/spaces/FE/pages/6925255078/AEB+SSA+MVP+-+Agent+on+the+Lakehouse)
- **Summary:** Oct 2026 proposal for SSA program pairing data engineering + AI specialists to build production-grade agents on lakehouse. Real case study (Smartsheet: $0→$150K ARR in 30 days, 25s end-to-end latency). Tool data-access patterns (query-per-tool vs. materialized views vs. precomputed). Qualification criteria, execution roadmap, lessons learned (streaming cost, partner capability, scope drift). Links to end-to-end architecture doc.
- **Date:** Oct 7, 2026 (v4, pending SSA leadership review)
- **Author(s):** SSA leadership initiative; Smartsheet case study
- **Audience:** SSA, sales, customer success; implementation partners
- **Level:** L300 (program/business)
- **Why it's a nugget:** Only documented agentic data management program with production Smartsheet results + DoorDash/Arctic Wolf. Covers streaming, real-time data access, latency targets, cost gates. Directly addresses "agents on the lakehouse" theme and LTAP principles (latency targeting, tool data patterns).

### 3. Databricks Lakebase (Lakehouse Platform)
- **Link:** [1Qp70jDM4mn1zVeOwSGIKg9czJzZzSSJLIK8pZB11-BA](https://docs.google.com/presentation/d/1Qp70jDM4mn1zVeOwSGIKg9czJzZzSSJLIK8pZB11-BA)
- **Summary:** Lakebase serverless Postgres OLTP engine fully managed & integrated with Databricks. Covers use cases (online feature store, data serving, app state, analytics over transactional data), fully-compatible Postgres 16 with pgvector/PostGIS, point-in-time recovery, multi-AZ HA, performance specs (16GB memory @ 1CU: <10ms latency, 10K read QPS, 15K write rows/sec), pricing (DSU storage + DBU compute), sync from Delta tables, authentication (OAuth, Postgres native). FY2026 roadmap (read pools, disaster recovery, CMEK, scale to 2TB).
- **Date:** Updated Aug 2025 (Neon acquisition announcement, public preview targeting)
- **Author(s):** Jacob Kranzler (original deck); Drew Minkin (customer intros: Capital One, Corteva)
- **Audience:** Data engineers, architects, app developers, technical prospects
- **Level:** L200 (technical overview)
- **Why it's a nugget:** Only unified Lakebase deck; foundational for Lakebase Search + serverless Postgres positioning; comprehensive architecture diagram, cost model, real customer context (Capital One, Corteva, NFCU LTAP POC).

### 4. Databricks Lakehouse Fundamentals — Slide Deck
- **Link:** [1J9_ZMJ9JlUH9erPxSMbnmltX6_qoq7R4UIgjCJcEvng](https://docs.google.com/presentation/d/1J9_ZMJ9JlUH9erPxSMbnmltX6_qoq7R4UIgjCJcEvng)
- **Summary:** 122-slide foundational educational deck tracing data platform evolution (data warehouses → data lakes → lakehouse). Covers Delta Lake (ACID, schema evolution, time travel, unified streaming), Photon engine (80% TCO savings, 2x TPC-DS 1TB), Unity Catalog (fine-grained governance, 38x faster metadata, lineage, ABAC), Delta Sharing (open, cross-cloud), divided security model (control plane/data plane), serverless SQL. Supported workloads: data warehousing, engineering, streaming, ML. Comprehensive but pedagogical.
- **Date:** Jun 2025 (content current through 2025)
- **Author(s):** Astrid Ng (Solutions Architect)
- **Audience:** Data practitioners (analysts, engineers, scientists), prospects, partners
- **Level:** L100 (foundational)
- **Why it's a nugget:** Most complete recent reference for lakehouse architecture foundation, Delta Lake + Photon + Unity Catalog cohesion, real numbers (80% TCO, 38x metadata, 2x perf). Solves "what is a lakehouse" for customer audiences. Enzyme optimization patterns embedded in transformation section.

### 5. Spark Declarative Pipelines (SDP fka DLT) — Internal Engineering Reference
- **Link:** [Confluence 881197796](https://databricks.atlassian.net/wiki/spaces/UN/pages/881197796/Spark+Declarative+Pipelines+SDP+fka+DLT)
- **Summary:** Engineering team page for Lakeflow declarative pipelines (SDP). Mission: Simplify Production ETL. Team structure, components, aliases, roadmap links, design docs, biweekly updates, support channels. Recent update Apr 2026. Foundational for understanding Lakeflow technical stack.
- **Date:** Last updated Apr 8, 2026 (v56)
- **Author(s):** Michael Armbrust (Architect); Lakeflow team
- **Audience:** Databricks engineers, SA/technical teams using Lakeflow
- **Level:** L300 (engineering reference)
- **Why it's a nugget:** Official Lakeflow team reference; directs to design docs, roadmap, support; validates Lakeflow as production-grade; SDP/DLT terminology locked down. Links to on-call, flaky tests, onboarding, biweekly updates.

### 6. Unity Catalog L100 Pitch
- **Link:** [18KvjnLJa8_9G7KvKvajtjNUhDLo8c1VL3i2KAgZv1cg](https://docs.google.com/presentation/d/18KvjnLJa8_9G7KvKvajtjNUhDLo8c1VL3i2KAgZv1cg)
- **Summary:** Comprehensive Unity Catalog governance pitch. Covers unified governance model, fine-grained access (row/column/view level), attribute-based access control (ABAC), audit trail, data discovery UI, automated lineage, integration with existing tools. Core data management & governance layer of Lakehouse Platform.
- **Date:** Last modified Aug 10, 2026
- **Author(s):** Ryan Lippert (Solutions Architect)
- **Audience:** Data architects, governance teams, prospects
- **Level:** L100 (business/technical overview)
- **Why it's a nugget:** Most recent governance reference (Aug 2026); unified governance across all data/AI assets; ABAC + lineage + discovery are core to data foundation; paired with governance decks below.

### 7. Data & AI Governance — Full Deck
- **Link:** [14qbxrxi3Xi0HL7Tzzkp6PtNuQ3jFzRiXAm57XI7erx4](https://docs.google.com/presentation/d/14qbxrxi3Xi0HL7Tzzkp6PtNuQ3jFzRiXAm57XI7erx4)
- **Summary:** Full governance strategy deck covering data classification, profiling, monitoring, anomaly detection, compliance (SOC2, ISO 27001, HIPAA, GDPR), audit, access control, cost governance. Includes governance patterns, tools (Unity Catalog, system tables), real-world use cases.
- **Date:** Updated Aug 3, 2026
- **Author(s):** Prashant Upadhyay (Solutions Architect)
- **Audience:** Data architects, governance officers, compliance teams
- **Level:** L200 (technical)
- **Why it's a nugget:** Addresses "agentic data management (classification/profiling/monitoring)" theme head-on. Most recent governance deep-dive; covers anomaly detection, data quality monitoring, compliance; complements UC L100.

---

## SECONDARY — Quality coverage, narrower scope

### Lakeflow DLT March 2025 Update
- **Link:** [1LcbZOnhLFWBq60Ofot_heETpRxyFnoq1h5XPF-b9pH4](https://docs.google.com/presentation/d/1LcbZOnhLFWBq60Ofot_heETpRxyFnoq1h5XPF-b9pH4)
- **Date:** Apr 25, 2025
- **Author(s):** Eliot Knudsen (Product Manager)
- **Summary:** Delta Live Tables product update. Focused technical refresh on DLT capabilities, roadmap.
- **Why secondary:** Narrower scope than Lakeflow Connect; updated content in Lakehouse Fundamentals.

### Data Science With Databricks
- **Link:** [1Hkh7g4iiNK4kQ41WHLC59TJxi_BP37DgvuL_ZnYMS8A](https://docs.google.com/presentation/d/1Hkh7g4iiNK4kQ41WHLC59TJxi_BP37DgvuL_ZnYMS8A)
- **Date:** Updated Sep 4, 2025
- **Author(s):** Mehdi Lamrani (Solutions Architect)
- **Summary:** End-to-end data science workflow on Databricks lakehouse. Covers feature store, model serving, MLflow, monitoring.
- **Why secondary:** Strong on ML serving but less comprehensive on data foundation & real-time themes.

### GenAI on Databricks L200 Tech Deck
- **Link:** [18q6e7yl1ldXtuvP2A2FgUm2vdrolh5We34Oca_RESwI](https://docs.google.com/presentation/d/18q6e7yl1ldXtuvP2A2FgUm2vdrolh5We34Oca_RESwI)
- **Date:** Feb 17, 2025
- **Author(s):** Mehdi Lamrani (Solutions Architect)
- **Summary:** GenAI applications on Databricks. RAG, agents, governance, cost models.
- **Why secondary:** GenAI-focused; overlaps with Agent on Lakehouse MVP but lacks production case study depth.

---

## GAPS & NOTES

### Not found (or minimal coverage):
- **CustomerLake / Lakewatch** (domain-specific applications) — No public decks located; may be internal-only or pre-launch.
- **Predictive Optimization (Enzyme)** — Referenced in Lakeflow Connect (cost modeling, incremental materialized view refresh) and Lakehouse Fundamentals (materialized view optimization strategies); no standalone deck. Enzyme deeply embedded in Lakeflow Connect efficiency section.
- **LTAP (Lakehouse Transactional Analytic Processing)** — Covered implicitly in Agent on Lakehouse MVP (latency targeting, tool data patterns) and Lakebase LTAP POC reference (NFCU); no standalone strategic deck found.

### Quality observations:
- **Recent & current:** All 7 top-tier decks dated 2025-2026; reflect current platform state.
- **Author depth:** Mix of solutions architects, product managers, engineering leadership—no shallow or outdated content.
- **Completeness:** Each addresses multiple sub-themes within data foundation; no single deck covers all themes but layering (Lakehouse Fundamentals + Lakeflow Connect + Lakebase + Governance + Agent MVP) provides full picture.
- **Customer-facing:** Lakeflow Connect, Lakebase, Lakehouse Fundamentals, and Agent MVP all directly customer-applicable; governance decks for architect/compliance audiences.

---

## Summary

**7 nuggets ranked for customer value:**
1. Lakeflow Connect (ingestion architecture, performance, Enzyme)
2. Agent on Lakehouse MVP (agentic data management, real-time patterns, Smartsheet case study)
3. Databricks Lakebase (serverless Postgres, OLTP + analytics convergence, cost model)
4. Lakehouse Fundamentals (foundational reference, Delta Lake + Photon + UC, 2x perf numbers)
5. Spark Declarative Pipelines (Lakeflow engineering reference, roadmap links)
6. Unity Catalog L100 (governance model, ABAC, lineage, discovery)
7. Data & AI Governance (classification, profiling, monitoring, compliance)

**Coverage by theme:**
- ✓ Lakehouse / Delta Lake (Lakehouse Fundamentals, Lakeflow Connect)
- ✓ Lakeflow (Lakeflow Connect, SDP reference)
- ✓ Lakebase (Lakebase deck, Lakebase L100 + LTAP POC references)
- ✓ Real-time / LTAP (Agent on Lakehouse MVP, Lakebase latency specs)
- ✓ Agentic Data Management (Agent on Lakehouse MVP, Data Governance)
- ⚠ Predictive Optimization (Enzyme embedded in Lakeflow Connect; no standalone deck)
- ✗ CustomerLake / Lakewatch (not found)

---

*Agent H5 · 2026-10-08 · Sources: Google Drive (filtered for Databricks employees, recent, slides/docs), Confluence (FE/UN spaces)*
