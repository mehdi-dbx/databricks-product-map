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
| 2 Data and AI foundation | How do you get data into one place, governed and fresh? | The data is ready. The first thing teams do with it is learn from it. How does a data science team work on it? |
| 3 Data science lifecycle | How does a data science team work on it? | Trained models must be served. Many use cases now start from models someone else trained. How do you serve and control any model? |
| 4 Model access and governance | How do you serve and control any model? | A model answers. Value comes when it can act on data and tools. How do you build agents? |
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

**Point 1.1 — Data spread across systems.**
Most companies already run analytics and have started with AI. Their data sits in
several places: operational databases behind the applications, a warehouse for
reporting, a data lake for raw files, and SaaS tools. Each system keeps its own copies
and its own access rules. Pipelines move data between them to keep the copies in sync.
These pipelines are written and scheduled by hand, and the copies they feed are often
out of date. When a table stops being refreshed or breaks, nobody is warned, and the
repair is manual. People who need an answer wait for the few colleagues who can query
these systems.

↳ **Link 1.1 → 1.2 (consequence).** AI needs that data. When the data is spread out,
every AI project first has to collect it.

**Point 1.2 — Model work that is slow and hard to reproduce.**
Data scientists rebuild the same features in each project, and features are often
computed differently for training and in production. Experiments are hard to
reproduce, results stay scattered across teams, and algorithms and settings are tried
by hand. Large datasets do not fit on one machine, and GPUs are scarce, hard to set up
or left idle.

↳ **Link 1.2 → 1.3 (models trained elsewhere).** Many use cases now start from models
that someone else trained.

**Point 1.3 — Every model provider handled separately.**
Each model provider comes with its own serving setup, and API keys end up scattered
across code and teams. Token spend grows without warning, calls to outside models go
unaudited, and relying on one provider creates lock-in. Adapting a model to the
company's needs takes large and costly GPU resources.

↳ **Link 1.3 → 1.4 (from answers to actions).** A model on its own only answers. Agents
also look up company data and use tools.

**Point 1.4 — Agents that cannot reach data and tools safely.**
Using AI on company documents often means exporting the data to outside services. An
agent also needs search, tools and memory, and each connection is built by hand, with
credentials spread across agents. Agents start every conversation from scratch, and the
code they generate can run with unrestricted access to data. A single agent is not
enough for complex tasks, and routing work between agents is manual.

↳ **Link 1.4 → 1.5 (trust).** Once AI acts on company data, it has to be trusted.

**Point 1.5 — AI that nobody can verify or control.**
When an agent gives a wrong answer, nobody sees which step failed, and the quality of
its answers is not measured. Prompts change without being tracked, and expert feedback
sits in spreadsheets, cut off from the agents. Models, agents and tools are not governed
like data. Nobody has a central view of how AI is used, and nothing is audited.

↳ **Link 1.5 → 1.6 (people).** These gaps also reach the people who use data and AI
every day, and those who build with it.

**Point 1.6 — Business users and developers held back.**
Business users depend on those few colleagues for every question, and the same metric is
defined differently from one team or dashboard to the next. What experts know stays with
them, and analysis done in spreadsheets escapes governance. Even a small internal app
needs a developer, and developers host each app on separate infrastructure, with its own
identity and secrets. Much of their time goes into repetitive code and hand-built agent
scaffolding.

↳ **Link 1.6 → 1.7 (business domains).** Some business domains add silos of their own.

**Point 1.7 — Customer and security data in separate silos.**
Customer data is fragmented across systems, with duplicate records and no lineage.
Security logs sit in separate tools, and many are deleted early to save cost.

↳ **Link 1.7 → 1.8 (consequence).** With data, models and tools in this state, an AI
project cannot start on live, governed data.

**Point 1.8 — AI pilots blocked before production.**
So AI projects start as pilots on extracts. A pilot can work on its extract. Going to
production means reaching live data, proving the answers are right, and controlling who
uses which model and at what cost. Many pilots stop at that step. The models that do
reach production are hard to run, because versions are not tracked and promoting a new
one is manual and slow.

**Hands off:** the work starts with the data. How do you get it into one place, governed
once and fresh enough for AI?

**Check M1.**
- Rewritten on 2026-10-11 following `docs/story-starting-situation.md`. Each point is one
  group of the pains listed in `docs/story-pains.md`, in the order of the chapters that
  solve them. Every sentence of the former points 1.1 and 1.2 is kept: 1.1 gained two
  sentences, and 1.2 became 1.8 and gained one.
- Map of the loop the ending closes: 1.1 → ch. 2 · 1.2 → ch. 3 · 1.3 → ch. 4 ·
  1.4 → ch. 5 · 1.5 → ch. 6 and 7 · 1.6 → ch. 8 and 9 · 1.7 → ch. 10 · 1.8 → ch. 11.
  Point 1.8 also recalls the three obstacles that stop pilots: live data (ch. 2), right
  answers (ch. 6), and control of models and cost (ch. 4 and 7).
- Sources of the new sentences, as capsule [row] in `docs/story-pains.md`:
  - 1.1: Lakeflow [0] [3] [4]; Lakehouse//RT [1]; LTAP [4]; Anomaly detection &
    remediation [0] [2] [3]; Lakehouse / Delta Lake [0].
  - 1.2: Feature Store (ai) [2], (ds) [0]; MLflow [0] [1]; AutoML (ai) [0] [1];
    Distributed training & GPU [0] [4]; AI Runtime [0] [1].
  - 1.3: Model Serving [0] [1]; External model services [0] [2] [4]; Foundation Model
    APIs [0] [1]; Model fine-tuning [0] [1].
  - 1.4: AI Functions [0] [3]; AI Search [0]; Managed MCP servers [0] [1]; MCP Services
    + custom MCP [3]; Custom Agents [3]; Managed memory & sessions [2]; Databricks
    Sandbox [0] [1]; Supervisor Agent [0] [1].
  - 1.5: MLflow 3 for GenAI [0] [4]; Agent evaluation & monitoring [0]; MLflow Prompt
    Registry [0]; Review Apps [1]; Unity Catalog for AI assets [0] [3]; Unity Gateway
    [1] [4].
  - 1.6: Genie One [1]; Genie Ontology [0]; Genie Agents [3]; Row Zero / Genie ZeroOps
    [3]; Genie App Builder [1]; Databricks Apps + App Spaces [0] [2]; Genie Code [0]
    [2]; AI Dev Kit [1].
  - 1.7: CustomerLake [0] [1] [3]; Lakewatch [0] [2].
  - 1.8: MLflow Model Registry [0] [4].
