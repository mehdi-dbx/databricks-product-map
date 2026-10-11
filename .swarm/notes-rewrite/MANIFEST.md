# Swarm: notes-rewrite — rewrite failing `note` fields into one plain sentence

Rule: docs/panel-slide-spec.md (note = one sentence, what it is / what it does).
Form gate: scripts/lint_notes.py. Check: `python3 -I scripts/notes_rewrite.py check <out file>`.
Merge: `python3 -I scripts/notes_rewrite.py merge` (exact path match).

Watch: tail -f .swarm/notes-rewrite/*.md

| agent | scope | journal | output | status |
|-------|-------|---------|--------|--------|
| R1 | AI Platform + Agentic Data Mgmt + Real-time + Domain | agent-R1.md | out-R1.json | DONE |
| R2 | Agents / Agent Bricks + Developer productivity | agent-R2.md | out-R2.json | DONE |
| R3 | Data foundation + Foundation Models | agent-R3.md | out-R3.json | DONE |
| R4 | Genie / AI.BI + Governance for AI | agent-R4.md | out-R4.json | DONE |
| R5 | MCP integration | agent-R5.md | out-R5.json | DONE |
| R6 | DS: Deploy & serve | agent-R6.md | out-R6.json | DONE |
| R7 | DS: Operate + Feature engineering | agent-R7.md | out-R7.json | DONE |
| R8 | DS: Develop & explore + Experimentation & AutoML | agent-R8.md | out-R8.json | DONE |
| R9 | DS: Training & compute + Languages & libraries | agent-R9.md | out-R9.json | DONE |
