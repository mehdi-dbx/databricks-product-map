# Story tab — design (validated first shot, not built)

Status: built. Structure from the plan v2 (2026-10-17).

## Principle

A third tab, **Story**, next to the AI and DS trees. It is a continuous narrative read
by scrolling. It is not a slide deck.

The trees are the map. The Story is the guided route through the map.

## Structure

The plan is `docs/feature-tree.md`, version 2 of 2026-10-17. It sets the story's title, the overview (the
platform architecture), the 9 chapters, their 47 slides, the features of each slide and the appendix (the
capability map). The chapters follow the order of dependency: a slide only uses what earlier slides
introduced. `scripts/story_check.py` fails when `app/src/story.json` leaves the plan in any of these.

| # | Chapter | Slides |
|---|---------|--------|
| 1 | Data storage and movement | 4 |
| 2 | Unity Catalog | 6 |
| 3 | Data science and machine learning | 6 |
| 4 | Agent development | 9 |
| 5 | Observability and evaluation | 4 |
| 6 | AI governance and security | 6 |
| 7 | AI for business users | 8 |
| 8 | Developer tools | 2 |
| 9 | Vertical applications | 2 |

The v1 arc, 11 chapters that opened with "Challenges", is in the journal and in `docs/archive/`.

## Capsules

A slide cites, as cards, the capsules its sentences rest on. A slide whose features have no capsule in the
trees, such as Cost and usage or Data sharing, has no cards: its bullets come from the plan's own labels.

## Chapter content

- A short narrative text, written once.
- Capsule cards for the nodes the chapter covers. The cards are pulled from the tree
  JSON (name, status, note, without/with pairs). There is no copy of tree content: when
  a capsule changes in the tree, the Story shows the change.
- A "see in tree" link on each card. It switches to the tree tab and focuses the node
  (same behaviour as the Focus button).

## Visual

A sticky mini-map of the pillars on the side. The pillars of the current chapter light
up as the reader scrolls.

## Data

`app/src/story.json` is the only source of the Story's text, edited by hand. Its format is in
`docs/story-tools.md`. A node reference is tree + path (root → node names), the same convention
as the pipeline. `scripts/story_check.py` checks the file, and the build fails on any error,
including a reference that does not resolve to a node.

## Decisions

1. **Angle: generic.** The story is a generic Databricks story, with no claims about
   Amadeus (decided on 2026-10-08).
2. **Length: accepted as is.** The story is about 2,100 words, presented while
   scrolling. No further cut is needed (decided on 2026-10-08).

Until 2026-10-16 the Story was drafted in `story-notes.md`, now archived in
`docs/archive/`, and generated into `story.json`. Each link sentence became the `lead` of
the next point, so the text flows from point to point.

## Build plan

What the Story tab is, as described on 2026-10-08.

**v1 built on 2026-10-08, local only.** Everything below is in v1 except the pillar
mini-map. v1 has a chapter rail instead, which lights up the chapter being read. The
points render as slides: title, transition line, one bullet per sentence.
`app/build.py` embeds `story.json` and fails on any reference that does not resolve to a
tree node.

**What the user sees, in a third tab next to the two trees:**
- The story, chapter by chapter, read by scrolling. The text is the one in
  `app/src/story.json`.
- In each point, the capsules it cites, shown as small cards (name, status, note). The
  cards are pulled from the trees, so a change to a capsule in a tree shows in the
  Story.
- On each card, a "see in tree" link. It switches to the tree tab and centers on the
  capsule, like the Focus button.
- On the side, the list of pillars. The pillars of the chapter being read light up.

**What it touches in the code:**
- A new data file, `app/src/story.json`: chapters, point texts, and capsule references
  (tree + path).
- The tab rendering in `mindmap.js`, `styles.css` and `template.html`.
- A check in `build.py` that every capsule referenced by the Story exists in the trees.

## Related

- `panel-slide-spec.md` — capsule content shown in the cards.
- `pipeline-design.md` — the narrative text can later be generated and judged by the
  pipeline like any other field.
