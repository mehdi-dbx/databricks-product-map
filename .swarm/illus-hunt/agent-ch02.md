# Agent ch02 — Chapter 2 illustrations (points 2.1–2.5)

**Status:** RUNNING · started 2026-10-11T20:45:00Z

## Plan (revised per coordinator feedback)
1. Search online docs (run/docs-inventory/pages.json) for each topic: Delta Lake, Lakeflow/DLT, Predictive Optimization, Lakebase, Lakehouse//RT, Unity Catalog, data quality
2. Fetch docs.databricks.com pages and extract images from /aws/en/assets/images/
3. Search databricks.com product pages and blog posts for announcements/diagrams
4. Replace off-topic candidates: 2.3 (remove agent/vector, add Lakebase transactional), 2.4 (remove serving/monitoring, add Lakehouse//RT)
5. Remove cross-chapter duplicates
6. Aim for 4-6 per point with mixed sources

## Timeline
⏳ 20:45 — Starting point extraction and deck search
✓ 20:50 — Downloaded 7 initial slides from Agent Bricks and Data Science decks
✓ 20:52 — Validated p2.1, p2.2, p2.3, p2.5 images as diagram-quality
✓ 20:58 — Downloaded 3 more slides + Lakeflow Connect tech deck slides
✓ 21:05 — Filtered by quality bar: rejecting text-heavy and non-visual slides
✓ 21:10 — Copied 13 images to app/static/img/ and built cands-ch02.json
✓ 21:12 — Finalized candidates with detailed sourcing and descriptions

## Findings

Point 2.1 (Delta Lake): 1 image
- p2.1-delta-architecture: Data Intelligence Platform overview from Data Science deck

Point 2.2 (Lakeflow, ingestion, transformation): 3 images
- p2.2-document-intelligence-pipeline: Complete workflow diagram showing Ingest → Transform → Orchestrate
- p2.2-ai-functions-transformation: SQL-based transformation showing declarative approach
- p2.2-data-ingestion-architecture: Multi-source ingestion patterns via Lakeflow Connect

Point 2.3 (Lakebase, transactional data, vector search): 3 images
- p2.3-agent-bricks-architecture: Agent Memory on Lakebase with Sandbox and tools integration
- p2.3-vector-search-pipeline: Document processing with embeddings and retrieval pipeline
- p2.3-agent-playground-tools: Agent app UI showing Vector Search MCP tool integration

Point 2.4 (Real-time analytics on operational data): 3 images
- p2.4-model-serving-architecture: Low-latency serving platform for models and agents
- p2.4-analytics-pipeline: Bronze/Silver/Gold layers with incremental processing for dashboards
- p2.4-lakehouse-monitoring: Data quality tracking and monitoring dashboard architecture
[Note: Specific Lakehouse//RT architecture diagrams limited in available decks; coverage uses related capabilities]

Point 2.5 (Unity Catalog, data quality, governance): 3 images
- p2.5-platform-governance: Central governance through Unity Catalog with permissions/lineage
- p2.5-service-policies-governance: Unity Gateway policy enforcement (ALLOW/ASK/DENY)
- p2.5-monitoring-quality: Data quality monitoring with profiling, drift, anomaly detection

Quality filtering applied: Rejected text-only slides, outdated product references, duplicate diagrams
All sources from internal Databricks decks (3 primary decks: Agent Bricks, Agentbricks Roadshow, Data Science, Lakeflow Connect)

## Summary

Successfully curated 13 high-quality illustration candidates across 5 points:
- **2.1 Delta Lake:** 1 diagram (Data Intelligence Platform overview)
- **2.2 Lakeflow:** 3 diagrams (pipeline workflow, SQL transformation, multi-source ingestion)
- **2.3 Lakebase:** 3 diagrams (agent memory architecture, vector search pipeline, agent tools UI)
- **2.4 Real-time analytics:** 3 diagrams (model serving, analytics pipeline, monitoring architecture)
- **2.5 Governance:** 3 diagrams (Unity Catalog governance, Service Policies, data quality monitoring)

All images copied to `/Users/mehdi.lamrani/code/Report/AmadeusAI/app/static/img/` with standardized naming (p<point>-<slug>.png) and all ≥ 600px width. Candidates documented in cands-ch02.json with source URLs and detailed descriptions.

⏳ 21:20 — Coordinator review: Off-topic candidates and cross-chapter duplicates identified
✓ 21:25 — Removed 7 off-topic/duplicate images (agent memory, model serving, monitoring)
✓ 21:30 — Searched docs.databricks.com: found fan-in/out, Lakebase architecture images
✓ 21:35 — Downloaded 5 doc images from architecture pages
✓ 21:40 — Downloaded 2 additional deck slides
✓ 21:45 — Built final candidates JSON with 13 images across points

## Blocker: Point 2.4 (Lakehouse//RT, LTAP, real-time analytics)
**Status:** ZERO candidates (0/4-6)
**Reason:** Lakehouse//RT and LTAP are new products with minimal published architecture diagrams in available sources. Searched:
- 50+ internal deck slides: No dedicated Lakehouse//RT architecture slides
- docs.databricks.com: found Lakehouse Real-Time overview page, but no architectural diagrams
- Product pages: databricks.com/product pages not directly accessible for image extraction
- Naming: Not called "Lakehouse//RT" in most decks; appears to be very recent announcement

**Attempted alternatives:**
- Real-time serving/deployment slides: refer to model serving (belongs to ch4)
- SQL warehouse slides: analytics/BI, not real-time operational
- Streaming architecture: Spark streaming, not Lakehouse//RT specific

**Recommendation:** Either (a) search published Lakehouse//RT announcement blogs/product pages directly via web search, or (b) note as coverage gap with explanation that product diagrams unavailable at publish time.

## Summary of changes per coordinator feedback
1. ✓ Removed cross-chapter duplicates (7 images)
2. ✓ Fixed point 2.3: replaced agent/vector with Lakebase transactional (3 doc images)
3. ✓ Added docs source images (5 from docs.databricks.com architecture pages)
4. ✓ Mixed sources: internal decks + docs + product pages (attempted)
5. ✗ Point 2.4: Could not locate specific Lakehouse//RT architecture diagrams

## Final candidates:
- **2.1 Delta Lake:** 2 images (deck + product usecases)
- **2.2 Lakeflow:** 5 images (deck + docs fan-in/out patterns + transformation)
- **2.3 Lakebase:** 3 images (all docs: architecture, monolith, write-path)
- **2.4 Lakehouse//RT:** 0 images (BLOCKER - product too new, diagrams unavailable)
- **2.5 Governance:** 3 images (deck governance + monitoring + gateway)

**Total: 13 candidates (9/13 viable, 4 needed for point 2.4)**
