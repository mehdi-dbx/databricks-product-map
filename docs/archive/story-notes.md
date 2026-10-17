> **Archived on 2026-10-16.** This file is no longer the source of the Story, and no script reads it.
> The Story's text lives in `app/src/story.json`, edited by hand (see `docs/story-tools.md`).
> This file keeps the design notes, checks and sources written while the Story was drafted here.
> Its text may be older than `app/src/story.json`.

# Story notes — working draft

Built bead by bead. Each chapter is written only after the previous one is checked.
Story text is in English (app content language), presenter-led (short), with no claim
about Amadeus (no sources yet). Facts come from the capsule notes and solves in the tree
JSON. Arc and capsule mapping: `story-design.md`.

How to read this draft:
- **Receives** — the question the chapter answers. It must be the previous chapter's handoff.
- **Point N.k** — one step of the chapter, tied to capsules.
- **↳ Link** — why the next point follows from this one. These lines are for checking
  coherence. They do not appear in the final story.
- **Hands off** — the question the chapter leaves open for the next one.

---

## M0 — Spine

**Thread of the whole story.** A company wants AI that works in production on its own
data. Databricks gets there by putting data, models, agents, users and operations on one
governed platform. Each chapter solves one problem and, by solving it, exposes the next.

**Chain of questions:**

| Ch | Receives | Hands off |
|----|----------|-----------|
| 1 Challenges | none | Where do you start? With the data. How do you get it into one place, governed once and fresh enough for AI? |
| 2 Data foundation for AI | How do you get data into one place, governed and fresh? | The data is ready. The first thing teams do with it is learn from it. How does a data science team work on it? |
| 3 Data Science | How does a data science team work on it? | Trained models must be served. Many use cases now start from models someone else trained. How do you serve and control any model? |
| 4 Model access | How do you serve and control any model? | A model answers. Value comes when it can act on data and tools. How do you build agents? |
| 5 Building agents | How do you build agents? | An agent that acts on company data must be trusted first. How do you know it is right and keep it safe? |
| 6 Evaluating and securing agents | How do you know it is right and keep it safe? | The agents can be trusted. Most people who need them do not write code. How do business users get to them? |
| 7 AI for business users | How do business users get to them? | No-code covers common needs. Developers build the rest. What do builders get? |
| 8 Developer tools | What do builders get? | Databricks builds with the same blocks. What does it ship ready-made for business domains? |
| 9 Domain applications | What comes ready-made? | Built or bought, every model and agent then runs for years. How do you run it? |
| 10 Production operations | How do you run it? | none |

**Check M0.** Each "Receives" restates the previous "Hands off": 9 links out of 9.
Two links need care when writing:
- 3 → 4. The DS chapter ends on trained models, and chapter 4 opens on large language
  models. The bridge is serving: both kinds of model are served the same way.
- 8 → 9. It moves from what customers build to what Databricks ships. The bridge is that
  Databricks builds its domain applications with the same blocks.

---

## M1 — Chapter 1. Challenges

**Receives:** none. This is the opening.

**Point 1.1 — Fragmented data.** *(Lakehouse / Delta Lake, Lakeflow, Lakehouse//RT, LTAP, Anomaly detection & remediation)*
Data is spread across operational databases, a warehouse, a data lake and SaaS tools,
each with **its own copies and access rules**. **Hand-built pipelines** keep the copies in
sync, and the data is often **out of date**. When a table breaks, **nobody is warned**.
Answers wait on the **few people** who can query these systems.

↳ **Link 1.1 → 1.2 (consequence).** Every AI project first has to collect that data.

**Point 1.2 — Slow ML development.** *(Feature Store, MLflow, AutoML, Distributed training & GPU, AI Runtime — serverless GPU, both trees)*
Features are **rebuilt for each project** and computed differently in training and
production. Experiments are **hard to reproduce**, and tuning is manual. Large datasets
**outgrow one machine**, and GPUs are **scarce** or sit idle.

↳ **Link 1.2 → 1.3 (models trained elsewhere).** Many use cases start from models trained
elsewhere.

**Point 1.3 — Model provider sprawl.** *(Model Serving, Foundation Model APIs, Model fine-tuning, External model services)*
Each provider has its **own serving setup**, with **API keys scattered** across code. Token
spend grows **without warning**, and outside calls are **not audited**. One vendor means
**lock-in**. Fine-tuning takes **costly GPUs**.

↳ **Link 1.3 → 1.4 (consequence).** Live, governed data stays out of reach.

**Point 1.4 — Pilots stuck before production.** *(MLflow Model Registry)*
AI projects start as **pilots on extracts**. Production needs **live data**, **proven
answers** and **control of models and cost**, and many pilots **stop there**. Models that
reach production are hard to run, because **versions are not tracked** and promotion is
manual.

↳ **Link 1.4 → 1.5 (agents).** Agents add company data and tools to these models.

**Point 1.5 — Unsafe agent access.** *(AI Functions, AI Search, Managed MCP servers, MCP Services + custom MCP, Custom Agents, Managed memory & sessions, Databricks Sandbox, Supervisor Agent)*
Documents are **exported to outside services**. Every connection to search, tools and
memory is **built by hand**, with **credentials everywhere**. Agents have **no memory**
between conversations. Generated code runs with **unrestricted access** to data.
Routing work between agents is **manual**.

↳ **Link 1.5 → 1.6 (trust).** Once AI acts on company data, it has to be trusted.

**Point 1.6 — No AI evaluation or governance.** *(MLflow 3 for GenAI, Agent evaluation & monitoring, MLflow Prompt Registry, Review Apps, Unity Catalog for AI assets, Unity Gateway)*
Nobody sees **which step failed** or measures **quality**. Prompts are **not versioned**, and
expert feedback stays **in spreadsheets**. Models, agents and tools are **not governed like
data**. AI usage has **no central view** and **no audit**.

↳ **Link 1.6 → 1.7 (people).** These gaps slow down users and developers.

**Point 1.7 — No self-service.** *(Genie One, Genie Ontology, Row Zero / Genie ZeroOps, Genie App Builder, Databricks Apps + App Spaces, Genie Code, AI Dev Kit + internal coding agents)*
Business users wait on data teams for **every question**. Metrics are **defined
differently** across teams and dashboards. Spreadsheet analysis **escapes governance**.
Every app needs a **developer** and its **own infrastructure**, identity and secrets.
Developers spend their time on **boilerplate** and agent scaffolding.

↳ **Link 1.7 → 1.8 (business domains).** Some domains add their own silos.

**Point 1.8 — Customer and security silos.** *(CustomerLake, Lakewatch)*
Customer data is **fragmented and duplicated**, with **no lineage**. Security logs sit in
**separate tools**, and many are **deleted early** to save cost.

**Hands off:** the work starts with the data. How do you get it into one place, governed
once and fresh enough for AI?

**Check M1.**
- Rewritten on 2026-10-11 following `docs/story-starting-situation.md`. Each point is one
  group of the pains listed in `docs/story-pains.md`, in the order of the chapters that
  solve them. Every sentence of the former points 1.1 and 1.2 is kept: 1.1 gained two
  sentences, and 1.2 became the pilots point and gained one. On 2026-10-12 the pilots point
  moved from 1.8 to 1.4, when Production operations became chapter 5.
- Condensed on 2026-10-12 for a technical audience: short titles, one fact per bullet, about
  30 bullets instead of 42. No fact was added.
- Capsules added on 2026-10-12: each point cites the capsules of the sources below, as the
  products that answer it. Genie Agents is left out of 1.7, because its sentence was dropped
  in the condensed text.
- Map of the loop the ending closes: 1.1 → ch. 2 · 1.2 → ch. 3 · 1.3 → ch. 4 ·
  1.4 → ch. 5 · 1.5 → ch. 6 · 1.6 → ch. 7 and 8 · 1.7 → ch. 9 and 10 · 1.8 → ch. 11.
  Point 1.4 also recalls the three obstacles that stop pilots: live data (ch. 2), right
  answers (ch. 7), and control of models and cost (ch. 4 and 8).
- Sources of the new sentences, as capsule [row] in `docs/story-pains.md`:
  - 1.1: Lakeflow [0] [3] [4]; Lakehouse//RT [1]; LTAP [4]; Anomaly detection &
    remediation [0] [2] [3]; Lakehouse / Delta Lake [0].
  - 1.2: Feature Store (ai) [2], (ds) [0]; MLflow [0] [1]; AutoML (ai) [0] [1];
    Distributed training & GPU [0] [4]; AI Runtime [0] [1].
  - 1.3: Model Serving [0] [1]; External model services [0] [2] [4]; Foundation Model
    APIs [0] [1]; Model fine-tuning [0] [1].
  - 1.4: MLflow Model Registry [0] [4].
  - 1.5: AI Functions [0] [3]; AI Search [0]; Managed MCP servers [0] [1]; MCP Services
    + custom MCP [3]; Custom Agents [3]; Managed memory & sessions [2]; Databricks
    Sandbox [0] [1]; Supervisor Agent [0] [1].
  - 1.6: MLflow 3 for GenAI [0] [4]; Agent evaluation & monitoring [0]; MLflow Prompt
    Registry [0]; Review Apps [1]; Unity Catalog for AI assets [0] [3]; Unity Gateway
    [1] [4].
  - 1.7: Genie One [1]; Genie Ontology [0]; Genie Agents [3]; Row Zero / Genie ZeroOps
    [3]; Genie App Builder [1]; Databricks Apps + App Spaces [0] [2]; Genie Code [0]
    [2]; AI Dev Kit [1].
  - 1.8: CustomerLake [0] [1] [3]; Lakewatch [0] [2].
- The 10 capsule references with no pains in the tree source no sentence here. Their
  chapters still answer the groups above.
- The handoff starts with the data, because every other group depends on it.

---

## M2 — Chapter 2. Data foundation for AI

**Receives:** how do you get the data into one place, governed once and fresh enough for AI?

**Point 2.1 — Open table storage with Delta Lake.** *(Lakehouse / Delta Lake)*
Databricks stores the data once, in **open tables** in your cloud storage. Delta adds
**transactions** to those files. Batch jobs and streaming jobs write to the same tables
without corrupting them. The schema can change without breaking readers.
**Effect:** Keep one consistent copy of your data, in an open format.
**Challenge:** Batch and streaming data often sit in separate stores, sometimes in closed or complex formats. A job that fails halfway can leave a table inconsistent. A schema change can break the jobs that read it.
**Pivot:** **Delta Lake** is now the single format for batch and streaming alike.

↳ **Link 2.1 → 2.2 (prerequisite).** The data then has to get into this storage
and stay usable.

**Point 2.2 — Lakeflow & Predictive Optimization.** *(Lakeflow, Predictive Optimization)*
It brings the data in and transforms it. Lakeflow Connect provides **managed
connectors** to databases and SaaS applications. **Declarative pipelines** describe the
transformations, and Lakeflow works out the order in which to run them. Predictive
Optimization then maintains the tables **on its own**, so nobody has to schedule
maintenance jobs.
**Effect:** Ingest data and maintain tables automatically.
**Challenge:** Getting it there means writing connector code for each source and wiring job dependencies by hand. The tables then need maintenance that someone has to schedule and tune.
**Pivot:** **Lakeflow** now hands both jobs over to the platform.

↳ **Link 2.2 → 2.3 (gap).** The analytical data is now in place. Applications and agents
also read and write transactional data, and that data usually lives in a separate
database with its own copy.

**Point 2.3 — Lakebase.** *(Lakebase, Lakebase Search)*
It is a **serverless Postgres** database inside the platform. It holds application
data and agent state, and its tables sync with Unity Catalog. Lakebase Search adds
vector and keyword search in the same Postgres database, with **no separate vector store**.
**Effect:** Applications and agents keep their data on the same platform as the analytics, under the same governance.
**Challenge:** It is not governed there. Searching it needs a separate vector store, with one more copy.
**Pivot:** **Lakebase** now keeps both next to the analytics, under the same rules.

↳ **Link 2.3 → 2.4 (the remaining copy).** Transactional and analytical data now sit on
the same platform. The remaining copy is the one that feeds analytics with fresh operational data.

**Point 2.4 — Lakehouse//RT & LTAP.** *(Lakehouse//RT, LTAP)*
It answers SQL queries in **under 100 milliseconds** directly on lakehouse
tables, so dashboards and applications no longer need a separate serving copy. LTAP, which is announced, keeps one dataset that is written in Lakebase and read in Lakehouse//RT, with **no replication pipeline** between them.
**Effect:** Dashboards and applications read live data instead of a stale copy.
**Challenge:** That feed takes replication pipelines and a second system to maintain. The copies lag behind the source. Dashboard queries take seconds.
**Pivot:** **Lakehouse//RT** now does away with the last replica and its pipeline.

↳ **Link 2.4 → 2.5 (condition).** Everything is now in one place. Access, lineage and quality then have to be handled once for all of it.

**Point 2.5 — Data quality monitoring.** *(Classification / profiling / monitoring, Anomaly detection & remediation)*
It applies **one set of permissions**, lineage and audit to tables and files. Data quality is watched in the same place.
Classification tags **sensitive data** such as PII. Profiling and monitoring track quality.
Anomaly detection flags **stale or broken tables** and can trigger a repair job.
**Effect:** Get alerted when a table goes stale, and repair it as an audited job.
**Challenge:** Data freshness is invisible and nobody is notified, so a stale table can go unnoticed. Repairing it is manual and risky.
**Pivot:** **Unity Catalog** now puts quality checks where access is controlled.

**Hands off:** the data is in one place, fresh and governed. How does a data science team work on it?

**Check M2.**
- Opening: answers ch. 1's handoff directly ("one place" → 2.1, "fresh" → 2.2–2.4,
  "governed once" → 2.5).
