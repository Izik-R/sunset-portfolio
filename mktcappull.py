import requests
import csv
from requests.api import head

# Creating an input for the API link.
link = input("Enter prices link here: ")

# Housing all of my code into a function so I'm able to call said code in other files.
def mcp():
    url = link

    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
# Calling the API, building the array, creating a dataset template, then pre-planning the headers or column names for my CSV file. 
# Additionally, creating the CSV's title that I can call later on.
    response = requests.request("GET", url,headers=headers,data={})
    cleaned1 = response.json()
    dset = []
    csvheader = ['Timestamp','Marketcap']
    csvname = 'part1.csv'

# Grabbing the indexes from the array(s), and appending those to the dataset template.
    for x in cleaned1['market_caps']:
        listing = [x[0], x[1]]
        dset.append(listing)

# Creating the CSV file, adding the column titles I noted above, then adding the data from the API in a fully composed dataset.
    with open(csvname, 'w', encoding='UTF8', newline='') as f:
        writer= csv.writer(f)
        writer.writerow(csvheader)
        writer.writerows(dset)

# Quick update msg for visual aid in the terminal.
    print('Market Cap API Complete')

# Best Pratice
    return


