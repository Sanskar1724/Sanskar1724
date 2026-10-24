<div align="center">

<img src="assets/hero.svg" width="100%" alt="Sanskar Chandawar - Data Engineer"/>

<p>
  <a href="https://github.com/Sanskar1724"><img src="https://img.shields.io/badge/GitHub-0b1424?style=for-the-badge&logo=github&logoColor=38bdf8" alt="GitHub"/></a>
  <a href="https://www.linkedin.com/in/sanskar-chandawar"><img src="https://img.shields.io/badge/LinkedIn-0b1424?style=for-the-badge&logo=linkedin&logoColor=38bdf8" alt="LinkedIn"/></a>
  <a href="https://forgeaistudio.vercel.app"><img src="https://img.shields.io/badge/Portfolio-0b1424?style=for-the-badge&logo=vercel&logoColor=38bdf8" alt="Portfolio"/></a>
  <a href="mailto:sanskarchandawar3@gmail.com"><img src="https://img.shields.io/badge/Email-0b1424?style=for-the-badge&logo=gmail&logoColor=38bdf8" alt="Email"/></a>
</p>

<p><strong>I build data systems that move from raw input to reliable decisions.</strong><br/>
Data engineering is the center of my work: pipelines, lakehouses, quality checks,
and analytics-ready models. AI and backend systems are the layer I use to make
those data products useful.</p>

</div>

<img src="assets/h-projects.svg" width="100%" alt="Selected projects"/>

These are the projects that best represent how I think about systems: define the
data boundary, make transformations explicit, and keep the result inspectable.

### [01 / Retail Lakehouse with Databricks](https://github.com/Sanskar1724/Retail-Lakehouse-with-Databricks)

<table><tr><td width="42%" valign="top"><a href="https://github.com/Sanskar1724/Retail-Lakehouse-with-Databricks"><img src="social/card-retail-lakehouse.svg" width="100%" alt="Retail Lakehouse with Databricks"/></a></td><td valign="top">
<strong>System:</strong> A medallion architecture for turning inconsistent retail sources into governed analytics data.<br/><br/>
<strong>Flow:</strong> Bronze preserves raw records and traceability; Silver handles cleansing, deduplication, type standardization, and validation; Gold serves dimensions, facts, KPIs, and Power BI models.<br/><br/>
<code>PySpark</code> <code>Databricks</code> <code>Delta Lake</code> <code>Unity Catalog</code>
</td></tr></table>

### [02 / DataPilot](https://github.com/Sanskar1724/DataPilot)

<table><tr><td width="42%" valign="top"><a href="https://github.com/Sanskar1724/DataPilot"><img src="social/card-datapilot.svg" width="100%" alt="DataPilot"/></a></td><td valign="top">
<strong>System:</strong> A data-quality pipeline for CSV, JSON, JSONL, Excel, and Parquet inputs.<br/><br/>
<strong>Boundary:</strong> Deterministic code profiles and validates the data. The LLM sees metadata only, returns a schema-checked fix plan, and never executes arbitrary code. Registered transformations produce the clean dataset and report.<br/><br/>
<code>Python</code> <code>pandas</code> <code>DuckDB</code> <code>Pydantic</code>
</td></tr></table>

### [03 / CampusOps](https://github.com/Sanskar1724/CampusOps)

<table><tr><td width="42%" valign="top"><a href="https://github.com/Sanskar1724/CampusOps"><img src="social/card-campusops.svg" width="100%" alt="CampusOps"/></a></td><td valign="top">
<strong>System:</strong> An academic operations assistant that unifies email, timetables, documents, deadlines, and reminders.<br/><br/>
<strong>Architecture:</strong> A retrieval-first agent gathers only the facts needed for each turn, serves web, Telegram, and email, and falls back to deterministic answers when a provider is unavailable. Hybrid search, OCR, and scheduled jobs complete the workflow.<br/><br/>
<code>FastAPI</code> <code>Next.js</code> <code>PostgreSQL</code> <code>pgvector</code>
</td></tr></table>

### [04 / FinSight AI](https://github.com/Sanskar1724/FinSight_AI)

<table><tr><td width="42%" valign="top"><a href="https://github.com/Sanskar1724/FinSight_AI"><img src="social/card-finsight.svg" width="100%" alt="FinSight AI"/></a></td><td valign="top">
<strong>System:</strong> A finance workspace for a transaction ledger, budgets, goals, analytics, scenarios, reminders, and a grounded assistant.<br/><br/>
<strong>Trust model:</strong> Backend services own calculations and user isolation. The AI layer receives calculated context and evidence, so it can explain the data without becoming the source of truth.<br/><br/>
<code>React</code> <code>TypeScript</code> <code>FastAPI</code> <code>SQLAlchemy</code>
</td></tr></table>

<p align="right"><a href="https://github.com/Sanskar1724"><strong>Browse all repositories -></strong></a></p>

<img src="assets/h-stack.svg" width="100%" alt="Technical stack"/>

| Focus | Tools and practices |
|---|---|
| **Data platforms** | PySpark, Apache Spark, Databricks, Delta Lake, Unity Catalog, SQL, data quality, dimensional modeling |
| **Software** | Python, FastAPI, SQLAlchemy, Pydantic, TypeScript, React, Next.js, REST APIs |
| **Applied AI** | RAG, hybrid search, OpenRouter, prompt design, grounded assistants, deterministic fallbacks |
| **Delivery** | PostgreSQL, SQLite, Docker, GitHub Actions, Power BI |

<img src="assets/h-writing.svg" width="100%" alt="Technical writing"/>

- [DataPilot architecture](https://github.com/Sanskar1724/DataPilot/blob/main/docs/architecture.md) — metadata-only reasoning and safe transformation execution.
- [CampusOps agent design](https://github.com/Sanskar1724/CampusOps/blob/master/docs/AGENT.md) — retrieval, composition, history, and fallback behavior.
- [FinSight architecture](https://github.com/Sanskar1724/FinSight_AI/blob/main/docs/ARCHITECTURE.md) — service boundaries, authentication, and financial invariants.
- [FinSight research methodology](https://github.com/Sanskar1724/FinSight_AI/blob/main/docs/RESEARCH.md) — reproducible baseline-versus-grounded evaluation.

<img src="assets/h-activity.svg" width="100%" alt="Activity"/>

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="profile-3d-contrib/profile-night-rainbow.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="profile-3d-contrib/profile-green-animate.svg"/>
  <img src="profile-3d-contrib/profile-night-rainbow.svg" width="100%" alt="GitHub contribution graph"/>
</picture>
<sub>Open to conversations about data platforms, backend systems, and practical AI applications / <a href="mailto:sanskarchandawar3@gmail.com">sanskarchandawar3@gmail.com</a></sub>
</div>
