
from dotenv import load_dotenv
from os import getenv

from pyspark.sql import SparkSession, functions as F
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType

## SET UP
load_dotenv()
spark = SparkSession.builder.getOrCreate()
spark.conf.set("spark.sql.session.timeZone", "UTC")

orders_schema = StructType([
    StructField("order_id", StringType(), True),
    StructField("customer_id", StringType(), True),
    StructField("product_category", StringType(), True),
    StructField("order_amount", DoubleType(), True),
    StructField("currency", StringType(), True),
    StructField("order_status", StringType(), True),
    StructField("created_at", TimestampType(), True),
])

df: DataFrame = spark.read.csv(getenv("ORDERS_CSV"), header=True, schema=orders_schema)

### CLEAN UP
df = df.withColumns({
    "currency": F.upper(F.trim(F.col("currency"))),
    "order_status": F.initcap(F.trim(F.col("order_status"))),
    "product_category": F.initcap(F.trim(F.col("product_category")))
})

df = df.dropna(subset=["order_id"])

df.write.mode("overwrite").parquet(getenv("BRONZE"))