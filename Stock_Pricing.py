import pandas as pd

data = pd.read_csv('Google.csv')

#print(data)

columns = list(data.columns)

#print(columns)

date = data['Date']
high = data['High']
low = data['Low']

topfive = data.head()

print(topfive)

#print(low)
#print(high)

#found = data.loc[data['High'].str.contains("104.06")]
#print(found)
#print(data['Date'][0:2])

#print(data.shape)
#print(data.size)
#print(data.describe())




#plt.plot(date,high, colour = 'red', linestyle = '--')
#plt.plot(date,low, colour = 'green', linestyle = '--')

#plt.scatter(x = date, y = high,colour = 'red')

#Add Labels
#plt.xlabel('Date')
#plt.ylabel('High, $')
#plt.title('Date vs High Prices')


#plt.show()
