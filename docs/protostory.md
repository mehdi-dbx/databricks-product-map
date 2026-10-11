# Proto-story — working draft

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
People who need an answer wait for the few colleagues who can query these systems.

↳ **Link 1.1 → 1.2 (consequence).** AI needs that data. When the data is spread out,
every AI project first has to collect it.

**Point 1.2 — AI pilots blocked before production.**
So AI projects start as pilots on extracts. A pilot can work on its extract. Going to
production means reaching live data, proving the answers are right, and controlling who
uses which model and at what cost. Many pilots stop at that step.

**Hands off:** the work starts with the data. How do you get it into one place, governed
once and fresh enough for AI?

**Check M1.**
- 1.1 → 1.2 is a consequence. Spread-out data forces each project to start on extracts,
  so the pilot problem follows from the data problem.
- Point 1.2 names four obstacles that later chapters answer: live data (ch. 2), correct
  answers (ch. 6), model control and cost (ch. 4), and the step to production (ch. 10).
  This is the loop the ending will close.
- The handoff picks the data as the starting point because 1.2 depends on 1.1.

---

## M2 — Chapter 2. Data and AI foundation

**Receives:** how do you get the data into one place, governed once and fresh enough for AI?

**Point 2.1 — Open table storage with Delta Lake.** *(Lakehouse / Delta Lake)*
Databricks stores the data once, in open Delta tables in your cloud storage. Delta adds
transactions to those files. Batch jobs and streaming jobs write to the same tables
without corrupting them, and the schema can change without breaking readers.

↳ **Link 2.1 → 2.2 (prerequisite).** A storage layer is only useful once the data gets
into it and stays usable.

**Point 2.2 — Ingestion, transformation and table maintenance.** *(Lakeflow, Predictive Optimization)*
Lakeflow brings the data in and transforms it. Lakeflow Connect provides managed
connectors to databases and SaaS applications. Declarative pipelines describe the
transformations, and Lakeflow works out the order in which to run them. Predictive
Optimization then maintains the tables on its own, so nobody has to schedule
maintenance jobs.

↳ **Link 2.2 → 2.3 (gap).** The analytical data is now in place. Applications and agents
also read and write transactional data, and that data usually lives in a separate
database with its own copy.

**Point 2.3 — Transactional data on the same platform.** *(Lakebase, Lakebase Search)*
Lakebase is a serverless Postgres database inside the platform. It holds application
data and agent state, and its tables sync with Unity Catalog. Lakebase Search adds
vector and keyword search in the same Postgres database, with no separate vector store.

↳ **Link 2.3 → 2.4 (the remaining copy).** Transactional and analytical data now sit on
the same platform. The remaining copy is the one that feeds analytics with fresh operational data.

