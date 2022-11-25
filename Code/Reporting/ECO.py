import pandas as pd
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def title():
    global start, stop, d_csv, h_csv, s_eco, c_eco
    month = input("Input month you're reporting on here: ")
    start = input("Input starting Timestamp: ")
    stop = input("Input ending Timestamp: ")
    h_csv = 'H_Eco_' + month + '22'  + '.csv'
    d_csv = 'D_Eco_' + month + '22'  + '.csv'
    s_eco = 'D_Eco_S' + '-' + month + '22' + '.csv'
    c_eco = 'D_Eco_C' + '-' + month + '22' + '.csv'

    return


# cosmos = cg.get_coin_market_chart_range_by_id(id='cosmos', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
# osmosis = cg.get_coin_market_chart_range_by_id(id='osmosis', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
# juno = cg.get_coin_market_chart_range_by_id(id='juno-network', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
# rowan = cg.get_coin_market_chart_range_by_id(id='sifchain', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
# sg = cg.get_coin_market_chart_range_by_id(id='stargaze', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
# evmos = cg.get_coin_market_chart_range_by_id(id='evmos', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
# akash = cg.get_coin_market_chart_range_by_id(id='akash-network', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
# secret = cg.get_coin_market_chart_range_by_id(id='secret', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
# kava = cg.get_coin_market_chart_range_by_id(id='kava', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
# eth = cg.get_coin_market_chart_range_by_id(id='ethereum', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
# btc = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)


def atom():
    global cosmos, prim, sec1
    cosmos = cg.get_coin_market_chart_range_by_id(id='cosmos', vs_currency='usd', 
                                                  from_timestamp=start, 
                                                  to_timestamp=stop, 
                                                  include_market_cap=True)
    
    df1 = []
    for x in cosmos['prices']:
        d1 = [x[0], x[1]]
        df1.append(d1)
        prim = pd.DataFrame(df1, columns=['Timestamp', 'P_ATOM'])
    
    
    df2 = []
    for x in cosmos['market_caps']:
        d2 = [x[1]]
        df2.append(d2)
        sec1 = pd.DataFrame(df2, columns=['M_ATOM'])
    
    prim['M_ATOM'] = sec1['M_ATOM']
    
    return
    

def osmo():
    global osmosis, prim2, sec2
    osmosis = cg.get_coin_market_chart_range_by_id(id='osmosis', vs_currency='usd', 
                                                  from_timestamp=start, 
                                                  to_timestamp=stop, 
                                                  include_market_cap=True)
    
    df1 = []
    for x in osmosis['prices']:
        d1 = [x[1]]
        df1.append(d1)
        prim2 = pd.DataFrame(df1, columns=['P_OSMO'])
    
    
    df2 = []
    for x in osmosis['market_caps']:
        d2 = [x[1]]
        df2.append(d2)
        sec2 = pd.DataFrame(df2, columns=['M_OSMO'])
    
    
    prim['P_OSMO'] = prim2['P_OSMO']
    prim['M_OSMO'] = sec2['M_OSMO']
    
    return

def juno_n():
    global juno, prim3, sec3
    juno = cg.get_coin_market_chart_range_by_id(id='juno-network', vs_currency='usd', 
                                                  from_timestamp=start, 
                                                  to_timestamp=stop, 
                                                  include_market_cap=True)
    
    df1 = []
    for x in juno['prices']:
        d1 = [x[1]]
        df1.append(d1)
        prim3 = pd.DataFrame(df1, columns=['P_JUNO'])
    
    
    df2 = []
    for x in juno['market_caps']:
        d2 = [x[1]]
        df2.append(d2)
        sec3 = pd.DataFrame(df2, columns=['M_JUNO'])
    
    
    prim['P_JUNO'] = prim3['P_JUNO']
    prim['M_JUNO'] = sec3['M_JUNO']
    
    return


