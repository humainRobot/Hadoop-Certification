
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("pyspark")
sc = SparkContext(conf=conf)
dataRDD = sc.textFile("/user/cloudera/sqoop_import/retail.db/departments")
for line in dataRDD.collect():
    print(line)

dataRDD.saveAsTextFile("/user/cloudera/pyspark/departmentsTesting")

#Run using this command
#master local will run in spark native mode : spark-submit --master local pyspark_app.py
#master yarn will run in yarn mode : spark-submit --master yarn pyspark_app.py