**Point 2.4 — Real-time analytics on operational data.** *(Lakehouse//RT, LTAP)*
Lakehouse//RT answers SQL queries in under 100 milliseconds directly on lakehouse
tables, so dashboards and applications no longer need a separate serving copy. LTAP, which is announced, keeps one dataset that is written in Lakebase and read in Lakehouse//RT, with no replication pipeline between them.

↳ **Link 2.4 → 2.5 (condition).** Everything is now in one place. That helps only if access, lineage and quality are handled once for all of it.

**Point 2.5 — Data catalog and data quality.** *(Classification / profiling / monitoring, Anomaly detection & remediation)*
Unity Catalog applies one set of permissions, lineage and audit to tables and files. Data quality is watched in the same place.
Classification tags sensitive data such as PII. Profiling and monitoring track quality.
Anomaly detection flags stale or broken tables and can trigger a repair job.

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

↳ **Link 3.2 → 3.3 (next step).** With features in place, the team trains many models
and compares them. Comparing them requires that every result can be reproduced.

**Point 3.3 — Experiment tracking and AutoML.** *(MLflow, AutoML, both trees)*
MLflow records every training run with its parameters, metrics, code version and
artifacts, so any result can be reproduced and compared. AutoML gives a first baseline.
It tries algorithms such as XGBoost and LightGBM, tunes them, and writes each trial as a
notebook the team can read and change.

↳ **Link 3.3 → 3.4 (limit).** Some datasets and models do not fit on one machine.

**Point 3.4 — Distributed training and GPUs.** *(Distributed training & GPU, AI Runtime — serverless GPU)*
Training then spreads across GPUs and clusters with managed libraries such as
TorchDistributor, DeepSpeed and Ray. AI Runtime provides GPUs on demand with no cluster
to manage, and it scales to zero when the job ends.

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

---

## M4 — Chapter 4. Model access and governance

**Receives:** how do you serve and control any model, your own or a provider's?

**Point 4.1 — Model serving.** *(Model Serving)*
Model Serving handles both cases with one kind of endpoint. Custom models, foundation
models and external models are served behind serverless endpoints with the same API.
Endpoints scale with demand, down to zero. They can be billed per token, with provisioned
throughput, or in batch. Features from the Feature Store are looked up at serving time.

↳ **Link 4.1 → 4.2 (what sits behind the endpoint).** For large language models, teams need to know which models are available behind those endpoints.

**Point 4.2 — Foundation models and their lifecycle.** *(Foundation Model APIs, Model versions, Model lifecycle churn)*
Foundation Model APIs give access through one API to models from providers that include Anthropic, OpenAI, Google and Meta. They are billed per token or with reserved capacity.
The catalog changes often. New versions arrive and older ones are retired. Databricks
publishes the supported models and their retirement dates. Because applications call
the same API for every model, moving to a newer model stays a small change.

↳ **Link 4.2 → 4.3 (when a general model falls short).** Sometimes a general model does not
know the company's vocabulary or tasks well enough.

**Point 4.3 — Model fine-tuning.** *(Model fine-tuning)*
Fine-tuning adapts an open model to company data with LoRA, QLoRA or full fine-tuning,
on serverless GPUs. The tuned model is logged in MLflow and served
like any other model.

↳ **Link 4.3 → 4.4 (models hosted elsewhere).** Some teams also call models that are hosted directly at a provider.

**Point 4.4 — External models.** *(External model services)*
These models are registered as external models, with their keys stored centrally, so their calls go through the same Model Serving endpoints as every other model.

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

---

## M5 — Chapter 5. Building agents

**Receives:** how do you build agents?

**Point 5.1 — Batch AI in SQL and pipelines.** *(AI Functions)*
AI Functions call a model from SQL or from a pipeline to classify, extract or summarize data and documents at scale.
The first step needs no agent. The results come back with
a fixed schema, and the data stays in Unity Catalog.

↳ **Link 5.1 → 5.2 (from batch to conversation).** An agent answers questions as they
come. To answer well, it first has to find the right information.

**Point 5.2 — Retrieval and document question answering.** *(AI Search, Knowledge Assistant)*
AI Search indexes documents and tables for vector and keyword search, keeps the index in
sync with the Delta tables, and returns citations. Knowledge Assistant packaged this into
a question-answering agent over documents that could be set up in minutes. It is now moving into Genie Agents.

↳ **Link 5.2 → 5.3 (from reading to acting).** Answering from documents only reads data.
Many tasks also need actions, such as running a query, opening a ticket or changing
code. Each of these tools needs a connection and permissions.

**Point 5.3 — Tool access through MCP.** *(Managed MCP servers, External connectors, MCP Services + custom MCP)*
The Model Context Protocol (MCP) is the standard way for an agent to call tools.
Databricks runs managed MCP servers for its own services, such as Genie, AI Search and
SQL. Connectors give governed access to Google Workspace, Microsoft 365, Slack and
GitHub. Teams can register their own MCP servers or host them as Databricks Apps. Every tool is a Unity Catalog object, so permissions and audit work the
same way as for data.

↳ **Link 5.3 → 5.4 (assembly).** An agent combines retrieval and tools with its own logic.

**Point 5.4 — Custom agents, memory and sandbox.** *(Custom Agents, Managed memory & sessions, Databricks Sandbox)*
Custom agents are written in code with frameworks such as LangGraph, LangChain or the
OpenAI SDK. They can use any model on Model Serving and any MCP tool. Managed
memory, stored in Lakebase, lets an agent remember context across conversations.
Databricks Sandbox runs the code an agent writes in an isolated environment, with scoped
access to data.

↳ **Link 5.4 → 5.5 (beyond one agent).** Some tasks are too large for one agent.

**Point 5.5 — Multi-agent orchestration.** *(Supervisor Agent)*
A supervisor agent splits a task across several agents and keeps each user's data
permissions. It is moving into Genie Agents as well.

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

---

## M6 — Chapter 6. Evaluating agents

**Receives:** how do you know the agent is right?

**Point 6.1 — Tracing.** *(MLflow 3 for GenAI)*
MLflow traces every request through the agent. It records each model call, tool call
and retrieval step, with inputs, outputs, latency and tokens, and it works with more
than 30 agent frameworks. When an answer is wrong, the trace shows the step where it
went wrong.

↳ **Link 6.1 → 6.2 (one request to many).** A trace shows one request. Judging quality
needs a score across many requests.

**Point 6.2 — Evaluation and prompt versioning.** *(Agent evaluation & monitoring, MLflow Prompt Registry)*
Agent evaluation applies LLM judges and custom scorers to traces. It runs in batch
before a release and continuously on live traffic. Each agent version gets its own
evaluation run, so versions can be compared. Prompts are versioned in the Prompt
Registry with staging and production aliases, so a prompt change is tracked like a code
change.

↳ **Link 6.2 → 6.3 (the judges need a reference).** An LLM judge is only useful if its
scores match what experts would say.

**Point 6.3 — Expert review and labeling.** *(Review Apps)*
Review Apps let domain experts test the agent in a chat interface and label its answers.
The labels attach to the traces and become evaluation datasets. They are also used to
align the judges with the experts.

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

---

## M13 — Chapter 7. Governance

**Receives:** how are data, models, agents and tools governed with one set of rules?

**Point 7.1 — Unity Catalog for AI assets.** *(Unity Catalog for AI assets)*
Unity Catalog governs models, agents, tools and credentials in the same way as tables
and files. Each of them is a Unity Catalog object with permissions, lineage and an audit
trail. Lineage follows the chain from data to model to agent. Credentials for external
services are stored in the catalog and encrypted.

↳ **Link 7.1 → 7.2 (from rules to traffic).** The catalog sets who may use each asset. Each
model call and each tool call also needs control at the moment it happens.

**Point 7.2 — Control of AI traffic with Unity Gateway.** *(Unity Gateway)*
Unity Gateway sits in front of all model and tool traffic and is built on Unity Catalog.
It sets who may call which model and tracks usage per user and team. Budgets cap spend.
Guardrails apply to every prompt and response, and every request is logged for audit.

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

---

## M7 — Chapter 8. AI for business users

**Receives:** how do business users get to the agents?

**Point 8.1 — Natural-language questions on company data.** *(Genie One)*
Genie One lets business users ask questions in plain language. They get answers from governed company data, with citations and with their own permissions
applied. When a dashboard or an agent already answers the question, Genie One sends the
user there.

↳ **Link 8.1 → 8.2 (trust needs shared definitions).** An answer is only trusted if
"revenue" or "active customer" means the same thing as in the official reports.

**Point 8.2 — Shared business definitions.** *(Genie Ontology)*
Genie Ontology holds those definitions. Each KPI is defined once, as a metric view in
Unity Catalog. The ontology also learns business context from existing dashboards,
queries and pipelines. It ranks sources by certification, usage and freshness, so Genie
answers from certified definitions first.

↳ **Link 8.2 → 8.3 (from definitions to know-how).** Once the definitions are shared,
domain experts can package what they know for others.

**Point 8.3 — No-code assistants built by domain experts.** *(Genie Agents)*
Genie Agents let a domain expert build a no-code assistant for a business area. The
assistant can follow up on questions, run multi-step analyses and explain its reasoning,
and it can be embedded in other applications. Knowledge Assistant and the supervisor agent are moving into Genie Agents.

↳ **Link 8.3 → 8.4 (familiar formats).** Many users still work in dashboards and
spreadsheets.

**Point 8.4 — AI-assisted dashboards and spreadsheets.** *(AI/BI Dashboards, Row Zero / Genie ZeroOps)*
An AI/BI dashboard can be built from a plain-language request. The assistant finds the
tables, writes the queries and picks the charts, and the author approves each step.
Row Zero, announced, brings the same governed data into a spreadsheet, with Genie
writing the queries behind the formulas.

↳ **Link 8.4 → 8.5 (from a question to a tool).** When the same question comes back
every week, it is worth turning into a small application.

**Point 8.5 — No-code app generation.** *(Genie App Builder)*
Genie App Builder generates a Databricks App from a plain-language description, within
the limits the admins set.

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

---

## M8 — Chapter 9. Developer tools

**Receives:** what do builders get?

**Point 9.1 — Application hosting.** *(Databricks Apps + App Spaces)*
Developers build applications with the frameworks they already use, such as Streamlit,
Gradio, React or FastAPI, and deploy them as Databricks Apps. The apps run serverless on
the platform. They sign users in with the platform's identity and read data through
Unity Catalog with each user's permissions. Custom MCP servers run the same way. App Spaces give admins one place to govern who deploys and uses which app.

↳ **Link 9.1 → 9.2 (what remains).** Hosting is now handled. Writing the code still takes
most of the time.

**Point 9.2 — Coding assistant.** *(Genie Code)*
Genie Code is the AI assistant inside notebooks, the SQL editor, pipelines and
dashboards. It writes and explains code from plain-language requests. A command-line
version, in beta, brings it into the terminal and into CI pipelines.

↳ **Link 9.2 → 9.3 (agents are code too).** Custom agents are code as well, and they need a project structure.

**Point 9.3 — Agent development kit and coding-agent harnesses.** *(AI Dev Kit + internal coding agents, Omnigent)*
The AI Dev Kit gives developers templates and scaffolding for agents, and a set of
tools governed in Unity Catalog. Databricks uses the same kit for its own internal
coding agents. Developers who already work with coding agents such as Claude, Codex or
Cursor can put them behind one interface with Omnigent, with shared context and central
policies.

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

---

## M9 — Chapter 10. Domain applications

**Receives:** what comes ready-made?

**Point 10.1 — Customer data application.** *(CustomerLake)*
CustomerLake, in private preview, builds customer 360 profiles on the lakehouse. It
joins transactions, behavior and engagement into one profile per customer. AI-assisted
identity resolution merges duplicate records. Campaign agents create and activate
audiences, and a real-time profile API feeds personalization.

↳ **Link 10.1 → 10.2 (same pattern, another domain).** CustomerLake applies the platform to
customer data. The same pattern applies to security data.

**Point 10.2 — Security operations application.** *(Lakewatch)*
Lakewatch, in private preview, runs security operations on the lakehouse. It keeps
security, IT and business logs in one place at object-storage cost, so they no longer
have to be deleted early. Autonomous agents investigate alerts and help write detection
rules, which are versioned and tested like code.

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

---

## M10 — Chapter 11. Production operations

**Receives:** how do you run models and agents in production, for years?

**Point 11.1 — Model registry.** *(MLflow Model Registry, Model Registry & governance)*
Every model in production is registered in Unity Catalog with its versions, its aliases
such as champion and challenger, and its lineage back to the training data. Promoting a new version means moving an alias, and model update triggers or deployment jobs can start the next steps automatically.

↳ **Link 11.1 → 11.2 (from registered to running).** A registered version then has to
serve traffic.

**Point 11.2 — Production serving.** *(Model Serving & batch inference)*
Model Serving endpoints run the registered version, for real-time
requests and for batch scoring. They handle more than 25,000 queries per second with low
added latency, and they scale with demand.

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
