# Python Performance Profiler CLI

## Goal
CLI tool (Typer + Rich) that profiles any Python script, generates a flame graph, identifies the top memory allocations, and uses Claude to suggest optimisations in plain English.

**Key skills:** py-spy, memray, subprocess, Typer, Rich, Claude API

## Structure
```
p9_profiler_cli/
├── starter/    ← skeleton code with TODOs
└── solution/   ← complete reference implementation
```

## Setup
```bash
cd p9_profiler_cli/starter
pip install -r requirements.txt
```

## How to work on it
1. Read this README fully
2. Start with `starter/` — fill in the TODOs in order
3. Run tests along the way: `pytest starter/`
4. When done (or stuck), compare with `solution/`