- The 10 capsule references with no pains in the tree source no sentence here. Their
  chapters still answer the groups above.
- The handoff starts with the data, because every other group depends on it.

---

## M2 — Chapter 2. Data and AI foundation

**Receives:** how do you get the data into one place, governed once and fresh enough for AI?

**Point 2.1 — Open table storage with Delta Lake.** *(Lakehouse / Delta Lake)*
Databricks stores the data once, in open Delta tables in your cloud storage. Delta adds
transactions to those files. Batch jobs and streaming jobs write to the same tables
without corrupting them, and the schema can change without breaking readers.
**Effect:** The company keeps one consistent copy of its data, in an open format.
**Challenge:** Batch and streaming data often sit in separate stores, sometimes in closed or complex formats. A job that fails halfway can leave a table inconsistent, and a schema change can break the jobs that read it.
**Pivot:** Delta Lake brings these workloads together on one open table format.

↳ **Link 2.1 → 2.2 (prerequisite).** A storage layer is only useful once the data gets
into it and stays usable.

**Point 2.2 — Ingestion, transformation and table maintenance.** *(Lakeflow, Predictive Optimization)*
Lakeflow brings the data in and transforms it. Lakeflow Connect provides managed
connectors to databases and SaaS applications. Declarative pipelines describe the
transformations, and Lakeflow works out the order in which to run them. Predictive
Optimization then maintains the tables on its own, so nobody has to schedule
maintenance jobs.
**Effect:** Data engineers no longer write connector code or schedule table maintenance by hand.
**Challenge:** Bringing data in means writing connector code for each source and wiring job dependencies by hand. The tables then need maintenance that someone has to schedule and tune.
**Pivot:** Lakeflow and Predictive Optimization take over this work.

↳ **Link 2.2 → 2.3 (gap).** The analytical data is now in place. Applications and agents
also read and write transactional data, and that data usually lives in a separate
database with its own copy.

**Point 2.3 — Transactional data on the same platform.** *(Lakebase, Lakebase Search)*
Lakebase is a serverless Postgres database inside the platform. It holds application
data and agent state, and its tables sync with Unity Catalog. Lakebase Search adds
vector and keyword search in the same Postgres database, with no separate vector store.
**Effect:** Applications and agents keep their data on the same platform as the analytics, under the same governance.
**Challenge:** Application data in that separate database escapes governance, and search over it needs yet another store for vectors, which copies the data again.
**Pivot:** Lakebase and Lakebase Search bring this data and its search onto the platform.

↳ **Link 2.3 → 2.4 (the remaining copy).** Transactional and analytical data now sit on
the same platform. The remaining copy is the one that feeds analytics with fresh operational data.

