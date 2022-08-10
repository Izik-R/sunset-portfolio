# %%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from matplotlib import rcParams

# Pulling CSV file from directory
df = pd.read_csv('Jan22_ATOM.csv')

# Creating variables for each data point
Price = df['Price']
Br = df['Bonded_Ratio']

# Choosing a visual format for the chart
plt.style.use('grayscale')

# Resizing the chart so it's to my liking
rcParams['figure.figsize'] = 9,6

# Creating, naming, and labeling the plot/chart
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(Price, '--', linewidth=3, label='PriceUSD', color='g')
ax1.set_ylabel('Price USD', color='g')
ax1.set_xlabel('Day of Month')
ax2.plot(Br, linewidth=3, label='Bonded Ratio', color='b')
ax2.set_ylabel('Bonded Ratio', color='b')
plt.title('ATOM Price and Bonded Ratio: Jan 2022')
plt.grid(False)


