# Time Series Forecasting Platform

## Goal
Multi-model forecasting system: train Prophet, NeuralForecast, and a baseline on multiple time series simultaneously. Auto-select best model per series by CV score. Expose via FastAPI with confidence intervals.

**Key skills:** statsforecast, NeuralForecast, MLflow, FastAPI, Plotly

## Structure
```
p7_forecasting_platform/
├── starter/    ← skeleton code with TODOs
└── solution/   ← complete reference implementation
```

## Setup
```bash
cd p7_forecasting_platform/starter
pip install -r requirements.txt
```

## How to work on it
1. Read this README fully
2. Start with `starter/` — fill in the TODOs in order
3. Run tests along the way: `pytest starter/`
4. When done (or stuck), compare with `solution/`
