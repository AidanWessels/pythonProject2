import pandas as pd

data = pd.read_csv('Google.csv')

print(data['Date'][0:2])

print(data.shape)
print(data.size)
#print(data.describe())



