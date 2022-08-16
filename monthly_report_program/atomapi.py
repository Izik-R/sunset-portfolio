import pandas as pd
import requests
import csv

# Grabbing or asking the user to input the API links (In API Info folder)
linkp = input("Enter Price and Marketcap API link: ")
linktx = input("Enter TXFee API link: ")
linkbr = input("Enter Bonded Ratio API link: ")

# Naming final CSV files
pcsvname = input("Enter Prices CSV file name here(Include .csv): ")
brcsvname = input("Enter Bonded Ratio CSV file name here(Include .csv): ")
txcsvname = input("Enter Transaction Fee CSV file name here(Include .csv): ")
finalcsv = input("Enter Final CSV File name here (Include .csv): ")

# Place holder names for CSV's so it's easier to stitch later on
p1 = 'blank1.csv'
p2 = 'blank2.csv'
p3 = 'blank3.csv'
p4 = 'blank4.csv'

# Getting the headers/config together for links
headers1 = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

headers2 = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

headers3 = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

headers4 = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Grabbing the data from each API link and converting it into a translatable format
responsep = requests.request("GET", linkp, headers=headers1,data={})
cleanedp = responsep.json()
pdset = []
pheader = ['Prices']

responsemc = requests.request("GET",linkp, headers=headers2,data={})
cleanedmc = responsemc.json()
mcdset = []
mcheader = ['Timestamp', 'Marketcap']

responsetx = requests.request("GET", linktx, headers=headers3,data={})
cleanedtx = responsetx.json()
txdset = []
txheader = ['Timestamp', 'TxFee']

responsebr = requests.request("GET", linkbr, headers=headers4,data={})
cleanedbr = responsebr.json()
brdset = []
brheader = ['Timestamp', 'Bonded_Ratio']

# Creating and formating each of the slightly organized data above into accual data sets
for x in cleanedp['prices']:
    listp = [x[1]]
    pdset.append(listp)
    
for x in cleanedmc['market_caps']:
    listmc = [x[0], x[1]]
    mcdset.append(listmc)
    
for x in cleanedtx:
    listtx = [x['time'], x['value']]
    txdset.append(listtx)
    
for x in cleanedbr:
    listbr = [x['time'], x['value']]
    brdset.append(listbr)
 
# Finalizing the starting CSV files with the placeholder names as this is not the final product   
with open(p1, 'w', encoding='UTF8', newline='') as f1:
    writer1=csv.writer(f1)
    writer1.writerow(pheader)
    writer1.writerows(pdset)
    print('Price Data Loaded')


with open(p2, 'w', encoding='UTF8', newline='') as f2:
    writer2=csv.writer(f2)
    writer2.writerow(mcheader)
    writer2.writerows(mcdset)
    print('Marketcap Data Loaded')
    

with open(p4, 'w', encoding='UTF8', newline='') as f4:
    writer4=csv.writer(f4)
    writer4.writerow(txheader)
    writer4.writerows(txdset)
    print('TxFees Data Loaded')


with open(p3, 'w', encoding='UTF8', newline='') as f3:
    writer3=csv.writer(f3)
    writer3.writerow(brheader)
    writer3.writerows(brdset)
    print('Bonded Ratio Data Loaded')

# Update notification for visualation and troubleshooting. Makes it easier to find errors.   
print('Loading next steps...')

# Loading in the placeholder CSV files
dfp = pd.read_csv('blank1.csv')
dfmc = pd.read_csv('blank2.csv')
dftx = pd.read_csv('blank4.csv')
dfbr = pd.read_csv('blank3.csv')

# Identifying the timestamps in the data sets so I can convert them to readable dates later on
ts_dfmc = dfmc['Timestamp']
ts_dftx = dftx['Timestamp']
ts_dfbr = dfbr['Timestamp']

# Converting timestamps to date/datetime
dfmc['Date'] = pd.to_datetime(ts_dfmc, unit='ms')
dftx['Date'] = pd.to_datetime(ts_dftx, unit='s')
dfbr['Date'] = pd.to_datetime(ts_dfbr, unit='s')

# Adding Prices to the Marketcap file as I isolated that originally
dfmc['Price'] = dfp['Prices']

# Finalizing first step of the CSV files so I given I may not want all of the data at once later on
dfmc.to_csv(pcsvname)
dftx.to_csv(txcsvname)
dfbr.to_csv(brcsvname)

# Another notification for error troubleshooting
print('Payload processed. Stitching final CSV')

# Loading in finalized CSV files to make a final report
df1 = pd.read_csv(pcsvname)
df2 = pd.read_csv(txcsvname)
df3 = pd.read_csv(brcsvname)

# Setting the index for as the date so I can convert the hourly price/mktcap data into daily and ensure continuity between the data sets
df1.set_index('Date')
df2.set_index('Date')
df3.set_index('Date')

# Converting hourly data into daily (Making sure its the highest point of the day)
df1['Date'] = pd.to_datetime(df1['Date'])
cdf1 = df1.resample('D', on = 'Date').max()

# Isolating metrics from other columns to stitch them in later on
txfee = df2['TxFee']
br = df3['Bonded_Ratio']
price = df1['Price']

# Stitching in said datasets
cdf1['TxFee'] = txfee.values
cdf1['Bonded_Ratio'] = br.values

# Finalizing CSV part 1 for easier editing
cdf1.to_csv(finalcsv)

# Reloading CSV to make some edits and metrics
df = pd.read_csv(finalcsv)

# Identifying column names and removing a dupe
df.columns = ['Date', 'Index', 'Timestamp', 'Marketcap', 'Datetime', 'Price', 'TxFee', 'Bonded Ratio']
del df['Datetime']

# Making a calculating USD value of Tx fees, and the percentage of fees vs marketcap
df['FeeValue'] = df['Price'] * df['TxFee']
df['AggValue'] = df['FeeValue'] / df['Marketcap']

# Final, Final CSV
df.to_csv(finalcsv)

# Done! Mission accomplished!
print('Final CSV Complete!')




