import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv('Google.csv')

low = data['Low']
date = data['Date']

topfive = data.head()

#print(topfive)

lowfive = topfive['Low']
highfive = topfive['High']
datefive = topfive['Date']

print(highfive)

#plt.scatter(x = datefive, y = lowfive,color = 'red')

#plt.plot(datefive,lowfive, color = 'green', linestyle = '--')

plt.hist(x=lowfive, bins = 6, alpha = 0.5, label = "Low Prices")
plt.hist(x=highfive, bins = 6, alpha = 0.5, label = "High Prices")

plt.legend()
plt.show()