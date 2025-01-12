from src.logs import info_logging, error_logging
from src.transform.process import process_credit_balance
import pandas as pd
import os

silver_path = './data/silver'
gold_path = './data/gold'

files = os.listdir(silver_path)

def optimized_exchange_rate() -> None:

    try:
        for file in files:
            if file.endswith("_rate.csv"):
                df = pd.read_csv(f"{silver_path}/{file}", sep=';')
                df.to_parquet(f"{gold_path}/{file}.parquet")
                info_logging(f"Exchange rate for {file.replace('.csv', '')} was successfully optimized, ready to be inserted")
    
    except Exception as e:
        error_logging(f"An error occurred while optimizing exchange rate: {e}")

def optimized_credit_balance() -> None:

    try:
        for file in files:
            if file.startswith("credit_balance"):
                df = pd.read_csv(f"{silver_path}/{file}", sep=';')
                df = process_credit_balance(df)
                df.to_parquet(f"{gold_path}/{file}.parquet")
                info_logging(f"Exchange rate for {file.replace('.csv', '')} was successfully optimized, ready to be inserted")
    
    except Exception as e:
        error_logging(f"An error occurred while optimizing exchange rate: {e}")

def optimized_brazil_indicators() -> None:

    try:
        for file in files:
            if file.startswith("brazil_indicators"):
                df = pd.read_csv(f"{silver_path}/{file}", sep=';')
                df.to_parquet(f"{gold_path}/{file}.parquet")
                info_logging(f"Exchange rate for {file.replace('.csv', '')} was successfully optimized, ready to be inserted")
    
    except Exception as e:
        error_logging(f"An error occurred while optimizing exchange rate: {e}")