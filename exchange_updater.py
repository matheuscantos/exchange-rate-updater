import info
import mysql.connector
from exchange_rates import get_exchange_rates
from datetime import datetime

Current_Date = datetime.today().strftime('%Y-%m-%d')

Base_Currency = 'USD'

Target_Currency = ['EUR','AUD','BRL','CAD','CHF','CNY','GBP','HKD','KRW','NOK','NZD','RUB','SEK','SGD','TWD','TRY','DKK','IDR','MXN']

Dict_Response = get_exchange_rates(base_currency=Base_Currency, target_currencies=Target_Currency, on_date=Current_Date)

cnx = mysql.connector.connect(user=info.User, password=info.Password,
                              host=info.Host,
                              database=info.Database)
cursor = cnx.cursor()

for Key,Value in Dict_Response.items():
    query = ("UPDATE exchanges "
             "SET exchange_rate = %s"
             "WHERE currency = %s")

    cursor.execute(query, (Value, Key))

cnx.commit()
cnx.close()
