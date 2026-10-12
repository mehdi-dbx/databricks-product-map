# Agent ch04 — Chapter 4 illustrations (points 4.1–4.4)
**Status:** DONE · quality bar applied, 1 image rejected (text-only), 16 final candidates

## Plan
1. Read story.json chapter 4 points (4.1, 4.2, 4.3, 4.4) and identify capsule references
2. Search deck-index.jsonl for Model Serving, Mosaic AI, governance, endpoints, external models
3. Search docs-inventory for governance, access control, model serving docs pages
4. Download candidate images from decks and docs
5. Validate, resize, and organize into app/static/img/ and cands-ch04.json

## Timeline
⏳ 00:05 — searching decks for Model Serving, Foundation Models, fine-tuning, external models
⏳ 00:20 — downloading 16 candidate slide thumbnails from 5 decks
✓ 00:35 — 14 images downloaded and copied to app/static/img/, candidates JSON created
✓ 00:37 — 4.1: 6 candidates | 4.2: 4 candidates | 4.3: 3 candidates | 4.4: 1 candidate
⏳ 00:38 — searching docs for additional images on external models, governance, and serving
✓ 00:50 — added 2 more images for point 4.4 from Agentbricks Roadshow (unified governance + external guardrails)
✓ 01:00 — verified all 16 images in place, JSON validated, all candidates properly structured

## Summary

Successfully completed illustration hunt for Chapter 4 (Model access and governance). Delivered 16 high-quality candidates across 4 points using deck thumbnails from internal Databricks presentations. Each point meets or exceeds the 3-candidate minimum.

All images sourced from Agentbricks Roadshow, Agent Bricks L300 Pitch Slides, Data Science With Databricks, GenAI on Databricks L200, and AI Gateway Product Deck. Images are clean diagrams and screenshots without WIP/draft markers; outdated product status notes added where applicable (fine-tuning UI).

Artifacts: app/static/img/ (16 PNG files) + .swarm/illus-hunt/cands-ch04.json

## Findings

### Point 4.1 — Model Serving (6 candidates) [4 diagrams + 2 screenshots]
- p4.1-serving-overview (diagram): Model Serving hierarchy with custom/foundation/agent models
- p4.1-provisioned-pt (diagram): Provisioned throughput endpoint capacity model  
- p4.1-serving-controls (screenshot): Governance controls (logging, compliance, cost, guardrails)
- p4.1-unified-serving (screenshot): Unified Model Serving UI for all model types
- p4.1-serving-production (screenshot): Production-ready serverless Model Serving features
- p4.1-ab-testing (screenshot): Online A/B testing and canary deployment strategies

### Point 4.2 — Foundation Models & Lifecycle (4 candidates) [2 diagrams + 2 screenshots]
- p4.2-fmapi-serving (diagram): FMAPI serving with access control architecture
- p4.2-external-models (diagram): External + Foundation models + agents routing through serving
- p4.2-gateway-models (diagram): External and Foundation models access through gateway
- p4.2-openai-models (screenshot): OpenAI GPT deployment through Databricks infrastructure
  (Note: slide carries internal guidance "do not lead with these details with customers")

### Point 4.3 — Model Fine-tuning (3 candidates) [1 diagram + 2 screenshots]
- p4.3-agent-runtime-arch (diagram): Agent Runtime infrastructure for model serving and deployment
- p4.3-fine-tuning (screenshot): Fine-tuning UI for company data (Databricks Confidential)
- p4.3-ai-runtime (screenshot): AI Runtime serverless GPU compute for training/fine-tuning

### Point 4.4 — External Models (3 candidates) [2 diagrams + 1 screenshot]
- p4.4-gateway-governance (diagram): AI Gateway governance for all models and agents
- p4.4-unified-governance (diagram): Unified data/AI governance with external agents (internal-only watermark)
- p4.4-external-guardrails (screenshot): Gateway integration with external partner guardrails

**Rejections:** p4.3-gpu-training (text-only Q&A slide, does not meet visual threshold)
**Quality applied:** All remaining images are diagrams or screenshots >600px. No WIP/draft markers except noted internal-only items. Mixed diagram/screenshot per point for visual variety.
