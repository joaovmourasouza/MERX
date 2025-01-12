from src.logs import info_logging, error_logging
from bs4 import BeautifulSoup
import requests
import os

def get_brazil_indicators() -> None:
    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
    }
    
    try:
        response = requests.get("https://tradingeconomics.com/brazil/indicators", headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", {"class": "table table-hover"})
        rows = table.find_all("tr")
        
        with open(os.path.join('./data/bronze', "brazil_indicators.txt"), "w") as file:
            for row in rows:
                columns = row.find_all("td")
                if len(columns) >= 2:
                    indicator = columns[0].text.strip()
                    value = columns[1].text.strip()
                    file.write(f"{indicator},{value}\n")
        
        info_logging("Brazil indicators were successfully extracted")

    except requests.RequestException as e:
        error_logging(f"An error occurred while extracting Brazil indicators: {e}")