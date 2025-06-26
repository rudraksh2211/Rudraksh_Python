import pandas as pd 

df=pd.DataFrame(['$4000*','$4000 Hello I am RD'],columns=['p'])
print(df)

df['p']=df['p'].str.replace(r"\D+","",regex=True).astype('int')
print(df)

#finding number
df['numbers'] = df['p'].str.extract(r"(\d+)")
print(df)

#remove special symbol
df['cleaned'] = df['p'].str.replace(r"[^\w\s]", "", regex=True)
print(df)