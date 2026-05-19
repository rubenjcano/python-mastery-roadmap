# pandas & Polars

## When to use each

| Situation | Use |
|---|---|
| Familiar API, small-medium data (<1GB) | pandas |
| Speed matters, large data, modern codebase | Polars |
| Lazy evaluation, query optimisation | Polars (lazy API) |
| Integration with sklearn, statsmodels | pandas |

## pandas must-know patterns
```python
import pandas as pd

df = pd.read_csv("sales.csv", parse_dates=["date"])

# Method chaining (always preferred)
result = (
    df
    .query("region == 'Europe' and revenue > 1000")
    .assign(
        profit=lambda x: x["revenue"] - x["cost"],
        month=lambda x: x["date"].dt.month,
    )
    .groupby("month")["profit"]
    .agg(["mean", "sum", "count"])
    .rename(columns={"mean": "avg_profit"})
    .reset_index()
)

# Window functions
df["rolling_avg"] = df.groupby("product")["revenue"].transform(
    lambda x: x.rolling(7, min_periods=1).mean()
)

# Efficient dtypes — always do this
df["category"] = df["category"].astype("category")   # saves 10x memory
df["id"] = pd.to_numeric(df["id"], downcast="integer")
```

## Polars — modern DataFrame library
```python
import polars as pl

df = pl.read_csv("sales.csv")

# Eager API
result = (
    df
    .filter(pl.col("region") == "Europe")
    .with_columns([
        (pl.col("revenue") - pl.col("cost")).alias("profit"),
        pl.col("date").str.to_date().dt.month().alias("month"),
    ])
    .group_by("month")
    .agg([
        pl.col("profit").mean().alias("avg_profit"),
        pl.col("profit").sum().alias("total_profit"),
    ])
    .sort("month")
)

# Lazy API — query optimised, best for large data
result = (
    pl.scan_csv("large_file.csv")    # lazy — reads nothing yet
    .filter(pl.col("value") > 100)
    .select(["id", "value", "category"])
    .collect()                        # executes here
)
```

## Performance comparison
| Operation | pandas | Polars |
|---|---|---|
| read_csv 1GB | ~30s | ~3s |
| groupby | ~2s | ~0.2s |
| Memory | baseline | ~2–5x less |
