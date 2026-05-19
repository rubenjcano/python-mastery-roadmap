"""
Solution 01 — pandas & Polars
"""
import pandas as pd
import polars as pl
from exercises.exercise_01 import create_sample_data


def top_products_by_profit(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    return (
        df
        .assign(
            profit=lambda x: x["revenue"] - x["cost"],
            margin=lambda x: (x["revenue"] - x["cost"]) / x["revenue"],
        )
        .groupby("product")
        .agg(
            total_profit=("profit", "sum"),
            avg_margin=("margin", "mean"),
        )
        .nlargest(n, "total_profit")
        .reset_index()
    )


def monthly_revenue_trend(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df
        .assign(year_month=df["date"].dt.to_period("M"))
        .groupby("year_month", as_index=False)["revenue"]
        .sum()
        .rename(columns={"revenue": "total_revenue"})
        .assign(mom_pct_change=lambda x: x["total_revenue"].pct_change() * 100)
    )


def find_anomalous_days(df: pd.DataFrame, z_threshold: float = 2.0) -> pd.DataFrame:
    daily = df.resample("D", on="date")["revenue"].sum().reset_index()
    mean, std = daily["revenue"].mean(), daily["revenue"].std()
    daily["zscore"] = (daily["revenue"] - mean) / std
    return daily[daily["zscore"].abs() > z_threshold].reset_index(drop=True)


def polars_top_regions(df_pd: pd.DataFrame) -> pl.DataFrame:
    return (
        pl.from_pandas(df_pd)
        .with_columns(
            ((pl.col("revenue") - pl.col("cost")) / pl.col("revenue")).alias("margin")
        )
        .group_by("region")
        .agg([
            pl.col("margin").mean().alias("avg_margin"),
            pl.col("revenue").sum().alias("total_revenue"),
        ])
        .sort("avg_margin", descending=True)
    )


if __name__ == "__main__":
    df = create_sample_data()
    print(top_products_by_profit(df))
    print(polars_top_regions(df))
