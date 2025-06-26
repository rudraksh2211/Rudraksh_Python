#csv file
import pandas as pd
pd.options.display.max_rows=200
df=pd.read_csv('customers-100.csv')

#data cleaning

"""
print(df.head(10))
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
"""
#basic analysis
print(df['Country'])
#all operation of dataframe
print(df.groupby('Country')['Index'].count())
print(df['Country'].value_counts())

#json file