# The Databricks data and AI story

**From scattered data to AI in production**

Most large organizations already run analytics and have started with AI. Their data sits in several systems, each with its own copies and rules, kept in sync by pipelines built by hand. Data scientists rebuild the same features and struggle to reproduce their results, every model provider is handled separately, and agents cannot reach data and tools safely. Nobody can verify the answers of the AI or see how it is used. Business users wait for the few colleagues who can query the data, developers host each application on its own infrastructure, and customer and security data stay in their own silos. So AI projects start as pilots on extracts, and many stop before production. The work starts with the data. How do you get it into one place, governed once and fresh enough for AI?

## 1. Challenges

### Data spread across systems

- Most companies already run analytics and have started with AI.
- Their data sits in several places: operational databases behind the applications, a warehouse for reporting, a data lake for raw files, and SaaS tools.
- Each system keeps its own copies and its own access rules.
- Pipelines move data between them to keep the copies in sync.
- These pipelines are written and scheduled by hand, and the copies they feed are often out of date.
- When a table stops being refreshed or breaks, nobody is warned, and the repair is manual.
- People who need an answer wait for the few colleagues who can query these systems.

### Model work that is slow and hard to reproduce

*AI needs that data. When the data is spread out, every AI project first has to collect it.*

- Data scientists rebuild the same features in each project, and features are often computed differently for training and in production.
- Experiments are hard to reproduce, results stay scattered across teams, and algorithms and settings are tried by hand.
- Large datasets do not fit on one machine, and GPUs are scarce, hard to set up or left idle.

### Every model provider handled separately

*Many use cases now start from models that someone else trained.*

- Each model provider comes with its own serving setup, and API keys end up scattered across code and teams.
- Token spend grows without warning, calls to outside models go unaudited, and relying on one provider creates lock-in.
- Adapting a model to the company's needs takes large and costly GPU resources.

### Agents that cannot reach data and tools safely

*A model on its own only answers. Agents also look up company data and use tools.*

- Using AI on company documents often means exporting the data to outside services.
- An agent also needs search, tools and memory, and each connection is built by hand, with credentials spread across agents.
- Agents start every conversation from scratch, and the code they generate can run with unrestricted access to data.
- A single agent is not enough for complex tasks, and routing work between agents is manual.

### AI that nobody can verify or control

*Once AI acts on company data, it has to be trusted.*

- When an agent gives a wrong answer, nobody sees which step failed, and the quality of its answers is not measured.
- Prompts change without being tracked, and expert feedback sits in spreadsheets, cut off from the agents.
- Models, agents and tools are not governed like data.
- Nobody has a central view of how AI is used, and nothing is audited.

### Business users and developers held back

*These gaps also reach the people who use data and AI every day, and those who build with it.*

- Business users depend on those few colleagues for every question, and the same metric is defined differently from one team or dashboard to the next.
- What experts know stays with them, and analysis done in spreadsheets escapes governance.
- Even a small internal app needs a developer, and developers host each app on separate infrastructure, with its own identity and secrets.
- Much of their time goes into repetitive code and hand-built agent scaffolding.

### Customer and security data in separate silos

*Some business domains add silos of their own.*

- Customer data is fragmented across systems, with duplicate records and no lineage.
- Security logs sit in separate tools, and many are deleted early to save cost.

### AI pilots blocked before production

*With data, models and tools in this state, an AI project cannot start on live, governed data.*

- So AI projects start as pilots on extracts.
- A pilot can work on its extract.
- Going to production means reaching live data, proving the answers are right, and controlling who uses which model and at what cost.
- Many pilots stop at that step.
- The models that do reach production are hard to run, because versions are not tracked and promoting a new one is manual and slow.

*The work starts with the data. How do you get it into one place, governed once and fresh enough for AI?*

## 2. Data and AI foundation

