from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FraudDetectionPipeline") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "bank_transactions") \
    .load()

transactions = df.selectExpr("CAST(value AS STRING)")

query = transactions.writeStream \
    .format("console") \
    .start()

query.awaitTermination()