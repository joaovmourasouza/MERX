from src.logs import info_logging, error_logging
from dotenv import load_dotenv
import requests
import json
import os

load_dotenv("/home/jvms/MERX/.env")

bronze_path = './data/bronze'

def get_exchange_rate(currency: str) -> None:
    try:
        response = requests.get(
            "https://v6.exchangerate-api.com/v6/" + os.getenv("EXCHANGERATE_API_KEY") + "/latest/" + currency
        )
        data = response.json()["conversion_rates"]
        with open(f"{bronze_path}/{currency.lower()}_exchange_rate.json", 'w') as file:
            json.dump(data, file, indent=4)
        info_logging(f"Exchange rate for {currency} was successfully extracted")
    except requests.RequestException as e:
        error_logging(f"An error occurred while extracting exchange rate for {currency}: {e}")

def get_credit_balance_cooperatives() -> None:
    try:
        response = requests.get(
            "https://api.bcb.gov.br/dados/serie/bcdata.sgs.25525/dados?formato=csv"
        )
        with open(f"{bronze_path}/credit_balance_cooperatives.txt", 'w') as file:
            file.write(response.text)
        info_logging("Credit balance for cooperatives was successfully extracted")
    except requests.RequestException as e:
        error_logging(f"An error occurred while extracting credit balance for cooperatives: {e}")

def get_credit_balance_with_direct_resources() -> None:
    try:
        response = requests.get(
            "https://api.bcb.gov.br/dados/serie/bcdata.sgs.20615/dados?formato=csv"
        )
        with open(f"{bronze_path}/credit_balance_direct_resources.txt", 'w') as file:
            file.write(response.text)
        info_logging("Credit balance with direct resources was successfully extracted")
    except requests.RequestException as e:
        error_logging(f"An error occurred while extracting credit balance with direct resources: {e}")