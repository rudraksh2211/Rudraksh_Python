#pandas liberary
import pandas

#series
a = [10, 20, 30, 40]
s = pandas.Series(a,index=["a","b","c","d"])
print(s["a"])
print(type(s))

qmark={"day1":420,"day2":410,"day3":390}
q=pandas.Series(qmark,dtype=float,index=["day1","day2"])
print(q)
print(type(q.tolist()))

#dataframe
dic={"num":[10,20,30],
     "alpha":["a","b","c"]}
df=pandas.DataFrame(dic)
print(df)
print(df.loc[[0,2]])
print(df.columns)
df.columns=["Number","Variable"]
print(df)

#data slicing
print(df.iloc[0:2,:])
df.iloc[0:2,0]=["x","y"]
print(df)

#propping row
print(df[df["Number"]!=10])
print(df.drop(df.index[0:2]))