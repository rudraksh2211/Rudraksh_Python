import pandas as pd
pd.options.display.max_rows=10
df=pd.read_csv('customer.csv')
#data cleaning
new_df=df.dropna()
print(new_df)
#data analysis
print(new_df.head(10))

print(new_df.info())

print(new_df.shape)

print(new_df.columns)

print(new_df.describe())

print(new_df['Country'])

print(new_df.groupby('Country')['Index'].count())

print(new_df['Country'].value_counts())
