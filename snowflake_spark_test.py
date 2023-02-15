import os
from pyspark.sql import SparkSession
#import net.snowflake.spark.snowflake.Utils.SNOWFLAKE_SOURCE_NAME

sfOptions = {
  "sfURL" : "moelis-dev.us-east-1.snowflakecomputing.com",
  "sfUser" : 'devtest',
  "sfPassword" : 'test123',
  "sfDatabase" : 'MDWSTAGE_FIVETRAN',
  "sfSchema" : 'MCONNECT_DEV',
  "sfRole" : 'DBA',
  "sfWarehouse" : 'ETL_WH'
}

snowJars = [os.path.join('/home/cdsw/jars', x) for x in os.listdir('/home/cdsw/jars')]

print(1, snowJars)
spark = SparkSession.builder \
    .appName("cml-spark-test") \
    .config("spark.jars", ",".join(snowJars)) \
    .getOrCreate()

SNOWFLAKE_SOURCE_NAME = "net.snowflake.spark.snowflake"

query = '''

select * from  "MDWSTAGE_FIVETRAN"."MCONNECT_DEV"."DEBTPRICING" limit 10;
'''


df = spark.read.format(SNOWFLAKE_SOURCE_NAME) \
    .options(**sfOptions) \
    .option("query", query) \
    .load()

display(df)