- 2.1 → 2.2 → 2.3 → 2.4 follows the copies one by one: storage, ingestion, the
  transactional copy, then the last sync copy. Each point removes the copy that the
  previous point exposed.
- 2.4 → 2.5 moves from "where the data is" to "who controls it". It is placed last
  because Unity Catalog is reused in every later chapter (models in 4, agents and tools
  in 5, judges and prompts in 6, users in 7). The sentence "which matters for every
  chapter that follows" makes that forward link explicit.
- Capsules covered: 10/10 for chapter 2.
- Watch item: Lakebase is mentioned for agent state here and returns in ch. 3 (online
  feature store) and ch. 5 (agent memory). Those later mentions must be callbacks.
  The product must not be re-introduced.
- Additions 2.1 (editorial guide):
  - Effect ← Lakehouse / Delta Lake, solves[3].solution, solves[4].solution
  - Challenge ← Lakehouse / Delta Lake, solves[2].problem, solves[3].problem, solves[0].problem, solves[4].problem, solves[1].problem
  - Pivot ← Lakehouse / Delta Lake, note
- Additions 2.2 (editorial guide):
  - Effect ← Lakeflow, solves[0].solution; Predictive Optimization, solves[0].solution
  - Challenge ← Lakeflow, solves[0].problem, solves[4].problem; Predictive Optimization, solves[0].problem, solves[1].problem
  - Pivot ← Lakeflow, note; Predictive Optimization, note
- Additions 2.3 (editorial guide):
  - Effect ← Lakebase — serverless Postgres, note, solves[2].solution
  - Challenge ← Lakebase — serverless Postgres, solves[2].problem; Lakebase Search, solves[1].problem, solves[3].problem
  - Pivot ← Lakebase — serverless Postgres, note; Lakebase Search, note
- Additions 2.4 (editorial guide):
  - Effect ← Lakehouse//RT, solves[1].solution; LTAP, solves[4].solution
  - Challenge ← LTAP, solves[0].problem, solves[2].problem, solves[1].problem; Lakehouse//RT, solves[1].problem, solves[0].problem
  - Pivot ← Lakehouse//RT, solves[2].solution; LTAP, solves[0].solution
- Additions 2.5 (editorial guide):
  - Effect ← Anomaly detection & remediation, solves[0].solution, solves[3].solution, solves[2].solution, solves[4].solution
  - Challenge ← Anomaly detection & remediation, solves[0].problem, solves[3].problem, solves[2].problem
  - Pivot ← Anomaly detection & remediation, note; Classification / profiling / monitoring, note

---

## M3 — Chapter 3. Data Science

**Receives:** how does a data science team work on the data?

**Point 3.1 — Notebooks.** *(Notebooks & collaboration, Data prep & EDA, DS languages & frameworks)*
Data scientists work in notebooks that run Python, SQL, R and Scala directly on the **governed tables**. Several people can edit the same notebook at once, and
notebooks are **versioned in Git**. Exploration uses the tools the team already knows:
pandas, Spark, SQL and built-in data profiles.

↳ **Link 3.1 → 3.2 (product of the work).** Exploration ends in features, the inputs a
model learns from. A feature computed one way for training and another way in production
gives wrong predictions.

**Point 3.2 — Feature Store.** *(Feature Store, both trees)*
It keeps each feature definition in one place, governed by Unity Catalog.
Training sets are built with **point-in-time correct joins**, and the same definitions feed
predictions in production. For real-time use, features are served from an **online store**
on Lakebase.
**Effect:** Build features once & reuse them across teams and models.
**Challenge:** Teams duplicate the same features across projects. Nobody sees where each one comes from or who may use it.
**Pivot:** The **Feature Store** ends the duplication with one shared registry.

↳ **Link 3.2 → 3.3 (next step).** With features in place, the team trains many models
and compares them. Comparing them requires that every result can be reproduced.

