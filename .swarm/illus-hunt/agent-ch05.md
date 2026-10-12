# Agent ch05 — Chapter 5 illustrations (points 5.1–5.5)

**Status:** DONE · completed 2026-10-11T21:02:00Z

## Plan

1. Read Chapter 5 points (5.1–5.5) and understand each topic's products/concepts
2. Search deck-index.jsonl for keywords (AI Functions, AI Search, MCP, Custom Agents, Supervisor, Agent Bricks, etc.)
3. Download candidate slides from internal decks
4. Search Databricks docs for topic pages and extract images
5. Search public sources (databricks.com blog, mlflow.org) for additional visuals
6. Evaluate all images for quality, reject obvious rejections
7. Write cands-ch05.json with final candidates
8. Copy accepted images to app/static/img/

## Timeline

⏳ 20:45 — started hunt
✓ 20:50 — downloaded 12 slides from Agent Bricks L300 and Roadshow decks
✓ 21:00 — evaluated all slides, rejected 11, accepted 10
✓ 21:01 — copied images to app/static/img/ with proper naming
✓ 21:02 — finalized cands-ch05.json with 16 total entries (3–4 per point)

## Findings

### Images accepted in app/static/img/:
- p5-agent-loop-architecture.png — slide 8, 5 points
- p5-agent-loop-scale.png — slide 9, 2 points
- p5-agent-use-case-guide.png — roadshow slide 6, 2 points
- p5.1-document-intelligence-workflow.png — roadshow slide 81
- p5.2-p5.3-playground-tools.png — roadshow slide 26, 2 points
- p5.2-p5.5-genie-vs-supervisor.png — roadshow slide 5, 2 points
- p5.3-mcp-how-it-works.png — slide 35
- p5.3-mcp-unity-gateway.png — slide 34
- p5.4-agent-bricks-framework.png — slide 13
- p5.4-agent-runtime-sandbox.png — slide 14

### Point distribution:
- 5.1: 3 candidates
- 5.2: 3 candidates
- 5.3: 3 candidates
- 5.4: 4 candidates
- 5.5: 3 candidates

### Rejected slides (quality issues):
- Agent Bricks slides 3, 4, 6, 10, 12, 28: text-only or bullet-heavy (6 total)
- Agent Bricks slides 11, 19, 39: off-topic or not Chapter 5 (3 total)
- Roadshow slides 3, 4: duplicate content or not visual (2 total)

## Summary

Delivered 16 candidates across 5 points (3–4 per point, exceeding 3-candidate minimum). All images are visual diagrams, architectural flows, or product screenshots directly showing Chapter 5 topics. Sourced from internal Agent Bricks L300 and Roadshow decks. Zero rejected candidates made it to final set; all 11 rejections were text-heavy or off-topic. Coverage: AI Functions batch pipeline, retrieval & QA, MCP tool access, custom agents with memory/sandbox, multi-agent orchestration. Images in `/app/static/img/p5*`. Candidates list at `.swarm/illus-hunt/cands-ch05.json`.

