"""
Solution 01 — PySpark
"""
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from exercises.exercise_01 import get_spark, create_sample_df


def task1_category_stats(df: DataFrame) -> DataFrame:
    return (
        df.groupBy("category")
        .agg(
            F.sum("amount").alias("total_revenue"),
            F.avg("amount").alias("avg_order"),
            F.count("*").alias("order_count"),
        )
        .orderBy(F.desc("total_revenue"))
    )


def task2_customer_ranking(df: DataFrame) -> DataFrame:
    window = Window.partitionBy("category").orderBy(F.desc("total_spend"))
    return (
        df.groupBy("customer_id", "category")
        .agg(F.sum("amount").alias("total_spend"))
        .withColumn("rank", F.rank().over(window))
    )


def task3_running_total(df: DataFrame) -> DataFrame:
    window = Window.orderBy("order_date").rowsBetween(
        Window.unboundedPreceding, Window.currentRow
    )
    return df.withColumn("running_total", F.sum("amount").over(window))


def task4_flag_high_value(df: DataFrame, threshold: float = 500.0) -> DataFrame:
    return df.withColumn(
        "order_tier",
        F.when(F.col("amount") >= threshold, "high").otherwise("standard"),
    ).withColumn(
        "discount_pct",
        F.when(F.col("amount") >= threshold, 10.0).otherwise(0.0),
    )


if __name__ == "__main__":
    spark = get_spark()
    spark.sparkContext.setLogLevel("ERROR")
    df = create_sample_df(spark)
    task1_category_stats(df).show()
    task2_customer_ranking(df).show()
    task3_running_total(df).show()
    task4_flag_high_value(df).show()
    spark.stop()