def sif():
    global juno, prim4, sec4
    rowan = cg.get_coin_market_chart_range_by_id(id='sifchain', vs_currency='usd', 
                                                  from_timestamp=start, 
                                                  to_timestamp=stop, 
                                                  include_market_cap=True)
    
    df1 = []
    for x in rowan['prices']:
        d1 = [x[1]]
        df1.append(d1)
        prim4 = pd.DataFrame(df1, columns=['P_ROWAN'])
    
    
    df2 = []
    for x in rowan['market_caps']:
        d2 = [x[1]]
        df2.append(d2)
        sec4 = pd.DataFrame(df2, columns=['M_ROWAN'])
    
    
    prim['P_ROWAN'] = prim4['P_ROWAN']
    prim['M_ROWAN'] = sec4['M_ROWAN']
    
    return


def stars():
    global star, prim5, sec5
    star = cg.get_coin_market_chart_range_by_id(id='stargaze', vs_currency='usd', 
                                                  from_timestamp=start, 
                                                  to_timestamp=stop, 
                                                  include_market_cap=True)
    
    df1 = []
    for x in star['prices']:
        d1 = [x[1]]
        df1.append(d1)
        prim5 = pd.DataFrame(df1, columns=['P_STARS'])
    
    
    df2 = []
    for x in star['market_caps']:
        d2 = [x[1]]
        df2.append(d2)
        sec5 = pd.DataFrame(df2, columns=['M_STARS'])
    
    
    prim['P_STARS'] = prim5['P_STARS']
    prim['M_STARS'] = sec5['M_STARS']
    
    return


def evmos():
    global evm, prim6, sec6
    evm = cg.get_coin_market_chart_range_by_id(id='evmos', vs_currency='usd', 
                                                  from_timestamp=start, 
                                                  to_timestamp=stop, 
                                                  include_market_cap=True)
    
    df1 = []
    for x in evm['prices']:
        d1 = [x[1]]
        df1.append(d1)
        prim6 = pd.DataFrame(df1, columns=['P_EVMOS'])
    
    
    df2 = []
    for x in evm['market_caps']:
        d2 = [x[1]]
        df2.append(d2)
        sec6 = pd.DataFrame(df2, columns=['M_EVMOS'])
    
    
    prim['P_EVMOS'] = prim6['P_EVMOS']
    prim['M_EVMOS'] = sec6['M_EVMOS']
    
    return


def akt():
    global akash, prim7, sec7
    akash = cg.get_coin_market_chart_range_by_id(id='akash-network', vs_currency='usd', 
                                                  from_timestamp=start, 
                                                  to_timestamp=stop, 
                                                  include_market_cap=True)
    
    df1 = []
    for x in akash['prices']:
        d1 = [x[1]]
        df1.append(d1)
        prim7 = pd.DataFrame(df1, columns=['P_AKASH'])
    
    
    df2 = []
    for x in akash['market_caps']:
        d2 = [x[1]]
        df2.append(d2)
        sec7 = pd.DataFrame(df2, columns=['M_AKASH'])
    
    
    prim['P_AKASH'] = prim7['P_AKASH']
    prim['M_AKASH'] = sec7['M_AKASH']
    
    return


def scrt():
    global secret, prim8, sec8
    secret = cg.get_coin_market_chart_range_by_id(id='secret', vs_currency='usd', 
                                                  from_timestamp=start, 
                                                  to_timestamp=stop, 
                                                  include_market_cap=True)
    
    df1 = []
    for x in secret['prices']:
        d1 = [x[1]]
        df1.append(d1)
        prim8 = pd.DataFrame(df1, columns=['P_SECRET'])
    
    
    df2 = []
    for x in secret['market_caps']:
        d2 = [x[1]]
        df2.append(d2)
        sec8 = pd.DataFrame(df2, columns=['M_SECRET'])
    
    
    prim['P_SECRET'] = prim8['P_SECRET']
    prim['M_SECRET'] = sec8['M_SECRET']
    
    return


