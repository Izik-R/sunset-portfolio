import sqlalchemy as sq
import pandas as pd
import requests
import datetime

# Database details to create a 'Database URL'
hostname = "#######"
dbname="#####"
uname="#####"
pwd="#####"


# Creating the engine/query method to the MySQL server
alch_db = sq.create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))


# API Link used to connect to the database
link = f'https://api-osmosis.imperator.co/apr/v2/all'


# Creating variables, designated the type of API.... 
# ...Then creating a blank list to later append data to
url = requests.get(link)
next = url.json()
main = []

# Functions to run specific index positions due to the API not being normalized
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

# Creating a Dataframe, naming the columns, filling blank values with '0'...
# ....creating a column for todays date, then appending it to my MySQL table
clean = pd.DataFrame(main)
clean.columns = ['ID', 'Token(s)', '1D', '7D', '14D', 'SPRFL']
final = clean.fillna(value=0)
final['Date'] = datetime.datetime.today().strftime('%Y-%m-%d')

final.to_sql('pools', alch_db, if_exists='append')