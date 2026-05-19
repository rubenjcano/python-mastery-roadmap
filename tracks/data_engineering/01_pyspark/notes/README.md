# PySpark

## Session setup
```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("MyPipeline")
    .config("spark.sql.adaptive.enabled", "true")       # AQE — always enable
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.driver.memory", "4g")
    .getOrCreate()
)
```

## DataFrame API — always prefer over RDD
```python
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Schema definition (explicit > inferred for large pipelines)
schema = StructType([
    StructField("id", StringType(), nullable=False),
    StructField("revenue", DoubleType(), nullable=True),
    StructField("region", StringType(), nullable=True),
])

df = spark.read.schema(schema).parquet("s3://bucket/data/")

result = (
    df
    .filter(F.col("revenue").isNotNull())
    .withColumn("profit_tier", 
        F.when(F.col("revenue") > 10000, "high")
         .when(F.col("revenue") > 1000, "mid")
         .otherwise("low")
    )
    .groupBy("region", "profit_tier")
    .agg(
        F.sum("revenue").alias("total_revenue"),
        F.count("*").alias("num_records"),
    )
    .orderBy("region", F.desc("total_revenue"))
)
```

## Window functions
```python
from pyspark.sql.window import Window

window = Window.partitionBy("region").orderBy(F.desc("revenue"))

df_ranked = df.withColumn("rank", F.rank().over(window))

# Running total per region
running_window = Window.partitionBy("region").orderBy("date").rowsBetween(
    Window.unboundedPreceding, Window.currentRow
)
df = df.withColumn("cumulative_revenue", F.sum("revenue").over(running_window))
```

## Performance tips
```python
# 1. Cache datasets you reuse multiple times
df.cache()        # in-memory
df.persist()      # configurable storage level

# 2. Broadcast small tables in joins
from pyspark.sql.functions import broadcast
result = large_df.join(broadcast(small_lookup), "key")

# 3. Partition wisely
df.repartition(200, "region")    # shuffle + repartition
df.coalesce(10)                  # reduce partitions (no shuffle)

# 4. Avoid UDFs when possible — use built-in F.* functions
# BAD: python UDF is slow
from pyspark.sql.functions import udf
slow = udf(lambda x: x * 2)

# GOOD: native Spark expression
fast = F.col("value") * 2
```

## Reading/Writing Delta Lake
```python
# Write
df.write.format("delta").mode("overwrite").save("/path/to/delta")

# Read
df = spark.read.format("delta").load("/path/to/delta")

# Merge (upsert)
from delta.tables import DeltaTable
target = DeltaTable.forPath(spark, "/path/to/delta")
target.alias("t").merge(
    updates.alias("u"), "t.id = u.id"
).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()
```
