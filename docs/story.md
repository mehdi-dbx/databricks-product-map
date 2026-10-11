# The Databricks data and AI story

## 1. Challenges

### Data spread across systems

- Most companies already run analytics and have started with AI.
- Their data sits in several places: operational databases behind the applications, a warehouse for reporting, a data lake for raw files, and SaaS tools.
- Each system keeps its own copies and its own access rules.
- Pipelines move data between them to keep the copies in sync.
- People who need an answer wait for the few colleagues who can query these systems.

### AI pilots blocked before production

*AI needs that data. When the data is spread out, every AI project first has to collect it.*

- So AI projects start as pilots on extracts.
- A pilot can work on its extract.
- Going to production means reaching live data, proving the answers are right, and controlling who uses which model and at what cost.
- Many pilots stop at that step.

*The work starts with the data. How do you get it into one place, governed once and fresh enough for AI?*

## 2. Data and AI foundation

### Open table storage with Delta Lake

- Databricks stores the data once, in open Delta tables in your cloud storage.
- Delta adds transactions to those files.
- Batch jobs and streaming jobs write to the same tables without corrupting them, and the schema can change without breaking readers.

*Capsules: Lakehouse / Delta Lake*

### Ingestion, transformation and table maintenance

*A storage layer is only useful once the data gets into it and stays usable.*

- Lakeflow brings the data in and transforms it.
- Lakeflow Connect provides managed connectors to databases and SaaS applications.
- Declarative pipelines describe the transformations, and Lakeflow works out the order in which to run them.
- Predictive Optimization then maintains the tables on its own, so nobody has to schedule maintenance jobs.

*Capsules: Lakeflow, Predictive Optimization*

### Transactional data on the same platform

*The analytical data is now in place. Applications and agents also read and write transactional data, and that data usually lives in a separate database with its own copy.*

- Lakebase is a serverless Postgres database inside the platform.
- It holds application data and agent state, and its tables sync with Unity Catalog.
- Lakebase Search adds vector and keyword search in the same Postgres database, with no separate vector store.

*Capsules: Lakebase, Lakebase Search*

### Real-time analytics on operational data

*Transactional and analytical data now sit on the same platform. The remaining copy is the one that feeds analytics with fresh operational data.*

- Lakehouse//RT answers SQL queries in under 100 milliseconds directly on lakehouse tables, so dashboards and applications no longer need a separate serving copy.
- LTAP, which is announced, keeps one dataset that is written in Lakebase and read in Lakehouse//RT, with no replication pipeline between them.

*Capsules: Lakehouse//RT, LTAP*

### Data catalog and data quality

*Everything is now in one place. That helps only if access, lineage and quality are handled once for all of it.*

- Unity Catalog applies one set of permissions, lineage and audit to tables and files.
- Data quality is watched in the same place.
- Classification tags sensitive data such as PII.
- Profiling and monitoring track quality.
- Anomaly detection flags stale or broken tables and can trigger a repair job.

*Capsules: Classification / profiling / monitoring, Anomaly detection & remediation*

*The data is in one place, fresh and governed. The first thing teams do with data like this is learn from it. How does a data science team work on it?*

## 3. Data science lifecycle

### Notebooks and data exploration

- Data scientists work in notebooks that run Python, SQL, R and Scala directly on the governed tables.
- Several people can edit the same notebook at once, and notebooks are versioned in Git.
- Exploration uses the tools the team already knows: pandas, Spark, SQL and built-in data profiles.

*Capsules: Notebooks & collaboration, Data prep & EDA, DS languages & frameworks*

### Feature Store

*Exploration ends in features, the inputs a model learns from. A feature computed one way for training and another way in production gives wrong predictions.*

- The Feature Store keeps each feature definition in one place, governed by Unity Catalog.
- Training sets are built with point-in-time correct joins, and the same definitions feed predictions in production.
- For real-time use, features are served from an online store on Lakebase.

*Capsules: Feature Store*

### Experiment tracking and AutoML

*With features in place, the team trains many models and compares them. Comparing them requires that every result can be reproduced.*

- MLflow records every training run with its parameters, metrics, code version and artifacts, so any result can be reproduced and compared.
- AutoML gives a first baseline.
- It tries algorithms such as XGBoost and LightGBM, tunes them, and writes each trial as a notebook the team can read and change.

*Capsules: MLflow, AutoML*

### Distributed training and GPUs

*Some datasets and models do not fit on one machine.*

- Training then spreads across GPUs and clusters with managed libraries such as TorchDistributor, DeepSpeed and Ray.
- AI Runtime provides GPUs on demand with no cluster to manage, and it scales to zero when the job ends.

*Capsules: Distributed training & GPU, AI Runtime — serverless GPU*

*The team now has trained models. A model is only useful once applications can call it. Many new use cases also start from large language models that someone else trained. How do you serve and control any model, your own or a provider's?*

## 4. Model access and governance

### Model serving