**Point 3.3 — MLflow & AutoML.** *(MLflow, AutoML, both trees)*
It records every training run with its parameters, metrics, code version and
artifacts, so any result can be **reproduced and compared**. AutoML gives a **first baseline**.
It tries algorithms such as XGBoost and LightGBM, tunes them, and writes each trial as a
notebook the team can read and change.
**Effect:** Repeat any experiment and get a first baseline fast.
**Challenge:** Each team keeps its metrics to itself. Searching algorithms and settings by hand delays every model.
**Pivot:** **MLflow** handles the bookkeeping, and the trial and error can be automated too.

↳ **Link 3.3 → 3.4 (limit).** Some datasets and models do not fit on one machine.

**Point 3.4 — Distributed training & AI Runtime.** *(Distributed training & GPU, AI Runtime — serverless GPU)*
Training then spreads across GPUs and clusters with **managed libraries** such as
TorchDistributor, DeepSpeed and Ray. AI Runtime provides **GPUs on demand** with no cluster
to manage, and it scales to zero when the job ends.
**Effect:** Train at any scale, with GPUs on demand.
**Challenge:** Distributed training code is hard to write correctly. GPUs are scarce. Clusters configured by hand are error-prone or sit idle.
**Pivot:** **AI Runtime** takes that work off the team.

**Hands off:** the team now has trained models. Applications have to call them. Many new use cases also start from large language models that someone else
trained. How do you serve and control any model, your own or a provider's?

**Check M3.**
- Opening: picks up "learn from the data" and stays on the same governed tables
  (callback to ch. 2, no re-introduction).
- 3.1 → 3.2 → 3.3 → 3.4 follows the order of the work: explore, build features,
  experiment, scale. Each link names what the previous step produces or where it hits
  a limit.
- Lakebase appears as a callback ("the database from chapter 2"), as planned in M2.
- The handoff builds the 3 → 4 bridge flagged in M0. Trained models and provider models
  meet on one question, serving and control, so chapter 4 can treat them together.
- Kept out on purpose: MLflow tracing of LLM calls (it belongs to ch. 6) and the model
  registry (ch. 10). Mentioning them here would announce later chapters too early.
- Capsules covered: 10/10 for chapter 3 (both copies of Feature Store and AutoML).
- Watch item: AI Runtime returns in ch. 4 for fine-tuning. That mention must be a callback.
- Additions 3.2 (editorial guide):
  - Effect ← Feature Store, solves[2].solution, solves[1].solution
  - Challenge ← Feature Store, solves[1].problem, solves[2].problem, solves[3].problem
  - Pivot ← Feature Store, solves[1].solution, solves[3].solution
- Additions 3.3 (editorial guide):
  - Effect ← MLflow, solves[0].solution; AutoML, solves[2].solution
  - Challenge ← MLflow, solves[1].problem; AutoML, solves[0].problem, solves[1].problem, solves[2].problem
  - Pivot ← MLflow, note; AutoML, note
- Additions 3.4 (editorial guide):
  - Effect ← Distributed training & GPU, solves[0].solution; AI Runtime — serverless GPU, solves[0].solution
  - Challenge ← Distributed training & GPU, solves[1].problem, solves[4].problem; AI Runtime — serverless GPU, solves[0].problem, solves[1].problem
  - Pivot ← Distributed training & GPU, solves[1].solution; AI Runtime — serverless GPU, note

---

## M4 — Chapter 4. Model access

**Receives:** how do you serve and control any model, your own or a provider's?

**Point 4.1 — Model Serving.** *(Model Serving)*
It serves your own models and providers' models with **one kind of endpoint**. Custom models, foundation
models and external models are served behind serverless endpoints with the **same API**.
Endpoints scale with demand, **down to zero**. They can be billed per token, with provisioned
throughput, or in batch. Features from the Feature Store are looked up **at serving time**.
**Effect:** Put any model into production on serverless infrastructure.
**Challenge:** Each kind of model needs its own serving system, provisioned by hand, with access control split across them. Idle machines keep costing money.
**Pivot:** **Model Serving** replaces them all as a single serverless service.

↳ **Link 4.1 → 4.2 (what sits behind the endpoint).** For large language models, teams need to know which models are available behind those endpoints.

**Point 4.2 — Foundation models.** *(Foundation Model APIs, Model versions, Model lifecycle churn)*
They give access through **one API** to models from providers that include Anthropic, OpenAI, Google and Meta. They are billed **per token** or with reserved capacity.
The catalog changes often. New versions arrive and older ones are **retired**. Databricks
publishes the supported models and their retirement dates. Because applications call
the same API for every model, moving to a newer model stays a **small change**.
**Effect:** Each task can get the best model, from any of the main providers.
**Challenge:** Depending on one provider creates lock-in. Token spend grows unpredictably. Models from different providers are tested piece by piece.
**Pivot:** **Foundation Model APIs** remove the dependency on any single vendor.

↳ **Link 4.2 → 4.3 (when a general model falls short).** Sometimes a general model does not
know the company's vocabulary or tasks well enough.

**Point 4.3 — Model fine-tuning.** *(Model fine-tuning)*
It adapts an open model to company data with LoRA, QLoRA or full fine-tuning,
on **serverless GPUs**. The tuned model is logged in MLflow and served
**like any other model**.
**Effect:** Adapt a model to your data with less GPU memory, paid by the minute.
**Challenge:** Full fine-tuning needs large amounts of GPU memory and is expensive and slow. Once tuned, the model often sits apart from the systems that serve the others.
**Pivot:** **Model fine-tuning** changes that with lighter methods, and keeps the result on the platform.

↳ **Link 4.3 → 4.4 (models hosted elsewhere).** Some teams also call models that are hosted directly at a provider.

**Point 4.4 — External models.** *(External model services)*
These models are registered as external models, with their keys **stored centrally**, so their calls go through the same endpoints as every other model.
**Effect:** Track and audit outside models like all the others.
**Challenge:** API keys end up scattered across code and people. These calls bypass security, with no view of what they cost.
**Pivot:** **Model Serving** brings them under the same control as the rest.

**Hands off:** every model, hosted on Databricks or at a provider, is now served the same way. Each one then runs in production for years. How do you run it?

**Check M4.**
- Opening: the handoff of ch. 3 asked about serving any model. 4.1 answers it first,
  then 4.2 to 4.4 go deeper into the language-model side. The 3 → 4 bridge holds: the
  trained models of ch. 3 and the provider models meet in 4.1.
- 4.1 → 4.2 goes from the container (the endpoint) to the content (the models).
  4.2 → 4.3 handles the case where the content is not good enough. 4.3 → 4.4 handles the
  consequence of having many of them.
- Callbacks, not re-introductions: Feature Store (ch. 3) in 4.1, serverless GPUs
  (ch. 3) and MLflow (ch. 3) in 4.3, Unity Catalog (ch. 2) in 4.4.
- Ch. 1 loop: 4.4 answers "controlling who uses which model and at what cost".
- Capsules covered: 7/7 for chapter 4.
- Weak spot to revisit in M11: point 4.2 is the longest point so far (four capsules).
  In the final text, the external-models sentence could move to 4.4, since it is about
  keys and control. Left here for now because it is also about which models are
  available.
- Additions 4.1 (editorial guide):
  - Effect ← Model Serving, solves[1].solution, solves[0].solution
  - Challenge ← Model Serving, solves[0].problem, solves[1].problem, solves[2].problem, solves[4].problem
  - Pivot ← Model Serving, note, solves[0].solution
- Additions 4.2 (editorial guide):
  - Effect ← Foundation Model APIs, solves[0].solution, solves[3].solution
  - Challenge ← Foundation Model APIs, solves[0].problem, solves[1].problem, solves[3].problem
  - Pivot ← Foundation Model APIs, solves[0].solution
- Additions 4.3 (editorial guide):
  - Effect ← Model fine-tuning, solves[0].solution, solves[1].solution
  - Challenge ← Model fine-tuning, solves[0].problem, solves[1].problem, solves[2].problem, solves[4].problem
  - Pivot ← Model fine-tuning, solves[0].solution, solves[4].solution
- Additions 4.4 (editorial guide):
  - Effect ← External model services, solves[2].solution, solves[4].solution
  - Challenge ← External model services, solves[0].problem, solves[1].problem, solves[2].problem
  - Pivot ← External model services, note

---

## M10 — Chapter 5. Production operations

**Receives:** how do you run models in production, for years?

**Point 5.1 — Model Registry.** *(MLflow Model Registry, Model Registry & governance)*
Every model in production is registered in Unity Catalog with its versions, its aliases
such as champion and challenger, and its **lineage** back to the training data. Promoting a new version means **moving an alias**, and model update triggers or deployment jobs can start the next steps automatically.
**Effect:** Know which model version is in production and where it came from.
**Challenge:** Nothing tracks model versions over time. Promotions are manual and error-prone. The link between a model and its training data gets lost. Without a shared view across workspaces, teams rebuild models that already exist.
**Pivot:** **MLflow** keeps that history for everyone in one registry.

↳ **Link 5.1 → 5.2 (from registered to running).** A registered version then has to
serve traffic.

