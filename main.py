from src.extract.api import (get_exchange_rate, 
                             get_credit_balance_cooperatives, 
                             get_credit_balance_with_direct_resources)

from src.extract.scraping import get_brazil_indicators

from src.transform.shape import (trasform_exchange_rate, 
                                 transform_credit_balance, 
                                 transform_brazil_indicators)

from src.transform.optmize import (optimized_exchange_rate, 
                                   optimized_credit_balance, 
                                   optimized_brazil_indicators)

from src.load.check import (check_exchange_rate, 
                            check_credit_balance, 
                            check_brazil_indicators)

from src.load.insert import upsert

def main() -> None:
    '''get_exchange_rate("USD")
    get_exchange_rate("BRL")
    get_credit_balance_cooperatives()
    get_credit_balance_with_direct_resources()
    get_brazil_indicators()'''

    '''trasform_exchange_rate()
    transform_credit_balance()
    transform_brazil_indicators()

    optimized_exchange_rate()
    optimized_credit_balance()
    optimized_brazil_indicators()'''

    '''check_exchange_rate()
    check_credit_balance()
    check_brazil_indicators()'''

    upsert()
    
if __name__ == "__main__":
    main()