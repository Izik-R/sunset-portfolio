from pycoingecko import CoinGeckoAPI
import pandas as pd
import csv

cg = CoinGeckoAPI()

csv1 = input('Type your Daily CSV name here: ')
csv2 = input('Type your Hourly CSV name here: ')

start = 1656658800
stop = 1659250800


cosmos = cg.get_coin_market_chart_range_by_id(id='cosmos', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
osmosis = cg.get_coin_market_chart_range_by_id(id='osmosis', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
juno = cg.get_coin_market_chart_range_by_id(id='juno-network', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
rowan = cg.get_coin_market_chart_range_by_id(id='sifchain', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
sg = cg.get_coin_market_chart_range_by_id(id='stargaze', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
evmos = cg.get_coin_market_chart_range_by_id(id='evmos', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
akash = cg.get_coin_market_chart_range_by_id(id='akash-network', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
secret = cg.get_coin_market_chart_range_by_id(id='secret', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
kava = cg.get_coin_market_chart_range_by_id(id='kava', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
eth = cg.get_coin_market_chart_range_by_id(id='ethereum', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)
btc = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='usd', from_timestamp=start, to_timestamp=stop, include_market_cap=True)

######################################################################

# Cosmos Dataframe
p_atom = []
for x in cosmos['prices']:
    patom = [x[0], x[1]]
    p_atom.append(patom)
    main = pd.DataFrame(p_atom, columns=['Timestamp', 'P_ATOM'])

m_atom = []
for x in cosmos['market_caps']:
    matom = [x[1]]
    m_atom.append(matom)
    df_atom = pd.DataFrame(m_atom, columns=['M_ATOM'])
    main['M_ATOM'] = df_atom
######################################################################

# Osmosis Dataframe
p_osmo = []
for x in osmosis['prices']:
    posmo = [x[1]]
    p_osmo.append(posmo)
    osmo = pd.DataFrame(p_osmo, columns=['P_OSMO'])

m_osmo = []
for x in osmosis['market_caps']:
    mosmo = [x[1]]
    m_osmo.append(mosmo)
    df_osmo = pd.DataFrame(m_osmo, columns=['M_OSMO'])
    main['P_OSMO'] = osmo
    main['M_OSMO'] = df_osmo
######################################################################

# Juno Dataframe
p_juno = []
for x in juno['prices']:
    pjuno = [x[1]]
    p_juno.append(pjuno)
    jno = pd.DataFrame(p_juno, columns=['P_JUNO'])
    
m_juno = []
for x in juno['market_caps']:
    mjuno = [x[1]]
    m_juno.append(mjuno)
    df_jno = pd.DataFrame(m_juno, columns=['M_JUNO'])
    main['P_JUNO'] = jno
    main['M_JUNO'] = df_jno
######################################################################

# Sifchain Dataframe
p_rowan = []
for x in rowan['prices']:
    prowan = [x[1]]
    p_rowan.append(prowan)
    rwn = pd.DataFrame(p_rowan, columns=['P_ROWAN'])

m_rowan = []    
for x in rowan['market_caps']:
    mrowan = [x[1]]
    m_rowan.append(mrowan)
    df_rwn = pd.DataFrame(m_rowan, columns=['M_ROWAN'])
    main['P_ROWAN'] = rwn
    main['M_ROWAN'] = df_rwn
######################################################################   

# Stargaze Dataframe
p_sg = []
for x in sg['prices']:
    psg = [x[1]]
    p_sg.append(psg)
    strgz = pd.DataFrame(p_sg, columns=['P_STARS'])
    
m_sg = []
for x in sg['market_caps']:
    msg = [x[1]]
    m_sg.append(msg)
    df_strgz = pd.DataFrame(m_sg, columns=['M_STARS'])
    main['P_STARS'] = strgz
    main['M_STARS'] = df_strgz
######################################################################    

# Evmos DataFrame
p_ev = []
for x in evmos['prices']:
    pev = [x[1]]
    p_ev.append(pev)
    evm = pd.DataFrame(p_ev, columns=['P_EVMOS'])
    
m_ev = []
for x in evmos['market_caps']:
    mev = [x[1]]
    m_ev.append(mev)
    df_evm = pd.DataFrame(m_ev, columns=['M_EVMOS'])
    main['P_EVMOS'] = evm
    main['M_EVMOS'] = df_evm
######################################################################

# Akash DataFrame
p_aks = []
for x in akash['prices']:
    paks = [x[1]]
    p_aks.append(paks)
    aks = pd.DataFrame(p_aks, columns=['P_AKASH'])

m_aks = []
for x in akash['market_caps']:
    maks = [x[1]]
    m_aks.append(maks)
    df_aks = pd.DataFrame(m_aks, columns=['M_AKASH'])
    main['P_AKASH'] = aks
    main['M_AKASH'] = df_aks
######################################################################

# Secret DataFrame
p_scrt = []
for x in secret['prices']:
    pscrt = [x[1]]
    p_scrt.append(pscrt)
    secrt = pd.DataFrame(p_scrt, columns=['P_SECRET'])
    
m_scrt = []
for x in secret['market_caps']:
    mscrt = [x[1]]
    m_scrt.append(mscrt)
    df_secrt = pd.DataFrame(m_scrt, columns=['M_SECRET'])
    main['P_SECRET'] = secrt
    main['M_SECRET'] = df_secrt
######################################################################

# Kava DataFrame
p_kv = []
for x in kava['prices']:
    pkv = [x[1]]
    p_kv.append(pkv)
    kva = pd.DataFrame(p_kv, columns=['P_KAVA'])

m_kv = []
for x in kava['market_caps']:
    mkv = [x[1]]
    m_kv.append(mkv)
    df_kva = pd.DataFrame(m_kv, columns=['M_KAVA'])
    main['P_KAVA'] = kva
    main['M_KAVA'] = df_kva
######################################################################

# ETH DataFrame
p_eth = []
for x in eth['prices']:
    peth = [x[1]]
    p_eth.append(peth)
    ethr = pd.DataFrame(p_eth, columns=['P_ETH'])

m_eth =[]
for x in eth['market_caps']:
    meth = [x[1]]
    m_eth.append(meth)
    df_ethr = pd.DataFrame(m_eth, columns=['M_ETH'])
    main['P_ETH'] = ethr
    main['M_ETH'] = df_ethr
######################################################################

# BTC DataFrame
p_bc = []
for x in btc['prices']:
    pbc = [x[1]]
    p_bc.append(pbc)
    bit = pd.DataFrame(p_bc, columns=['P_BTC'])
    
m_bc = []
for x in btc['market_caps']:
    mbc = [x[1]]
    m_bc.append(mbc)
    df_bit = pd.DataFrame(m_bc, columns=['M_BTC'])
    main['P_BTC'] = bit
    main['M_BTC'] = df_bit
######################################################################

dt = main['Timestamp']
date = pd.to_datetime(dt, unit='ms')
main['Date'] = date
final = main.resample('D', on='Date').max()

final.to_csv(csv1)
main.to_csv(csv2)

print('I think its done? I hope!')
    
    
    


