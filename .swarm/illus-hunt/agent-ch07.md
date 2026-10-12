# Agent ch07 — Chapter 7 illustrations (points 7.1–7.3)

**Status:** BLOCKED · Point 7.3 requires additional images; 7.1 & 7.2 have minimum candidates

## Plan
1. Read story points 7.1, 7.2, 7.3 and resolve tree references
2. Get docs links from ai-tree.json and ds-tree.json
3. Search deck-index.jsonl for governance, Unity Catalog, Unity Gateway, DASF, guardrails, security framework
4. Fetch docs pages and extract images
5. Search public sources (databricks.com, DASF whitepaper, blog, GitHub)
6. Download and validate all candidates (min 3 per point)
7. Write final cands-ch07.json

## Timeline
<!-- newest entries appended below; keep this sentinel last -->
⏳ 00:00:10 — searching deck index for governance, Unity Catalog, Unity Gateway, DASF slides
✓ 00:00:12 — found: 335 governance slides, 277 Unity Catalog, 12 Unity Gateway, 59 guardrails; dedicated DASF deck located
✓ 00:02:00 — downloaded and validated UC hierarchy + Gateway architecture from docs.databricks.com
✓ 00:03:00 — extracted Governance Hub images (overview UI + AI dashboard with metrics)
✓ 00:04:00 — created cands-ch07.json with 4 validated images (2 per point for 7.1, 7.2)
✓ 00:04:30 — final search for DASF/security: identified source decks & slides; blocked by download constraints

## Findings
- **7.1** (Unity Catalog for AI assets): ✓ 2 images
  - p7.1-unity-catalog-hierarchy.png (UC namespace: Metastore→Catalog→Schema→Assets; shows Models, Functions, Services, Secrets)
  - p7.1-governance-hub-overview.png (Governance Hub UI: central control plane for workspace admin)
- **7.2** (Control of AI traffic with Unity Gateway): ✓ 2 images
  - p7.2-unity-gateway-architecture.png (Gateway control flow: auth→OBO→authz→execute; multi-provider with single plane)
  - p7.2-ai-governance-dashboard.png (Observability: usage (48.5B tokens), governed traffic (17%), budgets, spend ($14.2K/30d))
- **7.3** (AI security risks & controls / DASF v3.0): ✗ 0 images (BLOCKED)
  - Identified sources: DASF blog, DASF presentation deck (1jQ_4m... slide 6, 18 images), Agent Bricks L300 (slide 20), Agentbricks (slide 156)
  - Blocker: image download constrained by network/gslides API auth. Recommend: gcloud auth or DAIS conference materials

## Summary
- **Point 7.1**: 2/3 minimum (want 1-4 more from Agent Bricks or Agentbricks deck slides showing permissions, lineage, audit)
- **Point 7.2**: 2/3 minimum (want 1-4 more from Product deck AI Gateway or Mosaic AI architecture slides)
- **Point 7.3**: 0/3 MINIMUM — BLOCKED. Needs 3-6 images from DASF framework, security controls, guardrails, agent-specific risks. Best sources are DASF presentation deck and Agent Bricks slides with security content.

## Artifacts
- Validated images: 4 PNG files in app/static/img/p7*
- Candidates JSON: .swarm/illus-hunt/cands-ch07.json (includes source recommendations)
- Download directory: .swarm/illus-hunt/dl-ch07/ (working files)

## Quality Notes
- All 4 images: non-deprecated, clear visual content (diagrams/dashboard screenshots), directly relevant to stated point topic
- No WIP/draft/internal-only banners detected
- 3/4 from official docs.databricks.com; 1/4 from internal presentations (both GA/current as of 2026)
- Duplicates removed; all unique content
