import pandas as pd 
import numpy as np

def transform (df):
    print("Transforming data....")
    df.columns = map(str.lower, df.columns)

# Convert all data in the value field to numeric and all invalid string to 0
    if "value" in df.columns:
        df['value'] = pd.to_numeric(df['value'], errors='coerce').fillna(0)

# add 10% to any > 80000
        # df["value"] = df['value'].apply(lambda x: x + (80000 /100) if x > 80000 else x)
         
    return df


