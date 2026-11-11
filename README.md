<img src="assets/wallpaper.svg" width="100%" alt="Sanskar Chandawar, a student coding on a hilltop under a starry twilight sky"/>

<p align="center">
I'm an enthusiastic developer who loves exploring new technologies, solving problems, and turning ideas into reality.
I'm passionate about <b>Data Engineering</b>, <b>AI/LLMs</b>, and <b>software development</b>, always experimenting with new tools and pushing myself to become a better engineer.
I believe in learning by building, improving through challenges, and creating technology that makes a real-world impact.
</p>

<p align="center">
<a href="https://www.linkedin.com/in/sanskar-chandawar"><img src="https://img.shields.io/badge/LinkedIn-connect-38bdf8?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=08111f" alt="LinkedIn"/></a>
<a href="https://forgeaistudio.vercel.app"><img src="https://img.shields.io/badge/Forge_AI_Studio-visit-a78bfa?style=for-the-badge&labelColor=08111f" alt="Forge AI Studio"/></a>
<a href="mailto:sanskarchandawar3@gmail.com"><img src="https://img.shields.io/badge/Email-say_hi-34d399?style=for-the-badge&logo=gmail&logoColor=white&labelColor=08111f" alt="Email"/></a>
<img src="https://komarev.com/ghpvc/?username=Sanskar1724&label=Profile%20views&color=fb923c&style=for-the-badge" alt="Profile views"/>
</p>

<img src="assets/stats.svg" width="100%" alt="35+ public repositories, 267+ automated tests, 11 public datasets benchmarked, 1 research paper"/>

<img src="assets/h-projects.svg" width="100%" alt="Projects"/>

<table>
<tr>
<td width="50%" valign="top">
<img src="social/card-finsight.svg" width="100%" alt="FinSight AI dashboard and grounded assistant"/>
<h3><a href="https://github.com/Sanskar1724/FinSight_AI">FinSight AI</a></h3>
A personal finance workspace for India where the AI calculates first and writes second.

🔬 **Research** on five public benchmarks
- Computing with code lifts **FinQA from 48.7% to 71.0%**; 82.6% correct when two methods agree
- Routing with bge-m3 reaches **93.4% on Banking77** (vs 65.5%)
- Retrieval scores **nDCG@10 0.410 on FiQA** (vs 0.236 for BM25)

<details><summary>Memory and agent results</summary>

- Conversation memory lifts ConvFinQA follow-ups from 48% to 63% and doubles fully correct conversations (21% → 42%)
- Router + specialists match one agent on TAT-QA (43.3% vs 46.3%, within noise) with 22% fewer tokens

</details>

🏭 **Engineering:** `Decimal` finance engine, rate-limited auth, migrations, 77 tests, CI for lint, types, and build.

`React 19` `TypeScript` `FastAPI` `PostgreSQL` `PWA`
</td>
<td width="50%" valign="top">
<a href="https://huggingface.co/spaces/EquilStable/MarginGraph"><img src="social/card-margingraph.svg" width="100%" alt="MarginGraph, live demo"/></a>
<h3><a href="https://github.com/Sanskar1724/MarginGraph">MarginGraph</a></h3>
Recommends add-ons that customers will buy and that keep the retailer profitable.

🔬 **Research** on five real retail datasets
- LightGBM hits **38.1% Hit@10** on 4,480 UCI baskets and holds up on Ta Feng, Dunnhumby, and Instacart
- A 30-day checkout replay earns **+24% add-on profit** over the ranker alone, with 0 margin-floor breaks vs 164
- 📄 Written up as a 19-page preprint: [*Margin-Aware, Constrained Recommendation of Checkout Add-Ons*](https://github.com/Sanskar1724/MarginGraph/blob/main/paper/main.pdf)

<details><summary>Per-dataset results and caveats</summary>

- Ta Feng +8.3 pts, Dunnhumby +9.8, Instacart +4.1 (once past purchases fill the pool first), a tie on small Olist
- +19% profit across 5 seeds; cost and stock are simulated
- LLM rankers were tested and documented as a no-go

</details>

🏭 **Engineering:** MILP optimizer enforces a 15% margin floor, served through FastAPI with CI at p50 22 ms.

`Python` `LightGBM` `PuLP` `FastAPI` `Gradio`
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://paytrustai.streamlit.app"><img src="social/card-paytrust.svg" width="100%" alt="PayTrust AI, live demo"/></a>
<h3><a href="https://github.com/Sanskar1724/PayTrust_AI">PayTrust AI</a></h3>
Decides whether an AI agent may make a payment: `ALLOW`, `ASK_USER`, or `DENY`. Built for the Razorpay Buildathon.

🔬 **Research** on IEEE-CIS fraud data
- Trained on **590k transactions** with a time-based split, never loaded whole
- **ROC-AUC 0.842, recall 0.823**, with a threshold tool to trade precision for recall

🏭 **Engineering:** deterministic policy gate, LLM kept advisory-only, HMAC-verified idempotent webhooks, 128 tests.

`Python` `FastAPI` `scikit-learn` `Streamlit` `Razorpay`
</td>
<td width="50%" valign="top">
<a href="https://campus-ops-chi.vercel.app"><img src="social/card-campusops.svg" width="100%" alt="CampusOps, live demo"/></a>
<h3><a href="https://github.com/Sanskar1724/CampusOps">CampusOps</a></h3>
An academic agent that reads college email, timetables, and documents, then answers on web, Telegram, and email.

🔬 **Retrieval**
- **Hybrid search** (embeddings + keywords) over PDFs, photos, and spreadsheets
- **Vision OCR** turns timetable photos and portal PDFs into searchable records

🏭 **Engineering:** one agent core for every channel, deterministic LLM fallback, JWT auth, Docker, 62 tests.

`Python` `FastAPI` `Next.js` `PostgreSQL` `pgvector`
</td>
</tr>
</table>

<img src="assets/h-stack.svg" width="100%" alt="Skills"/>

<img src="assets/skills.svg" width="100%" alt="Skills: LLM APIs, RAG, LLM evals, PyTorch, LightGBM, PySpark, Databricks, Python, TypeScript, React, FastAPI, Docker and more"/>

<img src="assets/h-activity.svg" width="100%" alt="Activity"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="profile-3d-contrib/profile-night-rainbow.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="profile-3d-contrib/profile-green-animate.svg"/>
  <img src="profile-3d-contrib/profile-night-rainbow.svg" width="100%" alt="GitHub contribution graph"/>
</picture>
