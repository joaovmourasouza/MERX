from src.extract.api import (get_exchange_rate, 
                             get_credit_balance_cooperatives, 
                             get_credit_balance_with_direct_resources)
from src.extract.scraping import get_brazil_indicators

def main() -> None:
    get_exchange_rate("USD")
    get_exchange_rate("BRL")
    get_credit_balance_cooperatives()
    get_credit_balance_with_direct_resources()
    get_brazil_indicators()

if __name__ == "__main__":
    main()