It starts by storing the data once. Copies multiply because every workload, from batch jobs to applications and dashboards, keeps its own. Delta Lake keeps one open copy, Lakeflow and Predictive Optimization bring the data in and maintain it, Lakebase and Lakehouse//RT put applications and live analytics on that same copy, and Unity Catalog governs all of it and watches its quality. The organization now works from one fresh, governed copy of its data. How does a data science team work on it?

### Open table storage with Delta Lake

The company keeps one consistent copy of its data, in an open format.

Batch and streaming data often sit in separate stores, sometimes in closed or complex formats. A job that fails halfway can leave a table inconsistent, and a schema change can break the jobs that read it.

Delta Lake brings these workloads together on one open table format.

- Databricks stores the data once, in open Delta tables in your cloud storage.
- Delta adds transactions to those files.
- Batch jobs and streaming jobs write to the same tables without corrupting them, and the schema can change without breaking readers.

*Capsules: Lakehouse / Delta Lake*

### Ingestion, transformation and table maintenance

Data engineers no longer write connector code or schedule table maintenance by hand.

*A storage layer is only useful once the data gets into it and stays usable.*

Bringing data in means writing connector code for each source and wiring job dependencies by hand. The tables then need maintenance that someone has to schedule and tune.

Lakeflow and Predictive Optimization take over this work.

- Lakeflow brings the data in and transforms it.
- Lakeflow Connect provides managed connectors to databases and SaaS applications.
- Declarative pipelines describe the transformations, and Lakeflow works out the order in which to run them.
- Predictive Optimization then maintains the tables on its own, so nobody has to schedule maintenance jobs.

*Capsules: Lakeflow, Predictive Optimization*

### Transactional data on the same platform

Applications and agents keep their data on the same platform as the analytics, under the same governance.

*The analytical data is now in place. Applications and agents also read and write transactional data, and that data usually lives in a separate database with its own copy.*

Application data in that separate database escapes governance, and search over it needs yet another store for vectors, which copies the data again.

Lakebase and Lakebase Search bring this data and its search onto the platform.

- Lakebase is a serverless Postgres database inside the platform.
- It holds application data and agent state, and its tables sync with Unity Catalog.
- Lakebase Search adds vector and keyword search in the same Postgres database, with no separate vector store.

*Capsules: Lakebase, Lakebase Search*

### Real-time analytics on operational data

Dashboards and applications read live data instead of a stale copy.

*Transactional and analytical data now sit on the same platform. The remaining copy is the one that feeds analytics with fresh operational data.*

Feeding analytics with operational data takes replication pipelines and a second system to maintain. The copies lag behind the source, and dashboard queries take seconds.

Lakehouse//RT and LTAP remove that last copy.

- Lakehouse//RT answers SQL queries in under 100 milliseconds directly on lakehouse tables, so dashboards and applications no longer need a separate serving copy.
- LTAP, which is announced, keeps one dataset that is written in Lakebase and read in Lakehouse//RT, with no replication pipeline between them.

*Capsules: Lakehouse//RT, LTAP*

### Data catalog and data quality

Data teams are alerted when a table goes stale, and repairs run as audited jobs.

*Everything is now in one place. That helps only if access, lineage and quality are handled once for all of it.*

Data freshness is invisible and nobody is notified, so a stale table can go unnoticed, and repairing it is manual and risky.

Anomaly detection and data classification add this watch to the catalog.

- Unity Catalog applies one set of permissions, lineage and audit to tables and files.
- Data quality is watched in the same place.
- Classification tags sensitive data such as PII.
- Profiling and monitoring track quality.
- Anomaly detection flags stale or broken tables and can trigger a repair job.

*Capsules: Classification / profiling / monitoring, Anomaly detection & remediation*

*The data is in one place, fresh and governed. The first thing teams do with data like this is learn from it. How does a data science team work on it?*

## 3. Data science lifecycle

