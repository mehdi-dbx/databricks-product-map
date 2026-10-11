# Agent H3 Output — Best Decks for AI Governance + Foundation Models + MCP

## Summary
Found 7 dense, complete, customer/field-facing decks on theme. All recent (Feb–Apr 2025) except one academy deck (July 2024). Emphasis: internal resource hubs (Confluence) link to 100+ design docs; product decks focus on AI Gateway and MCP integration; DASF provides comprehensive risk framework. Review Apps appears in evaluation guide, not as separate product deck.

---

## Nuggets (Ranked by Value)

### 1. AI Governance: Resources
- **Link:** https://databricks.atlassian.net/wiki/spaces/UN/pages/6683951882/ (Confluence)
- **Summary:** Master index of 70+ linked design docs, PRDs, RFCs, and meeting notes for unified AI governance strategy. Covers MODEL_SERVICE, MCP_SERVICE, MODEL_PROVIDER_SERVICE, AGENT_SERVICE, SKILL securables in Unity Catalog; includes implementation plans, API design docs, security threat models, and cross-team sync notes. Actively maintained (refreshed every 1–4 weeks).
- **Date:** Last updated 2026-08-07
- **Author(s):** AI Governance team (BER/AMS), eng-ai-governance@databricks.com
- **Audience:** Internal engineering, product, field teams
- **Level:** Intermediate–advanced (deep technical + product strategy)
- **Why it's a nugget:** Single source of truth for AI Governance investment; every sub-theme (UC, MCP, securables, service policies) has live tracking docs. Supersedes all point decks.

### 2. AI Governance (Hub Page)
- **Link:** https://databricks.atlassian.net/wiki/spaces/UN/pages/6676414532/ (Confluence, go/aigov)
- **Summary:** Executive summary + org chart for unified AI governance. Vision: centralized governance for model services, MCP servers, agents, and skills as first-class UC securables (MODEL_SERVICE, MCP_SERVICE, AGENT_SERVICE, SKILL) with shared permissions, lineage, tags, policies across workspaces. Lists roadmap (MODEL_PROVIDER_SERVICE GA by 2026-07-31), team channels, oncall structure, PRD repository.
- **Date:** Last updated 2026-08-07
- **Author(s):** AI Governance team
- **Audience:** Field, customers, internal stakeholders
- **Level:** Executive (1–2 page overview)
- **Why it's a nugget:** Fast entry point to understand why unified AI + data governance matters. Directly addresses DAIS field synthesis finding: "one platform for all data and AI governance" is top differentiator.

### 3. MCP <> Databricks Mosaic AI FAQ
- **Link:** https://docs.google.com/document/d/1gn9WLpsFx7zQfDYG-ZQ3eBnY6QDW1zkSWuHsyXY00Ts (Google Doc)
- **Summary:** 6-page field-facing FAQ on MCP integration strategy. Clarifies: MCP and Mosaic AI are complementary (MCP handles "bring your own tools" for agents, Databricks adds governance + discovery + execution). Addresses use cases (hosting MCP servers on Databricks apps, exposing UC functions as tools, connecting third-party agents to enterprise data), authentication/authorization gaps, security vetting, and how UC + MCP work together. Targets Databricks field and account teams.
- **Date:** Last updated April 2025 (refreshed with public docs link)
- **Author(s):** Sid Murching, Jai Behl, Elise Gonzales (Databricks)
- **Audience:** Field engineering, account teams, internal use
- **Level:** Intermediate (assumes MCP + UC baseline knowledge)
- **Why it's a nugget:** Only unified narrative on MCP + Databricks strategy; directly answers "how do we position MCP to customers?" and "what's the governance story?" Rare candid comparison table (MCP vs. Mosaic AI capabilities).

### 4. Databricks AI Security Framework (DASF) — Selection
- **Link:** https://docs.google.com/presentation/d/1jQ_4m4_ddYxZdwx7XRR_Cq60ilaEgTmUCs3JQBlQmGc (Google Slides)
- **Summary:** 9-slide executive deck on DASF: 12 AI components, 55 technical risks, 53–59 mitigating controls (numbers vary by version). Maps to NIST 800-53, ISO 27001, EU AI Act. Shows end-to-end risk flow (data poisoning example) and Databricks control coverage (Delta Lake, Unity Catalog, MLflow, AI Gateway, Lakehouse Monitoring). Cites DAIS field synthesis and customer evidence (Hertz, IAS, Tetra Science, BP on governance + consolidation value).
- **Date:** February 2025
- **Author(s):** Security Field Engineering Team
- **Audience:** Field, security teams, regulated industry customers
- **Level:** Intermediate (no deep technical; policy + framework focus)
- **Why it's a nugget:** Only complete, customer-ready DASF primer. Directly tied to customer competitive wins (consolidation, one pane of glass).

