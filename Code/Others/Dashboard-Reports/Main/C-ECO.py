import pandas as pd


csvname = input("Enter Calc CSV name Here: ")
df = pd.read_csv('D_Eco_Oct22.csv')

new = df.reset_index()

del new['Timestamp']
del new['Date']
del new['Date.1']

pd.DataFrame(new)

first = new.iloc[0]
last = new.iloc[-1]

calc = last / first - 1

pd.DataFrame(calc)
calc.to_csv(csvname)


print("Finished the Compute..")
