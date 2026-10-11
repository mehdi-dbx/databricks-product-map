# Internal decks for the AI and DS ecosystem trees

<!-- md-only -->
Collected 2026-10-08 with a 6-agent swarm. Audit trail is in `.swarm/deck-hunt/` (journals and `out-H*.md`).
Sources: Google Drive and Confluence. Glean and Sage were unavailable during the run.

All Drive files were checked by the orchestrator (file exists, owner, last modified, size). The Confluence links were not checked.
On 2026-10-09, documents from DAIS 2025, documents more than 18 months old (by update date, then by creation date), documents from 2024 or before, and 4 borderline cases were moved to the Deprecated section at the end.
Data Science With Databricks is kept despite its 2024 creation date: the original is maintained (updated 2026-02-11). It replaces the copy listed before.
Mosaic AI - System Architecture: the Poste Italiane copy (work in progress of 2025-10-16) is replaced by the Architecture SME version of 2026-02-25. The Confluence references (not decks) are in the Deprecated section.
Owner, dates and size come from Drive metadata, not from the agents' reports. Earlier slide counts reported by the agents were replaced: one of them was wrong.

Blocks between md-only markers (these notes, the Flags note, the per-theme gap lines, Gaps, Product changes, Deprecated) are not shown in the app.
<!-- /md-only -->

- **Created** is the Drive creation date. It reflects the age of the content better than **Updated**, which often records minor edits.
- **Size** is the Drive file size (decimal KB / MB).
- **Pages** is the slide count from the Google Slides API, for all 14 Google Slides decks. The PDF is not counted (it would need a download).

<!-- md-only -->
Flags (used in the Deprecated section):
- **copy** — the file is owned by you (Mehdi). It is a copy, not the canonical source. The original author is named when the content gives it. For a copy, **Created** is the date the copy was made.
<!-- /md-only -->

## Top picks (start here)

