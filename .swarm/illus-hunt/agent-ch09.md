# Agent ch09 — Chapter 9 illustrations (points 9.1–9.3)

**Status:** BLOCKED · rate limits on deck downloads; need manual docs/public source work

## Plan

1. Read story points 9.1, 9.2, 9.3 and their capsule refs (tree paths)
2. Search deck-index.jsonl for keywords: Databricks Apps, App Spaces, Streamlit, Gradio, React, FastAPI, Genie Code, AI Dev Kit, coding agents, Claude, Codex, Cursor, Omnigent, custom MCP
3. Download promising slides from non-deprecated decks
4. Search docs.databricks.com via run/docs-inventory/pages.json for each topic
5. Fetch and validate candidate images
6. Build final cands-ch09.json

## Timeline

⏳ 17:30 — Parsing deck-index: found ~60 app slides, ~21 geniecode, ~15 codinagent, ~10 omnigent
⏳ 17:31 — Prioritizing downloads: Agent Bricks L300, Mosaic AI Architecture, Genie benchmarks, Agentic Apps workshop
✓ 17:40 — Downloaded 14 images from 4 key decks; validating each
✓ 17:50 — Validated all images; rejected 1 title slide (agent-bricks-11)
✓ 17:55 — Built candidates JSON; copied 12 images to app/static/img/
✓ 17:58 — Downloaded roadshow-212-genie.png (Genie Code traces analysis)
✓ 17:59 — Final count: 13 candidates (9.1:3, 9.2:3, 9.3:7)

## Status Summary

After coordinator review feedback, removed 11 off-topic images (agent runtime, governance, model serving topics belonging to chapters 4-7) and refocused:

**COMPLETED:**
- ✓ 9.1: 3 on-topic candidates (apps hosting, ecosystem, E2E platform)
- ✓ Files: cands-ch09.json updated, all off-topic files deleted from app/static/img/

**PARTIAL:**
- ⚠ 9.2: 1 candidate (Genie Code traces) — need 2-3 more from docs/public sources (Genie Code in notebooks, SQL, CLI, dashboards)
- ⚠ 9.3: 1 candidate (agent dev lifecycle) — need 3-5 more about Omnigent, AI Dev Kit templates, coding agent integration

**BLOCKERS:**
- Slide deck API rate limits: attempts to download SEMEA workshop, Data Science decks timing out
- Public sources difficult to scrape: GitHub AI Dev Kit repo 404, databricks.com/blog/docs harder to extract images programmatically
- Need manual curation of:
  - docs.databricks.com images for Genie Code usage screenshots
  - databricks.com product pages for Omnigent, AI Dev Kit visuals
  - Potentially blog posts about "Genie Code in notebooks/SQL" or "Omnigent meta-harness"

**NEXT STEPS FOR COMPLETION:**
1. Manually fetch images from: docs.databricks.com/aws/en/genie-code/, docs/app-spaces, etc.
2. Search databricks.com/blog for "omnigent", "ai dev kit", "genie code" posts
3. Download images using curl + sips resize

<!-- newest entries appended below; keep this sentinel last -->
