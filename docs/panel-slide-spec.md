# Panel mini-slide — design spec (living document)

Status: in progress, still refining. This captures every decision made so far so we
don't re-litigate settled points.

## Node schema — what every population pass must fill

Every node carries these fields. New enrichment passes assign them **at population
time**, not retroactively.

- `n` — name.
- `note` — the intro sentence (what it is). One line, no "What is it" label.
- `type` — capsule archetype (REQUIRED on every d2+ node). Enum:
  - **feature** — a shippable Databricks product/feature (Unity Gateway, Model
    Serving, AI Search). Panel = problem/solution `solves` block + `matrix`.
  - **family** — an umbrella grouping concrete sub-products/tools. Panel = what's
    inside (the children), not a pitch.
  - **primitive** — a brick / function / API / fine-grained capability (usually a
    leaf). Panel = what it does + an example.
  - **concept** — a capability, practice, or framework with no shippable bundle
    (e.g. DASF, a lifecycle note). Panel = short descriptive text.
- `solves` — array of `{axis, problem, solution}` for the problem/solution block.
  Fill for **feature** type. `**bold**` in problem/solution marks keywords.
- `matrix` — a compete matrix (see `compete-matrix.schema.json`). Fill for
  **feature** type when a competitive field exists. Internal content; shown via the
  app-mode toggle. The app is internal-only.
- `docs`, `since`, `deck`, `s` (status), `c` (confidence), `new` — as before.

The `type` drives which panel template renders. A pass that adds a node without a
`type` is incomplete. Default classification rule when judgment is unclear: d2 =
feature unless it clearly groups distinct products (family) or has no shippable
bundle (concept); d3+ = feature if it has children, primitive if it is a leaf.

## Purpose

Each node in the ecosystem tree (AI and DS) opens a panel at the bottom. That panel
is a **mini-slide**: a presentation support for showing a Databricks feature to
customer stakeholders. It is not a tooltip and not a description. The tree already
shows the structure and the names; the panel carries what the tree cannot.

## Audience lens (hidden grid, never printed on the slide)

Used only to judge whether a slide is complete. Not shown as sections.

- What is it
- What it solves — the pain / the need
- How — the solution and the capabilities

The buyer, who may already have tooling, also silently asks:
- how does this compare to what I already have (DIY or a competitor)
- what does it cost me to adopt (dependency, migration, lock-in)

## Writing rules (hard constraints)

- **English** for all slide content.
- **No announcing section titles.** A heading like "What it solves" placed before
  the problem is redundant — the text itself does the job. Labels that only name
  what the content obviously is get cut.
- **No prose paragraphs** for the body. Short ideas, bullet form.
- **No litanies / no long enumerating lines.** Keep each line short.
- **No slop** (the `/noslop` skill is active for the whole session). In particular:
  no antithesis (two mirrored clauses split by a dash or semicolon), no rule of
  three padding, no aphoristic closers, no meta-narration.
- **Must be clear read cold, with zero context.** Every element carries its own
  status. A neutral list of problems under a product name is ambiguous (reads as
  the product's own limitations), so status is carried by a visual device, not by
  a word or a label.
- **Grounded in docs** (docs.databricks.com / Glean). No invented benefits.
- **Consolidate, never overwrite.** Each refinement adds to the validated base.
  Settled elements are not rewritten unless explicitly rejected.

## Panel structure

The panel has **tabs**:

- **Main tab** — the mini-slide (below).
- **Landscape tab** — competitive positioning: DIY alternatives and competitors
  (e.g. Kong, Portkey, Azure), and the displacement angle. Kept off the main face
  so it never reads as an out-of-nowhere competitive jab.

### Main tab layout

Top: title + status chip, then one intro sentence (what it is).

Then a **three-column problem/solution block**:

- **Left column** — the pain, "without the tool" (red).
- **Center column** — the axis word for each row (always full opacity, anchors both
  sides).
- **Right column** — "with the feature" (green).

**Every red (left) must be addressed by a green (right) on the same row.** The
columns are aligned pairwise; a left item without a matching right item, or a right
item that answers no left item, is a defect.

### Toggle interaction

A single real on/off toggle controls the block (one toggle, one panel — not two).

- **OFF (default)** = problem view. Left column full opacity, right column
  translucent (still legible, just dimmed).
- **ON** = solution view. Right column full opacity, left column translucent.
- The toggle's colour (red/off, green/on) and position carry the state. No "red" /
  "green" text label next to it — that would double-encode.
- The center axis column stays full opacity in both states.
- Translucent, not hidden, so the before/after is visible at a glance. (Open: could
  switch to fully hidden instead.)

Rationale: the toggle is the presenter's before/after storytelling control. Start on
the pain, flip live to show how the feature resolves it.

### Placeholders (future run)

- **Visual** — architecture diagram or product screenshot, for features where words
  undersell it.
- **Proof** — a named customer reference.

Both are planned slots, populated in a later pass, not now.

## Reference example — AI Gateway (Unity Gateway)

Title: 🔴 AI Gateway · *Unity Gateway*  ·  status `GA`

Intro: Databricks' governance layer for AI, built on Unity Catalog.

Three-column block:

| 🔴 without the tool | axis | 🟢 with AI Gateway |
|---|:---:|---|
| own keys and limits per provider | **Access** | one control plane fronts every provider |
| no central view of who calls what | **Visibility** | usage tracked per user and team |
| spend grows unchecked | **Cost** | budgets cap spend centrally |
| no guardrails on prompts and responses | **Guardrails** | policies applied on every request |
| no audit for compliance | **Audit** | every request and response logged |

Docs: https://docs.databricks.com/aws/en/ai-gateway/

All five capabilities are grounded in the AI Gateway doc page (access control,
observability via system tables, budgets, guardrail policies, request/response
auditing).

## Open points (to settle next)

- Where the **adoption** point ("apps keep their serving endpoint calls, no app
  change") lives. It answers no red, so it does not fit the pair block. Candidates:
  a single line under the block, or the Landscape tab.
- Translucent vs fully hidden for the inactive column.
- Default state OFF (problem) vs ON (solution) — currently OFF.
- Whether the `GA` status chip stays on the slide; that discussion was deferred.

## Scope reminder

When this is settled, the content pass applies the structure across the tree, under
`/doc /swarm /scan /dontstop`: every capsule and feature grounded in docs, verified,
no fabrication, full tally.