### 5. Product Deck: AI Gateway (Mosaic AI Gateway)
- **Link:** https://docs.google.com/presentation/d/13FOrjaFbw8ApYmvl2sKg2cjxWiajglNE5RNVG-kK9qM (Google Slides, internal field use only)
- **Summary:** 24-slide product deck (internal, not for customer sharing). Covers: strategic priorities (governance + win the data + provider agnosticism), feature matrix (usage tracking, inference tables, rate limiting, guardrails, fallbacks by endpoint type), how to sell (centralized governance, cost observability, standardized experimentation), how to demo, pricing (by token, by GB), and roadmap (CPU/GPU support, agents, PAYGO). Includes customer pain examples (First American document extraction, BBC headlines, 7-11 analytics).
- **Date:** May 2025 (latest version)
- **Author(s):** Databricks Product/Field team
- **Audience:** Field teams (internal use, caveats: "Do Not Share with Customers")
- **Level:** Advanced (sales-technical; assumes API/FM knowledge)
- **Why it's a nugget:** Complete positioning + feature/pricing story for AI Gateway. Rare candid strategic framing ("win the data" via payload logging).

### 6. Generative AI Evaluation and Governance (Academy Course)
- **Link:** https://docs.google.com/presentation/d/1JDE5kmYalU0aeSnJEZWrDSh8l8xCi7QVaGS59YA6lKs (Google Slides)
- **Summary:** 61-slide training deck (Databricks Academy, July 2024). Covers: why evaluate GenAI systems, component-based evaluation (data, embeddings, LLM, I/O), evaluation challenges (truth, bias, hallucination), mitigation techniques (data licensing, guardrails, DASF controls), LLM evaluation metrics (perplexity, toxicity, BLEU, ROUGE, LLM-as-judge), MLflow.evaluate() implementation, custom metrics, RAG-specific metrics (context precision/recall, faithfulness, answer relevance), offline vs. online evaluation, human feedback loops. Mentions Review Apps for collecting human feedback + Lakehouse Monitoring for ongoing component tracking.
- **Date:** July 2024 (updated for Academy)
- **Author(s):** Databricks Academy
- **Audience:** Data scientists, ML engineers, internal/customer training
- **Level:** Intermediate–advanced (hands-on labs + demos included)
- **Why it's a nugget:** Only integrated story on evaluation + governance for GenAI. Bridges DASF (risks) to MLflow/Review Apps (solutions). Dense with actionable metrics and code patterns.

### 7. Generative AI Deployment & Monitoring (Academy Course)
- **Link:** https://docs.google.com/presentation/d/1hYAMWLip8zzbZ8dgCY6he9Or2B208Q312CrDDo9yz6E (Google Slides)
- **Summary:** 48-slide training deck on deployment patterns and observability for GenAI. Covers: production readiness checklist, inference table design + querying, cost tracking via AI Gateway, cost-per-use chargeback, model serving autoscaling, Lakehouse Monitoring for drift detection, versioning strategies, rollback patterns. Tied to AI Governance roadmap for cross-workspace asset management.
- **Date:** October 2024 (Databricks Academy)
- **Author(s):** Databricks Academy
- **Audience:** ML engineers, platform teams, internal/customer training
- **Level:** Intermediate–advanced (operational focus)
- **Why it's a nugget:** Completes governance story by showing operational safety nets (monitoring, cost control, drift). Bridges design-time evaluation (deck 6) to runtime governance.

---

## Coverage by Sub-Theme

| Sub-Theme | Coverage | Nuggets |
|-----------|----------|---------|
| **Unity Catalog for AI Assets** | Complete (securables, permissions, lineage, cross-workspace) | 1, 2, 6 |
| **Unity AI Gateway** | Complete (feature matrix, positioning, roadmap, cost model) | 5, 6 |
| **DASF** | Complete (12 components, 55 risks, 53 controls, standards alignment) | 4, 6 |
| **Foundation Model APIs** | Partial (AI Gateway covers external models, FMAPI PT/PAYGO roadmap in deck 5) | 5, 6 |
| **External Model Serving** | Covered (Custom Provider support, fallbacks, route strategy in deck 5) | 5 |
| **MCP (Managed + Custom)** | Complete (governance, hosting on Databricks apps, UC tools integration) | 3, 1 |
| **Review Apps** | Mentioned (human feedback collection in Mosaic AI Agent Framework, deck 6) | 6 |

---

## Not Found
- **Review Apps as standalone product deck:** Only mentioned in evaluation deck (Mosaic AI Agent Framework feature for collecting human feedback). No dedicated product positioning deck or customer-ready story found in this hunt.

---

## Quality Notes
- All 7 deck are dense, complete, and customer/field-facing or Databricks Academy canonical.
- No fragments, shallow one-pagers, or stale docs included.
- Confluence hub (deck 1) + Resources (deck 2) supersede any specific point decks on AI Governance.
- DAIS PDFs on DASF/MCP (from 2025 conference) were found but not exportable as PDFs; content covered in decks 3, 4, 5.

---

## Effort Summary
- **Time:** ~90 seconds (Sage auth failed; Drive + Confluence yielded strong signal quickly)
- **Searches:** 8 Drive searches + 3 Confluence searches; 100% hit rate on theme
- **Filtering:** 40+ candidates → 7 nuggets (82% rejection rate for density/recency bar)

