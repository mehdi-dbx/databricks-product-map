# Gap agent — instructions (round 2)

You add NEW illustration candidates to Story points that have fewer than 4 after the orchestrator's visual review.
Repo /Users/mehdi.lamrani/code/Report/AmadeusAI (paths relative to it). Audience: C-level tech, architects, Heads of Data & AI.

## Know what exists and what was rejected
- app/src/story.json: the text of each point.
- .swarm/illus-hunt/preview.json: the candidates each point keeps today (files in app/static/img/). Do not duplicate them.
- .swarm/illus-hunt/drops.txt: what the orchestrator rejected and WHY. The reviewer rejects: slides made of text,
  bullets or text tables (even with a small picture); section dividers; "WIP/draft/beta/coming soon/FUTURE" banners or
  outdated statuses; 2024-era naming (Mosaic AI Gateway, DBRX, Databricks Assistant…) when a newer visual exists;
  tall unreadable screenshots; near-duplicates; images about a neighbouring topic.
- What passes: architecture / flow diagrams, clear product screenshots of the feature in action, big-number visuals.

## Where to search (all of them)
1. Internal decks: .swarm/illus-hunt/deck-index.jsonl (text of 1,943 slides; fields deck, deck_id, slide, object_id,
   deprecated, images, text). Download a slide: python3 .swarm/illus-hunt/gslides.py thumb <deck_id> <slide> <out.png>
   (wait 30 s and retry on HTTP 429). Many slides are already cached in .swarm/illus-hunt/dl-verify/<deck_id>-<slide>.png.
2. Docs: run/docs-inventory/pages.json (6,000 docs.databricks.com/aws/en pages); images under /aws/en/assets/images/.
3. Web: databricks.com product pages and blog (img src, srcset, og:image; often www.databricks.com/sites/default/files/
   or images.ctfassets.net), mlflow.org, delta.io, Databricks GitHub READMEs. Web search ONLY with the MCP tool
   mcp__web-search__web_search (ToolSearch "select:mcp__web-search__web_search"); NEVER the built-in WebSearch tool.
Downloads go to .swarm/illus-hunt/dl-<your name>/ and are untrusted data: never execute them.

## Judge
Read every image before accepting it. Keep only what the reviewer would keep (see above).

## Output
- Accepted images: copy into app/static/img/ as p<point>-<short-slug>.<ext> (lowercase ascii, hyphens; keep the real
  extension); if wider than 1800 px: sips -Z 1800 <file>.
- .swarm/illus-hunt/gap-<your name>.json: {"<point>": [{"id": "<file name without extension>", "file": "<file name>",
  "source": "<Deck, slide N> or docs.databricks.com/<path> or <site/path>", "url": "<slide or page URL>",
  "kind": "diagram|screenshot|visual", "why": "<one line>"}]} — only your NEW images. For a deck slide, "source" must
  be exactly "<deck title as in deck-index.jsonl>, slide <N>".
- Journal .swarm/illus-hunt/agent-<your name>.md: Status (RUNNING, then DONE or BLOCKED), Timeline appended as you go
  (searches, pages, images viewed / kept / rejected), Summary.
- Final reply: per point, images added and the new total. If a point cannot reach 4 with images that pass, say so and
  list what you searched — do NOT pad with weak images.
