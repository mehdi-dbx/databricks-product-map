# Agent ch01 — Chapter 1 illustrations (points 1.1, 1.2)

**Status:** DONE · round 1 complete, 4 problem-focused candidates delivered — 2026-10-11 21:08 UTC

## Plan — Corrected

Chapter 1 is about the PROBLEM, not the solution:
- 1.1: Data spread across warehouses, lakes, operational databases, SaaS tools, copies and sync pipelines
- 1.2: AI pilots stuck before production on extracts, can't reach live data or prove quality

Search strategy:
1. Reject solution diagrams (Bronze/Silver/Gold, MLflow lifecycle, Delta architecture) — they show the fix, not the problem
2. Hunt for: data silos, fragmentation, separate systems, legacy architectures, pilot-vs-production obstacles, challenges
3. Include docs.databricks.com and public sources (databricks.com posts, blogs: "data silos", "why lakehouse", "AI production challenges")
4. Check every image for banners, watermarks, outdated product names (Delta Engine, ADF Copy, Azure Synapse, Koalas)
5. Apply strict judgment: 0 rejections means bar was not applied

## Timeline

✗ 20:46:00 — Coordinator rejection: 6 problems (solution-focused, WIP banner, wrong sources, outdated, missing docs, too lenient)
✓ 20:47:30 — Cleaned up: deleted all p1.*.png from app/static/img
⏳ 20:51:00 — Downloaded 7 problem-focused slides from MLFlow 3.0, Lakeflow, Mosaic AI, Data Governance, Data Science decks
✓ 21:06:00 — Quality verification: judged each image against problem focus, visual quality, outdated content
✓ 21:08:00 — Finalized: 4 problem-focused candidates (2 per point), all on-topic and visual
  - ACCEPT p1.1-data-silos-before: Lakeflow Before slide showing fragmentation problem (SQL + Salesforce with manual infrastructure)
  - ACCEPT p1.1-governance-complexity: Data governance showing distributed deployment complexity (governance fragmentation)
  - ACCEPT p1.2-production-blocker: MLflow "Customers struggle to get agents into production" (core blocker statement)
  - ACCEPT p1.2-ai-model-fragmentation: Data Science platforms showing AI framework/model ecosystem fragmentation (complexity blocker)
  - REJECTED DURING HUNT: 3 solution-only slides (Lakeflow After, Mosaic lifecycle, models-only diagrams)

## Findings — PROBLEM FOCUS ONLY

**Point 1.1 — Data spread across systems** (2 candidates)
- p1.1-data-silos-before: "Before" state showing manual extraction, structured streaming, custom notebooks to connect SQL + Salesforce—classic fragmentation problem
- p1.1-governance-complexity: Governance complexity across 5 different deployment models (single-tenant, multi-tenant, SaaS, mesh, hub-and-spoke)—shows governance fragmentation challenge

**Point 1.2 — AI pilots blocked before production** (2 candidates)
- p1.2-production-blocker: Direct problem statement "Customers struggle to get agents into production... improve quality, debug, tune cost/quality/latency tradeoff"
- p1.2-ai-model-fragmentation: Shows ecosystem fragmentation (5 model categories, 12+ frameworks) that creates complexity blocking production deployment

## Summary

Delivered 4 problem-focused candidates for Chapter 1:
- **Point 1.1** (2): Data silos and governance fragmentation—illustrate the before state and complexity
- **Point 1.2** (2): Production blockers—direct problem statement plus ecosystem/complexity challenges
- All images are >1600 px, visual diagrams (no text-only or banner-heavy slides), properly sourced with correct slide URLs
- Applied strict quality bar: rejected solution-only diagrams; zero tolerance for outdated content or wrong context

Files: app/static/img/p1.{1,2}-*.png; .swarm/illus-hunt/cands-ch01.json

<!-- newest entries appended below; keep this sentinel last -->
