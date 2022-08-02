import pricepull as ppcp
import mktcappull as mccp
import bondedratio as brr
import pandas as pd
import csv

# Calling in the troops of files that previously made CSV files.
# Intentially created these in their own respective CSV's so I can edit them individually
mccp.mcp()
ppcp.pcp()
brr.br()

# Asking the user to name each of the CSV files in the terminal
price_csvname = input("Enter prices CSV file name here: ")
bonded_csvname = input("Enter Bonded Ratio CSV file name here: ")

# Reading/Importing each of the CSV files we've created so far.
dfm = pd.read_csv('part1.csv')
dfp = pd.read_csv('part2.csv')
df = pd.read_csv('part3.csv')

# Creating variables for the timestamps as I would like the dates to eventually be visible
timestamp1 = df['Timestamp']
timestamp = dfm['Timestamp']

# Adding a column that will show the date vs a timestamp
df['Date'] = pd.to_datetime(timestamp1, unit='s')

# Finalizing the Bonded Ratio CSV file
df.to_csv(bonded_csvname)

# Creating a variable to isolate the price data
price = dfp['Prices']

# Adding a column that will show the date vs a timestamp
dfm['Price'] = price
dfm['Date'] = pd.to_datetime(timestamp, unit='ms')

# Finalizing the Bonded Ratio CSV file
dfm.to_csv(price_csvname)

# Recalling the CSV's we've made so far
df1 = pd.read_csv(bonded_csvname)
df2 = pd.read_csv(price_csvname)

br = df1['Bonded_Ratio']
hdate = df2['Date']
timestamp = df2['Timestamp']

# Creating a metric for the circulating supply
df2['Circ_Supply'] = df2['Marketcap'] / df2['Price']

# Renaming all the columns to ensure continuity
df1.columns = ['Index','Timestamp','Bonded_Ratio','Date']
df2.columns = ['Index','Timestamp','Marketcap','Price','Date','Circ_Supply']

# Setting index in the dataset so I can format later
df1.set_index('Date')
df2.set_index('Date')

# Ensuring python is aware of the date format
df2['Date'] = pd.to_datetime(df2['Date'])

# Ordering data by 'D' (Daily) instead of hourly
cdf2 = df2.resample('D', on = 'Date').max()

# Adding in the bonded ratio data from the other CSV file
cdf2['Bonded_Ratio'] = br.values

# Asking the user for the name of 3rd and final CSV file
name = input("Final CSV title: ")

# Finalizing the CSV :)
cdf2.to_csv(name)

# Done! Terminal msg to signal said completion.
print('Mission Complete, Check the file')

