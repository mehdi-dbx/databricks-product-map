# Gap agent g2

## Status
RUNNING

## Current candidates to avoid duplicating

### 7.3 (AI security risks and controls)
- p7.3-lakehouse-security.png (docs.databricks.com)
- p7.3-dasf-motivation-framework.png (DASF v1/v2 with 59 controls - OUTDATED)
- p7.3-dasf-use-cases-to-controls.png (DASF methodology)
- p7.3-ai-governance-capabilities.png (governance matrix)
- p7.3-ai-governance-capabilities-2.png (Gartner governance styles)

**Outdated:** p7.3-dasf-motivation-framework.png, p7.3-dasf-use-cases-to-controls.png (old DASF version, not v3.0)

### 11.2 (Production serving)
- p11.2-model-serving-platform.png (Agent Bricks L300)
- p11.2-unity-gateway-governance.png (Agent Bricks L300)
- p11.2-serving-architecture.png (Mosaic AI System Architecture)
- p11.2-finetuning-architecture.png (Mosaic AI System Architecture)
- p11.2-route-optimization.png (docs.databricks.com)

## Search targets

### 7.3: DASF v3.0 visuals (4-5 new)
- DASF v3.0 blog post on databricks.com (agentic AI security, new risks and controls)
- DASF page / whitepaper / compendium on databricks.com
- DASF components diagram (12 components of an AI system)
- Agent risk diagrams
- 97 risks, 73 controls, 35 risks specific to agents

### 11.2: Production serving visuals (2-3 new)
- Model serving endpoints with registered model versions
- Real-time requests, 25k+ QPS, low latency, autoscaling
- Batch scoring / ai_query batch
- Serving endpoint UI with traffic/autoscaling
- databricks.com blog on high-QPS serving

## Outdated current 7.3 candidates (for orchestrator to drop)
- **p7.3-dasf-motivation-framework.png** — Shows "59 controls" (DASF v1/v2). DASF v3.0 has 97 risks, 73 controls. Outdated.
- **p7.3-dasf-use-cases-to-controls.png** — References old DASF version (59 controls, 12 components). DASF v3.0 adds Agentic AI as 13th component with 35 new risks. Outdated methodology visual.

## Images added

### 7.3 (DASF v3.0) — 3 new images
1. **p7.3-dasf-v3-components.png** — 13 canonical AI system components with DASF v3.0 (97 risks, 73 controls), Agentic AI highlighted as component 13
2. **p7.3-dasf-v3-lethal-trifecta.png** — Risk framework showing 3 conditions that spike agentic risk; maps to DASF v3.0 controls
3. **p7.3-dasf-v3-agent-components.png** — Component 13 breakdown: 35 agent-specific risks, 6 controls, 3 sub-components (Agent Core, MCP Server, MCP Client)

### 11.2 (Production serving) — 4 new images
1. **p11.2-serving-arch-high-qps.png** — Full Databricks Model Serving architecture for 300k+ QPS with autoscaling
2. **p11.2-serving-autoscaling-metrics.png** — AutoPilot autoscaler control loop with telemetry inputs
3. **p11.2-serving-endpoint-ui.png** — Production endpoint dashboard with traffic %, compute config, version management
4. **p11.2-serving-route-optimization.png** — Bonus: Route optimization for latency-first serving paths

## Timeline

- Searched for DASF v3.0 materials (97 risks, 73 controls, agentic AI)
- Found DASF v3.0 blog post with 3 high-quality component/risk diagrams (1200–1786px)
- Searched for high-QPS serving and autoscaling visuals
- Found AI Serving Platform blog (300k+ QPS, AutoPilot autoscaler) with 5 diagrams
- Downloaded and vetted all images (quality bar: ≥600px, diagram/screenshot/visual, not outdated/stock/logos)
- Selected best candidates per point (3 for 7.3, 4 for 11.2 — exceeds 2–3 target for 11.2)
- Copied to app/static/img/ with p{point}-{slug} naming
- Created gap-g2.json with metadata
- Identified 2 outdated DASF v1/v2 candidates for removal

## Summary

**DASF v3.0 visuals (7.3):** Successfully found 3 new DASF v3.0 images covering the full framework (13 components, Agentic AI specific risks/controls, lethal trifecta risk model). Replaced old 59-control DASF versions.

**Production serving visuals (11.2):** Successfully found 4 new high-quality serving images covering architecture for 300k+ QPS, autoscaling control loop, endpoint UI with traffic routing, and route optimization. All from official Databricks blog/docs.

**Quality bar met:** All accepted images ≥600px, clear diagrams/screenshots, no stock photos, no logos, no text walls, no outdated content.
