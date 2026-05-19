"""
Exercise 01 — PySpark
=======================
E-commerce pipeline. Requires pyspark installed.

Run: spark-submit exercise_01.py
  or: python exercise_01.py (if pyspark is in venv)
"""
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def get_spark() -> SparkSession:
    return (
        SparkSession.builder
        .appName("DE-Exercise-01")
        .master("local[*]")
        .config("spark.sql.adaptive.enabled", "true")
        .getOrCreate()
    )


def create_sample_df(spark: SparkSession) -> DataFrame:
    """Creates a sample e-commerce orders DataFrame."""
    data = [
        ("O001", "C01", "Electronics", 1200.0, "2024-01-05"),
        ("O002", "C02", "Clothing",     80.0, "2024-01-06"),
        ("O003", "C01", "Electronics",  350.0, "2024-01-07"),
        ("O004", "C03", "Food",          25.0, "2024-01-07"),
        ("O005", "C02", "Electronics",  900.0, "2024-01-08"),
        ("O006", "C04", "Clothing",     150.0, "2024-01-09"),
        ("O007", "C01", "Food",          40.0, "2024-01-10"),
        ("O008", "C03", "Electronics", 2000.0, "2024-01-10"),
        ("O009", "C05", "Clothing",     200.0, "2024-01-11"),
        ("O010", "C02", "Food",          60.0, "2024-01-12"),
    ]
    return spark.createDataFrame(data, ["order_id", "customer_id", "category", "amount", "order_date"])


# ── Tasks ─────────────────────────────────────────────────────────────────

def task1_category_stats(df: DataFrame) -> DataFrame:
    """Return per-category stats: total_revenue, avg_order, order_count.
    Sort descending by total_revenue.
    
    Hint: groupBy + agg with F.sum, F.avg, F.count
    """
    # TODO
    ...


def task2_customer_ranking(df: DataFrame) -> DataFrame:
    """Rank customers by total spend within each category (rank 1 = highest).
    
    Return: customer_id, category, total_spend, rank
    Hint: Window.partitionBy("category").orderBy(F.desc(...))
    """
    # TODO
    ...


def task3_running_total(df: DataFrame) -> DataFrame:
    """Add a column 'running_total' — cumulative revenue ordered by date.
    
    Return all original columns + running_total.
    Hint: Window unboundedPreceding to currentRow, orderBy("order_date")
    """
    # TODO
    ...


def task4_flag_high_value(df: DataFrame, threshold: float = 500.0) -> DataFrame:
    """Add column 'order_tier': 'high' if amount >= threshold, else 'standard'.
    Also add 'discount_pct': 10.0 for high orders, 0.0 for standard.
    
    Hint: F.when().otherwise()
    """
    # TODO
    ...


# ─── Main ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    spark = get_spark()
    spark.sparkContext.setLogLevel("ERROR")
    df = create_sample_df(spark)

    print("=== Task 1: Category Stats ===")
    task1_category_stats(df).show()

    print("=== Task 2: Customer Ranking ===")
    task2_customer_ranking(df).show()

    print("=== Task 3: Running Total ===")
    task3_running_total(df).show()

    print("=== Task 4: High Value Flags ===")
    task4_flag_high_value(df).show()

    spark.stop()
