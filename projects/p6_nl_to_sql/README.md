# P6 — Natural Language → SQL Engine

## Goal
Build a system that converts plain English questions into SQL, executes them against a DuckDB database, and explains the results.

## What you'll build
- Schema introspection module
- Prompt engineering for SQL generation
- SQL validation with SQLGlot
- DuckDB query execution
- Error correction loop
- FastAPI endpoint

## Stack
- `anthropic` or `openai` for SQL generation
- `duckdb` for execution
- `sqlglot` for SQL validation/formatting
- `fastapi` for API
- `pydantic` for input/output models

## Key learning
- Prompt engineering for structured output
- Error handling and retry loops
- Schema-aware prompting (give the model the DDL)
