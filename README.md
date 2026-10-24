# Sanskar Chandawar

## Data engineering systems, with an applied AI edge

I build data pipelines and software that turn messy inputs into reliable, usable
systems. My primary focus is **data engineering**: PySpark, Databricks, Delta
Lake, SQL, data quality, and lakehouse architecture. I also build AI/LLM
applications where retrieval, validation, and deterministic fallbacks matter.

[GitHub](https://github.com/Sanskar1724) ·
[LinkedIn](https://www.linkedin.com/in/sanskar-chandawar) ·
[Portfolio](https://forgeaistudio.vercel.app) ·
[Email](mailto:sanskarchandawar3@gmail.com)

---

## What I build

### [Retail Lakehouse with Databricks](https://github.com/Sanskar1724/Retail-Lakehouse-with-Databricks)

A governed retail data platform that moves source data through a Bronze–Silver–Gold
medallion architecture into analytics-ready datasets. Bronze preserves raw
records and traceability; Silver applies cleansing, deduplication, type
standardization, and business validation; Gold produces dimensional models,
aggregates, and KPI tables for Power BI. The repository also documents
metadata-driven ingestion, Databricks Jobs orchestration, Delta Lake guarantees,
and Unity Catalog governance.

`PySpark` `Databricks` `Delta Lake` `Unity Catalog` `Databricks SQL` `Power BI`

### [DataPilot](https://github.com/Sanskar1724/DataPilot)

An AI-assisted data quality pipeline for turning dirty CSV, JSON, JSONL, Excel,
and Parquet files into cleaned datasets and auditable reports. Deterministic
profiling and quality detectors inspect the data first; an LLM sees only schema,
statistics, and issue summaries, then returns a Pydantic-validated fix plan.
Execution is limited to a registered set of safe transformations, keeping data
processing reproducible and separate from model reasoning.

`Python` `pandas` `DuckDB` `Pydantic` `Streamlit` `OpenRouter` `pytest`

### [CampusOps](https://github.com/Sanskar1724/CampusOps)

An academic operations assistant that consolidates college email, timetables,
documents, deadlines, and reminders into a single conversational interface.
Its Core Agent retrieves only the facts needed for each question, composes
responses for the web, Telegram, and email channels, and falls back to a
deterministic facts composer when the model is unavailable. The system includes
hybrid document search, vision OCR, scheduled notifications, and a
Postgres/pgvector deployment path.

`Python` `FastAPI` `Next.js` `TypeScript` `PostgreSQL` `pgvector` `Docker`

### [FinSight AI](https://github.com/Sanskar1724/FinSight_AI)

A full-stack personal finance workspace built around a transaction ledger,
budgets, goals, analytics, scenarios, reminders, and a grounded assistant.
The FastAPI backend owns financial calculations and user-scoped data access,
while the React client consumes a single API; the optional AI layer receives
calculated context and evidence rather than inventing authoritative totals.
The repository includes architecture, API, deployment, and research notes.

`React` `TypeScript` `FastAPI` `SQLAlchemy` `SQLite` `PostgreSQL` `Pydantic`

---

## Technical writing

Selected project documentation:

- [DataPilot architecture](https://github.com/Sanskar1724/DataPilot/blob/main/docs/architecture.md)
  — metadata-only AI analysis, validation boundaries, and deterministic execution.
- [CampusOps agent design](https://github.com/Sanskar1724/CampusOps/blob/master/docs/AGENT.md)
  — retrieval, composition, history, and resilient fallback behavior.
- [FinSight architecture](https://github.com/Sanskar1724/FinSight_AI/blob/main/docs/ARCHITECTURE.md)
  — frontend/backend boundaries, authentication, financial invariants, and grounded AI.
- [FinSight research methodology](https://github.com/Sanskar1724/FinSight_AI/blob/main/docs/RESEARCH.md)
  — reproducible baseline-versus-grounded evaluation.

---

## Technical skills

**Data engineering** — PySpark, Apache Spark, Databricks, Delta Lake, Unity
Catalog, SQL, data quality, dimensional modeling, Power BI

**Programming and backend** — Python, FastAPI, SQLAlchemy, Pydantic, REST APIs,
TypeScript, React, Next.js

**AI and systems** — RAG, OpenRouter, hybrid search, prompt design, Docker,
GitHub Actions, PostgreSQL, SQLite

---

## Contact

For data platforms, backend systems, or practical AI applications:

[sanskarchandawar3@gmail.com](mailto:sanskarchandawar3@gmail.com) ·
[LinkedIn](https://www.linkedin.com/in/sanskar-chandawar) ·
[forgeaistudio.vercel.app](https://forgeaistudio.vercel.app)
