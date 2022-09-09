from pycoingecko import CoinGeckoAPI
import pandas as pd
import csv

cg = CoinGeckoAPI()

df = []
heads = ['Timestamp', 'Price']
csvname = 'yeah.csv'

start = 1656658800
stop = 1659250800

listing = cg.get_coin_market_chart_range_by_id(id='cosmos', vs_currency='usd', from_timestamp=start, to_timestamp=stop)

for x in listing['prices']:
    pclean = [x[0], x[1]]
    df.append(pclean)
    
with open(csvname, 'w', encoding='UTF8', newline='') as f:
    ww = csv.writer(f)
    ww.writerow(heads)
    ww.writerows(df)

data = pd.read_csv(csvname)

dt = data['Timestamp']

date = pd.to_datetime(dt, unit='ms')

data['Date'] = date

clean = data.resample('D', on='Date').max()

final = clean.to_csv(csvname)

print('Bingo!')