Data scientists explore that governed data in notebooks, with the languages they already know. Their work slows down when features are rebuilt for each project and results cannot be reproduced. The Feature Store shares each feature across teams, MLflow and AutoML track and speed up the experiments, and AI Runtime provides GPUs when the data outgrows one machine. The team ends up with models it can reproduce, while many new uses start from models trained by others. How do you serve and control any model, your own or a provider's?

### Notebooks and data exploration

- Data scientists work in notebooks that run Python, SQL, R and Scala directly on the governed tables.
- Several people can edit the same notebook at once, and notebooks are versioned in Git.
- Exploration uses the tools the team already knows: pandas, Spark, SQL and built-in data profiles.

*Capsules: Notebooks & collaboration, Data prep & EDA, DS languages & frameworks*

### Feature Store

Each feature is built once and reused by every team and every model.

*Exploration ends in features, the inputs a model learns from. A feature computed one way for training and another way in production gives wrong predictions.*

Teams duplicate the same features across projects, with no view of where each one comes from or who may use it.

The Feature Store makes features a shared, governed asset.

- The Feature Store keeps each feature definition in one place, governed by Unity Catalog.
- Training sets are built with point-in-time correct joins, and the same definitions feed predictions in production.
- For real-time use, features are served from an online store on Lakebase.

*Capsules: Feature Store*

### Experiment tracking and AutoML

Model work becomes repeatable, and teams reach a first model faster.

*With features in place, the team trains many models and compares them. Comparing them requires that every result can be reproduced.*

When each team keeps its own metrics, results cannot be compared, and searching algorithms and settings by hand delays every model.

MLflow and AutoML take care of the tracking and the search.

- MLflow records every training run with its parameters, metrics, code version and artifacts, so any result can be reproduced and compared.
- AutoML gives a first baseline.
- It tries algorithms such as XGBoost and LightGBM, tunes them, and writes each trial as a notebook the team can read and change.

*Capsules: MLflow, AutoML*

### Distributed training and GPUs

Training is no longer limited by the size of one machine or by access to GPUs.

*Some datasets and models do not fit on one machine.*

Distributed training code is hard to write correctly, GPUs are hard to get, and clusters configured by hand are error-prone or sit idle.

Managed training libraries and AI Runtime take that work off the team.

- Training then spreads across GPUs and clusters with managed libraries such as TorchDistributor, DeepSpeed and Ray.
- AI Runtime provides GPUs on demand with no cluster to manage, and it scales to zero when the job ends.

*Capsules: Distributed training & GPU, AI Runtime — serverless GPU*

*The team now has trained models. A model is only useful once applications can call it. Many new use cases also start from large language models that someone else trained. How do you serve and control any model, your own or a provider's?*

## 4. Model access and governance

Serving those models is the next step. Without one way to do it, every model and every provider brings its own system, keys and costs. Model Serving puts every model behind the same kind of endpoint, Foundation Model APIs reach the main providers through one API, fine-tuning adapts open models to the company's needs, and external models go through the same control. Every model is now served the same way, and many uses need one that can also look up company data and call tools. How do you build agents?

### Model serving

Putting a model into production no longer needs its own infrastructure.

Each kind of model needs its own serving system, provisioned by hand, with access control split across them. Idle machines keep costing money.

Model Serving replaces these systems with one serverless service.

- Model Serving handles both cases with one kind of endpoint.
- Custom models, foundation models and external models are served behind serverless endpoints with the same API.
- Endpoints scale with demand, down to zero.
- They can be billed per token, with provisioned throughput, or in batch.
- Features from the Feature Store are looked up at serving time.

*Capsules: Model Serving*

### Foundation models and their lifecycle

Teams can use the best model for each task, from any of the main providers.

*For large language models, teams need to know which models are available behind those endpoints.*

Depending on one provider creates lock-in, token spend grows unpredictably, and models from different providers are tested piece by piece.

Foundation Model APIs remove the dependency on any single provider.

- Foundation Model APIs give access through one API to models from providers that include Anthropic, OpenAI, Google and Meta.
- They are billed per token or with reserved capacity.
- The catalog changes often.
- New versions arrive and older ones are retired.
- Databricks publishes the supported models and their retirement dates.
- Because applications call the same API for every model, moving to a newer model stays a small change.

