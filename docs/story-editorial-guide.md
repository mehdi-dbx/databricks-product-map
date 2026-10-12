# Story editorial guide

These are the instructions for completing the points of the Story tab. Follow them exactly. The tools they use are described in `docs/story-additions-setup.md`.

The products are the core of the Story. Storytelling changes how they are told, not what is told.

- **Scope:** every point that cites capsules. Chapter 1 cites none, so it does not change.
- **Audience:** tech C-level, architects, Heads of Data and AI. Use plain words.
- **Source of the Story:** `docs/story-notes.md`. The tab reads `app/src/story.json`, which is generated from it.
- **Source of the facts:** the capsules in `app/src/ai-tree.json` and `app/src/ds-tree.json`.

## Conduct

- Act only on an explicit request.
- Before each step, say in French, in one line, what you are about to do.
- Write the Story in English, and talk in French.
- Do not ask about anything this guide already settles.

## Inputs

For each point of the chapter:

1. In `app/src/story.json`, read the point: `title`, `lead` (the transition), `bullets` and `refs`.
2. For each ref, open the capsule. `tree` names the file (`ai` or `ds`), and `path` lists the names from the root. Read its `note` and its `solves` rows. A row's `problem` is the "without" side, and its `solution` is the "with" side.

## Keep exactly as it is

- the point title
- the transition
- the bullets, word for word, as bullets
- the capsules and their cards
- the chapter's closing question

## Add three sentences

**Effect.** Write one sentence that goes under the title. It says what the product changes for the organization or for the people who use it.
- Source: `solution` rows or the `note`.
- A C-level reader must understand it without the bullets.
- It is never a slogan.

**Challenge.** Write one or two sentences that state the problem as any large organization has it.
- Source: `problem` rows only.
- Say who has the problem when the source says it.
- Keep it general: no scene, no meeting, no department, no person, no number.

**Pivot.** Write one short sentence that names the product, or the products, as the answer to the challenge.
- Source: the `note` or `solution` rows.
- It does not restate a bullet.

## Order on the slide

title → effect → transition → challenge → pivot → bullets → capsule cards. The added sentences have no labels and no box.

## Do not write

- a scene, a character or an example company
- a number or a fact that is not in the sources
- exaggeration, for example "spreads the confusion faster"
- slogans, taglines, refrains, or formulas such as "One set of rules: …"
- jargon a C-level reader would not know, unless you explain it
- a repeat of the transition or of a bullet, even in other words: the added sentence must say something the slide does not already say
- a near repeat of a sentence of chapter 1: chapter 1 announces, so the chapter's sentence gives the detail in other words
- a source row pasted as it is ("ACID transactions."): rows are notes, not sentences
- a pivot that only states that the product answers ("Lakeflow addresses this."): the pivot says how the product takes the problem on
- a number, even one taken from a source, unless the slide needs it

## Edge cases

- **No capsule of the point has `solves`, for example External connectors alone.** Leave the challenge and the pivot empty: a pivot answers a challenge. Write the effect only if it says something that the transition and the bullets do not. Otherwise leave it empty too. Say why in `report`. When other capsules of the point have rows, take the challenge from them.
- **The transition already states the problem.** Make the challenge add what the transition does not say.
- **The first bullet already introduces the product.** Keep the pivot short. It links the product to the challenge, without the bullet's facts.

## Output: `docs/story-additions.json`

Write one item per point, and keep the items of earlier chapters:

```json
{
  "chapter": 9,
  "point": "9.1",
  "effect": "…",
  "challenge": "…",
  "pivot": "…",
  "sources": {
    "effect": [{"ref": 0, "field": "solves[0].solution", "text": "…"}],
    "challenge": [{"ref": 0, "field": "solves[0].problem", "text": "…"}],
    "pivot": [{"ref": 0, "field": "note", "text": "…"}]
  },
  "report": ""
}
```

- `ref` is the 0-based index of the capsule in the point's `refs`.
- `field` is `note`, `solves[i].problem` or `solves[i].solution`, where `i` is the 0-based index of the row.
- `text` is the full content of that field, copied character for character, `**` markers included.
- When a sentence cannot meet these rules, leave it empty and say why in `report`.

