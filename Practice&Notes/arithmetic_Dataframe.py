import pandas as pd

dic={"A":[10,20,30,70],
     "B":[40,50,60,80]}
d=pd.DataFrame(dic)

print(d)
print(d+2)
print(d-2)
print(d*2)
print(d/2)
print(d**2)
print(d%2)
print(d//2)
d['C']=d['A']+d["B"]
print(d)

#with two dataframe
dic1={"A":[100,200,300],
     "B":[400,500,600]}
d1=pd.DataFrame(dic1,index=[1,2,3])
print(d1+d)
print(d1-d)
print(d1*d)
print(d1/d)
print(d1**d)
print(d1//d)
print(d1%d)

#NaN=Not a number

#dataframe concation
one=pd.DataFrame({"name":["A1","A2","A3","A4","A5"],"subject":["sub1","sub2","sub6","sub4","sub5"],"marks":[80,90,79,89,67]},index=[1,2,3,4,5])
two=pd.DataFrame({"name":["B1","B2","B3","B4","B5"],"subject":["sub2","sub1","sub3","sub5","sub6"],"marks":[83,91,76,83,62]},index=[1,2,3,4,5])
result=pd.concat([one,two],keys=['a','b'],ignore_index=True)
print(result)

#by column
result=pd.concat([one,two],axis=1)
print(result)

#merge
left=pd.DataFrame({"id":[1,2,3,4,5],"name":["A1","A2","A3","A4","A5"],"subject":["sub1","sub2","sub6","sub4","sub5"],"marks":[80,90,79,89,67]},index=[1,2,3,4,5])
right=pd.DataFrame({"id":[1,2,3,4,5],"name":["B1","B2","B3","B4","B5"],"subject":["sub2","sub1","sub3","sub5","sub6"],"marks":[83,91,76,83,62]},index=[1,2,3,4,5])
result=left.merge(right,on='subject')
print(result)
result=left.merge(right,on='id')
print(result)
result=left.merge(right,on=['id','subject'])
print(result)
result=left.merge(right,on='subject',how="left")
print(result)
result=left.merge(right,on='subject',how="right")
print(result)
result=left.merge(right,on='subject',how="inner")
print(result)
result=left.merge(right,on='subject',how="outer")
print(result)

#join
result=left.join(right,lsuffix='_left',rsuffix="_right")
print(result)

#pivote
df=pd.DataFrame({"Col1":range(12),"Col2":["A","A","A","B","B","B","C","C","C","D","D","D"],"date":pd.to_datetime(["2025-06-20","2025-06-21","2025-06-22"]*4)})
print(df)
pivoted=df.pivot(index="date",columns="Col2",values="Col1")
print(pivoted)

#povote by table
data={"Branch":["CS","DS","CS","DS","CS"],
      "Year":[1,2,2,1,1],
      "Student":[100,200,300,200,100]}
df=pd.DataFrame(data)
print(df)
pivot_df=df.pivot_table(
    values="Student",index="Branch",columns="Year",aggfunc="sum"
)
print(pivot_df)