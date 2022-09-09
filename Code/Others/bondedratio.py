import requests
import csv
from requests.api import head

# Creating an input for the API link.
link = input("Enter Bonded Ratio link here: ")

# Housing all of my code into a function so I'm able to call said code in other files.
def br():
        
    url = link

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
# Calling the API, building the array, creating a dataset template, then pre-planning the headers or column names for my CSV file.
    response = requests.request("GET", url,headers=headers,data={})
    cleaned1 = response.json()
    dset = []
    csvheader = ['Timestamp','Bonded_Ratio']

# Grabbing the indexes from the array(s), and appending those to the dataset template.
    for x in cleaned1:
        listing1 = [x['time'],x['value']]
        dset.append(listing1)

# Creating a variable for the CSV title or name so I'm able to change it if need be (Spoiler, I don't yet).
    csvp = 'part3.csv'

# Creating the CSV file, adding the column titles I noted above, then adding the data from the API in a fully compose dataset.
    with open(csvp, 'w', encoding='UTF8', newline='') as f:
        writer= csv.writer(f)
        writer.writerow(csvheader)
        writer.writerows(dset)

# Quick update msg for visual aid in the terminal.
    print('Bonded Ratio API Complete')

# Best Pratice
    return







