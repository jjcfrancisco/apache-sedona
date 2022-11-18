import os
from pyspark.sql import SparkSession
from sedona.register import SedonaRegistrator
from sedona.utils import KryoSerializer, SedonaKryoRegistrator

extra_jars_dir:str = os.path.join(os.environ["SPARK_HOME"], "extra_jars")
extra_jars:list = [os.path.join(extra_jars_dir, x) for x in os.listdir(extra_jars_dir)]

spark:SparkSession = SparkSession. \
                   builder. \
                   master("local[*]").\
                   appName("my_sedona_app"). \
                   config("spark.serializer", KryoSerializer.getName). \
                   config("spark.kryo.registrator", SedonaKryoRegistrator.getName). \
                   config('spark.jars.packages',
                          'org.apache.sedona:sedona-python-adapter-3.0_2.12:1.2.1-incubating,'
                          'org.datasyslab:geotools-wrapper:1.3.0-27.2'). \
                   config("spark.jars", ",".join(extra_jars)).\
                   getOrCreate()

SedonaRegistrator.registerAll(spark)
spark.sparkContext.setLogLevel("ERROR")