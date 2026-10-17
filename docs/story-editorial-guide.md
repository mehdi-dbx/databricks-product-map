# Story editorial guide

These are the instructions for completing the points of the Story tab. Follow them exactly. The file format and the tools are described in `docs/story-tools.md`.

The products are the core of the Story. Storytelling changes how they are told, not what is told.

- **Scope:** every point of every chapter.
- **Plan:** `docs/feature-tree.md` sets the chapters, the slides, their titles and their features. `scripts/story_check.py` fails when `app/src/story.json` leaves it.
- **Audience:** tech C-level, architects, Heads of Data and AI. Use plain words.
- **Source of the Story:** `app/src/story.json`, edited by hand. It is the only file that holds the Story's text. Each point also holds, in its `sources` key, the sources of its effect, challenge and pivot.
- **Source of the facts:** the capsules in `app/src/ai-tree.json` and `app/src/ds-tree.json`, and the plan's own labels, such as "Zerobus Ingest (event ingestion)".

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

- the transition
- the bullets, word for word, as bullets
- the capsules and their cards
- the slide's title, which comes from the plan

## Title

The title is the slide's label in the plan, word for word, with two exceptions:
- the plan's verification markers never show: "Online Feature Stores (to verify: GA status)" shows as "Online Feature Stores", and "Genie Ontology (business context layer, not verified: no docs page)" as "Genie Ontology (business context layer)";
- a slide's title leaves out the plan's "(see …)" pointer: "No-code agents: Genie Agents (see AI for business users)" shows as "No-code agents: Genie Agents".

A new title starts in the plan, on request. The plan's own title rules are in `docs/feature-tree.md`, point 7.

## Bullets and the plan

- The bullets cover the slide's features, in the plan's order.
- A feature that no capsule describes gets a bullet from its label in the plan, and nothing more. "Zerobus Ingest (event ingestion)" gives "Zerobus Ingest brings in event data."
- A product that the plan does not list does not appear, even when a capsule has it. For example, Row Zero, Lakebase Search and MLOps Stacks are not in the plan.
- A product that the plan marks as legacy or removed does not appear. Use the plan's current names: Feature Engineering in Unity Catalog, Models in Unity Catalog, Data Quality Monitoring, Declarative Automation Bundles.
- When the pivot's product is not the slide's first feature, the first bullet refers back to it, as in "ai_prep_search first splits the documents into chunks and prepares them for it." after "**AI Search** fixes this…".

## Add three sentences

**Effect.** Write the line that goes under the title: what the product changes, in one short line. A C-level reader must understand it without the bullets.
- Source: `solution` rows or the `note`.
- Write a short formula that starts with a verb, such as "Apply AI to large volumes of data and documents in place." or "Build features once & reuse them across teams and models." Or write one short, complete sentence with a concrete subject, such as "Dashboards and applications read live data instead of a stale copy."
- Never start with a generic subject such as "Teams", "The company" or "Developers". These repeat from slide to slide and add nothing.
- Write in the affirmative. "Training is no longer limited by hardware" is wrong, and "Train at any scale, with GPUs on demand." is right.
- Use plain words. "Replies draw on…" is too contrived, and "Retrieve targeted data from documents, based on checked sources." is right.
- Keep it short. A laborious line such as "Operators see inside every request, step by step, including what it costs." becomes "Trace request details and cost, step by step."
- It is never a slogan.

**Challenge.** State the problem as any large organization has it, with one problem per sentence. Each sentence shows as a bullet, because the Story serves as presentation slides.
- Source: `problem` rows only.
- Say who has the problem when the source says it.
- Keep it general: no scene, no meeting, no department, no person, no number.

