import requests
import pandas as pd
import datetime

# headers = {
#     'Accept': 'application/json',
#     'Content-Type': 'application/json'
# }

link = f'https://api-osmosis.imperator.co/apr/v2/all'


url = requests.get(link)
next = url.json()
main = []

def pool1():
    df = []
    d1 = next[0]['apr_list'][1]['apr_1d']
    d7 = next[0]['apr_list'][1]['apr_7d']
    d14 = next[0]['apr_list'][1]['apr_14d']
    spr = next[0]['apr_list'][1]['apr_superfluid']
    df.append(1)
    df.append('ATOM/OSMO')
    df.append(d1)
    df.append(d7)
    df.append(d14)
    df.append(spr)
    main.append(df)
    
    return
pool1()

def pool10():
    df = []
    d1 = next[1]['apr_list'][0]['apr_1d']
    d7 = next[1]['apr_list'][0]['apr_7d']
    d14 = next[1]['apr_list'][0]['apr_14d']
    spr = next[1]['apr_list'][0]['apr_superfluid']
    df.append(10)
    df.append('ATOM/CRO')
    df.append(d1)
    df.append(d7)
    df.append(d14)
    df.append(spr)
    main.append(df)
    
    return
pool10()


def pool497():
    df = []
    d1 = next[10]['apr_list'][0]['apr_1d']
    d7 = next[10]['apr_list'][0]['apr_7d']
    d14 = next[10]['apr_list'][0]['apr_14d']
    spr = next[10]['apr_list'][0]['apr_superfluid']
    df.append(497)
    df.append('JUNO/OSMO')
    df.append(d1)
    df.append(d7)
    df.append(d14)
    df.append(spr)
    main.append(df)
    
    return
pool497()


def pool604():
    df = []
    d1 = next[16]['apr_list'][0]['apr_1d']
    d7 = next[16]['apr_list'][0]['apr_7d']
    d14 = next[16]['apr_list'][0]['apr_14d']
    spr = next[16]['apr_list'][0]['apr_superfluid']
    df.append(604)
    df.append('STARS/OSMO')
    df.append(d1)
    df.append(d7)
    df.append(d14)
    df.append(spr)
    main.append(df)
    
    return
pool604()


def pool674():
    df = []
    d1 = next[47]['apr_list'][0]['apr_1d']
    d7 = next[47]['apr_list'][0]['apr_7d']
    d14 = next[47]['apr_list'][0]['apr_14d']
    spr = next[47]['apr_list'][0]['apr_superfluid']
    df.append(674)
    df.append('DAI/OSMO')
    df.append(d1)
    df.append(d7)
    df.append(d14)
    df.append(spr)
    main.append(df)
    
    return
pool674()

def pool678():
    df = []
    d1 = next[48]['apr_list'][0]['apr_1d']
    d7 = next[48]['apr_list'][0]['apr_7d']
    d14 = next[48]['apr_list'][0]['apr_14d']
    spr = next[48]['apr_list'][0]['apr_superfluid']
    df.append(678)
    df.append('USDC/OSMO')
    df.append(d1)
    df.append(d7)
    df.append(d14)
    df.append(spr)
    main.append(df)
    
    return
pool678()

def pool712():
    df = []
    d1 = next[51]['apr_list'][0]['apr_1d']
    d7 = next[51]['apr_list'][0]['apr_7d']
    d14 = next[51]['apr_list'][0]['apr_14d']
    spr = next[51]['apr_list'][0]['apr_superfluid']
    df.append(712)
    df.append('WBTC/OSMO')
    df.append(d1)
    df.append(d7)
    df.append(d14)
    df.append(spr)
    main.append(df)
    
    return
pool712()


def pool812():
    df = []
    d1 = next[70]['apr_list'][0]['apr_1d']
    d7 = next[70]['apr_list'][0]['apr_7d']
    d14 = next[70]['apr_list'][0]['apr_14d']
    spr = next[70]['apr_list'][0]['apr_superfluid']
    df.append(812)
    df.append('AXL/OSMO')
    df.append(d1)
    df.append(d7)
    df.append(d14)
    df.append(spr)
    main.append(df)
    
    return
pool812()


clean = pd.DataFrame(main)
clean.columns = ['ID', 'Token(s)', '1D', '7D', '14D', 'SPRFL']
csvname = "apr-" + datetime.datetime.today().strftime('%Y-%m-%d') + ".csv"
clean.to_csv(csvname)

