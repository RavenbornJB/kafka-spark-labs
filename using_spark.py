from pyspark.sql import SparkSession


if __name__ == '__main__':
    spark = SparkSession.builder.appName('using-spark').getOrCreate()

    df = spark.read.csv("data.csv")

    print(f"Our dataset has {df.count()} rows.")
