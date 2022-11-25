import pandas as pd

df = pd.read_csv('Oct22_ATOM.csv')

new = df.reset_index()

del new['Timestamp']
del new['Date']

pd.DataFrame(new)

## ,Date,Index,Timestamp,Marketcap,Price,TxFee,Bonded Ratio,FeeValue,AggValue

mk = new['Marketcap']
pr = new['Price']
tx = new['TxFee']
br = new['Bonded Ratio']
fv = new['FeeValue']

nf = []

def mkt():
    first = mk.iloc[0]
    last = mk.iloc[-1]
    calc = last / first -1
    mf = ['Marketcap_Yield']
    mf.append(calc)
    nf.append(mf)
    
    return

mkt()


def prc():
    first = pr.iloc[0]
    last = pr.iloc[-1]
    calc = last / first -1
    mf = ['Price_Yield']
    mf.append(calc)
    nf.append(mf)
    
    return

prc()

def txs():
    first = tx.iloc[0]
    last = tx.iloc[-1]
    calc = last / first -1
    mf = ['TX_Yield']
    mf.append(calc)
    nf.append(mf)
    
    return

txs()

def bnr():
    first =br.iloc[0]
    last = br.iloc[-1]
    calc = last / first -1
    mf = ['Bonded_Yield']
    mf.append(calc)
    nf.append(mf)
    
    return

bnr()

def fev():
    first =fv.iloc[0]
    last = fv.iloc[-1]
    calc = last / first -1
    mf = ['FeeValue_Yield']
    mf.append(calc)
    nf.append(mf)
    
    return
    
fev()

csvname = input("Enter CSV Title Here: ")
final = pd.DataFrame(nf)
final.columns = ['Metric', 'Yield']
final.to_csv(csvname)

print(final)
print("Done!")