- Model Serving handles both cases with one kind of endpoint.
- Custom models, foundation models and external models are served behind serverless endpoints with the same API.
- Endpoints scale with demand, down to zero.
- They can be billed per token, with provisioned throughput, or in batch.
- Features from the Feature Store are looked up at serving time.

*Capsules: Model Serving*

### Foundation models and their lifecycle

*For large language models, teams need to know which models are available behind those endpoints.*

- Foundation Model APIs give access through one API to models from providers that include Anthropic, OpenAI, Google and Meta.
- They are billed per token or with reserved capacity.
- The catalog changes often.
- New versions arrive and older ones are retired.
- Databricks publishes the supported models and their retirement dates.
- Because applications call the same API for every model, moving to a newer model stays a small change.

*Capsules: Foundation Model APIs, Model versions, Model lifecycle churn*

### Model fine-tuning

*Sometimes a general model does not know the company's vocabulary or tasks well enough.*

- Fine-tuning adapts an open model to company data with LoRA, QLoRA or full fine-tuning, on serverless GPUs.
- The tuned model is logged in MLflow and served like any other model.

*Capsules: Model fine-tuning*

### External models

*Some teams also call models that are hosted directly at a provider.*

- These models are registered as external models, with their keys stored centrally, so their calls go through the same Model Serving endpoints as every other model.

*Capsules: External model services*

*Every model, hosted on Databricks or at a provider, is now served the same way. Many use cases need a model that can also look up company data and call tools. How do you build agents?*

## 5. Building agents

### Batch AI in SQL and pipelines

- AI Functions call a model from SQL or from a pipeline to classify, extract or summarize data and documents at scale.
- The first step needs no agent.
- The results come back with a fixed schema, and the data stays in Unity Catalog.

*Capsules: AI Functions*

### Retrieval and document question answering

*An agent answers questions as they come. To answer well, it first has to find the right information.*

- AI Search indexes documents and tables for vector and keyword search, keeps the index in sync with the Delta tables, and returns citations.
- Knowledge Assistant packaged this into a question-answering agent over documents that could be set up in minutes.
- It is now moving into Genie Agents.

*Capsules: AI Search, Knowledge Assistant*

### Tool access through MCP

*Answering from documents only reads data. Many tasks also need actions, such as running a query, opening a ticket or changing code. Each of these tools needs a connection and permissions.*

- The Model Context Protocol (MCP) is the standard way for an agent to call tools.
- Databricks runs managed MCP servers for its own services, such as Genie, AI Search and SQL.
- Connectors give governed access to Google Workspace, Microsoft 365, Slack and GitHub.
- Teams can register their own MCP servers or host them as Databricks Apps.
- Every tool is a Unity Catalog object, so permissions and audit work the same way as for data.

*Capsules: Managed MCP servers, External connectors, MCP Services + custom MCP*

### Custom agents, memory and sandbox

*An agent combines retrieval and tools with its own logic.*

- Custom agents are written in code with frameworks such as LangGraph, LangChain or the OpenAI SDK.
- They can use any model on Model Serving and any MCP tool.
- Managed memory, stored in Lakebase, lets an agent remember context across conversations.
- Databricks Sandbox runs the code an agent writes in an isolated environment, with scoped access to data.

*Capsules: Custom Agents, Managed memory & sessions, Databricks Sandbox*

### Multi-agent orchestration

*Some tasks are too large for one agent.*

- A supervisor agent splits a task across several agents and keeps each user's data permissions.
- It is moving into Genie Agents as well.

*Capsules: Supervisor Agent*

*The agent can now use company data and tools, and keep memory across conversations. Before it reaches users, it has to be trusted. How do you know it is right?*

## 6. Evaluating agents

### Tracing

- MLflow traces every request through the agent.
- It records each model call, tool call and retrieval step, with inputs, outputs, latency and tokens, and it works with more than 30 agent frameworks.
- When an answer is wrong, the trace shows the step where it went wrong.

*Capsules: MLflow 3 for GenAI*

### Evaluation and prompt versioning

*A trace shows one request. Judging quality needs a score across many requests.*

- Agent evaluation applies LLM judges and custom scorers to traces.
- It runs in batch before a release and continuously on live traffic.
- Each agent version gets its own evaluation run, so versions can be compared.
- Prompts are versioned in the Prompt Registry with staging and production aliases, so a prompt change is tracked like a code change.

*Capsules: Agent evaluation & monitoring, MLflow Prompt Registry*

### Expert review and labeling

*An LLM judge is only useful if its scores match what experts would say.*

- Review Apps let domain experts test the agent in a chat interface and label its answers.
- The labels attach to the traces and become evaluation datasets.
- They are also used to align the judges with the experts.

*Capsules: Review Apps*

*The agent's answers can now be measured and reviewed. Data, models, agents and tools also need one set of rules for who may use what, and for what can go wrong. How is all of it governed?*

## 7. Governance

