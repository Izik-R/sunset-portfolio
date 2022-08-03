# %%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from matplotlib import rcParams
from matplotlib.dates import AutoDateFormatter, AutoDateLocator

df = pd.read_csv('Jan22_ATOM.csv')

Price = df['Price']
Date = df['Date']
Br = df['Bonded_Ratio']
Mkt = df['Marketcap']

#ndf = (date, price, br, mkt)

plt.style.use('grayscale')

rcParams['figure.figsize'] = 9,6


fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(Price, '--', linewidth=3, label='PriceUSD', color='g')
ax1.set_ylabel('Price USD', color='g')
ax2.plot(Br, linewidth=3, label='Bonded Ratio', color='b')
ax2.set_ylabel('Bonded Ratio', color='b')
plt.xlabel("Days")

# plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%m-%d'))
# plt.gca().xaxis.set_major_locator(dates.DayLocator(interval=5))
# #plt.twiny(Date, alpha=0)
# plt.gcf().autofmt_xdate()

plt.title('ATOM Price and Bonded Ratio: Jan 2022')
plt.grid(False)


