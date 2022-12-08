import pandas as pd
import requests


# 1669809600
# 1667304000

start = input("Please input the starting Timestamp here: ")
end = input("Please input the ending Timestamp here: ") 

link1 = 'https://api.cosmoscan.net/transfers/volume/agg?by=day&from='+ start + '&to=' + end
link2 = 'https://api.cosmoscan.net/delegations/volume/agg?by=day&from=' + start + '&to=' + end



def txvol():
    global cd1
    api = requests.get(link1)
    json = api.json()

    df = []

    for x in json:
        data = [x['time'], x['value']]
        df.append(data)

    cd1 = pd.DataFrame(df)
    cd1.columns = ['Timestamp', 'TX_Vol']  #type: ignore
    
    return


def delvol():
    global del_vol, cd2
    api = requests.get(link2)
    json = api.json()

    df = []

    for x in json:
        data = [x['time'], x['value']]
        df.append(data)

    cd2 = pd.DataFrame(df)
    cd2.columns = ['Timestamp', 'DEL_Vol']  #type: ignore
    del_vol = cd2['DEL_Vol']
    
    return


def concat():
    df = cd1
    df['DEL_Vol'] = del_vol
    df.columns = ['Timestamp', 'TX_Vol', 'DEL_Vol'] #type: ignore
    
    print(df)
    
    return


def main():
    txvol()
    delvol()
    concat()
    
    return

main()
    