"""
Solution 01 — Classical ML
"""
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report
from exercises.exercise_01 import create_churn_dataset


def build_baseline(X_train, y_train) -> Pipeline:
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=500, class_weight="balanced", random_state=42)),
    ])
    return pipeline.fit(X_train, y_train)


def build_xgboost(X_train, y_train):
    from xgboost import XGBClassifier
    model = XGBClassifier(
        n_estimators=200, learning_rate=0.05, max_depth=5,
        subsample=0.8, colsample_bytree=0.8,
        eval_metric="logloss", random_state=42,
    )
    return model.fit(X_train, y_train)


def top_features(model, feature_names: list[str], n: int = 5) -> pd.DataFrame:
    importances = model.feature_importances_
    return (
        pd.DataFrame({"feature": feature_names, "importance": importances})
        .nlargest(n, "importance")
        .reset_index(drop=True)
    )


def compare_models(X, y) -> pd.DataFrame:
    from xgboost import XGBClassifier
    models = {
        "LogisticRegression": Pipeline([("s", StandardScaler()), ("m", LogisticRegression(max_iter=500, class_weight="balanced"))]),
        "RandomForest":       RandomForestClassifier(n_estimators=100, class_weight="balanced", random_state=42),
        "XGBoost":            XGBClassifier(n_estimators=100, eval_metric="logloss", random_state=42),
    }
    rows = []
    for name, model in models.items():
        scores = cross_val_score(model, X, y, cv=5, scoring="roc_auc")
        rows.append({"model_name": name, "mean_auc": scores.mean(), "std_auc": scores.std()})
    return pd.DataFrame(rows).sort_values("mean_auc", ascending=False)