**Point 5.2 — Model Serving at scale.** *(Model Serving & batch inference)*
Its endpoints run the registered version, for real-time
requests and for **batch scoring**. They handle more than **25,000 queries per second** with low
added latency, and they scale with demand.
**Effect:** Production load can grow without anyone resizing the infrastructure.
**Challenge:** Models end up spread across several serving platforms, scaled by hand. Nobody has a central view of what is deployed.
**Pivot:** **Model Serving** runs them all in one place.

↳ **Link 5.2 → 5.3 (what happens over time).** Once a model is serving, its inputs
change over time and its quality can drift.

**Point 5.3 — Lakehouse Monitoring.** *(Monitoring & evaluation)*
Inference tables log **every request and response**. Lakehouse Monitoring profiles those
tables, detects **drift** in data and in predictions, and raises alerts. The same monitoring covers data quality and agents.

↳ **Link 5.3 → 5.4 (from detecting to fixing).** When monitoring shows a problem, the
fix has to reach production safely and the same way every time.

**Point 5.4 — MLOps & CI/CD.** *(MLOps & CI/CD)*
MLOps Stacks and Declarative Automation Bundles describe code, jobs, models and their
environments as **files in Git**. Lakeflow Jobs run the pipelines. Each change goes from development to production through that **automated path**.

**Hands off:** every model in production is now versioned, monitored and released through Git. Many use cases need a model that can also look up company data and call tools. How do you build agents?

**Check M10.**
- Opening: answers ch. 9's handoff for both paths (built and bought).
- 10.1 → 10.2 → 10.3 → 10.4 follows the life of a model in production: register, serve,
  watch, change. Each link names the next event in that life.
- Callbacks, not re-introductions: Model Serving (ch. 4) in 10.2. Monitoring (ch. 2 and
  ch. 6) in 10.3, which is the only place the story says the same monitoring serves
  data, agents and models.
- Closing: it maps the obstacles named in point 1.2 to the chapters that answered them.
  It is a factual recap that closes the loop, with no flourish. It lists only obstacles
  named in ch. 1, which is why business users are not in it yet (see M7 weak spot).
- Capsules covered: 5/5 for chapter 10 (both registry capsules).
- Running total: 10 + 10 + 7 + 10 + 5 + 6 + 4 + 2 + 5 = 59 capsules, all placed once (after the M11 move of Omnigent).
- Additions 5.1 (editorial guide):
  - Effect ← MLflow Model Registry, solves[0].solution, solves[2].solution; Model Registry & governance, solves[2].solution
  - Challenge ← MLflow Model Registry, solves[0].problem, solves[1].problem; Model Registry & governance, solves[2].problem, solves[0].problem
  - Pivot ← Model Registry & governance, note
- Additions 5.2 (editorial guide):
  - Effect ← Model Serving & batch inference, solves[1].solution
  - Challenge ← Model Serving & batch inference, solves[0].problem, solves[1].problem, solves[2].problem
  - Pivot ← Model Serving & batch inference, solves[0].solution, solves[2].solution

---

## M5 — Chapter 6. Building agents

**Receives:** how do you build agents?

**Point 6.1 — AI Functions.** *(AI Functions)*
They call a model **from SQL** or from a pipeline to classify, extract or summarize data and documents at scale.
This needs no agent. The results come back with
a **fixed schema**, and the data stays in Unity Catalog.
**Effect:** Apply AI to large volumes of data and documents in place.
**Challenge:** Running a model over company data usually means sending it to an outside service, building separate pipelines for documents and splitting the work into batches by hand. What comes back is unstructured.
**Pivot:** **AI Functions** now run this work where the information already lives.

↳ **Link 6.1 → 6.2 (from batch to conversation).** An agent answers questions as they
come. To answer well, it first has to find the right information.

**Point 6.2 — AI Search.** *(AI Search, Knowledge Assistant)*
It indexes documents and tables for vector and keyword search, keeps the index in
sync with the Delta tables, and returns **citations**. Knowledge Assistant packaged this into
a question-answering agent over documents that could be set up in minutes. It is now moving into **Genie Agents**.
**Effect:** Retrieve targeted data from documents, based on checked sources.
**Challenge:** Search indexes are built and kept in sync by hand. Generic retrieval misses what a document means. Answers then cite sources that are missing or false.
**Pivot:** **AI Search** fixes this by grounding them in the right material.

↳ **Link 6.2 → 6.3 (from reading to acting).** Answering from documents only reads data.
Many tasks also need actions, such as running a query, opening a ticket or changing
code. Each of these tools needs a connection and permissions.

**Point 6.3 — Tool access through MCP.** *(Managed MCP servers, External connectors, MCP Services + custom MCP)*
It is the **standard way** for an agent to call tools.
Databricks runs **managed MCP servers** for its own services, such as Genie, AI Search and
SQL. Connectors give **governed access** to Google Workspace, Microsoft 365, Slack and
GitHub. Teams can register their own MCP servers or host them as Databricks Apps. Every tool is a **Unity Catalog object**, so permissions and audit work the
same way as for data.
**Effect:** Agents reach tools through one governed route.
**Challenge:** Teams write a custom connector for every one of them and host the servers themselves. Credentials pile up across agents. Tool use stays hidden.
**Pivot:** The **Model Context Protocol (MCP)** lets every connection be governed in one place instead.

↳ **Link 6.3 → 6.4 (assembly).** An agent combines retrieval and tools with its own logic.

**Point 6.4 — Custom agents.** *(Custom Agents, Managed memory & sessions, Databricks Sandbox)*
They are written in code with frameworks such as LangGraph, LangChain or the
OpenAI SDK. They can use **any model** on Model Serving and any MCP tool. Managed
memory, stored in Lakebase, lets an agent **remember context** across conversations.
Databricks Sandbox runs the code an agent writes in an **isolated environment**, with scoped
access to data.
**Effect:** Build the agent you need, with memory and safe code execution.
**Challenge:** Platforms often impose the framework and the model, and leave sessions and memory to be handled by hand. Users repeat their instructions in each conversation. The code an agent writes is untrusted.
**Pivot:** **Custom agents** lift each of these limits.

↳ **Link 6.4 → 6.5 (beyond one agent).** Some tasks are too large for one agent.

**Point 6.5 — Supervisor Agent.** *(Supervisor Agent)*
It splits a task across several agents and keeps each user's **data
permissions**. It is moving into **Genie Agents** as well.
**Effect:** Work is split among specialists and comes back as one answer.
**Challenge:** Routing work between agents by hand gives disconnected answers. A chain of them can bypass a user's data permissions.
**Pivot:** The **Supervisor Agent** coordinates the routing.

**Hands off:** the agent can now use company data and tools, and keep memory across conversations. Before it
reaches users, it has to be trusted. How do you know it is right?

**Check M5.**
- Opening: answers "how do you build agents" in growing order of autonomy: bulk AI
  (5.1), retrieval (5.2), tools (5.3), one agent (5.4), several agents (5.5).
- Each link names what the previous point lacks: conversation, action, assembly, scale.
- Callbacks: Unity Catalog (ch. 2) in 5.1 and 5.3, Lakebase (ch. 2) in 5.4, models
  (ch. 4) in 5.4. Forward hooks: Genie Agents (ch. 7) twice, Databricks Apps (ch. 8)
  once. Forward hooks are allowed when they tell the listener where a thread continues.
- Status handled in the text where it changes the story: Knowledge Assistant and
  Supervisor Agent are moving into Genie Agents. Other statuses stay on the cards.
- Capsules covered: 11/11 for chapter 5.
- Weak spot to revisit in M11: Omnigent fits awkwardly in 5.5. It is about developers'
  agent harnesses, which is closer to chapter 8. It stays here because the capsule map
  puts it in chapter 5. M11 should decide whether to move it.
- Additions 6.1 (editorial guide):
  - Effect ← AI Functions, solves[0].solution, solves[3].solution
  - Challenge ← AI Functions, solves[0].problem, solves[4].problem, solves[2].problem, solves[1].problem
  - Pivot ← AI Functions, note
- Additions 6.2 (editorial guide):
  - Effect ← AI Search (ex-Vector Search), note; Knowledge Assistant, solves[2].solution
  - Challenge ← AI Search (ex-Vector Search), solves[0].problem, solves[2].problem; Knowledge Assistant, solves[1].problem, solves[2].problem
  - Pivot ← AI Search (ex-Vector Search), solves[0].solution; Knowledge Assistant, solves[0].solution
- Additions 6.3 (editorial guide):
  - Effect ← Managed MCP servers, solves[0].solution, solves[2].solution; MCP Services + custom MCP, solves[2].solution
  - Challenge ← Managed MCP servers, solves[0].problem, solves[3].problem, solves[1].problem, solves[5].problem
  - Pivot ← Managed MCP servers, note; MCP Services + custom MCP, note
