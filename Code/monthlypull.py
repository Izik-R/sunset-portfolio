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

# Done! Terminal msg to signal said completion.
print('Mission Complete, Check the file')




