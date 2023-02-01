import requests as rq
import pandas as pd
import sqlalchemy as sq
from pycoingecko import CoinGeckoAPI
from datetime import datetime as dt
from datetime import timedelta as td

## For personal analysis - already done in eco-auto repo
# cg = CoinGeckoAPI()

# df = ['cosmos']
# main = pd.DataFrame(df, columns=['asset'])
## --------------------------------


## Database cred's
hostname = "########"
dbname="######"
uname="#########"
pwd="####"

## Database variable to connect to later on
db = sq.create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))


def main():
    cosmo()



def cosmo():

## Grabbing timestamps from today, and yesterday as the api doesnt allow a single value to be returned...
## it must have a range

## Additionally turning them into strings with 'str', then trimming the decimals to comply with arguements...
## of the api

    now = dt.now()
    ts_now = str("{:.0f}".format(now.timestamp()))
    last = now - td(days=1)
    ts_last = str("{:.0f}".format(last.timestamp()))

## Preparing the link, parsing the data as json, given its a json api
    tx_url = rq.get('https://api.cosmoscan.net/transactions/fee/agg?by=day&from=' + ts_last + '&to=' + ts_now)
    tx_data = tx_url.json()
    tx_df = []

## For loop to gather data from dict's within the api
    for x in tx_data:
        info = [x['time'], x['value']]
        tx_df.append(info)

## Dropping todays value from the api as 'today' will no be a complete dataset
    tx_temp = pd.DataFrame(tx_df, columns=['timestamp', 'txfee'])
    tx_main = tx_temp.drop(index=1)

## repeating for the other api
    br_url = rq.get('https://api.cosmoscan.net/bonded-ratio/agg?by=day&from=' + ts_last + '&to=' + ts_now)
    br_data = br_url.json()
    br_df = []

    for x in br_data:
        info = [x['value']]
        br_df.append(info)

    br_temp = pd.DataFrame(br_df, columns=['bonded'])
    br_main = br_temp.drop(index=1)

## Joining the dataframes together, adding an 'asset' column to comply with the level of normalization in my schema...
## also adding date so I don't have to convert later on
    final = br_main.join(tx_main)
    final['asset'] = 'cosmos'
    final['date'] = dt.now()

## Uploading to SQL!
    #final.to_sql('cosmo', db, if_exists='append')
    final.to_csv('example.csv')
    return print(final)

## best practice :)
if __name__ == "__main__":
    main()



## For personal analysis - already done in eco-auto repo

# def coingecko():
    
#     data = cg.get_price(ids='cosmos', vs_currencies='usd', 
#                                     include_market_cap=True, include_24hr_vol=True, 
#                                     include_24hr_change=True, include_last_updated_at=True)

#     main['price_usd'] = (data['cosmos']['usd'])

#     mkt = data['cosmos']['usd_market_cap']
#     vol = data['cosmos']['usd_24h_vol']
#     move = data['cosmos']['usd_24h_change'] / 100

#     main['market_cap'] = ("{:.2f}".format(mkt))
#     main['volume_24hr'] = ("{:.2f}".format(vol))
#     main['change_24hr'] = ("{:.4f}".format(move))

## -------------------------
