# ML Model Registry + Drift Monitor

## Goal
Full MLOps loop: train a churn model → log experiments to MLflow → register best model → serve via FastAPI → monitor feature drift with Evidently → trigger retraining alerts.

**Key skills:** MLflow, FastAPI, Evidently, Docker, CI/CD with GitHub Actions

## Structure
```
p2_ml_registry/
├── starter/    ← skeleton code with TODOs
└── solution/   ← complete reference implementation
```

## Setup
```bash
cd p2_ml_registry/starter
pip install -r requirements.txt
```

## How to work on it
1. Read this README fully
2. Start with `starter/` — fill in the TODOs in order
3. Run tests along the way: `pytest starter/`
4. When done (or stuck), compare with `solution/`