- Additions 6.4 (editorial guide):
  - Effect ← Custom Agents, solves[0].solution; Managed memory & sessions, solves[1].solution; Databricks Sandbox, solves[0].solution
  - Challenge ← Custom Agents, solves[1].problem, solves[5].problem, solves[3].problem; Managed memory & sessions, solves[1].problem; Databricks Sandbox, solves[0].problem
  - Pivot ← Custom Agents, note; Managed memory & sessions, note; Databricks Sandbox, note
- Additions 6.5 (editorial guide):
  - Effect ← Supervisor Agent, solves[0].solution, solves[3].solution
  - Challenge ← Supervisor Agent, solves[0].problem, solves[3].problem, solves[4].problem
  - Pivot ← Supervisor Agent, solves[0].solution

---

## M6 — Chapter 7. Evaluating agents

**Receives:** how do you know the agent is right?

**Point 7.1 — MLflow Tracing.** *(MLflow 3 for GenAI)*
It traces every request through the agent. It records each model call, tool call
and retrieval step, with inputs, outputs, **latency and tokens**, and it works with more
than 30 agent frameworks. When an answer is wrong, the trace shows **the step where it
went wrong**.
**Effect:** Trace request details and cost, step by step.
**Challenge:** Agent chains are opaque to the people who run them. When an answer is wrong, the failing step is hard to isolate. The cost of each request is unknown.
**Pivot:** **MLflow** makes every step visible.

↳ **Link 7.1 → 7.2 (one request to many).** A trace shows one request. Judging quality
needs a score across many requests.

**Point 7.2 — Agent evaluation & Prompt Registry.** *(Agent evaluation & monitoring, MLflow Prompt Registry)*
It applies **LLM judges** and custom scorers to traces. It runs in batch
before a release and continuously on **live traffic**. Each agent version gets its own
evaluation run, so versions can be compared. Prompts are versioned in the Prompt
Registry with staging and production aliases, so a prompt change is tracked **like a code
change**.
**Effect:** Improve the quality of new agent versions.
**Challenge:** Without such scores, traces are reviewed by hand and versions cannot be compared. Prompts change with no record. Staging and production drift apart.
**Pivot:** **Agent evaluation** measures the answers, and versioned prompts close the remaining gaps.

↳ **Link 7.2 → 7.3 (the judges need a reference).** The scores of an LLM judge have to
match what experts would say.

**Point 7.3 — Review Apps.** *(Review Apps)*
They let domain experts test the agent in a chat interface and **label its answers**.
The labels attach to the traces and become **evaluation datasets**. They are also used to
align the judges with the experts.
**Effect:** Domain knowledge becomes the standard the agent is measured against.
**Challenge:** Without ground truth, agent quality is a matter of opinion. Experts label answers in spreadsheets that are not linked to the traces. Their criteria drift from one session to the next.
**Pivot:** **Review Apps** route that feedback directly into the evaluation.

**Hands off:** the agent's answers can now be measured and reviewed. Data, models,
agents and tools also need one set of rules for who may use what, and for what can go
wrong. How is all of it governed?

**Check M6.**
- Opening: the two halves of ch. 5's handoff ("right" and "safe") structure the chapter.
  Points 6.1–6.3 answer "right", and point 6.4 answers "safe". Link 6.3 → 6.4 names the
  switch explicitly.
- 6.1 → 6.2 → 6.3 goes from one trace, to scores over many traces, to the expert labels
  that make the scores trustworthy. Each link names the missing piece.
- 6.4 closes the agent part of the story by tying controls back to ch. 2 (Unity
  Catalog), ch. 4 (AI Gateway) and ch. 5 (Sandbox). That is a deliberate recap, without
  a flourish.
- Ch. 1 loop: 6.2 and 6.3 answer "proving the answers are right".
- Capsules covered: 5/5 for chapter 6.
- Wording checked: link 6.1 → 6.2 first read "seeing is not measuring". That is a reframe
  ("X is not Y") and was rewritten as two plain sentences.
- Additions 7.1 (editorial guide):
  - Effect ← MLflow 3 for GenAI, solves[0].solution, solves[4].solution, solves[3].solution
  - Challenge ← MLflow 3 for GenAI, solves[0].problem, solves[4].problem, solves[3].problem
  - Pivot ← MLflow 3 for GenAI, note
- Additions 7.2 (editorial guide):
  - Effect ← Agent evaluation & monitoring, solves[4].solution, solves[1].solution
  - Challenge ← Agent evaluation & monitoring, solves[0].problem, solves[1].problem, solves[4].problem; MLflow Prompt Registry, solves[0].problem, solves[1].problem
  - Pivot ← Agent evaluation & monitoring, solves[0].solution; MLflow Prompt Registry, solves[0].solution
- Additions 7.3 (editorial guide):
  - Effect ← Review Apps, solves[3].solution, solves[0].solution
  - Challenge ← Review Apps, solves[0].problem, solves[1].problem, solves[4].problem
  - Pivot ← Review Apps, note

---

## M13 — Chapter 8. Governance

**Receives:** how are data, models, agents and tools governed with one set of rules?

**Point 8.1 — Unity Catalog for AI assets.** *(Unity Catalog for AI assets)*
It governs models, agents, tools and credentials in the **same way as tables
and files**. Each of them is a Unity Catalog object with permissions, lineage and an audit
trail. Lineage follows the chain **from data to model to agent**. Credentials for external
services are stored in the catalog and **encrypted**.
**Effect:** Each model, agent and tool can be traced to the data behind it and to everyone who used it.
**Challenge:** Models, agents and tools are not governed as assets of their own. Permissions are enforced differently across them. External credentials are scattered. Nobody knows which data feeds which model.
**Pivot:** **Unity Catalog** extends the existing rules to these assets.

↳ **Link 8.1 → 8.2 (from rules to traffic).** The catalog sets who may use each asset. Each
model call and each tool call also needs control at the moment it happens.

**Point 8.2 — Unity Gateway for AI traffic control.** *(Unity Gateway)*
It sits in front of all model and tool traffic and is built on Unity Catalog.
It sets **who may call which model** and tracks usage per user and team. Budgets **cap spend**.
Guardrails apply to every prompt and response, and every request is **logged for audit**.
**Effect:** Every model and tool call is controlled and logged in one place.
**Challenge:** Teams connect to providers on their own, so nobody sees who uses which model or what it costs. Prompts and responses go through without guardrails. Nothing is logged for an audit.
**Pivot:** **Unity Gateway** puts one control plane in charge.

↳ **Link 8.2 → 8.3 (the full list of risks).** Permissions and guardrails address known
risks. A security team also needs the full list of risks and the control that covers
each one.

**Point 8.3 — Databricks AI Security Framework.** *(DASF v3.0)*
The Databricks AI Security Framework lists the risks of AI systems and the controls
that address them. Version 3.0 covers 97 risks and 73 controls, including 35 risks **specific to agents**. The controls include **least-privilege tool access** in Unity
Catalog, sandboxed code execution, guardrails in Unity Gateway, and human review.

**Hands off:** data, models, agents and tools are now governed with one set of rules.
Most of the people who need them do not write code. How do business users get to them?

**Check M13.**
- Opening: answers ch. 6's new handoff ("one set of rules ... what can go wrong").
- 7.1 → 7.2 goes from rules on assets to control of each call. 7.2 → 7.3 goes from known
  controls to the complete risk list.
- Placed after the agent chapters: it is the first point in the story where data,
  models, agents and tools have all been introduced, so governance covers them in one
  place.
- Ch. 1 obstacle "controlling who uses which model and at what cost" is answered here.
- Capsules: Unity Catalog for AI assets (from ch. 2), Unity Gateway (from ch. 4),
  DASF v3.0 (from ch. 6).
- Additions 8.1 (editorial guide):
  - Effect ← Unity Catalog for AI assets, solves[2].solution, solves[3].solution
  - Challenge ← Unity Catalog for AI assets, solves[0].problem, solves[1].problem, solves[4].problem, solves[2].problem
  - Pivot ← Unity Catalog for AI assets, note
- Additions 8.2 (editorial guide):
  - Effect ← Unity Gateway, solves[0].solution, solves[4].solution
  - Challenge ← Unity Gateway, solves[0].problem, solves[1].problem, solves[2].problem, solves[3].problem, solves[4].problem
  - Pivot ← Unity Gateway, solves[0].solution

---

## M7 — Chapter 9. AI for business users

**Receives:** how do business users get to the agents?

**Point 9.1 — Genie One.** *(Genie One)*
It lets business users ask questions in **plain language**. They get answers from governed company data, with citations and with **their own permissions**
applied. When a dashboard or an agent already answers the question, Genie One sends the
user there.
**Effect:** Anyone in the business can question the data directly.
**Challenge:** Most people who need data do not write SQL. Their questions queue up at the data team. The answer often comes after the decision.
**Pivot:** **Genie One** gives everyone a single entry point to the data.

↳ **Link 9.1 → 9.2 (trust needs shared definitions).** An answer is only trusted if
"revenue" or "active customer" means the same thing as in the official reports.

