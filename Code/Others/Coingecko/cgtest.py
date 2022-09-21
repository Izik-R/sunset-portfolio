from pycoingecko import CoinGeckoAPI
import pandas as pd
import timetest as tt

cg = CoinGeckoAPI()
tt.prev()

cosmos = cg.get_coin_market_chart_range_by_id(id='cosmos', 
                                              vs_currency='usd', 
                                              from_timestamp=tt.start, 
                                              to_timestamp=tt.stop, 
                                              include_market_cap=True)


t1 = []
for x in cosmos['prices']:
    patom = [x[0], x[1]]
    t1.append(patom)
    t2 = pd.DataFrame(t1, columns=['Timestamp', 'P_ATOM'])

t3 = []   
for x in cosmos['market_caps']:
    matom = [x[1]]
    t3.append(matom)
    t4 = pd.DataFrame(t3, columns=['M_ATOM'])
    t2['M_ATOM'] = t4
    
dt = t2['Timestamp']
date = pd.to_datetime(dt, unit='ms')
t2['Date'] = date
df = t2.resample('D', on='Date').max()
    
print(df)
    

