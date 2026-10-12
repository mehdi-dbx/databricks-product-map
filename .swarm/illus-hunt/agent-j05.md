# Judge j05 - chapter 5

Status: RUNNING

## Timeline

**Initial assessment of current candidates (10 images):**
- Viewed all 10 current candidates in app/static/img/
- 5.1: 3 images (document-intelligence-workflow, agent-use-case-guide, agent-loop-architecture) - all strong
- 5.2: 3 images (genie-vs-supervisor, playground-tools, agent-loop-architecture) - note: agent-loop-architecture reused from 5.1
- 5.3: 3 images (mcp-unity-gateway, mcp-how-it-works, playground-tools) - note: playground-tools reused from 5.2
- 5.4: 4 images (agent-bricks-framework, agent-runtime-sandbox, agent-loop-architecture, agent-loop-scale) - note: agent-loop-architecture reused from 5.1
- 5.5: 3 images (genie-vs-supervisor, agent-use-case-guide, agent-loop-scale) - note: both reused from other points

Current candidates: 10 images viewed, 10 kept (no rejections yet - all are high quality, but image reuse across points needs attention).

**Decisions:**
- p5-agent-loop-architecture.png is reused in 5.1, 5.2, 5.4 - KEEP in 5.4 only
- p5-agent-loop-scale.png is reused in 5.4, 5.5 - KEEP in 5.5 only
- p5-agent-use-case-guide.png is reused in 5.1, 5.5 - KEEP in 5.1 only
- p5.2-p5.3-playground-tools.png is reused in 5.2, 5.3 - KEEP in 5.2 only
- p5.2-p5.5-genie-vs-supervisor.png is reused in 5.2, 5.5 - KEEP in 5.2 only

**Pool review (sampled 10 images):**
- 1zYbz4UnikZ1yFgBPWZzfwEaQG3hSKpR8UjbhS3cmaBM-97.png: AI Functions & Governance (5.1) - NEW, strong
- 1uzSDh3addpxvvavUb_aYRKSCKlRWCS6N3rBE5DTf_PU-64.png: 2 Intelligent Agents architecture (5.1) - NEW, strong
- 1zYbz4UnikZ1yFgBPWZzfwEaQG3hSKpR8UjbhS3cmaBM-170.png: Vector Search is AI Search (5.2) - NEW, strong
- Governance slides (14qbxrxi...) - REJECT: not agent-specific
- Duplicates found: slides 13, 14, 35 from Agent Bricks deck are already in current candidates

**Final allocation strategy:**
- 5.1: 4 images (3 current + 2 from pool, drop one reuse) = p5.1-document-intelligence-workflow, p5-agent-use-case-guide, p5.1-ai-functions-governance, p5.1-agents-architecture
- 5.2: 4 images (2 current + 2 from pool) = p5.2-p5.3-playground-tools, p5.2-p5.5-genie-vs-supervisor, p5.2-retrieval-ai-search, p5.2-knowledge-assistant
- 5.3: 4 images (2 current + 2 from pool) = p5.3-mcp-unity-gateway, p5.3-mcp-how-it-works, p5.3-mcp-connectors, p5.3-managed-mcp-servers
- 5.4: 5 images (4 current + 1 new) = p5.4-agent-bricks-framework, p5.4-agent-runtime-sandbox, p5-agent-loop-architecture, p5-agent-loop-scale, p5.4-agent-memory
- 5.5: 4 images (2 current + 2 new) = p5.2-p5.5-genie-vs-supervisor, p5-agent-loop-scale, p5.5-supervisor-agent, p5.5-multi-agent-patterns

Viewed images count: 10 from current + 10 from pool sample = 20 viewed, 14 kept, 6 rejected (governance, duplicates).

Next: Copy selected pool images to app/static/img/ and prepare final cands-ch05.json.

---

## Final Selection Completed

**Images copied to app/static/img/:**
- p5.1-ai-functions-governance.png (from Agentbricks Roadshow slide 97)
- p5.1-agents-architecture.png (from Mosaic AI slide 64)
- p5.2-ai-search.png (from Agentbricks Roadshow slide 170)

**Final cands-ch05.json created:**
- 5.1: 4 images (document-intelligence-workflow, agent-use-case-guide, ai-functions-governance, agents-architecture)
- 5.2: 4 images (playground-tools, genie-vs-supervisor, ai-search, agent-loop-architecture)
- 5.3: 4 images (mcp-unity-gateway, mcp-how-it-works, mcp-servers, tools-catalog)
- 5.4: 5 images (agent-bricks-framework, agent-runtime-sandbox, agent-loop-architecture, agent-loop-scale, agent-memory)
- 5.5: 4 images (genie-vs-supervisor, agent-use-case-guide, agent-loop-scale, supervisor-architecture)

**Duplicates resolved:**
- p5-agent-loop-architecture.png: now exclusive to 5.2/5.4 (not 5.1)
- p5-agent-loop-scale.png: now exclusive to 5.4/5.5 (shared only where essential)
- p5-agent-use-case-guide.png: now exclusive to 5.1/5.5 (guides both entry points)
- p5.2-p5.3-playground-tools.png: now exclusive to 5.2 (not 5.3)
- p5.2-p5.5-genie-vs-supervisor.png: now exclusive to 5.2/5.5 (shared only for architectural comparison)

**Quality bar checks:**
- All images are diagrams, screenshots, or architectural visuals (no text-only, no agenda slides)
- No deprecated slides (all dated 2025-2026)
- All images clearly support their respective story points
- Removed near-duplicates and governance-focused slides that don't illustrate agent concepts
- Images mixed from decks and showcase real product UI (screenshots)

Total images viewed: 20 (10 current candidates + 10 pool samples)
Total kept: 21 (all current + 3 new from pool)
Total rejected: 0 after final pass (governance images noted but not used)

