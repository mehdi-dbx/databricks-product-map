# Hard Logging: AI Tree Leaf Drill-Down (Agents / Agent Bricks + Governance for AI)

**Start time:** 2026-10-07 (initiative)  
**Scope:** 2 pillars, ~12 leaves (AI Functions + Unity AI Gateway already done)

---

## PILLAR 1: Agents / Agent Bricks

### Leaf: AI Functions [ALREADY DONE]
[Step 1 | init] Copy verbatim from ai-tree.json ✓

### Leaf: Custom Agents
[Step 2 | mine run/tree-*.md] ATTEMPT
- tree-glean.md Section II.1 (page 101-117): Custom Agents described, frameworks listed
- tree-sage.md Section 2.1 (page 216): Eval Flywheel demo confirms MLflow tracing, LLM judges pattern
- tree-public.md Section 1.2 (page 29-33): Agent Bricks CLI Beta (Sep 29), DurableAgentServer, frameworks

[Step 2 | mine result] FOUND in all 3 docs ✓

### Leaf: Managed memory & sessions
[Step 3 | mine run/tree-*.md] ATTEMPT
- tree-glean.md (page 42-44): Lakebase-backed memory, semantic search, cross-session (Sep 16 Beta)
- tree-sage.md: No direct slot; inferred from Lakebase content
- tree-public.md Section 1.3 (page 42-48): Beta Sep 16, cross-session persistence, semantic search, SQL interface

[Step 3 | result] FOUND ✓

### Leaf: Databricks Sandbox
[Step 4 | mine run/tree-*.md] ATTEMPT
- tree-glean.md (page 108-109): "Isolated serverless code execution, scoped UC access"; also mentioned in Custom Agents (page 108)
- tree-public.md Section 1.5 (page 59-63): Sandbox Beta; 4 vCPU, 8GB RAM, Python/Node.js

[Step 4 | result] FOUND ✓

### Leaf: Supervisor Agent
[Step 5 | mine run/tree-*.md] ATTEMPT
- tree-glean.md (page 93-99): "Multi-Agent Supervisor" – GA but legacy; orchestrates agents, tools, endpoints, user-scoped auth
- tree-public.md: No dedicated section (legacy product; not separately documented in public)

[Step 5 | result] FOUND ✓

### Leaf: Knowledge Assistant
[Step 6 | mine run/tree-*.md] ATTEMPT
- tree-glean.md (page 87-91): "Knowledge Assistant (Legacy)"; GA but legacy; document-grounded chatbot, Instructed Retriever
- tree-public.md: No dedicated section

[Step 6 | result] FOUND ✓

### Leaf: Omnigent
[Step 7 | mine run/tree-*.md] ATTEMPT
- tree-glean.md (page 119-125): Agent meta-harness; Beta; framework-agnostic; Apache 2.0 OSS; managed version GA integration
- tree-public.md Section 1.4 (page 49-56): Open-source (Alpha), Managed Beta; CEL policies, Sandbox execution

[Step 7 | result] FOUND ✓

### Leaf: Agent evaluation & monitoring
[Step 8 | mine run/tree-*.md] ATTEMPT
- tree-glean.md (page 133-137): "Evaluation and Monitoring"; traces → Review Apps → datasets → LLM judges → dashboards; GA
- tree-public.md Section 5.3-5.4 (page 227-254): MLflow evaluation (8 scorers, workflow); Review Apps for human feedback; 5 status page
- tree-sage.md Section 2.1 (page 216-220): Eval Flywheel demo: end-to-end pattern with automated scoring

[Step 8 | result] FOUND ✓

---

## PILLAR 2: Governance for AI

### Leaf: Unity Catalog for AI assets [NOT ALREADY DONE]
[Step 9 | mine run/tree-*.md] ATTEMPT
- tree-glean.md (page 280-293): UC for AI assets; GA; governs models, agents, functions, MCP services, connections, skills, credentials; RLAC/ABAC, lineage, audit
- tree-public.md Section 5.1 (page 214-224): UC for AI Assets; three-level namespace, versioning, cross-workspace sharing, RLAC/ABAC

[Step 9 | result] FOUND ✓

### Leaf: Unity AI Gateway [ALREADY DONE]
[Step 10 | copy] Copy verbatim from ai-tree.json ✓

### Leaf: Review Apps
[Step 11 | mine run/tree-*.md] ATTEMPT
- tree-glean.md (page 316-325): "Web interface for domain experts to review GenAI traces and provide structured feedback"; GA
- tree-public.md Section 5.4 (page 247-254): Review Apps for human-in-the-loop; label traces, create eval datasets; GA

[Step 11 | result] FOUND ✓

### Leaf: DASF v3.0
[Step 12 | mine run/tree-*.md] ATTEMPT
- tree-glean.md (page 150-151): "AI Security Framework: 97 risks / 73 controls; Agentic extension (35 risks, 6 controls, 13 components). Published Mar 2026."
- tree-public.md Section 5.5 (page 255-271): DASF v3.0; 97 risks, 73 controls; Agentic AI extension detailed; March 20 published

[Step 12 | result] FOUND ✓

---

## DATA ENRICHMENT SUMMARY

All 12 leaves successfully mined. No Glean/web calls needed at this time (all data in run/ docs).
Next: enrich each with children, docs, since, deck fields.

---

## ENRICHMENT EXECUTION

[Step 13 | enrich PILLAR 1] Agents / Agent Bricks
- AI Functions: COPY VERBATIM ✓
- Custom Agents: enriched with 6 children (frameworks, server, CLI, tracing, model access) ✓
- Managed memory & sessions: enriched with 5 children (Lakebase, semantic search, persistence, SQL, multi-agent) ✓
- Databricks Sandbox: enriched with 5 children (compute, langs, UC-scoped, storage, isolation) ✓
- Supervisor Agent: enriched with 5 children (routing, auth, endpoint, tool, legacy note) ✓
- Knowledge Assistant: enriched with 6 children (ingestion, retriever, citations, SME, endpoint, legacy) ✓
- Omnigent: enriched with 6 children (composition, YAML, policy, sandbox, interfaces, governance) ✓
- Agent evaluation & monitoring: enriched with 6 children (tracing, judges, custom, Review Apps, datasets, monitoring) ✓

[Step 14 | enrich PILLAR 2] Governance for AI
- Unity Catalog for AI assets: enriched with 6 children (registry, permissions, versioning, lineage, cross-workspace, semantics) ✓
- Unity AI Gateway: COPY VERBATIM ✓
- Review Apps: enriched with 6 children (chat UI, labeling, feedback, datasets, MLflow, workflows) ✓
- DASF v3.0: enriched with 6 children (risk taxonomy, controls, least-privilege, oversight, sandbox, guardrails) ✓

[Step 15 | validate JSON] agents-gov.json
- Format: Valid JSON array with 2 pillar objects ✓
- Field schema: All leaves include children/docs/since/deck ✓
- Children count: 5–6 per leaf (within 3–7 spec) ✓

---

## FINAL STATUS

**Leaves enriched:** 12/12 (100%)
**Pillars complete:** 2/2 ✓
**Output file:** `/Users/mehdi.lamrani/code/Report/AmadeusAI/run/leaves/agents-gov.json` (validated)
**Verification:** JSON parses; children/docs/since/deck populated for all non-ALREADY-DONE leaves.
**Gaps:** None identified. All data sourced from run/tree-*.md files; no fabrication.
