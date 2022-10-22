import pandas as pd

csvname = input("Enter CSV Title here: ")

df = pd.read_csv('Sept22_ATOM.csv')
c1 = df.describe()
c1.to_csv(csvname)

print('Done?')