### Unity Catalog for AI assets

- Unity Catalog governs models, agents, tools and credentials in the same way as tables and files.
- Each of them is a Unity Catalog object with permissions, lineage and an audit trail.
- Lineage follows the chain from data to model to agent.
- Credentials for external services are stored in the catalog and encrypted.

*Capsules: Unity Catalog for AI assets*

### Control of AI traffic with Unity Gateway

*The catalog sets who may use each asset. Each model call and each tool call also needs control at the moment it happens.*

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

### Natural-language questions on company data

- Genie One lets business users ask questions in plain language.
- They get answers from governed company data, with citations and with their own permissions applied.
- When a dashboard or an agent already answers the question, Genie One sends the user there.

*Capsules: Genie One*

### Shared business definitions

*An answer is only trusted if "revenue" or "active customer" means the same thing as in the official reports.*

- Genie Ontology holds those definitions.
- Each KPI is defined once, as a metric view in Unity Catalog.
- The ontology also learns business context from existing dashboards, queries and pipelines.
- It ranks sources by certification, usage and freshness, so Genie answers from certified definitions first.

*Capsules: Genie Ontology*

### No-code assistants built by domain experts

*Once the definitions are shared, domain experts can package what they know for others.*

- Genie Agents let a domain expert build a no-code assistant for a business area.
- The assistant can follow up on questions, run multi-step analyses and explain its reasoning, and it can be embedded in other applications.
- Knowledge Assistant and the supervisor agent are moving into Genie Agents.

*Capsules: Genie Agents*

### AI-assisted dashboards and spreadsheets

*Many users still work in dashboards and spreadsheets.*

- An AI/BI dashboard can be built from a plain-language request.
- The assistant finds the tables, writes the queries and picks the charts, and the author approves each step.
- Row Zero, announced, brings the same governed data into a spreadsheet, with Genie writing the queries behind the formulas.

*Capsules: AI/BI Dashboards, Row Zero / Genie ZeroOps*

### No-code app generation

*When the same question comes back every week, it is worth turning into a small application.*

- Genie App Builder generates a Databricks App from a plain-language description, within the limits the admins set.

*Capsules: Genie App Builder*

*No-code covers the common needs. Developers build the rest, such as custom applications, agents and pipelines. What do builders get?*

## 9. Developer tools

### Application hosting

- Developers build applications with the frameworks they already use, such as Streamlit, Gradio, React or FastAPI, and deploy them as Databricks Apps.
- The apps run serverless on the platform.
- They sign users in with the platform's identity and read data through Unity Catalog with each user's permissions.
- Custom MCP servers run the same way.
- App Spaces give admins one place to govern who deploys and uses which app.

*Capsules: Databricks Apps + App Spaces*

### Coding assistant

*Hosting is now handled. Writing the code still takes most of the time.*

- Genie Code is the AI assistant inside notebooks, the SQL editor, pipelines and dashboards.
- It writes and explains code from plain-language requests.
- A command-line version, in beta, brings it into the terminal and into CI pipelines.

*Capsules: Genie Code*

### Agent development kit and coding-agent harnesses

*Custom agents are code as well, and they need a project structure.*

- The AI Dev Kit gives developers templates and scaffolding for agents, and a set of tools governed in Unity Catalog.
- Databricks uses the same kit for its own internal coding agents.
- Developers who already work with coding agents such as Claude, Codex or Cursor can put them behind one interface with Omnigent, with shared context and central policies.

*Capsules: AI Dev Kit + internal coding agents, Omnigent*

*Databricks uses the same platform components to build complete applications for specific business domains. What comes ready-made?*

## 10. Domain applications

### Customer data application

- CustomerLake, in private preview, builds customer 360 profiles on the lakehouse.
- It joins transactions, behavior and engagement into one profile per customer.
- AI-assisted identity resolution merges duplicate records.
- Campaign agents create and activate audiences, and a real-time profile API feeds personalization.

*Capsules: CustomerLake*

### Security operations application

*CustomerLake applies the platform to customer data. The same pattern applies to security data.*

- Lakewatch, in private preview, runs security operations on the lakehouse.
- It keeps security, IT and business logs in one place at object-storage cost, so they no longer have to be deleted early.
- Autonomous agents investigate alerts and help write detection rules, which are versioned and tested like code.

*Capsules: Lakewatch*

*Both applications are built from the same parts: data on the lakehouse, governance in Unity Catalog, and agents. Whether a company builds its own applications or uses ready-made ones, every model and agent then runs in production for years. How do you run it?*

## 11. Production operations

### Model registry

- Every model in production is registered in Unity Catalog with its versions, its aliases such as champion and challenger, and its lineage back to the training data.
- Promoting a new version means moving an alias, and model update triggers or deployment jobs can start the next steps automatically.

*Capsules: MLflow Model Registry, Model Registry & governance*

### Production serving

*A registered version then has to serve traffic.*

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
