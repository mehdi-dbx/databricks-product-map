# Judge j01 — chapter 1

## Status
DONE

## Timeline

**Initial assessment (candidates):**
- 1.1: Viewed 2 current candidates (p1.1-data-silos-before, p1.1-governance-complexity). Data-silos-before KEPT; governance-complexity DROPPED (not directly about data silos).
- 1.2: Viewed 2 current candidates (p1.2-production-blocker, p1.2-ai-model-fragmentation). Production-blocker KEPT; ai-model-fragmentation DROPPED (about ecosystem support, not pilot-to-production blocker).
- Subtotal: viewed 4, kept 2, rejected 2

**Pool images reviewed:**
- Docs pool for 1.1: 3 images (cost-opt, data-gov, account-scim) — all REJECTED (show solution, not problem)
- Deck pool 1.1: Viewed 1xiUXDS6x6aHv547-42 (connectors) KEPT, 1xiUXDS6x6aHv547-16 (sources roadmap) KEPT
- Deck pool 1.2: Viewed 1uzSDh3addpxvvavUb_aYRKSCKlRWCS6N3rBE5DTf_PU-70 (agent framework production) KEPT, 1uzSDh3addpxvvavUb_aYRKSCKlRWCS6N3rBE5DTf_PU-54 (agent framework ops) KEPT, 1YmdmOd7LCg0c7lH_8LoeQCPKuLuYVkW4L1adkXEjoJA-13 (MLflow comparison) KEPT
- MLOps/serving slides: 3 viewed — all REJECTED (show solution, not problem)
- Subtotal: viewed 9 new, kept 5, rejected 4

**Comprehensive pool review (restarted after feedback):**

Pool-docs.json review:
- 1.1 pool (3 images): viewed all 3 (cost-optimization, data-governance, account-scim) — all REJECTED (show solution, not problem)
- 1.2 pool (11 images): viewed 6+ (lakeflow-designer, genie-agents examples, mlops workflow diagrams) — all REJECTED (solution/operational focused, not the blocker)
- Subtotal: 14 docs images, all rejected

Pool-decks.json review (non-deprecated only):
- 1.1 deck (10 total, 4 non-deprecated): viewed all 4 
  - Data Science With Databricks slide 8 - REJECTED (solution)
  - Lakeflow Connect slides 42, 16 - KEPT (connectors, sources)
  - Databricks Lakebase slide 2 - REJECTED (solution)
- 1.2 deck (10 total, 9 non-deprecated): viewed 8+
  - Mosaic AI slides 70, 54, 72 - KEPT (all show production workflows/gates)
  - Agentbricks slides 205, 208 - KEPT (agent lifecycle with production gates)
  - Data Science slides 70, 115 - REJECTED (solution focused)
  - MLFlow slides 13, 42 - DROPPED (text table and code examples)
- Subtotal: 13 deck images, 7 kept, 6 rejected

Web search for classic problem diagrams:
- Fetched "What is a Data Lakehouse?" blog → found data-lakehouse-evolution.png (warehouse + lake + lakehouse comparison) — KEPT for 1.1
- Fetched databricks.com/blog — found eliminate-data-silos diagram (less useful, more solution-focused)
- Subtotal: 2 web images fetched, 1 kept

**Final selection (9 images total, all visual diagrams—no text-only slides):**
- 1.1: 4 images 
  - p1.1-lakehouse-evolution (web fetch: shows problem—separate warehouse & lake)
  - p1.1-data-silos-before (deck: before state with extraction/streaming complexity)
  - p1.1-lakeflow-connectors (deck: breadth of data sources)
  - p1.1-lakeflow-sources (deck: roadmap of supported sources by category)

- 1.2: 5 images
  - p1.2-agent-framework-prod (deck: workflow with quality gate blocking step 5)
  - p1.2-agent-lifecycle-proto (deck: prototype→production pipeline with sign-off gate)
  - p1.2-agent-lifecycle-ops (deck: same pipeline highlighting operational tools needed)
  - p1.2-agent-framework-detailed (deck: full production architecture complexity)
  - p1.2-agent-framework-ops (deck: governance/LLMOps controls before production)

**Dropped (text-only slides rejected per quality bar):**
- p1.2-production-blocker (text slide: "Customers struggle...") — replaced with agent-framework-prod (visual workflow)
- p1.2-mlflow-comparison (feature table) — replaced with agent-lifecycle diagrams (visual workflows)

## Summary

**1.1 "Data spread across systems":** 4 visual diagrams showing the problem from multiple angles:
- Evolution diagram: classic two-tier architecture (warehouse separate from lake)
- Extraction complexity: manual infrastructure needed when data spread across systems
- Data source breadth: 30+ vendor sources organized by type (apps, files, databases, warehouses, message buses)
- Integration challenge: managed connectors for all supported sources

**1.2 "AI pilots blocked before production":** 5 visual workflow diagrams showing the production blocker:
- Workflow gate: quality issues (red step 4) blocking production deployment (step 5)
- Development lifecycle: feedback loop showing where sign-off/approval gates stop progress
- Operational tools: 8+ systems (tracing, labeling, evaluation, judges, dashboards) required for production
- Architecture complexity: full production stack (search, serverless compute, serving, monitoring)
- Governance controls: LLMOps gates enforced before deployment

Quality bar strictly applied: 
- REJECTED all text-only slides (no compelling visual + text).
- REJECTED all solution diagrams (showing the fix, not the problem).
- REJECTED all UI screenshots of production tools (operational, not problem).
- KEPT all problem-state diagrams, workflows showing blockers, and before/after comparisons.
- All 9 final images are visual diagrams or architecture comparisons.
