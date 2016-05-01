#Developing simple scala based applications for spark
#Save this to a file with py extension

from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("pyspark")
sc = SparkContext(conf=conf)
dataRDD = sc.textFile("/user/cloudera/sqoop_import/departments")
for line in dataRDD.collect():
    print(line)
dataRDD.saveAsTextFile("/user/cloudera/pyspark/departmentsTesting")

#Run using this command
#master local will run in spark native mode
spark-submit --master local saveFile.py

#master yarn will run in yarn mode
spark-submit --master yarn saveFile.py