*Capsules: Foundation Model APIs, Model versions, Model lifecycle churn*

### Model fine-tuning

Adapting a model to company data takes less GPU memory and is paid by the minute.

*Sometimes a general model does not know the company's vocabulary or tasks well enough.*

Full fine-tuning needs large amounts of GPU memory and is expensive and slow. Once tuned, the model often sits apart from the systems that serve the others.

Model fine-tuning makes this adaptation lighter and keeps it on the platform.

- Fine-tuning adapts an open model to company data with LoRA, QLoRA or full fine-tuning, on serverless GPUs.
- The tuned model is logged in MLflow and served like any other model.

*Capsules: Model fine-tuning*

### External models

Calls to outside models are tracked and audited like every other model call.

*Some teams also call models that are hosted directly at a provider.*

API keys end up scattered across code and team members, and these calls bypass security, with no view of what they cost.

External model services bring these calls under the same control.

- These models are registered as external models, with their keys stored centrally, so their calls go through the same Model Serving endpoints as every other model.

*Capsules: External model services*

*Every model, hosted on Databricks or at a provider, is now served the same way. Many use cases need a model that can also look up company data and call tools. How do you build agents?*

## 5. Building agents

An agent starts from the company's own data. It has to find the right information, use tools, remember what it learned and run code without putting data at risk. AI Functions bring models to the data in SQL, AI Search and Knowledge Assistant find the right documents, MCP connects tools under Unity Catalog, custom agents get managed memory and Databricks Sandbox, and the Supervisor Agent shares out large tasks. The agent can now use company data and tools, and before it reaches users, it has to be trusted. How do you know it is right?

### Batch AI in SQL and pipelines

Teams apply AI to large volumes of data and documents without moving them out of the platform.

Running a model over company data usually means sending the data to an outside service, building separate pipelines for documents and splitting the work into batches by hand. What comes back is unstructured.

AI Functions do this work where the data already is.

- AI Functions call a model from SQL or from a pipeline to classify, extract or summarize data and documents at scale.
- The first step needs no agent.
- The results come back with a fixed schema, and the data stays in Unity Catalog.

*Capsules: AI Functions*

### Retrieval and document question answering

Agents answer from the company's own documents, with sources that can be checked.

*An agent answers questions as they come. To answer well, it first has to find the right information.*

Search indexes are built and kept in sync by hand, and generic retrieval misses what a document means. Answers then cite sources that are missing or false.

AI Search and Knowledge Assistant ground the answers in the right documents.

- AI Search indexes documents and tables for vector and keyword search, keeps the index in sync with the Delta tables, and returns citations.
- Knowledge Assistant packaged this into a question-answering agent over documents that could be set up in minutes.
- It is now moving into Genie Agents.

*Capsules: AI Search, Knowledge Assistant*

### Tool access through MCP

Agents reach the company's tools through one governed route instead of one-off connections.

*Answering from documents only reads data. Many tasks also need actions, such as running a query, opening a ticket or changing code. Each of these tools needs a connection and permissions.*

Teams write a custom connector for each tool and host the servers themselves, credentials pile up across agents, and tool use stays hidden.

Managed MCP servers and MCP Services turn each tool into a governed connection.

- The Model Context Protocol (MCP) is the standard way for an agent to call tools.
- Databricks runs managed MCP servers for its own services, such as Genie, AI Search and SQL.
- Connectors give governed access to Google Workspace, Microsoft 365, Slack and GitHub.
- Teams can register their own MCP servers or host them as Databricks Apps.
- Every tool is a Unity Catalog object, so permissions and audit work the same way as for data.

*Capsules: Managed MCP servers, External connectors, MCP Services + custom MCP*

### Custom agents, memory and sandbox

Developers build the agent they need, and it remembers its users and runs its code safely.

