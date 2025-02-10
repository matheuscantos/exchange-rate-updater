from exchange_rates import get_exchange_rates
from datetime import datetime

# https://github.com/ddofborg/exchange_rates

Current_Date = datetime.today().strftime('%Y-%m-%d')

Base_Currency = 'USD'

Target_Currency = ['EUR','AUD','BRL','CAD','CHF','CNY','GBP','HKD','KRW','NOK','NZD','RUB','SEK','SGD','TWD','TRY','DKK','IDR','MXN']

print( get_exchange_rates(base_currency=Base_Currency, target_currencies=Target_Currency, on_date=Current_Date))