**Pivot.** Write one short sentence whose subject is the product: it starts with the product's name, in bold, and says how the product takes the problem on. Never start with "With". Every pivot takes this form. The product's name then appears only once: the first bullet does not name it again.
- Write the bold as `**…**`. The Story tab and the PDF show it in bold.
- When the name takes an article, the article stays outside the bold: "The **Model Context Protocol (MCP)** lets every connection be governed in one place instead.".
- Source: the `note` or `solution` rows.
- Example: "**MLflow** makes every step visible." is followed by "It traces every request through the agent.", not by "MLflow traces every request through the agent.". In the same way, "**Model Serving** runs them all in one place." is followed by "Its endpoints run the registered version…".
- In the point's `bullets` in `app/src/story.json`, change only what repeats the name in the first bullet. The rest of the bullet stays word for word.
  - If the first bullet starts with the name, it starts with "It", "They" or "Its" instead.
  - If it names the product further on, the name goes: "deploy them as Databricks Apps" becomes "deploy them", and "open Delta tables" becomes "open tables".
  - If it does not name the product, it stays as it is.
- On a slide with two products, the pivot names the product of the first bullet, as in "**Lakebase** now keeps that data next to the analytics, under the same rules." on "Transactional and real-time data". The other product, Lakehouse//RT, keeps its name in its own bullet.
- Do not credit that product with the other one's work. On "Training compute", AI Runtime provides the GPUs, so the pivot is "**Databricks Runtime for Machine Learning** takes much of that work off the team.", and the GPUs stay in AI Runtime's bullet.
- Ordinary words that the name contains may stay, such as "lakehouse tables" after "**Lakehouse//RT** …".
- It does not restate a bullet.

## Keywords in the bullets

Bold the keyword of some bullets, in `app/src/story.json`, as `**…**`, so the slide reads at a glance. Keep a light hand:
- about two bullets out of three get one. A first pass at one in two was judged too light;
- at most one per bullet. A bullet that only links or introduces, such as "It holds those definitions.", gets none;
- a short phrase that carries the bullet's fact, such as "open tables", "down to zero" or "logged for audit", never a whole clause;
- not the product's name already in bold in the pivot.

## Order on the slide

