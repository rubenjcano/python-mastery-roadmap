# Polars vs pandas Benchmark Suite

## Goal
Build a reproducible benchmark comparing Polars and pandas across groupby, join, filter, and aggregation operations on datasets from 10MB to 1GB. Publish results as an interactive Streamlit report.

**Key skills:** Polars lazy API, pandas optimization, benchmarking with timeit, Streamlit charts

## Structure
```
p1_polars_benchmark/
├── starter/    ← skeleton code with TODOs
└── solution/   ← complete reference implementation
```

## Setup
```bash
cd p1_polars_benchmark/starter
pip install -r requirements.txt
```

## How to work on it
1. Read this README fully
2. Start with `starter/` — fill in the TODOs in order
3. Run tests along the way: `pytest starter/`
4. When done (or stuck), compare with `solution/`
