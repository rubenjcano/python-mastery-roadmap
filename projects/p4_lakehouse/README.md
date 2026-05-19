# P4 — Lakehouse: dbt + Iceberg + DuckDB

## Goal
Build a local lakehouse with raw → staging → mart layer modelling, Iceberg table format, and DuckDB as the query engine.

## Architecture
```
Raw CSVs → DuckDB staging → dbt transformations → Iceberg marts
```

## What you'll build
- Raw data ingestion scripts
- dbt project with staging + intermediate + mart models
- dbt tests (not_null, unique, accepted_values, custom)
- dbt documentation
- Iceberg table writes via PyArrow

## Stack
- `dbt-core` + `dbt-duckdb`
- `duckdb`
- `pyiceberg` or `pyarrow`
- `pandas` / `polars` for raw ingestion

## Folder layout
```
p4_lakehouse/
├── starter/
│   ├── ingestion/         # Load raw CSVs to DuckDB
│   ├── dbt_project/       # dbt project skeleton
│   └── data/              # Sample CSVs
└── solution/
    ├── ingestion/
    ├── dbt_project/       # Complete dbt models + tests
    └── data/
```
