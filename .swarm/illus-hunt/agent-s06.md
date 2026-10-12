# Judge s06

## Status
RUNNING

## Timeline

### Sheets Viewed
- 6.1-1.png: 9 tiles viewed
- 6.1-2.png: 9 tiles viewed  
- 6.1-3.png: 9 tiles viewed
- 6.2-1.png: 9 tiles viewed
- 6.2-2.png: 9 tiles viewed
- 6.2-3.png: 9 tiles viewed
- 6.2-4.png: 2 tiles viewed
- 6.3-1.png: 9 tiles viewed
- 6.3-2.png: 9 tiles viewed
- 6.3-3.png: 5 tiles viewed

### Initial Shortlisting (6.1 - Tracing)

**Strong candidates (screenshots of actual trace UI):**
- p6.1-trace-dashboard.png (6.1-1): Hero slide showing "Agent tracing - Powered by MLflow" with trace table. Legible, shows key message and actual UI.
- p6.1-trace-detail.png (6.1-2): Detail view showing all spans/steps of a single trace with inputs, outputs, latency, tokens. Excellent for showing "the step where it went wrong."
- p6.1-traces-list.png (6.1-3): List view of traces with full context. Good reference.

**Conceptual/reference diagrams:**
- 6.1-10 docs: "Raw/Redacted OTel tables" diagram showing data access patterns. Clean conceptual diagram.
- 6.1-19 deck: "How does it work?" architecture showing GenAI API, Agent Frameworks, MLFlow integration. Good system context.
- 6.1-23 deck: "Evaluate Traces" showing code for LLM-based evaluation. Shows practical usage.

**Strong deck references:**
- 6.1-22 deck: "Agent Bricks" framework overview (Framework, Model, Compute, Context, Observability). Conceptual.
- 6.1-24 deck: "LLMOps lifecycle management" flow diagram. Good reference.

**Marginal/questionable:**
- 6.1-26 deck: "Managed vs Open Source MLflow" comparison table - mostly text
- 6.1-27 deck: "Where is everything recorded?" - reference slide

**Rejecting:**
- 6.1-4, 11, 12, 13, 14, 15, 16: Icon illustrations (llama, bird, swarm logo) - not relevant to tracing
- 6.1-20, 21, 25: Deprecated or mostly text bullets
- 6.1-5, 6, 7, 8, 9: Documentation pages (too much text/UI clutter)

**Decision for 6.1:** Need 4-6. Top 4 are clear:
1. p6.1-trace-dashboard.png - hero + dashboard
2. p6.1-trace-detail.png - trace detail showing all steps
3. p6.1-traces-list.png - trace list/table
4. 6.1-10 docs diagram - OTel tables concept

**FINAL DECISION for 6.1:** Keep 4 candidates (already in app/static/img/, best coverage):
1. p6.1-trace-dashboard.png - hero slide with dashboard
2. p6.1-trace-detail.png - detail view showing all spans with inputs/outputs/latency/tokens
3. p6.1-traces-list.png - list view of traces
4. p6.1-unified-trace-table.png - unified trace table (governance view)

### Shortlisting (6.2 - Evaluation and prompt versioning)

**Already kept separately:** mlflow-eval-hero, mlflow-eval-1, mlflow-eval-custom-judge (3 items)

**Strong candidates (verified for legibility):**
- p6.2-eval-flow.png: Evaluation flow showing Test → Your GenAI app → Monitor, with callouts
- p6.2-prompt-registry.png: Prompt Registry UI showing versioning with Live buttons and JSON
- p6.2-mlflow-platform-arch.png: MLflow platform architecture context

**FINAL DECISION for 6.2:** Add 3 more (total 6 with existing 3):
1. p6.2-eval-flow.png - conceptual evaluation workflow
2. p6.2-prompt-registry.png - prompt versioning UI
3. p6.2-mlflow-platform-arch.png - platform architecture

### Shortlisting (6.3 - Expert review and labeling)

**Already kept separately:** mlflow-eval-feedback (1 item)

**Strong candidates (verified for legibility):**
- p6.3-review-session.png: Review App showing Conversation and Expectations for experts
- p6.3-review-labeling.png: "What is MLflow Labeling?" with hero message and screenshot
- p6.3-assessments-feedback.png: Trace detail showing Feedback and Expectations panels

**FINAL DECISION for 6.3:** Add 3 more (total 4 with existing 1):
1. p6.3-review-session.png - review app interface
2. p6.3-review-labeling.png - conceptual overview
3. p6.3-assessments-feedback.png - trace with feedback/assessment

## Summary

**6.1 Tracing:** 4 tiles (all candidates)
- Sheets viewed: 3 (27 tiles total)
- Tiles kept: 4
- Main reason for keeping: Show complete trace workflow (hero, detail, list, governance)

**6.2 Evaluation & Prompt Versioning:** 3 new tiles (+ 3 existing = 6 total)
- Sheets viewed: 4 (29 tiles total)
- Tiles kept: 3 new
- Main reason for keeping: Show evaluation flow, prompt versioning, and platform context

**6.3 Expert Review & Labeling:** 3 new tiles (+ 1 existing = 4 total)
- Sheets viewed: 3 (23 tiles total)
- Tiles kept: 3 new
- Main reason for keeping: Show review app, labeling concept, and feedback integration

## Final Output

All tiles are candidate images already in app/static/img/ — no copies needed.

Output JSON: /Users/mehdi.lamrani/code/Report/AmadeusAI/.swarm/illus-hunt/final-ch06.json

## Status
DONE

### Completion Details

6.1 (Tracing) — 4 tiles kept, 0 rejected for count:
- p6.1-trace-dashboard.png (hero + dashboard)
- p6.1-trace-detail.png (detail with nested spans, inputs/outputs/latency)
- p6.1-traces-list.png (list view)
- p6.1-unified-trace-table.png (governance/audit view)

6.2 (Evaluation & Prompt Versioning) — 3 tiles kept, supplementing 3 existing (mlflow-eval-hero, mlflow-eval-1, mlflow-eval-custom-judge):
- p6.2-eval-flow.png (workflow diagram)
- p6.2-prompt-registry.png (prompt versioning UI)
- p6.2-mlflow-platform-arch.png (platform architecture)

6.3 (Expert Review & Labeling) — 3 tiles kept, supplementing 1 existing (mlflow-eval-feedback):
- p6.3-review-session.png (review app interface)
- p6.3-review-labeling.png (conceptual overview)
- p6.3-assessments-feedback.png (feedback/assessment integration)

