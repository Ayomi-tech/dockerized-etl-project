import pandas as pd 
from sqlalchemy import create_engine


def load(df):
    print("Loading...")

    engine = create_engine("postgresql+psycopg2://etl_user:etl_pass@db:5432/etl_db") #SQLAlchemmy engine (Postgres)


    # This write Dataframe to SQL and rename 'df' to 'financial' 
    df.to_sql("financial", engine, if_exists="replace", index=False)

    print(f"Loaded {len(df)} rows into table 'financial")