**Point 9.2 — Genie Ontology.** *(Genie Ontology)*
It holds those definitions. Each KPI is **defined once**, as a metric view in
Unity Catalog. The ontology also learns **business context** from existing dashboards,
queries and pipelines. It ranks sources by certification, usage and freshness, so Genie
answers from **certified definitions first**.
**Effect:** Each metric has one certified definition, used everywhere.
**Challenge:** Metrics are defined differently across dashboards, queries and teams. Business context is scattered in documents, chats and tickets. An AI can then pick an obsolete or draft definition.
**Pivot:** **Genie Ontology** grounds answers in the certified version.

↳ **Link 9.2 → 9.3 (from definitions to know-how).** Once the definitions are shared,
domain experts can package what they know for others.

**Point 9.3 — Genie Agents.** *(Genie Agents)*
They let a domain expert build a **no-code assistant** for a business area. The
assistant can follow up on questions, run **multi-step analyses** and explain its reasoning,
and it can be embedded in other applications. Knowledge Assistant and the supervisor agent are moving into Genie Agents.
**Effect:** The knowledge of each business area becomes available to everyone in it.
**Challenge:** Today that knowledge stays with a few people. Dashboards only answer the questions they were built for. Deeper analysis is spread across separate tools.
**Pivot:** **Genie Agents** spread that expertise instead.

↳ **Link 9.3 → 9.4 (familiar formats).** Many users still work in dashboards and
spreadsheets.

**Point 9.4 — AI/BI Dashboards.** *(AI/BI Dashboards, Row Zero / Genie ZeroOps)*
A dashboard can be built from a **plain-language request**. The assistant finds the
tables, writes the queries and picks the charts, and the author **approves each step**.
Row Zero, announced, brings the same governed data into a spreadsheet, with Genie
writing the queries behind the formulas.
**Effect:** Analysts and business people serve themselves, without waiting for a specialist.
**Challenge:** Building one takes SQL and specialist skills, so requests wait. Meanwhile, analysis done in spreadsheets is cut off from the governed data and unaudited.
**Pivot:** **AI/BI Dashboards** come with an assistant that can help in both places.

↳ **Link 9.4 → 9.5 (from a question to a tool).** When the same question comes back
every week, it is worth turning into a small application.

**Point 9.5 — Genie App Builder.** *(Genie App Builder)*
It generates a Databricks App from a plain-language description, within
the **limits the admins set**.
**Effect:** Business teams turn an idea into a working app in minutes.
**Challenge:** Building an app takes software engineering skills. Every change needs a developer and a new deployment.
**Pivot:** **Genie App Builder** now makes describing the app enough.

↳ **Link 9.5 → 9.6 (where apps run).** These apps, like the ones developers write, need a place to run.

**Point 9.6 — Databricks Apps.** *(Databricks Apps + App Spaces)*
Developers build applications with the **frameworks they already use**, such as Streamlit,
Gradio, React or FastAPI, and deploy them. The apps run **serverless** on
the platform. They sign users in with the platform's identity and read data through
Unity Catalog with **each user's permissions**. Custom MCP servers run the same way. App Spaces give admins **one place to govern** who deploys and uses which app.
**Effect:** Data and AI applications run on the platform itself, next to the governed data.
**Challenge:** Usually each one runs on separate infrastructure, with its own identity management and secrets. It sits apart from the governed data. Access control and audit trails are hard to put in place.
**Pivot:** **Databricks Apps** now hosts them itself.

**Hands off:** no-code covers the common needs. Developers build the rest, such as custom applications, agents and pipelines. What do builders get?

**Check M7.**
- Opening: answers "how do business users get to the agents" with the front door first
  (7.1), then what makes it trustworthy (7.2), then what experts add (7.3), then the
  formats users already have (7.4 and 7.5).
- The ch. 5 forward hooks land here: 7.3 says where Knowledge Assistant and the
  supervisor agent end up. The thread opened in 5.2 and 5.5 is closed.
- 7.5 → handoff: the App Builder makes simple apps, and that naturally raises who builds
  the complex ones. It is the bridge to ch. 8.
- Capsules covered: 6/6 for chapter 7.
- Weak spot to revisit in M11: chapter 1 does not mention business users. The story
  solves a problem it never stated. M11 should add one sentence to ch. 1 (people who
  need answers wait for the few who can query the data), so the ending can close this
  loop too.
- Status check: Row Zero is announced. Its ZeroOps part (an agent that proposes
  operational fixes) is left out of the text. It does not serve this chapter's point,
  and the card carries it.
- Additions 9.1 (editorial guide):
  - Effect ← Genie One, solves[1].solution
  - Challenge ← Genie One, solves[0].problem, solves[1].problem
  - Pivot ← Genie One, solves[0].solution
- Additions 9.2 (editorial guide):
  - Effect ← Genie Ontology, solves[3].solution, solves[0].solution
  - Challenge ← Genie Ontology, solves[0].problem, solves[2].problem, solves[1].problem
  - Pivot ← Genie Ontology, note
- Additions 9.3 (editorial guide):
  - Effect ← Genie Agents, solves[3].solution
  - Challenge ← Genie Agents, solves[3].problem, solves[0].problem, solves[2].problem
  - Pivot ← Genie Agents, solves[3].solution
- Additions 9.4 (editorial guide):
  - Effect ← AI/BI Dashboards (Lakeview), solves[5].solution
  - Challenge ← AI/BI Dashboards (Lakeview), solves[1].problem, solves[5].problem, solves[4].problem; Row Zero / Genie ZeroOps, solves[0].problem, solves[3].problem
  - Pivot ← AI/BI Dashboards (Lakeview), note; Row Zero / Genie ZeroOps, note
- Additions 9.5 (editorial guide):
  - Effect ← Genie App Builder, solves[0].solution
  - Challenge ← Genie App Builder, solves[1].problem, solves[3].problem
  - Pivot ← Genie App Builder, solves[1].solution
- Additions 9.6 (editorial guide):
  - Effect ← Databricks Apps + App Spaces, solves[0].solution, solves[3].solution
  - Challenge ← Databricks Apps + App Spaces, solves[0].problem, solves[2].problem, solves[3].problem, solves[1].problem
  - Pivot ← Databricks Apps + App Spaces, note

---

## M8 — Chapter 10. Developer tools

**Receives:** what do builders get?

**Point 10.1 — Genie Code.** *(Genie Code)*
It is the AI assistant inside notebooks, the SQL editor, pipelines and
dashboards. It **writes and explains code** from plain-language requests. A **command-line
version**, in beta, brings it into the terminal and into CI pipelines.
**Effect:** Generate Databricks code with an AI assistant.
**Challenge:** Much of the code is repetitive boilerplate. Developers switch between separate tools for notebooks, SQL, pipelines and dashboards. Tuning SQL is hard for non-experts.
**Pivot:** **Genie Code** takes over much of that work.

↳ **Link 10.1 → 10.2 (agents are code too).** Custom agents are code as well, and they need a project structure.

**Point 10.2 — AI Dev Kit & Omnigent.** *(AI Dev Kit + internal coding agents, Omnigent)*
It gives developers **templates and scaffolding** for agents, and a set of
tools governed in Unity Catalog. Databricks uses the same kit for its own internal
coding agents. Developers who already work with coding agents such as Claude, Codex or
Cursor can put them behind **one interface** with Omnigent, with shared context and central
policies.
**Effect:** Start from a ready-made base, with governed and audited tools.
**Challenge:** Developers scaffold each one and its tool connections by hand. The integrations they create are not audited. Each coding-agent tool is its own isolated world, so content is copied between them by hand.
**Pivot:** The **AI Dev Kit** removes that manual work with a common base.

**Hands off:** Databricks uses the same platform components to build complete applications for specific business domains. What comes ready-made?

**Check M8.**
- Opening: ch. 7's handoff asked what builders get. The chapter follows a developer's
  day: where the app runs (8.1), how the code gets written (8.2), how agents get built
  (8.3).
- Callbacks: Unity Catalog (ch. 2) twice, the agents (ch. 5) in link 8.2 → 8.3, and the
  MCP hosting hook from 5.3 lands in 8.1 (custom MCP servers run as Databricks Apps).
  To make that landing explicit, 8.1 could add "including the custom MCP servers from
  chapter 5". Noted for M11.
- 8.3 → handoff builds the 8 → 9 bridge flagged in M0. "Databricks uses the same kit"
  leads to "Databricks builds with these same blocks".
- Left out of the text: the internal spend figures in the AI Dev Kit capsule. They are an
  internal proof point and not suited to the story.
- Capsules covered: 3/3 for chapter 8.
- Additions 10.1 (editorial guide):
  - Effect ← Genie Code, solves[2].solution, solves[1].solution
  - Challenge ← Genie Code, solves[2].problem, solves[1].problem, solves[3].problem
  - Pivot ← Genie Code, solves[0].solution
