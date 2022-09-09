import mktcappull as mccp
import csv
from requests.api import head
import requests

# Housing all of my code into a function so I'm able to call said code in other files.
def pcp():
    
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
# Calling the API from mktcappull.py, building the array, creating a dataset template, then pre-planning the headers or column names for my CSV file. 
# The titles are named in order of which is pulled first, and is added. Monthlypull.py will address this.
    response = requests.request("GET", mccp.link,headers=headers,data={})
    cleaned1 = response.json()
    dset = []
    csvheader = ['Prices']
    csvname = 'part2.csv'

# Grabbing the index from the array(s), and appending those to the dataset template.
    for x in cleaned1['prices']:
        listing = [x[1]]
        dset.append(listing)

# Creating the  additional CSV file, adding the column titles I noted above, then adding the data from the API in a fully composed dataset.
    with open(csvname, 'w', encoding='UTF8', newline='') as f:
        writer= csv.writer(f)
        writer.writerow(csvheader)
        writer.writerows(dset)
    
# Quick update msg for visual aid in the terminal.
    print('Price API Complete')
    
# Best Pratice 
    return