## Process for a chapter

1. Wait for the chapter to be named.
2. Read the inputs of every point of the chapter.
3. Write the items into `docs/story-additions.json`. Give each source as its `ref` and its `field`, then let a script fill its `text` from the tree. Never type a source text by hand.
4. Copy the notes: `cp docs/story-notes.md /tmp/story-notes.before.md`.
5. Run `python3 scripts/apply_story_additions.py docs/story-additions.json --check` first.
   - Fix every refused item, or drop it.
   - Read every `WARN` line. Either fix the sentence, or keep it and say why in `docs/story-journal.md`.
   - Then run the command again without `--check`.
6. Check the result:
   - `diff /tmp/story-notes.before.md docs/story-notes.md | grep '^<'` prints nothing. After a rewrite, it prints only the old lines of the rewritten sentences and of their sources.
   - Read each point straight through. The transition, challenge, pivot and bullets form one line of thought.
   - Check each added sentence against "Do not write".
7. Run `python3 scripts/story_extract.py`, then `python3 app/build.py`.
8. Show the chapter:
   - in the chat, each point laid out like the examples below;
   - the link to the local `ai-tree-mindmap.html`, Story tab.
9. Wait for the verdict on each point.
   - A validated point is frozen.
   - For a rejected sentence, rewrite only that sentence, from the comment, then go back to step 4.
10. Start the next chapter only after this one is validated.

## Examples

### Application hosting (chapter 9). This is the reference.

> **Application hosting**
>
> Data and AI applications run on the platform itself, next to the governed data.
>
> A data or AI application usually runs on separate infrastructure, with its own identity management and secrets. It sits apart from the governed data, and access control and audit trails are hard to put in place.
>
> Databricks Apps brings these applications onto the platform.
>
> - Developers build applications with the frameworks they already use, such as Streamlit, Gradio, React or FastAPI, and deploy them as Databricks Apps.
> - The apps run serverless on the platform.
> - They sign users in with the platform's identity and read data through Unity Catalog with each user's permissions.
> - Custom MCP servers run the same way.
> - App Spaces give admins one place to govern who deploys and uses which app.

```json
{"chapter": 9, "point": "9.1",
 "effect": "Data and AI applications run on the platform itself, next to the governed data.",
 "challenge": "A data or AI application usually runs on separate infrastructure, with its own identity management and secrets. It sits apart from the governed data, and access control and audit trails are hard to put in place.",
 "pivot": "Databricks Apps brings these applications onto the platform.",
 "sources": {
  "effect": [{"ref": 0, "field": "solves[0].solution", "text": "**Serverless Databricks Apps** eliminate external hosting costs and complexity"},
             {"ref": 0, "field": "solves[3].solution", "text": "Native **Unity Catalog integration** for permissions-aware data access"}],
  "challenge": [{"ref": 0, "field": "solves[0].problem", "text": "Apps require **separate infrastructure** outside Databricks platform"},
                {"ref": 0, "field": "solves[2].problem", "text": "Apps require **separate identity management** and secrets handling"},
                {"ref": 0, "field": "solves[3].problem", "text": "Apps **isolated** from governed data lake"},
                {"ref": 0, "field": "solves[1].problem", "text": "App-level access control and **audit trails** difficult to implement"}],
  "pivot": [{"ref": 0, "field": "note", "text": "Databricks Apps hosts interactive data and AI apps on Databricks, governed by Unity Catalog."}]},
 "report": ""}
```

### Natural-language questions on company data (chapter 8)

> **Natural-language questions on company data**
>
> Business users get answers from company data without writing SQL.
>
> Most people who need data do not write SQL. Their questions queue up at the data team, and the answer often comes after the decision.
>
> Genie One gives them a front door to the data.
>
> - Genie One lets business users ask questions in plain language.
> - They get answers from governed company data, with citations and with their own permissions applied.
> - When a dashboard or an agent already answers the question, Genie One sends the user there.

