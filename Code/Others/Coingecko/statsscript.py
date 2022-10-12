import pandas as pd


csvname = input("Enter Stats CSV Name here: ")

df = pd.read_csv('D_Eco_Sept22.csv')
c1 = df.describe()


c1.to_csv(csvname)
print('Seems to be complete!')