title → effect → transition → challenge → pivot → bullets → capsule cards. The challenge sits in a box labelled "Challenges". The effect and the pivot have no label and no box. A text of two or more sentences (a transition, a challenge, a chapter's closing question) shows one bullet per sentence, with a small black dot. The product bullets keep their red dots.

## Do not write

- a scene, a character or an example company
- a number or a fact that is not in the sources
- exaggeration, for example "spreads the confusion faster"
- slogans, taglines, refrains, or formulas such as "One set of rules: …"
- jargon a C-level reader would not know, unless you explain it
- a repeat of the transition or of a bullet, even in other words: the added sentence must say something the slide does not already say
- a source row pasted as it is ("ACID transactions."): rows are notes, not sentences
- a pivot that only states that the product answers ("Lakeflow addresses this."): the pivot says how the product takes the problem on
- a number, even one taken from a source, unless the slide needs it
- a term repeated from the line just before or just after, when a pronoun or another word would do. Example: "Pipelines move data between them to keep the copies in sync." is followed by "They are written and scheduled by hand…", not by "These pipelines are written… and the copies they feed…". Product names and the slide's subject may repeat, except the product's name between the pivot and the first bullet.

## Edge cases

- **No capsule of the point has `solves`, for example External connectors alone.** Leave the challenge and the pivot empty: a pivot answers a challenge. Write the effect only if it says something that the transition and the bullets do not. Otherwise leave it empty too. Say why in `report`. When other capsules of the point have rows, take the challenge from them.
- **The transition already states the problem.** Make the challenge add what the transition does not say.
- **The first bullet starts with the product's name.** That is the usual case. The pivot starts with the name in bold ("**<Product>** …"), and the first bullet starts with "It", "They" or "Its" instead.

## Output

- The three sentences go into the point's `effect`, `challenge` and `pivot` fields in `app/src/story.json`. The challenge is one string, its sentences one after the other.
- Their sources go into the point's `sources` key, in the same file:

```json
"sources": {
  "effect": [{"ref": 0, "field": "solves[0].solution", "text": "…"}],
  "challenge": [{"ref": 0, "field": "solves[0].problem", "text": "…"}],
  "pivot": [{"ref": 0, "field": "note", "text": "…"}],
  "report": ""
}
```

- `ref` is the 0-based index of the capsule in the point's `refs`.
- `field` is `note`, `solves[i].problem` or `solves[i].solution`, where `i` is the 0-based index of the row.
- `text` is the full content of that field, copied character for character, `**` markers included.
- When a sentence cannot meet these rules, leave it empty and say why in the `report` of `sources`.

## Process for a chapter

1. Wait for the chapter to be named.
2. Read the inputs of every point of the chapter.
3. Copy the file: `cp app/src/story.json /tmp/story.before.json`.
4. Write the sentences into the points' fields in `app/src/story.json`, and their sources into each point's `sources`. Give each source as its `ref` and its `field`, then let a script fill its `text` from the tree. Never type a source text by hand.
5. Check that each slide's title and features are the plan's. Then run `python3 scripts/story_check.py --diff /tmp/story.before.json`.
   - Fix every `ERROR`.
   - Read every `WARN` line. Either fix the sentence, or keep it and say why in `docs/story-journal.md`.
6. Check the result:
   - The diff lists only the sentences you meant to write or change.
   - Read each point straight through. The transition, challenge, pivot and bullets form one line of thought.
   - Check each added sentence against "Do not write".
7. Run `python3 app/build.py`, then `python3 scripts/story_pdf.py`.
8. Show the chapter:
   - in the chat, each point laid out like the examples below;
   - the link to the local `ai-tree-mindmap.html`, Story tab.
9. Wait for the verdict on each point.
   - A validated point is frozen.
   - For a rejected sentence, rewrite only that sentence, from the comment, then go back to step 4.
10. Start the next chapter only after this one is validated.

## Examples

### Applications (chapter 7). This is the reference.

> **Applications**
>
> Data and AI applications run on the platform itself, next to the governed data.
>
> *When the same question comes back every week, it is worth turning into a small application.*
>
> - Usually each one runs on separate infrastructure, with its own identity management and secrets.
> - It sits apart from the governed data.
> - Access control and audit trails are hard to put in place.
>
> **Databricks Apps** now hosts them itself.
>
> - Developers build applications with the frameworks they already use, such as Streamlit, Gradio, React or FastAPI, and deploy them.
> - Databricks AppKit is a framework for building them.
> - The apps run serverless on the platform.
> - They sign users in with the platform's identity and read data through Unity Catalog with each user's permissions.
> - Custom MCP servers run the same way.
> - App Spaces give admins one place to govern who deploys and uses which app.
> - Genie App Builder generates an app from a plain-language description, within the limits the admins set.

```json
{"id": "7.6",
 "effect": "Data and AI applications run on the platform itself, next to the governed data.",
 "challenge": "Usually each one runs on separate infrastructure, with its own identity management and secrets. It sits apart from the governed data. Access control and audit trails are hard to put in place.",
 "pivot": "**Databricks Apps** now hosts them itself.",
 "sources": {
  "effect": [{"ref": 0, "field": "solves[0].solution", "text": "**Serverless Databricks Apps** eliminate external hosting costs and complexity"},
             {"ref": 0, "field": "solves[3].solution", "text": "Native **Unity Catalog integration** for permissions-aware data access"}],
  "challenge": [{"ref": 0, "field": "solves[0].problem", "text": "Apps require **separate infrastructure** outside Databricks platform"},
                {"ref": 0, "field": "solves[2].problem", "text": "Apps require **separate identity management** and secrets handling"},
                {"ref": 0, "field": "solves[3].problem", "text": "Apps **isolated** from governed data lake"},
                {"ref": 0, "field": "solves[1].problem", "text": "App-level access control and **audit trails** difficult to implement"}],
  "pivot": [{"ref": 0, "field": "note", "text": "Databricks Apps hosts interactive data and AI apps on Databricks, governed by Unity Catalog."}],
  "report": ""}}
```

### Genie One (conversational assistant) (chapter 7)

> **Genie One (conversational assistant)**
>
> Anyone in the business can question the data directly.
>
> - Most people who need data do not write SQL.
> - Their questions queue up at the data team.
> - The answer often comes after the decision.
>
> **Genie One** gives everyone a single entry point to the data.
>
> - It lets business users ask questions in plain language.
> - They get answers from governed company data, with citations and with their own permissions applied.
> - When a dashboard or an agent already answers the question, Genie One sends the user there.
> - It runs on the web, as a desktop app on macOS, and on iOS and Android.
> - Other AI assistants reach it through the Genie One MCP server.
> - Web search adds outside sources to its answers.
> - Users with account-only access can use it too.

```json
{"id": "7.1",
 "effect": "Anyone in the business can question the data directly.",
 "challenge": "Most people who need data do not write SQL. Their questions queue up at the data team. The answer often comes after the decision.",
 "pivot": "**Genie One** gives everyone a single entry point to the data.",
 "sources": {
  "effect": [{"ref": 0, "field": "solves[1].solution", "text": "Users **answer** ad-hoc questions directly without SQL or waiting"}],
  "challenge": [{"ref": 0, "field": "solves[0].problem", "text": "Business users **blocked** by technical Databricks interface"},
                {"ref": 0, "field": "solves[1].problem", "text": "Analyst **dependency** for every data question"}],
  "pivot": [{"ref": 0, "field": "solves[0].solution", "text": "Simplified, non-technical **front door** with natural language chat"}],
  "report": ""}}
```

### Unity Gateway: policies (chapter 6): a point with a transition

> **Unity Gateway: policies**
>
> Every model and tool call follows the same policies.
>
> *The catalog sets who may use each asset. Each model call and each tool call also needs control at the moment it happens.*
>
> - Prompts and responses go through without guardrails.
>
> **Unity Gateway** puts one control plane in charge.
>
> - It sits in front of all model and tool traffic and is built on Unity Catalog.
> - Service policies set the rules for the calls to each service.
> - LLM-as-a-judge policies check prompts and responses with a model.
> - Sensitive data is redacted, and partner guardrails can be added.
> - Request tags attribute each call to a user, team or project.

The transition already says that each call needs control. The challenge does not repeat it: it says what is missing without a gateway.

```json
{"id": "6.2",
 "effect": "Every model and tool call follows the same policies.",
 "challenge": "Prompts and responses go through without guardrails.",
 "pivot": "**Unity Gateway** puts one control plane in charge.",
 "sources": {
  "effect": [{"ref": 0, "field": "solves[3].solution", "text": "**policies** applied on every request"}],
  "challenge": [{"ref": 0, "field": "solves[3].problem", "text": "**no guardrails** on prompts and responses"}],
  "pivot": [{"ref": 0, "field": "solves[0].solution", "text": "**one control plane** fronts every provider"}],
  "report": ""}}
```

## Delegating to agents

Writing these sentences takes judgment that the rules alone do not carry. If agents write them:

1. Give each agent the prompt below, word for word. Fill in its chapter, its points and its output file.
2. Start with one agent on one chapter. Review its output, and only then hand out the other chapters.
3. Do not accept an output because `story_check.py` passes. The check proves that the sources exist, not that the sentences are good. Review every item against this guide and rewrite the weak ones.

In the first run, on 2026-10-11, three agents were given only this guide and a summary of the rules. All three had to be rewritten:
- they pasted source rows as sentences;
- one of them generated its sentences with a script and wrote pivots in the form "X addresses this";
- they restated bullets;
- they invented a duration.

The prompt below is written against those faults.

On 2026-10-12 a pilot ran with this prompt on chapter 4, on a clean copy of the repository with no sentence already written. Its check passed with no warning, and review still found four faults:
- an effect that reworded a bullet (4.1);
- a challenge with a fact no source states, "requires substantial rework" (4.2);
- a pivot that named no product of its point (4.2);
- a pivot that named a product of another point (4.3).

The script now flags a sentence that repeats a term of the line next to it. The other faults need review.

The conclusion is that agents write drafts. The main session reviews every item and rewrites it before applying, or writes the chapter itself.

### Agent prompt

```
You add three sentences to each point of a chapter of the Story tab of an internal
Databricks field app. Repository: /Users/mehdi.lamrani/code/Report/AmadeusAI. Work from its root.

Chapter: {N}. Points: {ids} ({count} points). Work folder: /tmp/story-ch{N}/.

1. Read docs/story-editorial-guide.md entirely before writing: rules, examples and
   counter-examples. Ignore its "Conduct" and "Process for a chapter" sections: they are for
   the main session. This prompt is your task.
2. Print your inputs with a short script, and use the script for nothing else:
   - for each point of app/src/story.json: its title, its lead, its bullets and its refs;
   - for each ref, with its 0-based index: the capsule's note, and every solves row with its
     index (problem and solution), from app/src/ai-tree.json or app/src/ds-tree.json;
   - for each point, its features in docs/feature-tree.md.
3. Write every sentence yourself. Never let a script write or assemble a sentence.
   Some points may already have an effect, a challenge or a pivot in app/src/story.json.
   Do not read them, and do not reuse them. Write your own.
4. For each point, write the effect, the challenge and the pivot. Follow the guide's
   "Add three sentences", "Do not write" and "Edge cases" sections.
   - The effect is one short line about what the product changes: a formula that starts
     with a verb, or one short complete sentence with a concrete subject. Never start with
     "Teams", "The company" or "Developers". Write it in the affirmative, with plain words.
   - Never change a slide's title or its features: they come from docs/feature-tree.md.
   - The challenge states the problem in full sentences, from problem rows only.
   - The pivot starts with the product's name in bold, as its subject, and says how the
     product takes the problem on: "**MLflow** makes every step visible.". Never start with
     "With". On a slide with two products, name the product of the first bullet, and do not
     credit it with the other one's work. If the first bullet names the product, say in "report" how it stops:
     its subject becomes "It", "They" or "Its", or the name goes. The main session changes
     it in app/src/story.json. "X addresses this" is not a pivot.
   - Never repeat a term of the line just before or after, when a pronoun or another word
     would do.
   - A solves row is a note, not a sentence: never paste one.
   - Never restate a bullet or the lead in other words. Never use a number.
5. Write each source as its "ref" and its "field", then let a script fill its "text" from
   the tree.
6. Before you hand anything in, check each point. Read it in slide order: title, effect, lead,
   challenge, pivot, bullets. For each of your sentences, write one "adds:" line that names the
   precise fact or angle the sentence brings and that neither the lead nor the bullets state.
   A generic line such as "what the organization gains" does not count. If you cannot name
   one, rewrite the sentence.
7. Copy app/src/story.json into /tmp/story-ch{N}/. Write your sentences into the points'
   effect, challenge and pivot in the copy, and your sources into each point's "sources".
   Then run:
   python3 scripts/story_check.py --story /tmp/story-ch{N}/story.json --diff app/src/story.json
   It writes nothing. It must report 0 errors, and the diff must list only your sentences.
   For every WARN line, either rewrite the sentence, or keep it and say why in the "report"
   of the point's "sources".
8. Do not change any file in the repository, and do not run build.py or story_pdf.py.
   Another session is editing the repository.

Return:
- the path of your copy;
- the full output of story_check.py;
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
| Title "Batch AI in SQL and pipelines" | The feature is not named. | The title names the product: "AI Functions". |
| Title "Ingestion, transformation and table maintenance" | It is long and lists notions. | Short and synthetic: "Lakeflow & Predictive Optimization". |
| Effect "Teams apply AI to large volumes of data and documents without moving them out of the platform." | A generic subject, and too long. | "Apply AI to large volumes of data and documents in place." |
| Effect "Putting a model into production no longer takes dedicated infrastructure." | Negative form. | Affirmative: "Put any model into production on serverless infrastructure." |
| Effect "Replies draw on the company's own documents, with sources that can be checked." | A contrived word, and too long. | Plain words: "Retrieve targeted data from documents, based on checked sources." |
| Pivot "Feature Engineering in Unity Catalog makes features a shared, governed asset." just before the bullet "Feature Engineering in Unity Catalog keeps each feature definition in one place, governed by Unity Catalog." | The product's name and "governed" repeated on consecutive lines. | Name the product once: "**Feature Engineering in Unity Catalog** ends the duplication with one shared registry.", then "It keeps each definition in one place, with the same governance as the data." |
| "These pipelines are written and scheduled by hand, and the copies they feed are often out of date." just after "Pipelines move data between them to keep the copies in sync." | "Pipelines" and "copies" repeated on consecutive lines. | No term repeated from the neighbouring line. |