*An agent combines retrieval and tools with its own logic.*

Agent platforms often impose the framework and the model, and leave sessions and memory to be handled by hand. Users repeat their instructions in each conversation, and the code an agent writes is untrusted.

Custom agents, managed memory and Databricks Sandbox take these limits away.

- Custom agents are written in code with frameworks such as LangGraph, LangChain or the OpenAI SDK.
- They can use any model on Model Serving and any MCP tool.
- Managed memory, stored in Lakebase, lets an agent remember context across conversations.
- Databricks Sandbox runs the code an agent writes in an isolated environment, with scoped access to data.

*Capsules: Custom Agents, Managed memory & sessions, Databricks Sandbox*

### Multi-agent orchestration

Large tasks are shared across specialized agents and come back as one answer.

*Some tasks are too large for one agent.*

Routing work between agents by hand gives disconnected answers, and a chain of agents can bypass a user's data permissions.

The Supervisor Agent takes over the routing.

- A supervisor agent splits a task across several agents and keeps each user's data permissions.
- It is moving into Genie Agents as well.

*Capsules: Supervisor Agent*

*The agent can now use company data and tools, and keep memory across conversations. Before it reaches users, it has to be trusted. How do you know it is right?*

## 6. Evaluating agents

Knowing that an agent is right starts with seeing what it does. Without that, a wrong answer cannot be traced, quality is a matter of opinion, and a prompt change can go unnoticed. MLflow 3 traces every request step by step, agent evaluation scores the answers of each version, the Prompt Registry versions the prompts, and Review Apps bring the experts' judgment in. Quality is now measured before each release, and data, models, agents and tools also need rules for who may use what. How is all of it governed?

### Tracing

Operators see inside every agent request, step by step, including what it costs.

Agent chains are opaque to the people who run them. When an answer is wrong, the failing step is hard to isolate, and the cost of each request is unknown.

MLflow 3 makes each request visible.

- MLflow traces every request through the agent.
- It records each model call, tool call and retrieval step, with inputs, outputs, latency and tokens, and it works with more than 30 agent frameworks.
- When an answer is wrong, the trace shows the step where it went wrong.

*Capsules: MLflow 3 for GenAI*

### Evaluation and prompt versioning

Teams know whether a new agent version is better before it ships.

*A trace shows one request. Judging quality needs a score across many requests.*

Without quality metrics, traces are reviewed by hand and versions cannot be compared. Prompts change without a record, and staging and production drift apart.

Agent evaluation scores the answers, and the Prompt Registry versions the prompts.

- Agent evaluation applies LLM judges and custom scorers to traces.
- It runs in batch before a release and continuously on live traffic.
- Each agent version gets its own evaluation run, so versions can be compared.
- Prompts are versioned in the Prompt Registry with staging and production aliases, so a prompt change is tracked like a code change.

*Capsules: Agent evaluation & monitoring, MLflow Prompt Registry*

### Expert review and labeling

What domain experts know becomes the standard the agent is judged against.

*An LLM judge is only useful if its scores match what experts would say.*

Without ground truth, agent quality is a matter of opinion. Experts label answers in spreadsheets that are not linked to the traces, and their criteria drift from one session to the next.

Review Apps connect the experts to the agent.

- Review Apps let domain experts test the agent in a chat interface and label its answers.
- The labels attach to the traces and become evaluation datasets.
- They are also used to align the judges with the experts.

*Capsules: Review Apps*

*The agent's answers can now be measured and reviewed. Data, models, agents and tools also need one set of rules for who may use what, and for what can go wrong. How is all of it governed?*

## 7. Governance

Governance has to cover all of it at once. Models, agents and tools often sit outside the rules that govern data, calls to models go unchecked, and the risks of AI are not mapped. Unity Catalog governs them the same way as tables, Unity Gateway controls and logs every model and tool call, and the Databricks AI Security Framework links each risk to the control that covers it. Data, models, agents and tools are now governed with one set of rules, but most of the people who need them do not write code. How do business users get to them?

