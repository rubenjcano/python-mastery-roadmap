# 🐍 Python Mastery Roadmap

> A complete, self-contained learning repository to take you from Python basics to expert-level mastery across every major data domain.

## 📚 What's Inside

- 📖 **Notes** — concise theory with examples and pitfalls
- 🏋️ **Exercises** — problems with hints (attempt before peeking at solutions!)
- ✅ **Solutions** — fully commented reference implementations
- 🚀 **Projects** — 9 capstone builds with starter code and full solutions

## 🗺️ Repository Structure

```
python-mastery-roadmap/
│
├── phase_01_foundations/          # Syntax, OOP, I/O — the non-negotiables
├── phase_02_intermediate/         # Async, packaging, testing, stdlib
├── phase_03_advanced/             # Metaprogramming, memory, performance
│
├── tracks/                        # Domain specialisations
│   ├── data_science/
│   ├── machine_learning/
│   ├── ai_llms/
│   ├── data_engineering/
│   ├── web_apis/
│   └── advanced_python/
│
├── projects/                      # 9 capstone projects (starter + solution)
└── phase_06_expert_habits/        # OSS, writing, code review
```

## 🚦 Recommended Path

```
Phase 1 → Phase 2 → Phase 3 → Pick 1-2 Tracks → Projects
```

| Phase / Track | Time |
|---|---|
| Phase 1 — Foundations | 4–6 weeks |
| Phase 2 — Intermediate | 6–8 weeks |
| Phase 3 — Advanced | 6–8 weeks |
| Each Domain Track | 8–12 weeks |
| Each Capstone Project | 2–4 weeks |

## 🎯 Domain Tracks

| Track | Key Libraries |
|---|---|
| 📊 Data Science | pandas, Polars, NumPy, Plotly, Streamlit, DuckDB |
| 🤖 Machine Learning | scikit-learn, PyTorch, XGBoost, MLflow, SHAP |
| ✨ AI / LLMs | LangChain, LangGraph, ChromaDB, Instructor, MCP |
| ⚙️ Data Engineering | PySpark, dbt, Airflow, Iceberg, Kafka |
| 🌐 Web / APIs | FastAPI, httpx, Playwright, Pydantic, Docker |
| 🔬 Advanced Python | Numba, py-spy, memray, OpenTelemetry, Typer |

## 🛠️ Setup

```bash
git clone https://github.com/YOUR_USERNAME/python-mastery-roadmap.git
cd python-mastery-roadmap

# Using uv (recommended — much faster than pip)
pip install uv
uv venv
source .venv/bin/activate          # Linux/Mac
.venv\Scripts\activate             # Windows PowerShell

# Base dependencies
uv pip install -r requirements.txt

# For a specific track
uv pip install -r tracks/data_engineering/requirements.txt
```

## 🏆 Capstone Projects

| # | Project | Tracks | Difficulty |
|---|---|---|---|
| P1 | Polars vs pandas Benchmark Suite | DS | ⭐⭐ |
| P2 | ML Model Registry + Drift Monitor | ML | ⭐⭐⭐ |
| P3 | RAG Chatbot over your Documents | AI | ⭐⭐ |
| P4 | Lakehouse: dbt + Iceberg + DuckDB | DE | ⭐⭐⭐ |
| P5 | Async Web Scraper at Scale | Web + Adv | ⭐⭐⭐ |
| P6 | Natural Language → SQL Engine | AI + DE | ⭐⭐⭐ |
| P7 | Time Series Forecasting Platform | ML + DS | ⭐⭐⭐ |
| P8 | Multi-Agent Data Analysis System | AI + DS | ⭐⭐⭐ |
| P9 | Python Performance Profiler CLI | Advanced | ⭐⭐⭐ |

## 📜 License

MIT
