"""
Exercise 01 — Classical ML
============================
Churn prediction on a synthetic telecom dataset.
"""
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score


def create_churn_dataset() -> tuple[pd.DataFrame, pd.Series]:
    """Synthetic churn dataset with realistic feature names."""
    X, y = make_classification(
        n_samples=5000, n_features=15, n_informative=10,
        n_redundant=3, weights=[0.85, 0.15], random_state=42,
    )
    feature_names = [
        "tenure_months", "monthly_charge", "total_charge",
        "num_products", "call_centre_calls", "late_payments",
        "contract_type", "internet_speed", "has_tv",
        "has_phone", "data_usage_gb", "avg_call_duration",
        "support_tickets", "billing_issues", "nps_score"
    ]
    return pd.DataFrame(X, columns=feature_names), pd.Series(y, name="churn")


# ── Task 1: Build and evaluate a baseline model ───────────────────────────
def build_baseline(X_train, y_train) -> Pipeline:
    """Build a LogisticRegression pipeline with StandardScaler.
    Return the fitted pipeline.
    """
    # TODO
    ...


# ── Task 2: Try XGBoost and compare ──────────────────────────────────────
def build_xgboost(X_train, y_train) -> object:
    """Build and fit an XGBClassifier.
    Hint: from xgboost import XGBClassifier
    """
    # TODO
    ...


# ── Task 3: Feature importance from XGBoost ──────────────────────────────
def top_features(model, feature_names: list[str], n: int = 5) -> pd.DataFrame:
    """Return DataFrame with top n features by importance.
    Columns: feature, importance — sorted descending.
    Hint: model.feature_importances_
    """
    # TODO
    ...


# ── Task 4: Compare models with cross-validation ─────────────────────────
def compare_models(X, y) -> pd.DataFrame:
    """Compare LogisticRegression, RandomForest, XGBoost using 5-fold CV.
    Return DataFrame: model_name, mean_auc, std_auc
    Scoring: roc_auc
    """
    # TODO
    ...


if __name__ == "__main__":
    X, y = create_churn_dataset()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    baseline = build_baseline(X_train, y_train)
    y_pred = baseline.predict(X_test)
    print("=== Baseline (Logistic Regression) ===")
    print(classification_report(y_test, y_pred))

    print("\n=== Model Comparison ===")
    print(compare_models(X, y))