### Unity Catalog for AI assets

Each model, agent and tool can be traced to the data behind it and to everyone who used it.

Models, agents and functions are not governed as assets of their own, permissions are enforced differently across them, and external credentials are scattered. Nobody knows which data feeds which model.

Unity Catalog extends to these assets.

- Unity Catalog governs models, agents, tools and credentials in the same way as tables and files.
- Each of them is a Unity Catalog object with permissions, lineage and an audit trail.
- Lineage follows the chain from data to model to agent.
- Credentials for external services are stored in the catalog and encrypted.

*Capsules: Unity Catalog for AI assets*

### Control of AI traffic with Unity Gateway

Every model and tool call is controlled and logged in one place.

*The catalog sets who may use each asset. Each model call and each tool call also needs control at the moment it happens.*

Each team connects to model providers on its own, so nobody sees who calls which model or what it costs. Prompts and responses go through without guardrails, and nothing is logged for an audit.

Unity Gateway puts this traffic under one control plane.

- Unity Gateway sits in front of all model and tool traffic and is built on Unity Catalog.
- It sets who may call which model and tracks usage per user and team.
- Budgets cap spend.
- Guardrails apply to every prompt and response, and every request is logged for audit.

*Capsules: Unity Gateway*

### AI security risks and controls

*Permissions and guardrails address known risks. A security team also needs the full list of risks and the control that covers each one.*

- The Databricks AI Security Framework lists the risks of AI systems and the controls that address them.
- Version 3.0 covers 97 risks and 73 controls, including 35 risks specific to agents.
- The controls include least-privilege tool access in Unity Catalog, sandboxed code execution, guardrails in Unity Gateway, and human review.

*Capsules: DASF v3.0*

*Data, models, agents and tools are now governed with one set of rules. Most of the people who need them do not write code. How do business users get to them?*

## 8. AI for business users

Business users depend on analysts for every question, and the same metric can mean different things from one report to the next. Genie One lets them ask in plain language and answers with their own permissions, and Genie Ontology makes each answer use the certified definition. Genie Agents, AI/BI Dashboards, Row Zero and Genie App Builder carry the same help into assistants, dashboards, spreadsheets and small apps. No-code now covers the common needs, and developers build the rest. What do builders get?

### Natural-language questions on company data

Business users get answers from company data without writing SQL.

Most people who need data do not write SQL. Their questions queue up at the data team, and the answer often comes after the decision.

Genie One gives them a front door to the data.

- Genie One lets business users ask questions in plain language.
- They get answers from governed company data, with citations and with their own permissions applied.
- When a dashboard or an agent already answers the question, Genie One sends the user there.

*Capsules: Genie One*

### Shared business definitions

Every answer uses the company's certified definition of each metric.

*An answer is only trusted if "revenue" or "active customer" means the same thing as in the official reports.*

Metrics are defined differently across dashboards, queries and teams, and business context is scattered across documents, chats and tickets. An AI can then pick an obsolete or draft definition.

Genie Ontology is the layer that grounds Genie in these definitions.

- Genie Ontology holds those definitions.
- Each KPI is defined once, as a metric view in Unity Catalog.
- The ontology also learns business context from existing dashboards, queries and pipelines.
- It ranks sources by certification, usage and freshness, so Genie answers from certified definitions first.

*Capsules: Genie Ontology*

### No-code assistants built by domain experts

The knowledge of each business area becomes available to everyone in it.

*Once the definitions are shared, domain experts can package what they know for others.*

Business knowledge stays with a few experts, and dashboards only answer the questions they were built for. Deeper analysis is spread across separate tools.

Genie Agents turn that expertise into a shared assistant.

- Genie Agents let a domain expert build a no-code assistant for a business area.
- The assistant can follow up on questions, run multi-step analyses and explain its reasoning, and it can be embedded in other applications.
- Knowledge Assistant and the supervisor agent are moving into Genie Agents.

