import alpaca_trade_api as tradeapi
from datetime import date
import json

#API KEYS
API_KEY = "PK1TKGZQ9LQHV3ZW4T8A"
SECRET_KEY = "2FtT2exHZnYgN6wtMmeOTiQJ3UnCL8BgqeUbYsG1"
BASE_URL = "https://paper-api.alpaca.markets"


api = tradeapi.REST(
    base_url=BASE_URL,
    key_id=API_KEY,
    secret_key=SECRET_KEY
)

NUM_DAYS = 6
#Get Trading Data for AAPL
AAPL_D_BARSET = api.get_barset('AAPL', 'day', limit = NUM_DAYS)
AAPL_D_BARS = AAPL_D_BARSET['AAPL']

#See % change over barset
week_open = AAPL_D_BARS[0].o
week_close = AAPL_D_BARS[-1].c
percent_change = (week_close - week_open) / week_open * 100
#print('AAPL moved {}% over the last 5 days' .format(percent_change))


#FORMAT DAILY PRINT
print("{:<25} {:<15} {:<15} {:<15} {:<15}".format('DATE(DAY)', 'OPEN', 'CLOSE', 'HIGH', 'LOW'))
for i in range (6):

    print("{:<25} {:<15} {:<15} {:<15} {:<15}".format((NUM_DAYS - (i+1)), AAPL_D_BARS[i].o, AAPL_D_BARS[i].c, AAPL_D_BARS[i].h, AAPL_D_BARS[i].l))

#print(AAPL_D_BARS)