```json
{"chapter": 8, "point": "8.1",
 "effect": "Business users get answers from company data without writing SQL.",
 "challenge": "Most people who need data do not write SQL. Their questions queue up at the data team, and the answer often comes after the decision.",
 "pivot": "Genie One gives them a front door to the data.",
 "sources": {
  "effect": [{"ref": 0, "field": "solves[1].solution", "text": "Users **answer** ad-hoc questions directly without SQL or waiting"}],
  "challenge": [{"ref": 0, "field": "solves[0].problem", "text": "Business users **blocked** by technical Databricks interface"},
                {"ref": 0, "field": "solves[1].problem", "text": "Analyst **dependency** for every data question"}],
  "pivot": [{"ref": 0, "field": "solves[0].solution", "text": "Simplified, non-technical **front door** with natural language chat"}]},
 "report": ""}
```

### Control of AI traffic with Unity Gateway (chapter 7): a point with a transition

> **Control of AI traffic with Unity Gateway**
>
> Every model and tool call is controlled and logged in one place.
>
> *The catalog sets who may use each asset. Each model call and each tool call also needs control at the moment it happens.*
>
> Each team connects to model providers on its own, so nobody sees who calls which model or what it costs. Prompts and responses go through without guardrails, and nothing is logged for an audit.
>
> Unity Gateway puts this traffic under one control plane.
>
> - Unity Gateway sits in front of all model and tool traffic and is built on Unity Catalog.
> - It sets who may call which model and tracks usage per user and team.
> - Budgets cap spend.
> - Guardrails apply to every prompt and response, and every request is logged for audit.

The transition already says that each call needs control. The challenge does not repeat it: it says what is missing without a gateway.

```json
{"chapter": 7, "point": "7.2",
 "effect": "Every model and tool call is controlled and logged in one place.",
 "challenge": "Each team connects to model providers on its own, so nobody sees who calls which model or what it costs. Prompts and responses go through without guardrails, and nothing is logged for an audit.",
 "pivot": "Unity Gateway puts this traffic under one control plane.",
 "sources": {
  "effect": [{"ref": 0, "field": "solves[0].solution", "text": "**one control plane** fronts every provider"},
             {"ref": 0, "field": "solves[4].solution", "text": "every request and response **logged**"}],
  "challenge": [{"ref": 0, "field": "solves[0].problem", "text": "**self-managed** per provider"},
                {"ref": 0, "field": "solves[1].problem", "text": "**no central view** of who calls what"},
                {"ref": 0, "field": "solves[2].problem", "text": "**spend** grows unchecked"},
                {"ref": 0, "field": "solves[3].problem", "text": "**no guardrails** on prompts and responses"},
                {"ref": 0, "field": "solves[4].problem", "text": "**no audit** for compliance"}],
  "pivot": [{"ref": 0, "field": "solves[0].solution", "text": "**one control plane** fronts every provider"}]},
 "report": ""}
```

## Delegating to agents

Writing these sentences takes judgment that the rules alone do not carry. If agents write them:

1. Give each agent the prompt below, word for word. Fill in its chapter, its points and its output file.
2. Start with one agent on one chapter. Review its output, and only then hand out the other chapters.
3. Do not accept an output because `--check` passes. The check proves that the sources exist, not that the sentences are good. Review every item against this guide and rewrite the weak ones.

In the first run, on 2026-10-11, three agents were given only this guide and a summary of the rules. All three had to be rewritten:
- they pasted source rows as sentences;
- one of them generated its sentences with a script and wrote pivots in the form "X addresses this";
- they restated bullets;
- they invented a duration.

The prompt below is written against those faults.

On 2026-10-12 a pilot ran with this prompt on chapter 4, on a clean copy of the repository with no sentence already written. Its `--check` passed with no warning, and review still found four faults:
- an effect that reworded a bullet (4.1);
- a challenge with a fact no source states, "requires substantial rework" (4.2);
- a pivot that named no product of its point (4.2);
- a pivot that named a product of another point (4.3).

The script now flags pivots that name no product of their point. The other faults need review.

