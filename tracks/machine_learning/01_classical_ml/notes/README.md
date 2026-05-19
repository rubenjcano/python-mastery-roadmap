# Classical Machine Learning

## The scikit-learn API — one pattern for everything
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

# 1. Build pipeline (preprocessing + model)
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model",  RandomForestClassifier(n_estimators=200, random_state=42)),
])

# 2. Evaluate with cross-validation (always — never just train/test split)
scores = cross_val_score(pipeline, X, y, cv=5, scoring="f1_weighted")
print(f"F1: {scores.mean():.3f} ± {scores.std():.3f}")

# 3. Fit on full training data once you're happy
pipeline.fit(X_train, y_train)

# 4. Predict
y_pred = pipeline.predict(X_test)
y_proba = pipeline.predict_proba(X_test)
```

## Hyperparameter tuning with Optuna
```python
import optuna
from sklearn.ensemble import GradientBoostingClassifier

def objective(trial):
    params = {
        "n_estimators":   trial.suggest_int("n_estimators", 50, 500),
        "max_depth":      trial.suggest_int("max_depth", 2, 8),
        "learning_rate":  trial.suggest_float("learning_rate", 0.01, 0.3, log=True),
        "subsample":      trial.suggest_float("subsample", 0.5, 1.0),
    }
    model = GradientBoostingClassifier(**params, random_state=42)
    return cross_val_score(model, X_train, y_train, cv=3, scoring="f1").mean()

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=50)
print(study.best_params)
```

## Evaluation checklist
```python
from sklearn.metrics import (
    classification_report, confusion_matrix,
    roc_auc_score, average_precision_score
)

print(classification_report(y_test, y_pred))
print("AUC-ROC:", roc_auc_score(y_test, y_proba[:, 1]))
print("AUC-PR:", average_precision_score(y_test, y_proba[:, 1]))
```

## XGBoost / LightGBM (prefer over RandomForest for tabular data)
```python
import xgboost as xgb

model = xgb.XGBClassifier(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="logloss",
    early_stopping_rounds=50,
    random_state=42,
)
model.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=False)
```
