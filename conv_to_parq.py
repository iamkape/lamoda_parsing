import pandas as pd

def convert_to_parq():
    """Convert csv file to parquet file"""
    pd.set_option('display.max_columns', 4)
    pd.set_option('display.max_rows', 40)
    pd.set_option('display.max_colwidth', 25)
    df = pd.read_csv('/home/unotuno/python/pythonProject/lamoda_parsing/out.csv')
    df.to_parquet('output.parquet')
    parquet_file = pd.read_parquet('output.parquet', engine='pyarrow')
    return parquet_file


if __name__ == '__main__':
    s = convert_to_parq()