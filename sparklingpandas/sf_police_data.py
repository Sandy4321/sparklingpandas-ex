from pyspark import SparkContext
from sparklingpandas.pcontext import PSparkContext

# Create spark context.
sc = SparkContext("local", "example sfpd data")

# Create sparklingpandas context.
psc = PSparkContext(sc)

# read csv file with sparkling pandas context.
spDF = psc.read_csv("ex-data/SFPD_Incidents.csv")
spDF.groupby("Category").count().collect().to_csv(path_or_buf="/home/juliet/src/sparklingpandas-ex/my_csv.csv")