| Theme | Deck | Owner | Created | Updated | Level | Size | Pages | What it covers |
|---|---|---|---|---|---|---|---|---|
| Agent Bricks | [Agent Bricks — L300 Pitch Slides](https://docs.google.com/presentation/d/1yHFQN3ZD7PWDnpEInf8nhiToChVn_g5XfTlY98Ls58U) | Sirui Sun | 2026-08-02 | 2026-10-05 | L300 | 35.0 MB | 60 | Agent Bricks positioning, capabilities, roadmap and the competitive landscape. |
| Agent Bricks | [Agentbricks Roadshow (go/airoadshow)](https://docs.google.com/presentation/d/1zYbz4UnikZ1yFgBPWZzfwEaQG3hSKpR8UjbhS3cmaBM) | Field Engineering | 2026-06-18 | 2026-10-06 | L200–300 | 111.5 MB | 225 | Platform vision, multi-agent patterns, Genie integration, use cases and workshop modules. |
| Genie Agents | [[Customer-facing] Knowledge Assistant & Supervisor Agent updates](https://docs.google.com/presentation/d/1QYbJUGDqzon9NQmK7ZPAA09O26XG-tb3oJse6Bcf-ko) | Elise Gonzales | 2026-08-24 | 2026-10-01 | L200–300 | 21.5 MB | 13 | The move from KA/SA to Genie Agents, the deprecation timeline and the upgrade paths. |
| MLflow | [MLFlow 3.0 (L100-L200) Pitch Deck](https://docs.google.com/presentation/d/1YmdmOd7LCg0c7lH_8LoeQCPKuLuYVkW4L1adkXEjoJA) | Puneet Jain | 2025-06-12 | 2026-10-01 | L100–200 | 84.2 MB | 56 | The MLflow 3.0 release: tracking, registry, and the GenAI features. It is the most recent MLflow pitch. |
| Genie | [Genie benchmarks](https://docs.google.com/presentation/d/1luYXYZXzb5ut1ebZIMtf6r8h8a9m7AVDTEl4FbIApSY) | Samuel Westley (PM) | 2026-09-29 | 2026-09-29 | L200–300 | 32.6 MB | 25 | Compares Genie with Claude Code, ChatGPT Enterprise and Gemini on 401 internal tasks. |
| DS lifecycle | [Data Science With Databricks](https://docs.google.com/presentation/d/1p-lb7UxBJLcrAIqQ6sIxsyI5-li-Fpy4hqYDUkHCoBI) | Rohit Dashora | 2024-05-21 | 2026-02-11 | L100–300 | 86.6 MB | 132 | The full DS lifecycle: Feature Store, AutoML, MLflow, Registry, Serving, Monitoring and Asset Bundles. |

## By theme

### AI Platform / ML lifecycle

| Theme | Deck | Owner | Created | Updated | Level | Size | Pages | What it covers |
|---|---|---|---|---|---|---|---|---|
| MLflow | [MLFlow 3.0 (L100-L200) Pitch Deck](https://docs.google.com/presentation/d/1YmdmOd7LCg0c7lH_8LoeQCPKuLuYVkW4L1adkXEjoJA) | Puneet Jain | 2025-06-12 | 2026-10-01 | L100–200 | 84.2 MB | 56 | The MLflow 3.0 release: tracking, registry, and the GenAI features. It is the most recent MLflow pitch. |
| AI architecture | [Mosaic AI - System Architecture 2026-02-25](https://docs.google.com/presentation/d/1uzSDh3addpxvvavUb_aYRKSCKlRWCS6N3rBE5DTf_PU) | Architecture SME | 2026-04-13 | 2026-09-23 | L300 | 5.3 MB | 74 | Reference architectures for agents, MCP and agent authentication, MLflow 3, Model Serving, AI Gateway, monitoring, Vector Search and Feature Store. The annex has L100 and L200 architecture patterns. |

<!-- md-only -->
No recent deck was found for **AutoML**, **AI Search / Vector Search** or **fine-tuning**.
<!-- /md-only -->

### Agents / Agent Bricks

| Theme | Deck | Owner | Created | Updated | Level | Size | Pages | What it covers |
|---|---|---|---|---|---|---|---|---|
| Agent Bricks | [Agent Bricks — L300 Pitch Slides](https://docs.google.com/presentation/d/1yHFQN3ZD7PWDnpEInf8nhiToChVn_g5XfTlY98Ls58U) | Sirui Sun | 2026-08-02 | 2026-10-05 | L300 | 35.0 MB | 60 | Agent Bricks positioning, capabilities, roadmap and the competitive landscape. |
| Agent Bricks | [Agentbricks Roadshow](https://docs.google.com/presentation/d/1zYbz4UnikZ1yFgBPWZzfwEaQG3hSKpR8UjbhS3cmaBM) | Field Engineering | 2026-06-18 | 2026-10-06 | L200–300 | 111.5 MB | 225 | Platform vision, multi-agent patterns, Genie integration, use cases and workshop modules. |
| Knowledge Assistant | [[SEMEA] Agent Bricks - Knowledge Assistant Workshop](https://docs.google.com/presentation/d/1nzunOxTG68OgOkrSE8QSD1_uctXsI9LH6dzXj4LGoBc) | Nereida Agüera López | 2026-04-27 | 2026-05-08 | L200–300 | 68.8 MB | 59 | A hands-on workshop for building a Knowledge Assistant. |
| Agents market | [State of AI Agents 2026](https://drive.google.com/file/d/1kRdR35IvOpFOv_cLLLpML6_BhrX971NS/view) (PDF) | Sidhtara Tep | 2026-02-02 | 2026-03-04 | L200 | 7.7 MB | — | A market report. It is the only source found that covers Omnigent and managed memory. |

<!-- md-only -->
No deck was found for **Databricks Sandbox**.
<!-- /md-only -->

<!-- md-only -->
### Governance for AI, Foundation Models, MCP

No standalone deck was found for **Review Apps** or **Foundation Model APIs**.
<!-- /md-only -->

### Genie / AI/BI and Developer productivity

| Theme | Deck | Owner | Created | Updated | Level | Size | Pages | What it covers |
|---|---|---|---|---|---|---|---|---|
| Genie | [Genie benchmarks](https://docs.google.com/presentation/d/1luYXYZXzb5ut1ebZIMtf6r8h8a9m7AVDTEl4FbIApSY) | Samuel Westley | 2026-09-29 | 2026-09-29 | L200–300 | 32.6 MB | 25 | Compares Genie with Claude Code, ChatGPT Enterprise and Gemini on 401 internal tasks. |
| Genie Agents | [[Customer-facing] KA & Supervisor Agent updates](https://docs.google.com/presentation/d/1QYbJUGDqzon9NQmK7ZPAA09O26XG-tb3oJse6Bcf-ko) | Elise Gonzales | 2026-08-24 | 2026-10-01 | L200–300 | 21.5 MB | 13 | The move from KA/SA to Genie Agents, the deprecation timeline and the upgrade paths. |
| Genie One | [Claude Desktop vs. Genie One — When to Use Which](https://docs.google.com/presentation/d/1auJrMVrBVXzHcaEiAnY3w2afVy2FNvz76a009bqbfHs) | Parastou Eslami | 2026-05-29 | 2026-06-17 | L200 | 6.2 MB | 13 | When to use each one and how to use them together. |
| Agentic applications | [How to set up an Agentic Applications workshop](https://docs.google.com/presentation/d/1qzWNKqEJogGPmiwdNrmm-_nVIc4gXU3yELKcmWb_aRU) | Stef Creemers | 2025-12-04 | 2026-07-01 | L200–300 | 35.3 MB | 66 | Agent architecture, a bootcamp flow and customer stories (Block, A2go, Real Chemistry). |
| Genie Ontology | [UPS - Ontology Integration with Genie](https://docs.google.com/presentation/d/1Hdnb-RQYSLgia-EeILzrNDL6poPYPmzvVQjyw3hlr-k) | Abhijeet Rao | 2026-03-30 | 2026-04-16 | L300+ | 7.0 MB | 22 | A customer case on Genie with an ontology, across BigQuery and Databricks. |

<!-- md-only -->
No deck was found for **AI/BI Dashboards strategy**, **App Spaces** or **AI Dev Kit / Genie Code**.
<!-- /md-only -->

### Data foundation, Real-time, Domain-specific

| Theme | Deck | Owner | Created | Updated | Level | Size | Pages | What it covers |
|---|---|---|---|---|---|---|---|---|
| Lakeflow | [Lakeflow Connect Tech Deck - L200](https://docs.google.com/presentation/d/1xiUXDS6x6aHv547-daQKBhvoOidHy_eVxdC8qdiHQxs) | Chad Macumber | 2025-11-15 | 2025-11-15 | L200 | 22.7 MB | 55 | Ingestion connectors, CDC, schema evolution and Enzyme. The file title says "Copy of", but Chad owns it. |
| Lakebase | [Databricks Lakebase](https://docs.google.com/presentation/d/1Qp70jDM4mn1zVeOwSGIKg9czJzZzSSJLIK8pZB11-BA) | Jacob Kranzler | 2025-08-06 | 2025-08-13 | L200 | 17.6 MB | 30 | Serverless Postgres use cases, performance figures, pricing and the roadmap. Predates Lakebase GA and Lakebase Search. |
| Data governance | [Data & AI Governance - Full deck](https://docs.google.com/presentation/d/14qbxrxi3Xi0HL7Tzzkp6PtNuQ3jFzRiXAm57XI7erx4) | Prashant Upadhyay | 2026-08-03 | 2026-08-03 | L200 | 3.6 MB | 88 | Classification, profiling, monitoring, anomaly detection and compliance. |

<!-- md-only -->
No deck was found for **Predictive Optimization** (Enzyme only appears inside the Lakeflow Connect deck), **LTAP**, **Lakehouse//RT**, **CustomerLake** or **Lakewatch**.
<!-- /md-only -->

### DS lifecycle (DS tree)

| Theme | Deck | Owner | Created | Updated | Level | Size | Pages | What it covers |
|---|---|---|---|---|---|---|---|---|
| DS lifecycle | [Data Science With Databricks](https://docs.google.com/presentation/d/1p-lb7UxBJLcrAIqQ6sIxsyI5-li-Fpy4hqYDUkHCoBI) | Rohit Dashora | 2024-05-21 | 2026-02-11 | L100–300 | 86.6 MB | 132 | The full DS lifecycle: Feature Store, AutoML, MLflow, Registry, Serving, Monitoring and Asset Bundles. |

<!-- md-only -->
## Gaps (no deck met the bar)

| Theme | Notes |
|---|---|
| Unity Catalog | Nothing recent found |
| MCP | Nothing recent found |
| Agent evaluation | Nothing recent found |
| Lakehouse / Delta Lake | Nothing recent found |
| Feature Store | Only inside Data Science With Databricks |
| AutoML | Nothing recent found |
| AI Search / Vector Search | Nothing recent found |
| Fine-tuning | Nothing recent found |
| Databricks Sandbox | Nothing found |
| Review Apps | Nothing recent found |
| Foundation Model APIs | Nothing recent found |
| AI/BI Dashboards strategy | Nothing recent found |
| App Spaces | Nothing found |
| AI Dev Kit / Genie Code | Nothing found |
| Predictive Optimization | Enzyme only inside the Lakeflow Connect deck |
| LTAP | Nothing found |
| Lakehouse//RT | Nothing found |
| CustomerLake | Nothing found |
| Lakewatch | Nothing found |

A second run with Glean and Sage available should target these.

## Product changes surfaced during the hunt

| Theme | Change | Source | Status in the app |
|---|---|---|---|
| Agent Bricks | Agent Bricks is split into Agent Platform (pro-code) and Genie (no-code). The Supervisor API is deprecated. | Slack thread from Scott McKean | Not applied to the trees |
| Genie Agents | Knowledge Assistant and Supervisor Agent move to Genie Agents, with a deprecation timeline starting Oct 2026. | Elise Gonzales deck | Stated in the Story (chapters 5 and 8). Capsule placement in the AI tree not changed yet |

## Deprecated (not shown in the app)

Documents removed from the list, kept here for reference. The app build skips this section.

| Theme | Deck | Owner | Created | Updated | Level | Size | Pages | Reason |
|---|---|---|---|---|---|---|---|---|
| Unity Catalog | [Unity Catalog L100 Pitch (go/pitchuc)](https://docs.google.com/presentation/d/18KvjnLJa8_9G7KvKvajtjNUhDLo8c1VL3i2KAgZv1cg) | Ryan Lippert | 2023-03-08 | 2026-08-10 | L100 | 46.3 MB | 47 | Created in 2024 or before |
| Lakehouse | [Databricks Lakehouse Fundamentals](https://docs.google.com/presentation/d/1J9_ZMJ9JlUH9erPxSMbnmltX6_qoq7R4UIgjCJcEvng) | Astrid Ng | 2024-01-16 | 2025-06-03 | L100 | 242 KB | 122 | Created in 2024 or before |
| Agent evaluation | [L200: Agent Framework & Agent Evaluation](https://docs.google.com/presentation/d/1nGHSov7O4Y9bTi20yfrAqcy4DVd7YwNvfVPobt7JFxI) | Craig Wiley | 2024-10-31 | 2025-09-17 | L200 | 170.9 MB | 51 | Created in 2024 or before |
| Agents | [[FieldKit] Mosaic AI Agents](https://docs.google.com/presentation/d/19yDn0cpMSs0-GxZk-zG4WwzkJ8tbcKnfEPjPcCFFogM) | Ehsan Olfat | 2025-02-18 | 2026-07-08 | L200–300 | 23.9 MB | 32 | Created more than 18 months ago |
| Genie and AI/BI APIs | [ISV Partner Integration Guide for AI/BI (Genie + Dashboards)](https://docs.google.com/document/d/1jsQzZwDrZHTdeF2s30QiSSSfeyi6ArZZiyPZnmAUPe0) (doc) | Prasad Kona | 2025-03-28 | 2025-06-17 | L300 | 57 KB | — | Created more than 18 months ago |
| MCP | [MCP <> Databricks Mosaic AI FAQ](https://docs.google.com/document/d/1gn9WLpsFx7zQfDYG-ZQ3eBnY6QDW1zkSWuHsyXY00Ts) (doc) | Sid Murching | 2025-04-07 | 2026-03-27 | — | 41 KB | — | Created more than 18 months ago |
| DS/ML platform | [[Field] Databricks Overview for Data Science and ML](https://docs.google.com/presentation/d/1NugPRilivLHJsBUwy53HdenHUj_yvpu5bRRMFhWESuI) | DS/ML platform | — | Joseph Bradley | 2025-01-27 | L100–300 | 73.1 MB | Updated more than 18 months ago |
| Feature Store | [Databricks ML: Feature Store](https://docs.google.com/presentation/d/1kFr-a9YhRKMSzyN7EsOD7xW8ARdruUGHkKjklS4EBs8) | Will Block | — | 2022-08-23 | — | 9.2 MB | 46 | Updated more than 18 months ago |
| Multi-agent | [Building Multi-Agent Systems With Mosaic AI (DAIS25)](https://drive.google.com/file/d/19vxkVEpWST4i5KEoRy4oHZ-__sZ_wbDi/view) **ext** | DAIS 2025 session | — | 2025-06-16 | L300 | 3.2 MB | — | DAIS 2025 session |
| MCP | [Building Agents with Mosaic AI and MCP (DAIS25)](https://drive.google.com/file/d/1XZHIlA3EwPFPn4aDP74oibpNExvKTzxu/view) **ext** | DAIS 2025 session | — | 2025-06-16 | L300 | 1.3 MB | — | DAIS 2025 session |
| AI security | [Databricks AI Security Framework (DASF) - Selection](https://docs.google.com/presentation/d/1jQ_4m4_ddYxZdwx7XRR_Cq60ilaEgTmUCs3JQBlQmGc) **copy** | you | — | 2025-02-19 | Executive | 13.1 MB | 12 | Updated more than 18 months ago |
| Agent evaluation | [GenAI Evaluation and Governance (GenAI-As-03)](https://docs.google.com/presentation/d/1JDE5kmYalU0aeSnJEZWrDSh8l8xCi7QVaGS59YA6lKs) **copy** | Academy course | — | 2024-10-23 | — | 15.0 MB | 86 | Updated in 2024 |
| GenAI deployment | [GenAI Deployment and Monitoring (GenAI-As-04)](https://docs.google.com/presentation/d/1hYAMWLip8zzbZ8dgCY6he9Or2B208Q312CrDDo9yz6E) **copy** | Academy course | — | 2024-10-23 | — | 19.8 MB | 97 | Updated in 2024 |
| Databricks Apps | [Level Up \| Databricks Apps [L300]](https://docs.google.com/presentation/d/1PxL-RXgzqZQ5gE3tUnIrVbQEZHEHKu4_RR4kthHcvic) **copy** | you (content: Giran Moodley, Ivan Trusov) | — | 2025-01-20 | L300 | 45.7 MB | 71 | Updated more than 18 months ago |
| MLOps | [MLOps on Databricks](https://docs.google.com/presentation/d/1NXAQNb2ZRcPxHM9WzLnW-hZixnd-BxLqCmgTrcOTrQo) | Salman Ali | — | 2025-01-27 | L200–300 | 7.5 MB | 63 | Updated more than 18 months ago |
| MLOps | [ML-in-Production-EN](https://docs.google.com/presentation/d/1xSVnUxXShOzwSJfOx3UHWkzvaKGx0_dpOV0mB3lf0sM) **copy** | course material | — | 2025-02-13 | L200–300 | 11.3 MB | 106 | Updated more than 18 months ago |
| Data prep | [M1 - Data Preparation for Machine Learning](https://docs.google.com/presentation/d/1xRcGl_zGYL9T2FSnjU8VUBn5E-qd92qNaWqGqdgbIPo) **copy** | Academy | — | 2025-02-14 | L100–200 | 8.8 MB | 31 | Updated more than 18 months ago |
| GenAI | [GenAI on Databricks L200 Tech Deck](https://docs.google.com/presentation/d/18q6e7yl1ldXtuvP2A2FgUm2vdrolh5We34Oca_RESwI) **copy** | you | — | 2025-02-17 | L200 | 48.1 MB | 69 | Updated more than 18 months ago |
| Lakeflow | [Lakeflow DLT March 2025 update](https://docs.google.com/presentation/d/1LcbZOnhLFWBq60Ofot_heETpRxyFnoq1h5XPF-b9pH4) | Eliot Knudsen (PM) | — | 2025-04-25 | — | 14.1 MB | 50 | Borderline: updated 16 days inside the 18-month limit |
| Unity Gateway | [Product Deck: AI Gateway](https://docs.google.com/presentation/d/13FOrjaFbw8ApYmvl2sKg2cjxWiajglNE5RNVG-kK9qM) **copy** **internal** | you | — | 2025-05-20 | — | 5.6 MB | 34 | Borderline: predates the Unity Gateway rename |
| Agents | [Deep Dive: Production-Ready AI Agents With Agent Bricks](https://drive.google.com/file/d/1qxkSDKSjrmCRJ_8ciCdMoJFc2q7z7QcZ/view) **ext** | event vendor | — | 2025-10-21 | L300 | 4.3 MB | — | Borderline: event vendor file, event not identified |
| Feature Store | [Feature Store overview](https://docs.google.com/presentation/d/1Fa6Emvm4x4wY5MI8QiCg2n9x_VGF9w2A0awAXYJFmLs) | Venkata Wunnava | — | 2025-11-06 | L200–300 | 9.5 MB | 49 | Borderline: created in 2023 |
| DS lifecycle | [Data Science With Databricks](https://docs.google.com/presentation/d/1Hkh7g4iiNK4kQ41WHLC59TJxi_BP37DgvuL_ZnYMS8A) **copy** | you (content: Rohit Dashora) | 2025-07-16 | 2025-07-16 | L100–300 | 81.6 MB | 119 | Copy, replaced by the original (Rohit Dashora) |
| Model Serving | [Poste 6 Mosaic AI - System Architecture - wip 2025-10-16](https://docs.google.com/presentation/d/15kie8V3Nv-Ekm81ernaHwD_MQCGrohTjsMx3RyW4GLA) | Erni Durdevic | 2026-02-12 | 2026-02-12 | L300 | 4.1 MB | 74 | Customer copy (Poste Italiane) of the 2025-10-16 work in progress, replaced by the 2026-02-25 version |

### References (not decks)

| Theme | Reference (not a deck) | Where | Why it is useful | Reason |
|---|---|---|---|---|
| AI governance | [AI Governance hub (go/aigov)](https://databricks.atlassian.net/wiki/spaces/UN/pages/6676414532/) | Confluence | Tracks the Unity Catalog securables roadmap. Not material to present. | Not a deck |
| AI governance | [AI Governance: Resources](https://databricks.atlassian.net/wiki/spaces/UN/pages/6683951882/) | Confluence | Index of the AI governance design docs. Not material to present. | Not a deck |
| Agents on the lakehouse | [Agent on the Lakehouse SSA MVP](https://databricks.atlassian.net/wiki/spaces/FE/pages/6925255078/AEB+SSA+MVP+-+Agent+on+the+Lakehouse) | Confluence | 2026-10 program page, includes the Smartsheet case. | Not a deck |
| Lakeflow | [Spark Declarative Pipelines eng page](https://databricks.atlassian.net/wiki/spaces/UN/pages/881197796/Spark+Declarative+Pipelines+SDP+fka+DLT) | Confluence | Engineering reference for Lakeflow pipelines. | Not a deck |
<!-- /md-only -->