*Capsules: Genie Agents*

### AI-assisted dashboards and spreadsheets

Analysts and business users go from a question to a governed dashboard on their own.

*Many users still work in dashboards and spreadsheets.*

Building a dashboard takes SQL and specialist skills, so requests wait. Meanwhile, analysis done in spreadsheets is cut off from the governed data and unaudited.

AI/BI Dashboards and Row Zero bring the assistant into both.

- An AI/BI dashboard can be built from a plain-language request.
- The assistant finds the tables, writes the queries and picks the charts, and the author approves each step.
- Row Zero, announced, brings the same governed data into a spreadsheet, with Genie writing the queries behind the formulas.

*Capsules: AI/BI Dashboards, Row Zero / Genie ZeroOps*

### No-code app generation

Business teams turn an idea into a working app in minutes.

*When the same question comes back every week, it is worth turning into a small application.*

Building an app takes software engineering skills, and every change needs a developer and a new deployment.

Genie App Builder lets the team describe the app instead.

- Genie App Builder generates a Databricks App from a plain-language description, within the limits the admins set.

*Capsules: Genie App Builder*

*No-code covers the common needs. Developers build the rest, such as custom applications, agents and pipelines. What do builders get?*

## 9. Developer tools

Developers build the rest on the same platform. Each application usually needs its own infrastructure, identity and secrets, and much of the code is repetitive. Databricks Apps hosts applications next to the governed data, App Spaces governs who deploys and uses them, Genie Code writes and explains code in every tool, and the AI Dev Kit and Omnigent give agent development a common base. Databricks builds with these same components, up to complete applications for specific business domains. What comes ready-made?

### Application hosting

Data and AI applications run on the platform itself, next to the governed data.

A data or AI application usually runs on separate infrastructure, with its own identity management and secrets. It sits apart from the governed data, and access control and audit trails are hard to put in place.

Databricks Apps brings these applications onto the platform.

- Developers build applications with the frameworks they already use, such as Streamlit, Gradio, React or FastAPI, and deploy them as Databricks Apps.
- The apps run serverless on the platform.
- They sign users in with the platform's identity and read data through Unity Catalog with each user's permissions.
- Custom MCP servers run the same way.
- App Spaces give admins one place to govern who deploys and uses which app.

*Capsules: Databricks Apps + App Spaces*

### Coding assistant

Developers write less repetitive code, with the same assistant in every tool.

*Hosting is now handled. Writing the code still takes most of the time.*

Much of that code is repetitive boilerplate, developers switch between separate tools for notebooks, SQL, pipelines and dashboards, and tuning SQL is hard for non-experts.

Genie Code takes on that work.

- Genie Code is the AI assistant inside notebooks, the SQL editor, pipelines and dashboards.
- It writes and explains code from plain-language requests.
- A command-line version, in beta, brings it into the terminal and into CI pipelines.

*Capsules: Genie Code*

### Agent development kit and coding-agent harnesses

Teams build agents on a ready structure, with their tools governed and audited.

*Custom agents are code as well, and they need a project structure.*

Developers scaffold each agent and its tool connections by hand, and the integrations they create are not audited. Each coding-agent tool is its own isolated world, so content is copied between them by hand.

The AI Dev Kit and Omnigent give this work a common base.

- The AI Dev Kit gives developers templates and scaffolding for agents, and a set of tools governed in Unity Catalog.
- Databricks uses the same kit for its own internal coding agents.
- Developers who already work with coding agents such as Claude, Codex or Cursor can put them behind one interface with Omnigent, with shared context and central policies.

*Capsules: AI Dev Kit + internal coding agents, Omnigent*

*Databricks uses the same platform components to build complete applications for specific business domains. What comes ready-made?*

## 10. Domain applications

Some of these applications come ready-made. Customer data and security logs each sit in their own silo, with duplicate records, separate tools and logs deleted to save cost. CustomerLake builds one governed profile per customer and lets agents run the campaigns, and Lakewatch keeps the logs on the lakehouse and investigates alerts with agents. Whether the organization builds its applications or uses ready-made ones, every model and agent then runs in production for years. How do you run it?

