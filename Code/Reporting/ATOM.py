import pandas as pd
import requests

# https://api.cosmoscan.net/transactions/fee/agg?by=day&from=TIMESTAMP&to=TIMESTAMP
# https://api.coingecko.com/api/v3/coins/cosmos/market_chart/range?vs_currency=usd&from=TIMESTAMP&to=TIMESTAMP
# https://api.cosmoscan.net/bonded-ratio/agg?by=day&from=TIMESTAMPto=TIMESTAMP

def title():
    global atomcsv
    global s_atomcsv
    global c_atomcsv
    global start_ts
    global end_ts
    global tx_link
    global coin_link
    global br_link
    month = input("Enter Month of report here: ")
    start_ts = input("Paste the beginning time stamp here: ")
    end_ts = input("Paste the ending time stamp here: ")
    tx_link = 'https://api.cosmoscan.net/transactions/fee/agg?by=day&from=' + start_ts + '&to=' + end_ts
    coin_link = 'https://api.coingecko.com/api/v3/coins/cosmos/market_chart/range?vs_currency=usd&from=' + start_ts + '&to=' + end_ts
    br_link = 'https://api.cosmoscan.net/bonded-ratio/agg?by=day&from=' + start_ts + '&to=' + end_ts
    atomcsv = month + '22_ATOM' + '.csv'
    s_atomcsv = month + '22_S_ATOM' + '.csv'
    c_atomcsv = month + '22_C_ATOM' + '.csv'
    
    return
title()

def tx_func():
    global tx_api
    global tx_br
    tx_api = requests.get(tx_link)
    cleaned = tx_api.json()
    tx_d = []
    
    for x in cleaned:
        tx_loop = [x['time'], x['value']]
        tx_d.append(tx_loop)
    
    tx_br = pd.DataFrame(tx_d)
    tx_br.columns = ['Timestamp', 'TxFee'] # type: ignore
    
    return
tx_func()


def br_func():
    global br_api
    global extra
    br_api = requests.get(br_link)
    cleaned = br_api.json()
    br_d = []
    
    for x in cleaned:
        br_loop = [x['value']]
        br_d.append(br_loop)
    
    br = pd.DataFrame(br_d)
    br.columns = ['Bonded_Ratio'] # type: ignore
    tx_br['Bonded_Ratio'] = br
    timestamp = tx_br['Timestamp']
    tx_br['Date'] = pd.to_datetime(timestamp, unit='s')
    tx_br.set_index('Timestamp')
    
    extra = tx_br
    
    return
br_func()

def coin_func():
    global coin_d
    coin_api = requests.get(coin_link)
    cleaned = coin_api.json()
    temp = []
    temp1 = []
    
    for x in cleaned['market_caps']:
        mc_loop = [x[0], x[1]]
        temp.append(mc_loop)
    
    for x in cleaned['prices']:
        price_loop = [x[1]]
        temp1.append(price_loop)
    
    tempdf = pd.DataFrame(temp)
    temp1df = pd.DataFrame(temp1)
    tempdf['Price'] = temp1df
    
    tempdf.columns = ['Timestamp', 'Marketcap', 'Price'] # type: ignore
    timestamp = tempdf['Timestamp']
    tempdf['Datetime'] = pd.to_datetime(timestamp, unit='ms')
    tempdf.set_index('Datetime')
    
    coin_d = tempdf.resample('D', on='Datetime').max()
    coin_d.columns = ['Timestamp', 'Marketcap', 'Price', 'Del']  # type: ignore
    del coin_d['Del']
    
    return
coin_func()

def atom_func():
    tx = extra['TxFee']
    br = extra['Bonded_Ratio']
    coin_d['TxFee'] = tx.values
    coin_d['Bonded_Ratio'] = br.values

    coin_d.to_csv(atomcsv)
    df = pd.read_csv(atomcsv)
    df['FeeValue'] = df['Price'] * df['TxFee']
    df['AggValue'] = df['FeeValue'] / df['Marketcap']
    
    df.to_csv(atomcsv)
    
    return
atom_func()


c_atom = pd.read_csv(atomcsv)
new = c_atom.reset_index()
del new['Timestamp']
del new['Datetime']
pd.DataFrame(new)

mk = new['Marketcap']
pr = new['Price']
tx = new['TxFee']
br = new['Bonded_Ratio']
fv = new['FeeValue']

nf = []

def mkt():
    first = mk.iloc[0]
    last = mk.iloc[-1]
    calc = last / first -1
    mf = ['Marketcap_Yield']
    mf.append(calc)
    nf.append(mf)
    
    return

mkt()


def prc():
    first = pr.iloc[0]
    last = pr.iloc[-1]
    calc = last / first -1
    mf = ['Price_Yield']
    mf.append(calc)
    nf.append(mf)
    
    return

prc()

def txs():
    first = tx.iloc[0]
    last = tx.iloc[-1]
    calc = last / first -1
    mf = ['TX_Yield']
    mf.append(calc)
    nf.append(mf)
    
    return

txs()

def bnr():
    first =br.iloc[0]
    last = br.iloc[-1]
    calc = last / first -1
    mf = ['Bonded_Yield']
    mf.append(calc)
    nf.append(mf)
    
    return

bnr()

def fev():
    first =fv.iloc[0]
    last = fv.iloc[-1]
    calc = last / first -1
    mf = ['FeeValue_Yield']
    mf.append(calc)
    nf.append(mf)
    
    return
    
fev()

s_atom = pd.read_csv(atomcsv)
c1 = s_atom.describe()
c1.to_csv(s_atomcsv)

final = pd.DataFrame(nf)
final.columns = ['Metric', 'Yield'] # type: ignore
final.to_csv(c_atomcsv)