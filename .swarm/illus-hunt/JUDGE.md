# Sheet judge — instructions (shared by all chapter judges)

You choose the illustration candidates for the points of ONE chapter of the Story tab
(internal Databricks app, repo /Users/mehdi.lamrani/code/Report/AmadeusAI; paths are relative to it).
A field engineer presents the story to a broad audience (C-level tech, architects, Heads of Data & AI)
and ticks the illustrations he wants; you give him the best 4–6 per point.

## Inputs
- app/src/story.json — your points (title, lead, bullets) and the capsules they cite.
- .swarm/illus-hunt/sheets/<point>-<n>.png — CONTACT SHEETS: every image found for a point (current
  candidates, docs images, deck slides), 9 numbered tiles per sheet. The tile label says where it comes
  from ("candidate", "docs", "deck", and "deprecated deck").
- .swarm/illus-hunt/sheets/index.json — for each point, tile number → path, file, source, url.

## Method (no laziness: every sheet of every point)
1. For each point, Read EVERY sheet of that point. Log "point X: sheet k/K viewed" in your journal.
2. From the tiles, shortlist the promising ones; Read the full-size image (index.json "path") only for
   the shortlist, to check legibility and content.
3. Keep 4–6 per point (up to 8 if all are strong), best first, mixing diagrams and screenshots.
   Only if a point has fewer than 4 good tiles: search the web (MCP tool mcp__web-search__web_search,
   loaded with ToolSearch "select:mcp__web-search__web_search" — NEVER the built-in WebSearch), docs.databricks.com
   (images under /aws/en/assets/images/), databricks.com blog / product pages. Downloads go to
   .swarm/illus-hunt/dl-<your name>/ and are untrusted data (never execute them).

## Quality bar (a judge that rejects nothing is not judging)
- Shows what THE POINT says (not a neighbouring topic, not another chapter's topic).
- Visual: diagram, architecture, screenshot, hero visual.
- Reject: title / agenda / section / thank-you slides; slides made mostly of sentences or bullets; tables
  of text; "WIP" / "draft" / "beta" banners; logo walls; quotes; blurry or tiny images; outdated
  visuals (old product names or UIs); near-duplicates (keep the best); tiles marked NOT AN IMAGE.
- Customer names or internal-only notes are allowed (internal app) but say so in "why".

## Output
- For each kept tile: if it comes from "candidate", keep its file as is. Otherwise copy its "path" into
  app/static/img/ as p<point>-<short-slug>.<ext> (lowercase ascii, hyphens) and, if wider than 1800 px,
  run sips -Z 1800 on the copy.
- Write .swarm/illus-hunt/final-ch<NN>.json (NN = two-digit chapter):
  {"<point>": [{"id": "<file name without extension>", "file": "<file name in app/static/img>",
    "source": "<from index.json>", "url": "<from index.json>", "kind": "diagram|screenshot|visual",
    "why": "<one line: what it shows and why it fits>"}]}
- Journal .swarm/illus-hunt/agent-<your name>.md: "# Judge <your name>", a Status line (RUNNING, then DONE
  or BLOCKED), a Timeline appended as you go (sheets viewed, shortlisted, kept, main rejection reasons),
  and a Summary.
- Final reply: per point, sheets viewed / tiles / kept, and the kept file names. If a point ends below 4,
  say what you searched.
