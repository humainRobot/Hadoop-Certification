# The SparkContext & SparkConf are not available by default when submitting spark application.
# The import is required.

from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("pyspark")
sc = SparkContext(conf=conf)
dataRDD = sc.textFile("/user/cloudera/sqoop_import/departments")
for line in dataRDD.collect():
    print(line)
dataRDD.saveAsTextFile("/user/cloudera/spark/pyspark/departmentsTesting"))

#Run using this command
#master local will run in spark native mode : spark-submit --master local pyspark_app.py
#master yarn will run in yarn mode : spark-submit --master yarn pyspark_app.py
