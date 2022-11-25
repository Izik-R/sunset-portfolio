import pandas as pd

jan = pd.read_csv('E:\Projects\CodeData\Monthly_Reports\Jan22_ATOM.csv')
feb = pd.read_csv('E:\Projects\CodeData\Monthly_Reports\Feb22_ATOM.csv')
march = pd.read_csv('E:\Projects\CodeData\Monthly_Reports\March22_ATOM.csv')
april = pd.read_csv('E:\Projects\CodeData\Monthly_Reports\April22_ATOM.csv')
may = pd.read_csv('E:\Projects\CodeData\Monthly_Reports\May22_ATOM.csv')
june = pd.read_csv('E:\Projects\CodeData\Monthly_Reports\June22_ATOM.csv')
july = pd.read_csv('E:\Projects\CodeData\Monthly_Reports\July22_ATOM.csv')
aug = pd.read_csv('E:\Projects\CodeData\Monthly_Reports\Aug22_ATOM.csv')

df = jan.append(feb)
df1 = df.append(march)
df2 = df1.append(april)
df3 = df2.append(may)
df4 = df3.append(june)
df5 = df4.append(july)
ytd = df5.append(aug)

ytd.to_csv('YTD.csv')
print('Donzo!')