- Additions 10.2 (editorial guide):
  - Effect ← AI Dev Kit + internal coding agents (Isaac), solves[1].solution, solves[0].solution
  - Challenge ← AI Dev Kit + internal coding agents (Isaac), solves[1].problem, solves[4].problem; Omnigent, solves[0].problem, solves[2].problem
  - Pivot ← AI Dev Kit + internal coding agents (Isaac), note; Omnigent, note

---

## M9 — Chapter 11. Domain applications

**Receives:** what comes ready-made?

**Point 11.1 — CustomerLake.** *(CustomerLake)*
In private preview, it builds **customer 360 profiles** on the lakehouse. It
joins transactions, behavior and engagement into one profile per customer. AI-assisted
**identity resolution** merges duplicate records. Campaign agents create and **activate
audiences**, and a real-time profile API feeds personalization.
**Effect:** Campaigns and personalization run on governed customer profiles that stay current.
**Challenge:** Each system holds its own part of the customer, often duplicated and without lineage. Audiences are built and activated by hand.
**Pivot:** **CustomerLake** now covers this work as a ready-made application.

↳ **Link 11.1 → 11.2 (same pattern, another domain).** CustomerLake applies the platform to
customer data. The same pattern applies to security data.

**Point 11.2 — Lakewatch.** *(Lakewatch)*
In private preview, it runs security operations on the lakehouse. It keeps
security, IT and business logs in one place at **object-storage cost**, so they no longer
have to be deleted early. Autonomous agents **investigate alerts** and help write detection
rules, which are versioned and tested like code.
**Effect:** Keep every log and investigate faster.
**Challenge:** Telemetry is split across separate tools. Threat hunting and triage are manual. Detection rules are hard to version and test.
**Pivot:** **Lakewatch** now lets agents share the load.

**Hands off:** both applications are built from the same parts: data on the lakehouse, governance in Unity Catalog, and agents.

**Check M9.**
- Opening: answers "what comes ready-made" with two concrete applications.
- 9.1 → 9.2 is a parallel, not a sequence. The link states the shared pattern so the
  two points do not read as a list.
- The last link carries the chapter's real point: the domain applications prove the
  blocks compose. That point is what justifies the chapter. Without it, ch. 9 would be a
  product catalogue.
- The handoff joins the two paths ("built" = ch. 3–8, "bought" = ch. 9) into one question
  about production, which ch. 10 needs.
- Capsules covered: 2/2 for chapter 9.
- Status stated in the text: both are in private preview. For applications this new,
  leaving the status out would mislead.
- Additions 11.1 (editorial guide):
  - Effect ← CustomerLake, solves[3].solution, solves[4].solution
  - Challenge ← CustomerLake, solves[0].problem, solves[1].problem, solves[3].problem, solves[2].problem
  - Pivot ← CustomerLake, note
- Additions 11.2 (editorial guide):
  - Effect ← Lakewatch, solves[2].solution, solves[4].solution, solves[1].solution
  - Challenge ← Lakewatch, solves[0].problem, solves[1].problem, solves[3].problem
  - Pivot ← Lakewatch, note

---

## M11 — End-to-end check of the articulations

The story read through its links only: each point title, the link to the next point,
and each chapter handoff. If this chain reads as one argument, the full text holds.

1. Data is spread out. → Because AI needs that data, every AI project starts on extracts. → Pilots stop before production. → *So the work starts with the data.*
2. One open copy (Delta). → Storage only helps once data gets in. → Lakeflow brings it in, Predictive Optimization keeps it in shape. → Apps and agents also need transactional data. → Lakebase. → One sync copy is left. → Lakehouse//RT and LTAP remove it. → One place only helps if it is governed once. → Unity Catalog and data quality. → *Ready data is first used to learn from it.*
3. Notebooks on the governed tables. → Exploration produces features, which must be the same in training and production. → Feature Store. → Many models must be comparable. → MLflow and AutoML. → Some models outgrow one machine. → Distributed training and serverless GPUs. → *Trained models must be served, and provider models arrive too.*
4. One serving layer for every model. → Which models sit behind it. → Foundation Model APIs and their lifecycle. → When a general model falls short. → Fine-tuning. → Many models from many providers need one control. → External models and Unity Gateway. → *A model that answers is not enough. It has to act.*
5. Bulk AI on data. → Conversation first needs the right information. → AI Search. → Reading data is not enough for many tasks. Tools are needed. → MCP. → An agent assembles parts with its own logic. → Custom agents, memory, sandbox. → Some tasks are too large for one agent. → Supervisor. → *Before users, the agent must be trusted.*
6. See each request. → Scores across many requests. → Evaluation and prompt versions. → Judges need an expert reference. → Review Apps. → The agent is right. What can go wrong? → DASF and its controls. → *Trusted, but most users do not code.*
7. Front door in plain language. → Trust needs shared definitions. → Ontology. → Shared definitions let experts package know-how. → Genie Agents. → Users still live in dashboards and spreadsheets. → AI/BI, Row Zero. → A recurring question becomes a tool. → App Builder. → *Developers build the rest.*
8. Hosting apps. → Writing the code remains. → Genie Code. → Agents are code too. → AI Dev Kit, Omnigent. → *Databricks builds with the same blocks.*
9. Customer data, ready-made. → Same pattern, security data. → Both are made of the earlier blocks. → *Built or ready-made, everything then runs for years.*
10. Know what is in production. → Registered versions serve traffic. → Over time, quality drifts. → Monitoring. → Fixes must reach production the same way every time. → MLOps. → *Closing: each starting obstacle mapped to its chapter.*

**Result.** 29 links inside chapters, 9 handoffs between chapters, and 1 closing loop. Every link states a reason
(consequence, prerequisite, gap, limit or condition). None is a bare "next".

