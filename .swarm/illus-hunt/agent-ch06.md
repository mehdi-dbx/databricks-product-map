# Agent ch06 — Chapter 6 illustrations (points 6.1–6.3)
**Status:** RUNNING · started 2026-10-11 20:44:07

## Plan
1. Read chapter 6 points (6.1, 6.2, 6.3) from app/src/story.json and resolve capsule refs in ai-tree.json/ds-tree.json
2. Search deck-index.jsonl for images on MLflow evaluation, LLM judges, agents, review/scoring concepts
3. Hunt docs.databricks.com for evaluation and MLflow pages via docs-inventory
4. Search mlflow.org, databricks.com, and public sources for additional visuals
5. Download, validate, and catalog all images; write final cands-ch06.json

## Timeline
⏳ 20:44:07 — reading chapter 6 structure
✓ 20:44:30 — parsed points: 6.1 Tracing, 6.2 Evaluation & prompts, 6.3 Review Apps; capsules mapped
⏳ 20:45:15 — downloading from internal decks (Agent Bricks, Agentbricks Roadshow, MLflow 3.0)
✓ 20:46:00 — 12 deck slides + 2 docs images downloaded; quality-checked all
✓ 20:47:30 — copied 11 accepted images to app/static/img/, resized oversized image
✓ 20:47:45 — wrote cands-ch06.json with full metadata

**Status:** DONE (revised) · 2026-10-11 21:18:00

⏳ 20:48:15 — addressed coordinator feedback
✓ 20:49:00 — rejected p6.1-tracing-features (text-only, wrong kind label)
✓ 20:50:00 — shrunk p6.3-review-session from 2042px to 1800px
✓ 20:52:00 — hunted docs pages: downloaded 3 new high-quality images (trace-detail, traces-list, assess-trace)
✓ 20:55:00 — downloaded from GenAI-As-03 deck (mostly section dividers, not usable)
✓ 20:58:00 — resized all oversized docs images to 1800px
✓ 21:05:00 — updated cands-ch06.json with 13 verified images + corrected kind labels

## Fixes Applied
- ✗ Rejected: p6.1-tracing-features.png (text-only slide, mislabeled as "visual")
- ✓ Shrunk: p6.3-review-session.png (2042px → 1800px)
- ✓ Added 3 high-quality docs images with correct kind labels:
  - p6.1-trace-detail: screenshot showing span tree, inputs/outputs, assessments
  - p6.1-traces-list: screenshot of trace table UI with sidebar navigation
  - p6.3-assessments-feedback: screenshot of feedback/expectations panels
- ✓ Corrected all kind labels (visual → screenshot for UI images)

## Final Candidates (13 verified images)

**6.1 - Tracing** (4 candidates):
- p6.1-trace-dashboard (screenshot): Agent autologging dashboard with trace table, filters, metrics
- p6.1-trace-detail (screenshot): Detailed trace view — span tree (input_guardrail, query_rewrite, embed_query, vector_search), inputs/outputs, assessments
- p6.1-traces-list (screenshot): MLflow Traces UI list view — table with Time, Input, Output, Session, Duration, State, Tokens columns; sidebar navigation
- p6.1-unified-trace-table (screenshot): OpenTelemetry unified table — every request/response logged with trace IDs, services, principals

**6.2 - Evaluation & Prompt Registry** (6 candidates + 3 existing = 9 total):
- p6.2-eval-flow (diagram): Lifecycle diagram — test dev → deploy → monitor prod → iteratively improve (scorers, eval sets, feedback)
- p6.2-agent-bricks-observability (diagram): Observability stack — tracing, 8 LLM judges, custom scorers, human feedback, eval datasets, monitoring
- p6.2-prompt-registry (screenshot): Prompt Registry UI — versioned prompts (Address validator), side-by-side comparison, system/user roles
- p6.2-mlflow-platform-arch (diagram): MLflow platform architecture — tracing (prompt loading, trace logging), evaluation (feedback, judges), prompt registry
- p6.2-eval-scorers (screenshot): Evaluation UI — 'Run scorer on 2 traces' dialog showing 13 pre-built LLM judges (Completeness, Correctness, Equivalence, Fluency), custom scorer option
- p6.2-eval-actions (screenshot): Trace actions menu — Use for evaluation, Evaluate, Add to evaluation dataset, Flag for review

**6.3 - Expert Review & Labeling** (3 candidates + 1 existing = 4 total):
- p6.3-review-session (screenshot): Chat review interface — conversation view with Expectations panel (Expected facts, Guidelines, Expected response), progress tracker (40%, 1/5)
- p6.3-review-labeling (screenshot): Review app workflow — interactive chat testing, targeted labeling, synthetic bootstrapping, auto-save to MLflow
- p6.3-assessments-feedback (screenshot): Trace assessment — Feedback panel (Add custom feedback) and Expectations panel (Add custom expectation) for expert labeling

**Sources**: 4 internal decks (Agent Bricks L300, Agentbricks Roadshow, MLflow 3.0, GenAI-As-03), 3 docs.databricks.com pages (tracing, eval-monitor, human-feedback)

**Quality**: All images visual (screenshots, diagrams); correct kind labels; no text-only slides; 4-6 per point met; all resized ≤ 1800px
<!-- newest entries appended below; keep this sentinel last -->
