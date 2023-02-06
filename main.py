from pyspark.sql import *

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("hello spark") \
        .master("local[2]") \
        .getOrCreate()

    data_list = [("rohan", 1), ("anand", 2), ("rohit", 3)]
    df = spark.createDataFrame(data_list).toDF("Name", "No.")
    df.show()