def kva():
    global secret, prim9, sec9
    kava = cg.get_coin_market_chart_range_by_id(id='kava', vs_currency='usd', 
                                                  from_timestamp=start, 
                                                  to_timestamp=stop, 
                                                  include_market_cap=True)
    
    df1 = []
    for x in kava['prices']:
        d1 = [x[1]]
        df1.append(d1)
        prim9 = pd.DataFrame(df1, columns=['P_KAVA'])
    
    
    df2 = []
    for x in kava['market_caps']:
        d2 = [x[1]]
        df2.append(d2)
        sec9 = pd.DataFrame(df2, columns=['M_KAVA'])
    
    
    prim['P_KAVA'] = prim9['P_KAVA']
    prim['M_KAVA'] = sec9['M_KAVA']
    
    return


def ether():
    global secret, prim10, sec10
    eth = cg.get_coin_market_chart_range_by_id(id='ethereum', vs_currency='usd', 
                                                  from_timestamp=start, 
                                                  to_timestamp=stop, 
                                                  include_market_cap=True)
    
    df1 = []
    for x in eth['prices']:
        d1 = [x[1]]
        df1.append(d1)
        prim10 = pd.DataFrame(df1, columns=['P_ETH'])
    
    
    df2 = []
    for x in eth['market_caps']:
        d2 = [x[1]]
        df2.append(d2)
        sec10 = pd.DataFrame(df2, columns=['M_ETH'])
    
    
    prim['P_ETH'] = prim10['P_ETH']
    prim['M_ETH'] = sec10['M_ETH']
    
    return


def bitcoin():
    global secret, prim11, sec11
    bit = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='usd', 
                                                  from_timestamp=start, 
                                                  to_timestamp=stop, 
                                                  include_market_cap=True)
    
    df1 = []
    for x in bit['prices']:
        d1 = [x[1]]
        df1.append(d1)
        prim11 = pd.DataFrame(df1, columns=['P_BTC'])
    
    
    df2 = []
    for x in bit['market_caps']:
        d2 = [x[1]]
        df2.append(d2)
        sec11 = pd.DataFrame(df2, columns=['M_BTC'])
    
    
    prim['P_BTC'] = prim11['P_BTC']
    prim['M_BTC'] = sec11['M_BTC']
    
    return


def daily():
    global df
    ts = prim['Timestamp']
    date = pd.to_datetime(ts, unit='ms')
    prim['Date'] = date
    df = prim.resample('D', on='Date').max()
    df.columns = ['Timestamp', 'P_ATOM', 'M_ATOM', 
                  'P_OSMO', 'M_OSMO', 'P_JUNO', 
                  'M_JUNO', 'P_ROWAN', 'M_ROWAN', 
                  'P_EVMOS', 'M_EVMOS', 'P_STARS', 
                  'M_STARS', 'P_AKASH', 'M_AKASH', 
                  'P_SECRET', 'M_SECRET', 'P_KAVA', 
                  'M_KAVA', 'P_ETH', 'M_ETH', 
                  'P_BTC', 'M_BTC', 'OldTime'] # type:ignore
    
    del df['OldTime']
    
    df.to_csv(d_csv)
    eco_c = df.describe()
    eco_c.to_csv(s_eco)
    
    return


def s_c():
    edit = pd.read_csv(d_csv)
    del edit['Timestamp']
    del edit['Date']
    pd.DataFrame(edit)
    
    first = edit.iloc[0]
    last = edit.iloc[-1]
    calc = last / first - 1

    calc.to_csv(c_eco)
    
    final = pd.read_csv(c_eco)
    final.columns = ['Metric', 'Yield'] #type: ignore
    final.to_csv(c_eco)
    
    return




def main():
    title()
    atom()
    osmo()
    juno_n()
    sif()
    evmos()
    stars()
    akt()
    scrt()
    kva()
    ether()
    bitcoin()
    daily()
    s_c()
    
    print('o7')

    return

main()