The conclusion is that agents write drafts. The main session reviews every item and rewrites it before applying, or writes the chapter itself.

### Agent prompt

```
You add three sentences to each point of a chapter of the Story tab of an internal
Databricks field app. Repository: /Users/mehdi.lamrani/code/Report/AmadeusAI. Work from its root.

Chapter: {N}. Points: {ids} ({count} points). Output file: /tmp/story-additions-ch{N}.json.

1. Read docs/story-editorial-guide.md entirely before writing: rules, examples and
   counter-examples. Ignore its "Conduct" and "Process for a chapter" sections: they are for
   the main session. This prompt is your task.
2. Print your inputs with a short script, and use the script for nothing else:
   - for each point of app/src/story.json: its title, its lead, its bullets and its refs;
   - for each ref, with its 0-based index: the capsule's note, and every solves row with its
     index (problem and solution), from app/src/ai-tree.json or app/src/ds-tree.json;
   - the bullets of chapter 1.
3. Write every sentence yourself. Never let a script write or assemble a sentence.
   Some points may already have an effect, a challenge or a pivot, in app/src/story.json,
   docs/story-notes.md or docs/story-additions.json. Do not read them, and do not reuse them.
   Write your own.
4. For each point, write the effect, the challenge and the pivot. Follow the guide's
   "Add three sentences", "Do not write" and "Edge cases" sections.
   - The effect is a full sentence about what changes for the organization or its users.
   - The challenge states the problem in full sentences, from problem rows only.
   - The pivot says how the product takes that problem on. "X addresses this" is not a pivot.
   - A solves row is a note, not a sentence: never paste one.
   - Never restate a bullet or the lead in other words. Never come close to a sentence of
     chapter 1. Never use a number.
5. Write each source as its "ref" and its "field", then let a script fill its "text" from
   the tree.
6. Before you hand anything in, check each point. Read it in slide order: title, effect, lead,
   challenge, pivot, bullets. For each of your sentences, write one "adds:" line that names the
   precise fact or angle the sentence brings and that neither the lead nor the bullets state.
   A generic line such as "what the organization gains" does not count. If you cannot name
   one, rewrite the sentence.
7. Run: python3 scripts/apply_story_additions.py /tmp/story-additions-ch{N}.json --check
   It writes nothing. It must report "refused 0". For every WARN line, either rewrite the
   sentence, or keep it and say why in the item's "report".
8. Do not change any file in the repository. Do not run story_extract.py, build.py, or
   apply_story_additions.py without --check. Another session is editing the repository.

Return:
- the output file;
- the full --check output;
- for each point: its title, then your three sentences in slide order, each followed by
  its "adds:" line, then its first bullet.
```

## Counter-examples

Each of these broke a rule in an earlier draft.

| Draft | Problem | Rule broken |
|---|---|---|
| The title replaced by "Business questions answered without waiting for the data team" | The product is no longer the title. | Keep the title. |
| "In a meeting, two departments bring two different figures for the same KPI. An AI that picks the wrong definition spreads the confusion faster." | An invented scene, and a claim that no source supports. | No scene, no exaggeration. |
| "One set of rules: each person sees only what their Unity Catalog permissions allow." | A refrain line written as a formula. | No refrains or formulas. |
| The five bullets of Application hosting merged into one paragraph | The slide is harder to read, and the list effect stays. | Keep the bullets. |
| "Budgets cap spend." rewritten as "caps spend with budgets", and "with their own permissions applied" dropped | Validated, fact-checked text was rewritten, and a fact was lost. | Rewrite nothing that exists. |
| Effect "ACID transactions.", challenge "Data corruption mid-stream. Enforcement breaks on change." | Source rows pasted as they are. | Write sentences. |
| Pivot "Lakehouse / Delta Lake addresses this." | A formula that says nothing. | The pivot says how the product takes the problem on. |
| Effect "A supervisor agent breaks down large tasks across specialized agents while maintaining each user's data permissions" | The first bullet, reworded. | No repeat of a bullet. |
| Challenge "New applications usually need weeks to build" | No source gives a duration. | No fact outside the sources. |
