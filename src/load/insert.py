from src.logs import info_logging, error_logging
import psycopg2.extras
import pandas as pd
import psycopg2
import os

conn = psycopg2.connect(
        dbname="mydb", 
        user="user", 
        password="password", 
        host="127.0.0.1", 
        port="5432"
    )

gold_path = './data/gold'
files = os.listdir(gold_path)

def upsert() -> None:

    try:
        for file in files:
            df = pd.read_parquet(f"{gold_path}/{file}")
            table_name = file.replace('.parquet', '')
            primary_key = df.columns[0]
            table_cols = ', '.join(df.columns)
            placeholders = ', '.join(['%s'] * len(df.columns))

            update_cols = ', '.join([f"{col} = EXCLUDED.{col}" for col in df.columns if col != primary_key])
            query = f"""
            INSERT INTO {table_name} ({table_cols})
            VALUES ({placeholders})
            ON CONFLICT ({primary_key})
            DO UPDATE SET {update_cols};
            """

            data_to_insert = [tuple(row) for row in df.itertuples(index=False, name=None)]
            
            with conn.cursor() as cur:
                psycopg2.extras.execute_batch(cur, query, data_to_insert)
                conn.commit()

            info_logging(f"{file} was successfully loaded")
    
    except Exception as e:
        error_logging(f"An error occurred while inserting data: {e}")
        conn.rollback()

    finally:
        conn.close()