**Fixes made in M11:**
1. **Chapter 1 now states the business-user problem** ("people who need an answer wait
   for the few colleagues who can query these systems"). The closing names chapter 7.
   Before this fix, the story answered a problem it never stated (flagged in M7).
2. **External models moved from 4.2 to 4.4.** They are about keys and control. Point 4.2
   is shorter and stays on the catalog of models (flagged in M4).
3. **Omnigent moved from chapter 5 to chapter 8.** It serves developers' coding agents.
   Point 5.5 is now only the supervisor, and its link is simpler. The capsule map in
   `story-design.md` is updated (flagged in M5).
4. **Custom MCP servers land in 8.1** ("run the same way"). The hook opened in 5.3 now
   closes explicitly (flagged in M8).
5. **Three wordings rewritten as plain statements:**
   - link 5.2 → 5.3 was a mirrored pair ("answering is reading, acting is calling") ;
   - link 6.3 → 6.4 was a first / second pair ;
   - the ch. 9 handoff was a balanced "built or bought" clause.

**Coverage after M11.** All 59 capsules are named in the story text, checked against the
tree JSON. The capsule table in `story-design.md` matches: 59 rows, 0 duplicates.

**Decided after M11 (Mehdi, 2026-10-08):**
- Angle: generic. No change needed, the text already makes no claim about Amadeus.
- Length: accepted as is. The text is written to be presented, with a short paragraph per point.
  It runs to 2136 words (points, handoffs and closing, without the link and check lines). The cards carry the
  detail, so the final text could be cut further.

---

## M12 — /noslop pass on the story text (2026-10-08)

- 37 point titles rewritten as plain labels that name the topic (rule 12). Chapter 1 is
  now "Scattered data and stalled AI pilots".
- 29 sentences rewritten:
  - chapter cross-references removed ("from chapter 2", "covered in chapter 7", "point 5.3"), rule 5 ;
  - cadenced triads and anaphora removed ("its own keys, its own spend and its own rules", "read, act and remember", "look up, call, follow"), rules 1 and 3 ;
  - figures replaced by plain words ("the front door", "the blocks", "joins the two sides"), rule 8 ;
  - a vague "and other providers" and three repetitions fixed.
- The closing paragraph is removed. It was a summary that talked about the document
  ("Chapter 1 started with..."), which breaks rules 4 and 5. The story now ends on the
  last real point, MLOps and CI/CD. The check notes in M0, M10 and M11 that mention the
  closing are superseded by this entry.

---

## M14 — Governance as its own chapter (2026-10-08)

Requested by Mehdi. The story now has 11 chapters.
- New chapter 7, Governance: Unity Catalog for AI assets, Unity Gateway, DASF v3.0.
- Chapter 2 keeps the data catalog and data quality ("Data catalog and data quality").
- Chapter 4 keeps external models. Its handoff no longer claims central control.
- Chapter 5 hands off "is it right" only. Chapter 6 is "Evaluating agents" and hands off
  the governance question.
- Old chapters 7 to 10 are now 8 to 11. Point ids and link labels were renumbered.
- The M0 chain and the per-milestone checks describe the 10-chapter version. This entry
  supersedes them where they differ.

---

## M15 — The complete story

Written on 2026-10-11 following `docs/story-cement.md`. `scripts/story_extract.py` reads this
section into the Story tab: the title and the opening at the top, each chapter's bullets at the
head of its chapter, and the closing after chapter 11. Each block is a bullet list, because the
Story serves as presentation slides.

**Title:** AI in Production with Databricks

**Opening.**
- Most large organizations already run analytics and have started with AI.
- Their data sits in **several systems**, each with its own copies and rules, kept in sync by pipelines built by hand.
- Data scientists rebuild the **same features** and struggle to reproduce their results.
- Every model provider is **handled separately**.
- AI projects start as pilots on extracts, and many **stop before production**.
- Agents cannot reach data and tools **safely**.
- Nobody can **verify the answers** of the AI or see how it is used.
- Business users wait for the **few colleagues** who can query the data.
- Developers host each application on **its own infrastructure**.
- Customer and security data stay in **their own silos**.
- The work starts with the data.
- How do you get it into one place, governed once and fresh enough for AI?

**Chapter 2.**
- It starts by storing the data once.
- **Copies multiply** because every workload, from batch jobs to applications and dashboards, keeps its own.
- Delta Lake keeps **one open copy**.
- Lakeflow and Predictive Optimization bring the data in and maintain it.
- Lakebase and Lakehouse//RT put applications and live analytics on that **same copy**.
- Unity Catalog governs all of it and **watches its quality**.
- The organization now has one **fresh, governed copy** of its data.
- How does a data science team work on it?

**Chapter 3.**
- Data scientists explore that governed data in notebooks, with the languages they already know.
- Their work slows down when features are rebuilt for each project and results **cannot be reproduced**.
- The Feature Store shares them **across teams**.
- MLflow and AutoML track and speed up the experiments.
- AI Runtime provides **GPUs** when the data outgrows one machine.
- The team ends up with models it can reproduce.
- Many new uses start from models **trained by others**.
- How do you serve and control any model, your own or a provider's?

**Chapter 4.**
- Those models now have to be served.
- Without one way to do it, each model and provider brings its own system, **keys and costs**.
- Model Serving puts them all behind the **same kind of endpoint**.
- Foundation Model APIs reach the main providers through **one API**.
- Fine-tuning adapts open models to the company's needs.
- External models go through the **same control**.
- Each one is now served the same way, and then runs in production **for years**.
- How do you run it?

**Chapter 5.**
- Running it means keeping track of **every version**.
- **Models drift** as their inputs change, and each fix has to reach production the same way every time.
- The Model Registry in Unity Catalog records each version and its **lineage**.
- Model Serving runs the registered one at scale.
- Lakehouse Monitoring detects drift and raises alerts.
- MLOps Stacks and bundles carry each change from **development to production**.
- Each model is now served, monitored and updated for as long as it is used.
- Many uses need one that can also look up company data and **call tools**.
- How do you build agents?

**Chapter 6.**
- An agent starts from the **company's own data**.
- It has to find the right information, use tools, remember what it learned and run code **without putting the data at risk**.
- AI Functions bring models to the data in SQL.
- AI Search and Knowledge Assistant find the **right documents**.
- MCP connects tools under Unity Catalog.
- Custom agents get **managed memory** and Databricks Sandbox.
- The Supervisor Agent shares out large tasks.
- The agent can now use company data and tools.
- Before it reaches users, it **has to be trusted**.
- How do you know it is right?

**Chapter 7.**
- Knowing that an agent is right starts with **seeing what it does**.
- Without that, a wrong answer **cannot be traced**, quality is a matter of opinion, and a prompt change can go unnoticed.
- MLflow 3 traces every request **step by step**.
- Agent evaluation scores the answers of each version.
- The Prompt Registry keeps a history of the prompts.
- Review Apps bring the **experts' judgment** in.
- Quality is now **measured before each release**.
- Data, models, agents and tools also need rules for who may use what.
- How is all of it governed?

**Chapter 8.**
- Governance has to cover all of it at once.
- Models, agents and tools often sit **outside the rules** that govern data.
- Calls to them go **unchecked**.
- The risks of AI are **not mapped**.
- Unity Catalog governs models, agents and tools the **same way as tables**.
- Unity Gateway checks and logs **every call** to them.
- The Databricks AI Security Framework links each risk to the control that covers it.
- Data, models, agents and tools are now governed with **one set of rules**.
- Most of the people who need them do not write code.
- How do business users get to them?

**Chapter 9.**
- Business users depend on analysts for **every question**.
- The same metric can mean **different things** from one report to the next.
- Each application usually needs its own infrastructure, identity and secrets.
- Genie One lets them ask in **plain language** and answers with their own permissions.
- Genie Ontology grounds every reply in the **certified definition**.
- Genie Agents, AI/BI Dashboards, Row Zero and Genie App Builder carry the same help into assistants, dashboards, spreadsheets and small apps.
- Databricks Apps hosts them **next to the governed data**.
- App Spaces governs who deploys and uses them.
- No-code now covers the **common needs**.
- Developers build the rest.
- What do builders get?

**Chapter 10.**
- Developers build the rest on the same platform.
- Much of the code is **repetitive**.
- Genie Code writes and explains code in every tool.
- The AI Dev Kit and Omnigent give agent development a **common base**.
- Databricks builds with these same components, up to **complete applications** for specific business domains.
- What comes ready-made?

**Chapter 11.**
- Some of these applications come **ready-made**.
- Customer data and security logs each sit in their own silo, with duplicate records, separate tools and logs deleted to save cost.
- CustomerLake builds **one governed profile** per customer and automates the campaigns.
- Lakewatch keeps the logs on the lakehouse and **investigates alerts** with agents.
- Both are built from the same parts: data on the lakehouse, governance in Unity Catalog, and agents.

**Closing.**
- Every part of the starting situation now has its answer.
- The data foundation stores the scattered copies once and governs them.
- The data science lifecycle makes the work **reproducible**.
- Model access puts every provider behind **one way of serving**.
- Production operations keep every model **under control**.
- Building agents lets them reach data and tools **safely**.
- Evaluation measures their answers.
- Governance sets **who may use what**.
- Business users and developers get **tools of their own**.
- Domain applications break the customer and security silos.
- AI projects now go **from pilot to production**.

**Check M15.**
- Each paragraph from chapter 2 to 10 ends on the last sentence of its chapter's handoff, word
  for word. The opening ends on chapter 1's handoff. Chapter 11's handoff asks no question,
  and its paragraph leads into the closing.
- The closing follows the Check M1 map in order: 1.1 data foundation, 1.2 data science
  lifecycle, 1.3 model access, 1.4 production operations, 1.5 building agents, 1.6 evaluation and
  governance, 1.7 business users and developers, 1.8 domain applications.
- Every product a paragraph names is cited by its chapter's points, as a capsule or in the
  bullets.

## M16 — Overview

The first slide of the Story tab: the path the story takes, one block per step, left to right.
Each block shows its modules as tiles and, next to it, a few short points for the presenter.
`scripts/story_extract.py` reads this section into `overview`. A tile is written "Label (slide id)",
and a click on it opens that slide. The build fails if a slide id does not exist.

**Block: Data Layer.**
- Tiles: Delta Lake (2.1) · Lakeflow (2.2) · Predictive Optimization (2.2) · Lakebase (2.3) · Lakehouse//RT (2.4) · LTAP (2.4) · Data quality monitoring (2.5)
- One place
- Governed once
- Fresh enough for AI

**Block: Models.**
- Tiles: Notebooks (3.1) · Feature Store (3.2) · MLflow (3.3) · AutoML (3.3) · AI Runtime (3.4) · Model Serving (4.1) · Foundation Model APIs (4.2) · Model fine-tuning (4.3) · External models (4.4)
- Train models
- Use any model

**Block: Ops.**
- Tiles: Model Registry (5.1) · Model Serving (5.2) · Lakehouse Monitoring (5.3) · MLOps & CI/CD (5.4)
- Versions tracked
- Models monitored
- Promoted through CI/CD

**Block: Agents.**
- Tiles: AI Functions (6.1) · AI Search (6.2) · Knowledge Assistant (6.2) · MCP (6.3) · Custom agents (6.4) · Supervisor Agent (6.5)
- Access to company data and tools
- Agents that act

**Block: Observability.**
- Tiles: MLflow Tracing (7.1) · Agent evaluation (7.2) · Prompt Registry (7.2) · Review Apps (7.3)
- Every step traced
- Quality measured
- Expert review

**Block: Governance.**
- Tiles: Unity Catalog (8.1) · Unity Gateway (8.2) · DASF (8.3)
- Governed like data
- One control plane

**Block: Business Users.**
- Tiles: Genie One (9.1) · Genie Ontology (9.2) · Genie Agents (9.3) · AI/BI Dashboards (9.4) · Genie App Builder (9.5) · Databricks Apps (9.6) · Genie Code (10.1) · AI Dev Kit (10.2) · Omnigent (10.2) · CustomerLake (11.1) · Lakewatch (11.2)
- No-code tools for business users
- Tools for developers
- Ready-made applications
