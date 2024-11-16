import pandas as pd
from sqlalchemy import create_engine

def load_to_database():
    # Load transformed data
    merged_data = pd.read_csv('../data/merged_data.csv')

    # Database connection string
    db_url = 'postgresql://postgres:yourpassword@localhost:5432/postgres'
    engine = create_engine(db_url)

    # Load data into PostgreSQL
    merged_data.to_sql('merged_data', engine, if_exists='replace', index=False)
    print("Data loaded into PostgreSQL successfully!")

if __name__ == "__main__":
    load_to_database()