**Point 2.4 — Real-time analytics on operational data.** *(Lakehouse//RT, LTAP)*
Lakehouse//RT answers SQL queries in under 100 milliseconds directly on lakehouse
tables, so dashboards and applications no longer need a separate serving copy. LTAP, which is announced, keeps one dataset that is written in Lakebase and read in Lakehouse//RT, with no replication pipeline between them.
**Effect:** Dashboards and applications read live data instead of a stale copy.
**Challenge:** Feeding analytics with operational data takes replication pipelines and a second system to maintain. The copies lag behind the source, and dashboard queries take seconds.
**Pivot:** Lakehouse//RT and LTAP remove that last copy.

↳ **Link 2.4 → 2.5 (condition).** Everything is now in one place. That helps only if access, lineage and quality are handled once for all of it.

**Point 2.5 — Data catalog and data quality.** *(Classification / profiling / monitoring, Anomaly detection & remediation)*
Unity Catalog applies one set of permissions, lineage and audit to tables and files. Data quality is watched in the same place.
Classification tags sensitive data such as PII. Profiling and monitoring track quality.
Anomaly detection flags stale or broken tables and can trigger a repair job.
**Effect:** Data teams are alerted when a table goes stale, and repairs run as audited jobs.
**Challenge:** Data freshness is invisible and nobody is notified, so a stale table can go unnoticed, and repairing it is manual and risky.
**Pivot:** Anomaly detection and data classification add this watch to the catalog.

**Hands off:** the data is in one place, fresh and governed. The first thing teams do
with data like this is learn from it. How does a data science team work on it?

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

## M3 — Chapter 3. Data science lifecycle

**Receives:** how does a data science team work on the data?

**Point 3.1 — Notebooks and data exploration.** *(Notebooks & collaboration, Data prep & EDA, DS languages & frameworks)*
Data scientists work in notebooks that run Python, SQL, R and Scala directly on the governed tables. Several people can edit the same notebook at once, and
notebooks are versioned in Git. Exploration uses the tools the team already knows:
pandas, Spark, SQL and built-in data profiles.

↳ **Link 3.1 → 3.2 (product of the work).** Exploration ends in features, the inputs a
model learns from. A feature computed one way for training and another way in production
gives wrong predictions.

**Point 3.2 — Feature Store.** *(Feature Store, both trees)*
The Feature Store keeps each feature definition in one place, governed by Unity Catalog.
Training sets are built with point-in-time correct joins, and the same definitions feed
predictions in production. For real-time use, features are served from an online store
on Lakebase.
**Effect:** Each feature is built once and reused by every team and every model.
**Challenge:** Teams duplicate the same features across projects, with no view of where each one comes from or who may use it.
**Pivot:** The Feature Store makes features a shared, governed asset.

↳ **Link 3.2 → 3.3 (next step).** With features in place, the team trains many models
and compares them. Comparing them requires that every result can be reproduced.

**Point 3.3 — Experiment tracking and AutoML.** *(MLflow, AutoML, both trees)*
MLflow records every training run with its parameters, metrics, code version and
artifacts, so any result can be reproduced and compared. AutoML gives a first baseline.
It tries algorithms such as XGBoost and LightGBM, tunes them, and writes each trial as a
notebook the team can read and change.
**Effect:** Model work becomes repeatable, and teams reach a first model faster.
**Challenge:** When each team keeps its own metrics, results cannot be compared, and searching algorithms and settings by hand delays every model.
**Pivot:** MLflow and AutoML take care of the tracking and the search.

↳ **Link 3.3 → 3.4 (limit).** Some datasets and models do not fit on one machine.

**Point 3.4 — Distributed training and GPUs.** *(Distributed training & GPU, AI Runtime — serverless GPU)*
Training then spreads across GPUs and clusters with managed libraries such as
TorchDistributor, DeepSpeed and Ray. AI Runtime provides GPUs on demand with no cluster
to manage, and it scales to zero when the job ends.
**Effect:** Training is no longer limited by the size of one machine or by access to GPUs.
**Challenge:** Distributed training code is hard to write correctly, GPUs are hard to get, and clusters configured by hand are error-prone or sit idle.
**Pivot:** Managed training libraries and AI Runtime take that work off the team.

**Hands off:** the team now has trained models. A model is only useful once applications
can call it. Many new use cases also start from large language models that someone else
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

## M4 — Chapter 4. Model access and governance

**Receives:** how do you serve and control any model, your own or a provider's?

**Point 4.1 — Model serving.** *(Model Serving)*
Model Serving handles both cases with one kind of endpoint. Custom models, foundation
models and external models are served behind serverless endpoints with the same API.
Endpoints scale with demand, down to zero. They can be billed per token, with provisioned
throughput, or in batch. Features from the Feature Store are looked up at serving time.
**Effect:** Putting a model into production no longer needs its own infrastructure.
**Challenge:** Each kind of model needs its own serving system, provisioned by hand, with access control split across them. Idle machines keep costing money.
**Pivot:** Model Serving replaces these systems with one serverless service.

↳ **Link 4.1 → 4.2 (what sits behind the endpoint).** For large language models, teams need to know which models are available behind those endpoints.

**Point 4.2 — Foundation models and their lifecycle.** *(Foundation Model APIs, Model versions, Model lifecycle churn)*
Foundation Model APIs give access through one API to models from providers that include Anthropic, OpenAI, Google and Meta. They are billed per token or with reserved capacity.
The catalog changes often. New versions arrive and older ones are retired. Databricks
publishes the supported models and their retirement dates. Because applications call
the same API for every model, moving to a newer model stays a small change.
**Effect:** Teams can use the best model for each task, from any of the main providers.
**Challenge:** Depending on one provider creates lock-in, token spend grows unpredictably, and models from different providers are tested piece by piece.
**Pivot:** Foundation Model APIs remove the dependency on any single provider.

↳ **Link 4.2 → 4.3 (when a general model falls short).** Sometimes a general model does not
know the company's vocabulary or tasks well enough.

**Point 4.3 — Model fine-tuning.** *(Model fine-tuning)*
Fine-tuning adapts an open model to company data with LoRA, QLoRA or full fine-tuning,
on serverless GPUs. The tuned model is logged in MLflow and served
like any other model.
**Effect:** Adapting a model to company data takes less GPU memory and is paid by the minute.
**Challenge:** Full fine-tuning needs large amounts of GPU memory and is expensive and slow. Once tuned, the model often sits apart from the systems that serve the others.
**Pivot:** Model fine-tuning makes this adaptation lighter and keeps it on the platform.

↳ **Link 4.3 → 4.4 (models hosted elsewhere).** Some teams also call models that are hosted directly at a provider.

**Point 4.4 — External models.** *(External model services)*
These models are registered as external models, with their keys stored centrally, so their calls go through the same Model Serving endpoints as every other model.
**Effect:** Calls to outside models are tracked and audited like every other model call.
**Challenge:** API keys end up scattered across code and team members, and these calls bypass security, with no view of what they cost.
**Pivot:** External model services bring these calls under the same control.

**Hands off:** every model, hosted on Databricks or at a provider, is now served the same way. Many use cases need a model that can also look up company data and call tools. How do you build agents?

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

## M5 — Chapter 5. Building agents

**Receives:** how do you build agents?

**Point 5.1 — Batch AI in SQL and pipelines.** *(AI Functions)*
AI Functions call a model from SQL or from a pipeline to classify, extract or summarize data and documents at scale.
The first step needs no agent. The results come back with
a fixed schema, and the data stays in Unity Catalog.
**Effect:** Teams apply AI to large volumes of data and documents without moving them out of the platform.
**Challenge:** Running a model over company data usually means sending the data to an outside service, building separate pipelines for documents and splitting the work into batches by hand. What comes back is unstructured.
**Pivot:** AI Functions do this work where the data already is.

↳ **Link 5.1 → 5.2 (from batch to conversation).** An agent answers questions as they
come. To answer well, it first has to find the right information.

**Point 5.2 — Retrieval and document question answering.** *(AI Search, Knowledge Assistant)*
AI Search indexes documents and tables for vector and keyword search, keeps the index in
sync with the Delta tables, and returns citations. Knowledge Assistant packaged this into
a question-answering agent over documents that could be set up in minutes. It is now moving into Genie Agents.
**Effect:** Agents answer from the company's own documents, with sources that can be checked.
**Challenge:** Search indexes are built and kept in sync by hand, and generic retrieval misses what a document means. Answers then cite sources that are missing or false.
**Pivot:** AI Search and Knowledge Assistant ground the answers in the right documents.

↳ **Link 5.2 → 5.3 (from reading to acting).** Answering from documents only reads data.
Many tasks also need actions, such as running a query, opening a ticket or changing
code. Each of these tools needs a connection and permissions.

**Point 5.3 — Tool access through MCP.** *(Managed MCP servers, External connectors, MCP Services + custom MCP)*
The Model Context Protocol (MCP) is the standard way for an agent to call tools.
Databricks runs managed MCP servers for its own services, such as Genie, AI Search and
SQL. Connectors give governed access to Google Workspace, Microsoft 365, Slack and
GitHub. Teams can register their own MCP servers or host them as Databricks Apps. Every tool is a Unity Catalog object, so permissions and audit work the
same way as for data.
**Effect:** Agents reach the company's tools through one governed route instead of one-off connections.
**Challenge:** Teams write a custom connector for each tool and host the servers themselves, credentials pile up across agents, and tool use stays hidden.
**Pivot:** Managed MCP servers and MCP Services turn each tool into a governed connection.

↳ **Link 5.3 → 5.4 (assembly).** An agent combines retrieval and tools with its own logic.

**Point 5.4 — Custom agents, memory and sandbox.** *(Custom Agents, Managed memory & sessions, Databricks Sandbox)*
Custom agents are written in code with frameworks such as LangGraph, LangChain or the
OpenAI SDK. They can use any model on Model Serving and any MCP tool. Managed
memory, stored in Lakebase, lets an agent remember context across conversations.
Databricks Sandbox runs the code an agent writes in an isolated environment, with scoped
access to data.
**Effect:** Developers build the agent they need, and it remembers its users and runs its code safely.
**Challenge:** Agent platforms often impose the framework and the model, and leave sessions and memory to be handled by hand. Users repeat their instructions in each conversation, and the code an agent writes is untrusted.
**Pivot:** Custom agents, managed memory and Databricks Sandbox take these limits away.

↳ **Link 5.4 → 5.5 (beyond one agent).** Some tasks are too large for one agent.

**Point 5.5 — Multi-agent orchestration.** *(Supervisor Agent)*
A supervisor agent splits a task across several agents and keeps each user's data
permissions. It is moving into Genie Agents as well.
**Effect:** Large tasks are shared across specialized agents and come back as one answer.
**Challenge:** Routing work between agents by hand gives disconnected answers, and a chain of agents can bypass a user's data permissions.
**Pivot:** The Supervisor Agent takes over the routing.

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
- Additions 5.1 (editorial guide):
  - Effect ← AI Functions, solves[0].solution, solves[3].solution
  - Challenge ← AI Functions, solves[0].problem, solves[4].problem, solves[2].problem, solves[1].problem
  - Pivot ← AI Functions, note
- Additions 5.2 (editorial guide):
  - Effect ← AI Search (ex-Vector Search), note; Knowledge Assistant, solves[2].solution
  - Challenge ← AI Search (ex-Vector Search), solves[0].problem, solves[2].problem; Knowledge Assistant, solves[1].problem, solves[2].problem
  - Pivot ← AI Search (ex-Vector Search), solves[0].solution; Knowledge Assistant, solves[0].solution
- Additions 5.3 (editorial guide):
  - Effect ← Managed MCP servers, solves[0].solution, solves[2].solution; MCP Services + custom MCP, solves[2].solution
  - Challenge ← Managed MCP servers, solves[0].problem, solves[3].problem, solves[1].problem, solves[5].problem
  - Pivot ← Managed MCP servers, note; MCP Services + custom MCP, note
- Additions 5.4 (editorial guide):
  - Effect ← Custom Agents, solves[0].solution; Managed memory & sessions, solves[1].solution; Databricks Sandbox, solves[0].solution
  - Challenge ← Custom Agents, solves[1].problem, solves[5].problem, solves[3].problem; Managed memory & sessions, solves[1].problem; Databricks Sandbox, solves[0].problem
  - Pivot ← Custom Agents, note; Managed memory & sessions, note; Databricks Sandbox, note
- Additions 5.5 (editorial guide):
  - Effect ← Supervisor Agent, solves[0].solution, solves[3].solution
  - Challenge ← Supervisor Agent, solves[0].problem, solves[3].problem, solves[4].problem
  - Pivot ← Supervisor Agent, solves[0].solution

---

## M6 — Chapter 6. Evaluating agents

**Receives:** how do you know the agent is right?

**Point 6.1 — Tracing.** *(MLflow 3 for GenAI)*
MLflow traces every request through the agent. It records each model call, tool call
and retrieval step, with inputs, outputs, latency and tokens, and it works with more
than 30 agent frameworks. When an answer is wrong, the trace shows the step where it
went wrong.
**Effect:** Operators see inside every agent request, step by step, including what it costs.
**Challenge:** Agent chains are opaque to the people who run them. When an answer is wrong, the failing step is hard to isolate, and the cost of each request is unknown.
**Pivot:** MLflow 3 makes each request visible.

↳ **Link 6.1 → 6.2 (one request to many).** A trace shows one request. Judging quality
needs a score across many requests.

**Point 6.2 — Evaluation and prompt versioning.** *(Agent evaluation & monitoring, MLflow Prompt Registry)*
Agent evaluation applies LLM judges and custom scorers to traces. It runs in batch
before a release and continuously on live traffic. Each agent version gets its own
evaluation run, so versions can be compared. Prompts are versioned in the Prompt
Registry with staging and production aliases, so a prompt change is tracked like a code
change.
**Effect:** Teams know whether a new agent version is better before it ships.
**Challenge:** Without quality metrics, traces are reviewed by hand and versions cannot be compared. Prompts change without a record, and staging and production drift apart.
**Pivot:** Agent evaluation scores the answers, and the Prompt Registry versions the prompts.

↳ **Link 6.2 → 6.3 (the judges need a reference).** An LLM judge is only useful if its
scores match what experts would say.

**Point 6.3 — Expert review and labeling.** *(Review Apps)*
Review Apps let domain experts test the agent in a chat interface and label its answers.
The labels attach to the traces and become evaluation datasets. They are also used to
align the judges with the experts.
**Effect:** What domain experts know becomes the standard the agent is judged against.
**Challenge:** Without ground truth, agent quality is a matter of opinion. Experts label answers in spreadsheets that are not linked to the traces, and their criteria drift from one session to the next.
**Pivot:** Review Apps connect the experts to the agent.

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
- Additions 6.1 (editorial guide):
  - Effect ← MLflow 3 for GenAI, solves[0].solution, solves[4].solution, solves[3].solution
  - Challenge ← MLflow 3 for GenAI, solves[0].problem, solves[4].problem, solves[3].problem
  - Pivot ← MLflow 3 for GenAI, note
- Additions 6.2 (editorial guide):
  - Effect ← Agent evaluation & monitoring, solves[4].solution, solves[1].solution
  - Challenge ← Agent evaluation & monitoring, solves[0].problem, solves[1].problem, solves[4].problem; MLflow Prompt Registry, solves[0].problem, solves[1].problem
  - Pivot ← Agent evaluation & monitoring, solves[0].solution; MLflow Prompt Registry, solves[0].solution
- Additions 6.3 (editorial guide):
  - Effect ← Review Apps, solves[3].solution, solves[0].solution
  - Challenge ← Review Apps, solves[0].problem, solves[1].problem, solves[4].problem
  - Pivot ← Review Apps, note

---

## M13 — Chapter 7. Governance

**Receives:** how are data, models, agents and tools governed with one set of rules?

**Point 7.1 — Unity Catalog for AI assets.** *(Unity Catalog for AI assets)*
Unity Catalog governs models, agents, tools and credentials in the same way as tables
and files. Each of them is a Unity Catalog object with permissions, lineage and an audit
trail. Lineage follows the chain from data to model to agent. Credentials for external
services are stored in the catalog and encrypted.
**Effect:** Each model, agent and tool can be traced to the data behind it and to everyone who used it.
**Challenge:** Models, agents and functions are not governed as assets of their own, permissions are enforced differently across them, and external credentials are scattered. Nobody knows which data feeds which model.
**Pivot:** Unity Catalog extends to these assets.

↳ **Link 7.1 → 7.2 (from rules to traffic).** The catalog sets who may use each asset. Each
model call and each tool call also needs control at the moment it happens.

**Point 7.2 — Control of AI traffic with Unity Gateway.** *(Unity Gateway)*
Unity Gateway sits in front of all model and tool traffic and is built on Unity Catalog.
It sets who may call which model and tracks usage per user and team. Budgets cap spend.
Guardrails apply to every prompt and response, and every request is logged for audit.
**Effect:** Every model and tool call is controlled and logged in one place.
**Challenge:** Each team connects to model providers on its own, so nobody sees who calls which model or what it costs. Prompts and responses go through without guardrails, and nothing is logged for an audit.
**Pivot:** Unity Gateway puts this traffic under one control plane.

↳ **Link 7.2 → 7.3 (the full list of risks).** Permissions and guardrails address known
risks. A security team also needs the full list of risks and the control that covers
each one.

**Point 7.3 — AI security risks and controls.** *(DASF v3.0)*
The Databricks AI Security Framework lists the risks of AI systems and the controls
that address them. Version 3.0 covers 97 risks and 73 controls, including 35 risks specific to agents. The controls include least-privilege tool access in Unity
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
- Additions 7.1 (editorial guide):
  - Effect ← Unity Catalog for AI assets, solves[2].solution, solves[3].solution
  - Challenge ← Unity Catalog for AI assets, solves[0].problem, solves[1].problem, solves[4].problem, solves[2].problem
  - Pivot ← Unity Catalog for AI assets, note
- Additions 7.2 (editorial guide):
  - Effect ← Unity Gateway, solves[0].solution, solves[4].solution
  - Challenge ← Unity Gateway, solves[0].problem, solves[1].problem, solves[2].problem, solves[3].problem, solves[4].problem
  - Pivot ← Unity Gateway, solves[0].solution

---

## M7 — Chapter 8. AI for business users

**Receives:** how do business users get to the agents?

**Point 8.1 — Natural-language questions on company data.** *(Genie One)*
Genie One lets business users ask questions in plain language. They get answers from governed company data, with citations and with their own permissions
applied. When a dashboard or an agent already answers the question, Genie One sends the
user there.
**Effect:** Business users get answers from company data without writing SQL.
**Challenge:** Most people who need data do not write SQL. Their questions queue up at the data team, and the answer often comes after the decision.
**Pivot:** Genie One gives them a front door to the data.

↳ **Link 8.1 → 8.2 (trust needs shared definitions).** An answer is only trusted if
"revenue" or "active customer" means the same thing as in the official reports.

**Point 8.2 — Shared business definitions.** *(Genie Ontology)*
Genie Ontology holds those definitions. Each KPI is defined once, as a metric view in
Unity Catalog. The ontology also learns business context from existing dashboards,
queries and pipelines. It ranks sources by certification, usage and freshness, so Genie
answers from certified definitions first.
**Effect:** Every answer uses the company's certified definition of each metric.
**Challenge:** Metrics are defined differently across dashboards, queries and teams, and business context is scattered across documents, chats and tickets. An AI can then pick an obsolete or draft definition.
**Pivot:** Genie Ontology is the layer that grounds Genie in these definitions.

↳ **Link 8.2 → 8.3 (from definitions to know-how).** Once the definitions are shared,
domain experts can package what they know for others.

**Point 8.3 — No-code assistants built by domain experts.** *(Genie Agents)*
Genie Agents let a domain expert build a no-code assistant for a business area. The
assistant can follow up on questions, run multi-step analyses and explain its reasoning,
and it can be embedded in other applications. Knowledge Assistant and the supervisor agent are moving into Genie Agents.
**Effect:** The knowledge of each business area becomes available to everyone in it.
**Challenge:** Business knowledge stays with a few experts, and dashboards only answer the questions they were built for. Deeper analysis is spread across separate tools.
**Pivot:** Genie Agents turn that expertise into a shared assistant.

↳ **Link 8.3 → 8.4 (familiar formats).** Many users still work in dashboards and
spreadsheets.

**Point 8.4 — AI-assisted dashboards and spreadsheets.** *(AI/BI Dashboards, Row Zero / Genie ZeroOps)*
An AI/BI dashboard can be built from a plain-language request. The assistant finds the
tables, writes the queries and picks the charts, and the author approves each step.
Row Zero, announced, brings the same governed data into a spreadsheet, with Genie
writing the queries behind the formulas.
**Effect:** Analysts and business users go from a question to a governed dashboard on their own.
**Challenge:** Building a dashboard takes SQL and specialist skills, so requests wait. Meanwhile, analysis done in spreadsheets is cut off from the governed data and unaudited.
**Pivot:** AI/BI Dashboards and Row Zero bring the assistant into both.

↳ **Link 8.4 → 8.5 (from a question to a tool).** When the same question comes back
every week, it is worth turning into a small application.

**Point 8.5 — No-code app generation.** *(Genie App Builder)*
Genie App Builder generates a Databricks App from a plain-language description, within
the limits the admins set.
**Effect:** Business teams turn an idea into a working app in minutes.
**Challenge:** Building an app takes software engineering skills, and every change needs a developer and a new deployment.
**Pivot:** Genie App Builder lets the team describe the app instead.

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
- Additions 8.1 (editorial guide):
  - Effect ← Genie One, solves[1].solution
  - Challenge ← Genie One, solves[0].problem, solves[1].problem
  - Pivot ← Genie One, solves[0].solution
- Additions 8.2 (editorial guide):
  - Effect ← Genie Ontology, solves[3].solution, solves[0].solution
  - Challenge ← Genie Ontology, solves[0].problem, solves[2].problem, solves[1].problem
  - Pivot ← Genie Ontology, note
- Additions 8.3 (editorial guide):
  - Effect ← Genie Agents, solves[3].solution
  - Challenge ← Genie Agents, solves[3].problem, solves[0].problem, solves[2].problem
  - Pivot ← Genie Agents, solves[3].solution
- Additions 8.4 (editorial guide):
  - Effect ← AI/BI Dashboards (Lakeview), solves[5].solution
  - Challenge ← AI/BI Dashboards (Lakeview), solves[1].problem, solves[5].problem, solves[4].problem; Row Zero / Genie ZeroOps, solves[0].problem, solves[3].problem
  - Pivot ← AI/BI Dashboards (Lakeview), note; Row Zero / Genie ZeroOps, note
- Additions 8.5 (editorial guide):
  - Effect ← Genie App Builder, solves[0].solution
  - Challenge ← Genie App Builder, solves[1].problem, solves[3].problem
  - Pivot ← Genie App Builder, solves[1].solution

---

## M8 — Chapter 9. Developer tools

**Receives:** what do builders get?

**Point 9.1 — Application hosting.** *(Databricks Apps + App Spaces)*
Developers build applications with the frameworks they already use, such as Streamlit,
Gradio, React or FastAPI, and deploy them as Databricks Apps. The apps run serverless on
the platform. They sign users in with the platform's identity and read data through
Unity Catalog with each user's permissions. Custom MCP servers run the same way. App Spaces give admins one place to govern who deploys and uses which app.
**Effect:** Data and AI applications run on the platform itself, next to the governed data.
**Challenge:** A data or AI application usually runs on separate infrastructure, with its own identity management and secrets. It sits apart from the governed data, and access control and audit trails are hard to put in place.
**Pivot:** Databricks Apps brings these applications onto the platform.

↳ **Link 9.1 → 9.2 (what remains).** Hosting is now handled. Writing the code still takes
most of the time.

**Point 9.2 — Coding assistant.** *(Genie Code)*
Genie Code is the AI assistant inside notebooks, the SQL editor, pipelines and
dashboards. It writes and explains code from plain-language requests. A command-line
version, in beta, brings it into the terminal and into CI pipelines.
**Effect:** Developers write less repetitive code, with the same assistant in every tool.
**Challenge:** Much of that code is repetitive boilerplate, developers switch between separate tools for notebooks, SQL, pipelines and dashboards, and tuning SQL is hard for non-experts.
**Pivot:** Genie Code takes on that work.

↳ **Link 9.2 → 9.3 (agents are code too).** Custom agents are code as well, and they need a project structure.

**Point 9.3 — Agent development kit and coding-agent harnesses.** *(AI Dev Kit + internal coding agents, Omnigent)*
The AI Dev Kit gives developers templates and scaffolding for agents, and a set of
tools governed in Unity Catalog. Databricks uses the same kit for its own internal
coding agents. Developers who already work with coding agents such as Claude, Codex or
Cursor can put them behind one interface with Omnigent, with shared context and central
policies.
**Effect:** Teams build agents on a ready structure, with their tools governed and audited.
**Challenge:** Developers scaffold each agent and its tool connections by hand, and the integrations they create are not audited. Each coding-agent tool is its own isolated world, so content is copied between them by hand.
**Pivot:** The AI Dev Kit and Omnigent give this work a common base.

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
- Additions 9.1 (editorial guide):
  - Effect ← Databricks Apps + App Spaces, solves[0].solution, solves[3].solution
  - Challenge ← Databricks Apps + App Spaces, solves[0].problem, solves[2].problem, solves[3].problem, solves[1].problem
  - Pivot ← Databricks Apps + App Spaces, note
- Additions 9.2 (editorial guide):
  - Effect ← Genie Code, solves[2].solution, solves[1].solution
  - Challenge ← Genie Code, solves[2].problem, solves[1].problem, solves[3].problem
  - Pivot ← Genie Code, solves[0].solution
- Additions 9.3 (editorial guide):
  - Effect ← AI Dev Kit + internal coding agents (Isaac), solves[1].solution, solves[0].solution
  - Challenge ← AI Dev Kit + internal coding agents (Isaac), solves[1].problem, solves[4].problem; Omnigent, solves[0].problem, solves[2].problem
  - Pivot ← AI Dev Kit + internal coding agents (Isaac), note; Omnigent, note

---

## M9 — Chapter 10. Domain applications

**Receives:** what comes ready-made?

**Point 10.1 — Customer data application.** *(CustomerLake)*
CustomerLake, in private preview, builds customer 360 profiles on the lakehouse. It
joins transactions, behavior and engagement into one profile per customer. AI-assisted
identity resolution merges duplicate records. Campaign agents create and activate
audiences, and a real-time profile API feeds personalization.
**Effect:** Campaigns and personalization run on governed customer profiles that stay current.
**Challenge:** Each system holds its own part of the customer, often duplicated and without lineage, and audiences are built and activated by hand.
**Pivot:** CustomerLake gives the platform a ready-made answer for customer data.

↳ **Link 10.1 → 10.2 (same pattern, another domain).** CustomerLake applies the platform to
customer data. The same pattern applies to security data.

**Point 10.2 — Security operations application.** *(Lakewatch)*
Lakewatch, in private preview, runs security operations on the lakehouse. It keeps
security, IT and business logs in one place at object-storage cost, so they no longer
have to be deleted early. Autonomous agents investigate alerts and help write detection
rules, which are versioned and tested like code.
**Effect:** Security teams keep all their logs and investigate faster.
**Challenge:** Security telemetry is split across separate tools, threat hunting and triage are manual, and detection rules are hard to version and test.
**Pivot:** Lakewatch adds agents to security operations.

↳ **Link 10.2 → handoff (what the two share).** Both applications are built from the same parts: data on the lakehouse, governance in Unity Catalog, and agents.

**Hands off:** whether a company builds its own applications or uses ready-made ones,
every model and agent then runs in production for years. How do you run it?

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
- Additions 10.1 (editorial guide):
  - Effect ← CustomerLake, solves[3].solution, solves[4].solution
  - Challenge ← CustomerLake, solves[0].problem, solves[1].problem, solves[3].problem, solves[2].problem
  - Pivot ← CustomerLake, note
- Additions 10.2 (editorial guide):
  - Effect ← Lakewatch, solves[2].solution, solves[4].solution, solves[1].solution
  - Challenge ← Lakewatch, solves[0].problem, solves[1].problem, solves[3].problem
  - Pivot ← Lakewatch, note

---

## M10 — Chapter 11. Production operations

**Receives:** how do you run models and agents in production, for years?

**Point 11.1 — Model registry.** *(MLflow Model Registry, Model Registry & governance)*
Every model in production is registered in Unity Catalog with its versions, its aliases
such as champion and challenger, and its lineage back to the training data. Promoting a new version means moving an alias, and model update triggers or deployment jobs can start the next steps automatically.
**Effect:** Teams always know which model version is in production and where it came from.
**Challenge:** Model versions go untracked, promotions are manual and error-prone, and the link between a model and its training data gets lost. Without a shared view across workspaces, teams rebuild models that already exist.
**Pivot:** The Model Registry in Unity Catalog keeps this history and governs every model.

↳ **Link 11.1 → 11.2 (from registered to running).** A registered version then has to
serve traffic.

**Point 11.2 — Production serving.** *(Model Serving & batch inference)*
Model Serving endpoints run the registered version, for real-time
requests and for batch scoring. They handle more than 25,000 queries per second with low
added latency, and they scale with demand.
**Effect:** Production traffic can grow without anyone resizing the infrastructure.
**Challenge:** Models end up spread across several serving platforms, scaled by hand, with no central view of what is deployed.
**Pivot:** Model Serving runs them all from one place.

↳ **Link 11.2 → 11.3 (what happens over time).** Once a model is serving, its inputs
change over time and its quality can drift.

**Point 11.3 — Monitoring and drift detection.** *(Monitoring & evaluation)*
Inference tables log every request and response. Lakehouse Monitoring profiles those
tables, detects drift in data and in predictions, and raises alerts. The same monitoring covers data quality and agents.

↳ **Link 11.3 → 11.4 (from detecting to fixing).** When monitoring shows a problem, the
fix has to reach production safely, and the same way every time.

**Point 11.4 — MLOps and CI/CD.** *(MLOps & CI/CD)*
MLOps Stacks and Declarative Automation Bundles describe code, jobs, models and their
environments as files in Git. Lakeflow Jobs run the pipelines. Each change goes from development to production through that automated path.

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
- Additions 11.1 (editorial guide):
  - Effect ← MLflow Model Registry, solves[0].solution, solves[2].solution; Model Registry & governance, solves[2].solution
  - Challenge ← MLflow Model Registry, solves[0].problem, solves[1].problem; Model Registry & governance, solves[2].problem, solves[0].problem
  - Pivot ← Model Registry & governance, note
- Additions 11.2 (editorial guide):
  - Effect ← Model Serving & batch inference, solves[1].solution
  - Challenge ← Model Serving & batch inference, solves[0].problem, solves[1].problem, solves[2].problem
  - Pivot ← Model Serving & batch inference, solves[0].solution, solves[2].solution

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
section into the Story tab: the title and the opening at the top, each chapter's paragraph at
the head of its chapter, and the closing after chapter 11.

**Title:** From scattered data to AI in production

**Opening.**
Most large organizations already run analytics and have started with AI. Their data sits in
several systems, each with its own copies and rules, kept in sync by pipelines built by hand.
Data scientists rebuild the same features and struggle to reproduce their results, every model
provider is handled separately, and agents cannot reach data and tools safely. Nobody can
verify the answers of the AI or see how it is used. Business users wait for the few colleagues
who can query the data, developers host each application on its own infrastructure, and
customer and security data stay in their own silos. So AI projects start as pilots on
extracts, and many stop before production. The work starts with the data. How do you get it
into one place, governed once and fresh enough for AI?

**Chapter 2.**
It starts by storing the data once. Copies multiply because every workload, from batch jobs to
applications and dashboards, keeps its own. Delta Lake keeps one open copy, Lakeflow and
Predictive Optimization bring the data in and maintain it, Lakebase and Lakehouse//RT put
applications and live analytics on that same copy, and Unity Catalog governs all of it and
watches its quality. The organization now works from one fresh, governed copy of its data. How
does a data science team work on it?

**Chapter 3.**
Data scientists explore that governed data in notebooks, with the languages they already know.
Their work slows down when features are rebuilt for each project and results cannot be
reproduced. The Feature Store shares each feature across teams, MLflow and AutoML track and
speed up the experiments, and AI Runtime provides GPUs when the data outgrows one machine. The
team ends up with models it can reproduce, while many new uses start from models trained by
others. How do you serve and control any model, your own or a provider's?

**Chapter 4.**
Serving those models is the next step. Without one way to do it, every model and every provider
brings its own system, keys and costs. Model Serving puts every model behind the same kind of
endpoint, Foundation Model APIs reach the main providers through one API, fine-tuning adapts
open models to the company's needs, and external models go through the same control. Every
model is now served the same way, and many uses need one that can also look up company data and
call tools. How do you build agents?

**Chapter 5.**
An agent starts from the company's own data. It has to find the right information, use tools,
remember what it learned and run code without putting data at risk. AI Functions bring models
to the data in SQL, AI Search and Knowledge Assistant find the right documents, MCP connects
tools under Unity Catalog, custom agents get managed memory and Databricks Sandbox, and the
Supervisor Agent shares out large tasks. The agent can now use company data and tools, and
before it reaches users, it has to be trusted. How do you know it is right?

**Chapter 6.**
Knowing that an agent is right starts with seeing what it does. Without that, a wrong answer
cannot be traced, quality is a matter of opinion, and a prompt change can go unnoticed. MLflow 3
traces every request step by step, agent evaluation scores the answers of each version, the
Prompt Registry versions the prompts, and Review Apps bring the experts' judgment in. Quality is
now measured before each release, and data, models, agents and tools also need rules for who may
use what. How is all of it governed?

**Chapter 7.**
Governance has to cover all of it at once. Models, agents and tools often sit outside the rules
that govern data, calls to models go unchecked, and the risks of AI are not mapped. Unity
Catalog governs them the same way as tables, Unity Gateway controls and logs every model and
tool call, and the Databricks AI Security Framework links each risk to the control that covers
it. Data, models, agents and tools are now governed with one set of rules, but most of the
people who need them do not write code. How do business users get to them?

**Chapter 8.**
Business users depend on analysts for every question, and the same metric can mean different
things from one report to the next. Genie One lets them ask in plain language and answers with
their own permissions, and Genie Ontology makes each answer use the certified definition. Genie
Agents, AI/BI Dashboards, Row Zero and Genie App Builder carry the same help into assistants,
dashboards, spreadsheets and small apps. No-code now covers the common needs, and developers
build the rest. What do builders get?

**Chapter 9.**
Developers build the rest on the same platform. Each application usually needs its own
infrastructure, identity and secrets, and much of the code is repetitive. Databricks Apps hosts
applications next to the governed data, App Spaces governs who deploys and uses them, Genie Code
writes and explains code in every tool, and the AI Dev Kit and Omnigent give agent development a
common base. Databricks builds with these same components, up to complete applications for
specific business domains. What comes ready-made?

**Chapter 10.**
Some of these applications come ready-made. Customer data and security logs each sit in their
own silo, with duplicate records, separate tools and logs deleted to save cost. CustomerLake
builds one governed profile per customer and lets agents run the campaigns, and Lakewatch keeps
the logs on the lakehouse and investigates alerts with agents. Whether the organization builds
its applications or uses ready-made ones, every model and agent then runs in production for
years. How do you run it?

**Chapter 11.**
Running it means keeping track of every version. Models drift as their inputs change, and each
fix has to reach production the same way every time. The Model Registry in Unity Catalog records
each version and its lineage, Model Serving runs the registered version at scale, Lakehouse
Monitoring detects drift and raises alerts, and MLOps Stacks and bundles carry each change from
development to production. Each model and agent now runs, is watched and is updated in
production for as long as it is used.

**Closing.**
Every part of the starting situation now has its answer. The data foundation stores the
scattered data once and governs it, the data science lifecycle makes model work reproducible,
and model access puts every provider behind one way of serving. Building agents gives them safe
access to data and tools, evaluation measures their answers, and governance sets who may use
what. Business users and developers get tools of their own, domain applications break the
customer and security silos, and production operations keep every model under control. AI no
longer stops at the pilot.

**Check M15.**
- Each paragraph from chapter 2 to 10 ends on the last sentence of its chapter's handoff, word
  for word. The opening ends on chapter 1's handoff. Chapter 11 has no handoff and leads into
  the closing.
- The closing follows the Check M1 map in order: 1.1 data foundation, 1.2 data science
  lifecycle, 1.3 model access, 1.4 building agents, 1.5 evaluation and governance, 1.6 business
  users and developers, 1.7 domain applications, 1.8 production operations.
- Every product a paragraph names is cited by its chapter's points, as a capsule or in the
  bullets.
