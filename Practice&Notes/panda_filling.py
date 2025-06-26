import pandas as pd
import numpy as np

data={"col1":[3,np.nan,np.nan,2],"col2":[1.0,pd.NA,pd.NA,2.0]}
df=pd.DataFrame(data)
print(df)
print(df.fillna('-'))

#forward fill and backword fills
df=pd.DataFrame([[9,-3,2],[7,5,-9],[-8,-5,0]],index=['a','c','d'],columns=['one','two','three'])
print(df)
df=df.reindex(['a','b','c','d','e'])
print(df)
print(df.fillna('-'))
print(df.ffill())
print(df.bfill())

df=df.reindex(['a','b','d','e','f'])
print(df.ffill(limit=1))

#replace 
print(df.replace({9:2,-3:9}))
print(df.replace({9:2,-3:9}).ffill())

#regular expression
df=pd.DataFrame(['$4000*','$4000 Hello I am RD'],columns=['p'])
print(df)
df['p']=df['p'].str.replace(r"\D","",regex=True).astype('int')
print(df)

#groupby
data={'Category':['A','B','A','C','A','B'],'value':[10,20,12,13,14,20]}
df=pd.DataFrame(data)
print(df.groupby('Category')['value'].sum())
print(df.groupby('Category')['value'].min())
print(df.groupby('Category')['value'].max())
print(df.groupby('Category')['value'].count())
print(df.groupby('Category')['value'].agg("sum"))

data={'Category':['A','B','A','C','A','B'],"Subcategory":['X','Y','Z','X','X','Y'],'value':[10,20,12,13,14,20]}
df=pd.DataFrame(data)
print(df.groupby(['Category','Subcategory'])['value'].sum())

#sorting
df=pd.DataFrame({'name':['ABC','XYZ','PQR'],'age':[12,23,34]})
print(df.sort_values(by='name'))
print(df.sort_values(by='age'))
print(df.sort_values(by='age',ascending=False))
df.sort_values(by='age',inplace=True)
print(df)
data={'Category':['A','B','A','C','A','B'],"Subcategory":['X','Y','Z','X','X','Y'],'value':[10,20,12,13,14,20]}
df=pd.DataFrame(data)
print(df.sort_values(by=['Category','Subcategory'],ascending=[True,False]))

#by indexing
df=pd.DataFrame({'name':['ABC','XYZ','PQR'],'age':[12,23,34]},index=[2,1,3])
print(df.sort_index())

#by column lable
print(df.sort_index(axis=1).sort_index())

#date functionality
print(pd.date_range('6/1/2025',periods=10))