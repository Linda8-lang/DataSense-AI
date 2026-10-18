# 📊 DataSense AI - Dataset & SQL Copilot

**Live demo:** https://datasense-si.streamlit.app/ · **Product portfolio:** https://linda8-lang.github.io/DataSense-AI/portfolio.html

DataSense AI turns raw spreadsheets into executive-ready insights. Upload a dataset, ask a question in plain English, and get a short summary plus a ready-to-run SQL query.

## The Problem
Data analysts lose hours translating raw files into executive summaries and SQL queries. General-purpose LLMs hallucinate numbers and can't do exact computation, and non-technical teams struggle to write good prompts.

## How DataSense Solves It
- **Exact math with Pandas** - row counts, column counts and missing values are computed directly from the data, never guessed by the AI.
- **AI for language, not arithmetic** - the LLM only sees the column names and types, and writes the plain-English summary and the ANSI SQL query.

## Features
- 📁 **Flexible data sources** - CSV, Excel (`.xlsx`, `.xls`, with a sheet picker) and public Google Sheets links
- 🔍 **Instant data profile** - preview, total rows, total columns and missing values
- 💬 **Text-to-SQL** - ask a question in plain English and get a 2-sentence summary plus an optimized SQL query
- ⚡ **Fast and free** - runs open-source models on Groq's free tier

## Tech Stack
| Layer | Tool |
|-------|------|
| UI | Streamlit |
| Data engine | Pandas, openpyxl, xlrd |
| LLM | `openai/gpt-oss-20b` via Groq |
| Config | python-dotenv |

## Run It Locally
```bash
git clone <this-repo-url>
cd DataSense
pip install -r requirements.txt
cp .env.example .env      # then paste your free Groq key into .env
streamlit run app.py
```
Get a free Groq API key (no credit card) at https://console.groq.com.

## Project Docs
See [PRD.md](PRD.md) for the product requirements, user persona and KPIs.
