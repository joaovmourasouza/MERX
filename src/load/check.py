from src.logs import info_logging, error_logging
import pandas as pd
import os

gold_path = './data/gold'
files = os.listdir(gold_path)

def check_brazil_indicators() -> None:
    try:
        for file in files:
            if file.startswith("brazil_indicators"):
                dataframe = pd.read_parquet(f"{gold_path}/{file}")
                if dataframe.empty:
                    error_logging(" Brazil indicators Dataframe is empty")
                if dataframe.duplicated().any():
                    error_logging(" Brazil indicators Dataframe has duplicates")
                if not dataframe['Indice'].apply(lambda x: isinstance(x, str)).all():
                    error_logging(" Brazil indicators Dataframe has non string values in Indice column")
                if not dataframe['Valor'].apply(lambda x: isinstance(x, float)).all():
                    error_logging(" Brazil indicators Dataframe has non float values in Valor column")
                info_logging(" Brazil indicators Dataframe was successfully checked")
    except Exception as e:
        error_logging(f"An error occurred while checking Brazil indicators: {e}")

def check_exchange_rate() -> None:
    try:
        for file in files:
            if file.endswith("_rate.parquet"):
                currency = file.split("_")[0]
                dataframe = pd.read_parquet(f"{gold_path}/{file}")
                if dataframe.empty:
                    error_logging(" Exchange rate Dataframe is empty")
                if dataframe.duplicated().any():
                    error_logging(" Exchange rate Dataframe has duplicates")
                if not dataframe['Moeda'].apply(lambda x: isinstance(x, str)).all():
                    error_logging(f" Exchange {currency} rate Dataframe has non string values in Indice column")
                if not dataframe['Valor'].apply(lambda x: isinstance(x, float)).all():
                    error_logging(f" Exchange {currency} rate Dataframe has non float values in Valor column")
                info_logging(" Exchange rate Dataframe was successfully checked")

    except Exception as e:
        error_logging(f"An error occurred while checking Exchange rate: {e}")

def check_credit_balance() -> None:
    try:
        for file in files:
            if file.startswith("credit_balance"):
                dataframe = pd.read_parquet(f"{gold_path}/{file}")
                if dataframe.empty:
                    error_logging(" Credit balance Dataframe is empty")
                if dataframe.duplicated().any():
                    error_logging(" Credit balance Dataframe has duplicates")
                if not pd.to_datetime(dataframe['Data'], errors='coerce').notnull().all():
                    error_logging(" Credit balance Dataframe has non-date values in Data column")
                if not dataframe['Valor'].apply(lambda x: isinstance(x, float)).all():
                    error_logging(" Credit balance Dataframe has non-float values in Valor column")
                info_logging(" Credit balance Dataframe was successfully checked")
    except Exception as e:
        error_logging(f"An error occurred while checking Credit balance: {e}")