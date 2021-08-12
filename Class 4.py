import pandas as pd

data = pd.read_csv('netflix_titles.csv')

#print(data)

#print(data.isnull())

#print(data.isnull().sum())

#clean_data = data.dropna(axis=0) --Rows = 0, Columns = 1

#print(data.shape,clean_data.shape)

#cleaned_data = data.fillna("aidan")
#cleaned_data = data.fillna(data.mean)
#cleaned_data = data.fillna(method="bfill") #ffill following value bfill
#cleaned_data = data.fillna(method="bfill").fillna(method="ffill") #like a case statement - where bfill fails use ffill
#cleaned_data = data.fillna(method="bfill",axis=1).fillna(method="ffill",axis=1) #like a case statement - where bfill fails use ffill
#search fillna - method Google will give many soluation

#print(cleaned_data.isnull().sum())

#print(data["cast"])

cleaned_data = data.drop_duplicates(subset=["cast"])

print(data.shape,cleaned_data.shape)

#try this with missing data sets from Kaggle