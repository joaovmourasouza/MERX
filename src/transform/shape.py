from src.logs import info_logging, error_logging
import pandas as pd
import json
import os 

bronze_path = './data/bronze'
silver_path = './data/silver'

files = os.listdir(bronze_path)

def trasform_exchange_rate() -> None:

    try:
        for file in files:
            if file.endswith("_rate.json"):
                with open(f"{bronze_path}/{file}", "r", encoding="utf-8") as f:
                        data = json.load(f)
                data_list = list(data.items())                        
                df = pd.DataFrame(data_list, columns=['Moeda', 'Valor'])
                df.to_csv(f"{silver_path}/{file.replace('.json', '.csv')}", index=False, sep=';')
                info_logging(f"Exchange rate for {file.replace('.json', '')} was successfully transformed")
    
    except Exception as e:
        error_logging(f"An error occurred while transforming exchange rate: {e}")

def transform_credit_balance() -> None:

    try:
        for file in files:
            if file.startswith("credit_balance") and file.endswith(".txt"):
                df = pd.read_csv(f"{bronze_path}/{file}", sep=';')
                df.to_csv(f"{silver_path}/{file.replace('.txt', '.csv')}", index=False, sep=';')
                info_logging(f"Credit balance for {file.replace('.txt', '')} was successfully transformed")
    
    except Exception as e:
        error_logging(f"An error occurred while transforming credit balance: {e}")

def transform_brazil_indicators() -> None:
    try:
        for file in files:
            if file.startswith("brazil_indicators") and file.endswith(".txt"):
                df = pd.read_csv(f"{bronze_path}/{file}", sep=',')
                data_list = df.values.tolist()
                df = pd.DataFrame(data_list, columns=['Indice', 'Valor'])
                df.to_csv(f"{silver_path}/{file.replace('.txt', '.csv')}", index=False, sep=';')
                info_logging(f"Brazil indicators for {file.replace('.txt', '')} was successfully transformed")
    
    except Exception as e:
        error_logging(f"An error occurred while transforming brazil indicators: {e}")