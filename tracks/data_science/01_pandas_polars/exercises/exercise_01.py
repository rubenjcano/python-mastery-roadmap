"""
Exercise 01 — pandas & Polars
==============================
Sales dataset analysis. Complete each function.

Setup: pip install pandas polars
"""
import pandas as pd
import polars as pl
from pathlib import Path


# ── Generate sample data ──────────────────────────────────────────────────
def create_sample_data() -> pd.DataFrame:
    import numpy as np
    rng = np.random.default_rng(42)
    n = 1000
    return pd.DataFrame({
        "date": pd.date_range("2023-01-01", periods=n, freq="D")[:n],
        "product": rng.choice(["A", "B", "C", "D"], n),
        "region": rng.choice(["EU", "US", "APAC"], n),
        "revenue": rng.uniform(100, 10000, n).round(2),
        "cost": rng.uniform(50, 5000, n).round(2),
        "units": rng.integers(1, 100, n),
    })


# ── pandas exercises ──────────────────────────────────────────────────────
def top_products_by_profit(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """Return top n products by total profit (revenue - cost).
    
    Expected columns: product, total_profit, avg_margin
    where avg_margin = mean((revenue - cost) / revenue)
    Sort descending by total_profit.
    
    Hint: .assign(), .groupby(), .agg(), .nlargest()
    """
    # TODO
    ...


def monthly_revenue_trend(df: pd.DataFrame) -> pd.DataFrame:
    """Return monthly revenue with month-over-month % change.
    
    Expected columns: year_month (Period), total_revenue, mom_pct_change
    Hint: dt.to_period("M"), .pct_change() * 100
    """
    # TODO
    ...


def find_anomalous_days(df: pd.DataFrame, z_threshold: float = 2.0) -> pd.DataFrame:
    """Return days where daily revenue is more than z_threshold std devs from mean.
    
    Hint: .resample("D"), zscore = (x - mean) / std
    """
    # TODO
    ...


# ── Polars exercises ──────────────────────────────────────────────────────
def polars_top_regions(df_pd: pd.DataFrame) -> pl.DataFrame:
    """Convert to Polars and return regions ranked by profit margin.
    
    Profit margin = (revenue - cost) / revenue
    Expected: region, avg_margin, total_revenue — sorted by avg_margin desc
    """
    df = pl.from_pandas(df_pd)
    # TODO: use Polars expressions
    ...


# ─── Run ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    df = create_sample_data()
    print("Shape:", df.shape)
    print("\n--- Top Products ---")
    print(top_products_by_profit(df))
    print("\n--- Monthly Trend (first 5) ---")
    print(monthly_revenue_trend(df).head())
    print("\n--- Anomalous Days ---")
    print(find_anomalous_days(df))
    print("\n--- Polars Regions ---")
    print(polars_top_regions(df))
