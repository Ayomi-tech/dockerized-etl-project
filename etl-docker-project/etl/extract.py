import pandas as pd

def extract (file_path= "/data/annual-enterprise-survey-2023-financial-year-provisional.csv"):
    df = pd.read_csv(file_path)
    print((f"Extracted {len(df)} rows from CSV"))
    return df


