# Run — Databricks AI Tree (round 1: cartography)

**Goal:** map EVERYTHING Databricks does in AI, from DAIS 2026 → early Oct 2026, all sources.
Round 1 builds the **AI tree** (blocks → products/features). It will drive the doc hunt in round 2.

Started: 2026-10-07

## Agents (each logs live to its own file; never a black box)

| Agent | Sources | Live log | Tree output |
|-------|---------|----------|-------------|
| public | Public web: DAIS 2026, blog, docs.databricks.com | `agent-public.md` | `tree-public.md` |
| glean | Internal Glean (knowledge + Slack + Drive index) | `agent-glean.md` | `tree-glean.md` |
| sage | Sage Context Catalog (curated field assets) | `agent-sage.md` | `tree-sage.md` |

## Logging protocol (enforced on every agent)
- Create the log file first thing; append after EVERY tool call.
- Each entry: `[step N | HH:MM:SS] ATTEMPT …` then `[...] RESULT …` (ok/empty/error + counts).
- Log hangs/errors; max 2 retries per call; never silently loop.
- Flush as you go — the file must reflect live progress at any instant.

## Status
- [x] public — done (7 pillars, 50+ features; some names to verify)
- [x] glean — done (10+ layers, grounded with doc URLs; 1 glean_chat timeout, retried OK)
- [x] sage — done (110+ curated assets, real slugs + quality tiers + authors)
- [x] merge into unified AI tree (`AI-TREE.md`) — DONE

## Round 2 (next): doc hunt driven by AI-TREE.md
- Resolve canonical-deck authors via `mcp__glean__get_person`
- Pull & read the Gold decks per pillar; produce /doc skill cards
- Verify the open-queue items in AI-TREE.md
