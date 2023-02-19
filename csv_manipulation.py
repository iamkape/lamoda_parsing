from IPython.lib.pretty import pprint
from pyspark.sql import SparkSession
import pyspark.pandas as ps


def csv_work():

    spark = SparkSession.builder.appName('PySpark').getOrCreate()
    csv_file = "/home/unotuno/Загрузки/out.csv"
    df = spark.read.option('header', True).csv('out.csv').selectExpr("cast(Model as string) Model",
                                                                        "cast(Rank as int) Rank",
                                                                        "cast(Price as float) Price",
                                                                        "cast(Link as string) Link ")


    # Some variables.
    # df_col = df.select(['Model', 'Price']) # Show only Model & Price column.
    # double_price = df.withColumn('Double Price', df['Price']*2) # Price multiplication
    # drop_column = df.drop('Double Price') # drop 'Double Price' from Data Frame
    # rename_column = df.withColumnRenamed('Model', 'Nike Sneakers') # renamed column.
    # drop_some = df.na.drop(how='any', thresh=4) # show rows  with full info... if have NOne => remove this row.
    # change_data = df.na.fill('No info') # change None -> No info
    # expensive_goods = df.filter('Price >= 500').select(['Model', 'Price']) # Show only expensive sneaker's... (500 and more)
    # all_price = df.agg({'Price': 'sum'}) # summary of all goods.

    return df

if __name__ == "__main__":
    k = csv_work()
    k.show(50)



