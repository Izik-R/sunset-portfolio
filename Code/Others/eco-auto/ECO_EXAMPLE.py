import pandas as pd
from pycoingecko import CoinGeckoAPI
from datetime import datetime as dt
import sqlalchemy as sq


## Init coingecko's api and simplfying the call to 'cg'
cg = CoinGeckoAPI()


# database cred's
hostname = "#####"
dbname="##"
uname="####"
pwd="####"

# connecting to the database
db = sq.create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

# constants for arguments 'get_price' as I use this code for ~9 other scripts
CONST_CUR = 'usd'
CONST_MK = True
CONST_VOL = True
CONST_24 = True
CONST_LAST = True
CONST_CHAIN = ['cosmos']


def main():
    
    parse()

def parse():
    
    # For loop isnt needed, however, I do use this script for multiple assets at a time for niche projects so it's developed with scalability in mind
    for chainid in CONST_CHAIN:
        data = cg.get_price(ids=chainid, vs_currencies=CONST_CUR, 
                                    include_market_cap=CONST_MK, include_24hr_vol=CONST_VOL, 
                                    include_24hr_change=CONST_24, include_last_updated_at=CONST_LAST)
        
        # isolating marketcap, volume, and 24h change in price to later append to a dataframe
        mkt = data[chainid]['usd_market_cap']
        vol = data[chainid]['usd_24h_vol']
        move = data[chainid]['usd_24h_change'] / 100
        
        # creating a list, dataframe, then migrating certain stats into the dataframe and also trimming decimals off the end of certain stats
        df = [chainid]
        main = pd.DataFrame(df)
        main['date'] = dt.now()
        main['timestamp'] = data[chainid]['last_updated_at']
        main['price_usd'] = data[chainid]['usd']
        main['market_cap'] = "{:.2f}".format(mkt)
        main['volume_24hr'] = "{:.2f}".format(vol)
        main['change_24hr'] = "{:.4f}".format(move)
        
        # uploading to MySQL server
        #main.to_sql('cosmos', db, if_exists='append')
        
        main.to_csv('example2.csv')
            
        
    
    return(print('All done!'))


if __name__ == "__main__":
    main()
    