### Customer data application

Campaigns and personalization run on governed customer profiles that stay current.

Each system holds its own part of the customer, often duplicated and without lineage, and audiences are built and activated by hand.

CustomerLake gives the platform a ready-made answer for customer data.

- CustomerLake, in private preview, builds customer 360 profiles on the lakehouse.
- It joins transactions, behavior and engagement into one profile per customer.
- AI-assisted identity resolution merges duplicate records.
- Campaign agents create and activate audiences, and a real-time profile API feeds personalization.

*Capsules: CustomerLake*

### Security operations application

Security teams keep all their logs and investigate faster.

*CustomerLake applies the platform to customer data. The same pattern applies to security data.*

Security telemetry is split across separate tools, threat hunting and triage are manual, and detection rules are hard to version and test.

Lakewatch adds agents to security operations.

- Lakewatch, in private preview, runs security operations on the lakehouse.
- It keeps security, IT and business logs in one place at object-storage cost, so they no longer have to be deleted early.
- Autonomous agents investigate alerts and help write detection rules, which are versioned and tested like code.

*Capsules: Lakewatch*

*Both applications are built from the same parts: data on the lakehouse, governance in Unity Catalog, and agents. Whether a company builds its own applications or uses ready-made ones, every model and agent then runs in production for years. How do you run it?*

## 11. Production operations

Running it means keeping track of every version. Models drift as their inputs change, and each fix has to reach production the same way every time. The Model Registry in Unity Catalog records each version and its lineage, Model Serving runs the registered version at scale, Lakehouse Monitoring detects drift and raises alerts, and MLOps Stacks and bundles carry each change from development to production. Each model and agent now runs, is watched and is updated in production for as long as it is used.

### Model registry

Teams always know which model version is in production and where it came from.

Model versions go untracked, promotions are manual and error-prone, and the link between a model and its training data gets lost. Without a shared view across workspaces, teams rebuild models that already exist.

The Model Registry in Unity Catalog keeps this history and governs every model.

- Every model in production is registered in Unity Catalog with its versions, its aliases such as champion and challenger, and its lineage back to the training data.
- Promoting a new version means moving an alias, and model update triggers or deployment jobs can start the next steps automatically.

*Capsules: MLflow Model Registry, Model Registry & governance*

### Production serving

Production traffic can grow without anyone resizing the infrastructure.

*A registered version then has to serve traffic.*

Models end up spread across several serving platforms, scaled by hand, with no central view of what is deployed.

Model Serving runs them all from one place.

- Model Serving endpoints run the registered version, for real-time requests and for batch scoring.
- They handle more than 25,000 queries per second with low added latency, and they scale with demand.

*Capsules: Model Serving & batch inference*

### Monitoring and drift detection

*Once a model is serving, its inputs change over time and its quality can drift.*

- Inference tables log every request and response.
- Lakehouse Monitoring profiles those tables, detects drift in data and in predictions, and raises alerts.
- The same monitoring covers data quality and agents.

*Capsules: Monitoring & evaluation*

### MLOps and CI/CD

*When monitoring shows a problem, the fix has to reach production safely, and the same way every time.*

- MLOps Stacks and Declarative Automation Bundles describe code, jobs, models and their environments as files in Git.
- Lakeflow Jobs run the pipelines.
- Each change goes from development to production through that automated path.

*Capsules: MLOps & CI/CD*

## Closing

Every part of the starting situation now has its answer. The data foundation stores the scattered data once and governs it, the data science lifecycle makes model work reproducible, and model access puts every provider behind one way of serving. Building agents gives them safe access to data and tools, evaluation measures their answers, and governance sets who may use what. Business users and developers get tools of their own, domain applications break the customer and security silos, and production operations keep every model under control. AI no longer stops at the pilot.
