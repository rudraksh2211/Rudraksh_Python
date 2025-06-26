import pandas as pd
df1 = pd.DataFrame({"Name":['RD','Sachin','ABC','XYZ'], "id":[1,2,3,4]})           #create first dataframe
print("\n dataframe 1:",df1)
df2 = pd.DataFrame({"Score":[100,200,300,400], "id":[1,5,3,6]})                       #create second dataframe
print("\n dataframe 2:",df2)

#inner merge.......
res1 = pd.merge(df1,df2, on="id", how="inner")
print("\n inner merge is:", res1)

#left join.....
res2 = pd.merge(df1,df2, on="id", how="left")
print("\n left join is:", res2)
# missing values :
#  Notice how ID=2 and ID=4 has NaN for Score (no match in df2)

#right join.....
res3 = pd.merge(df1,df2, on="id", how="right")
print("\n right join is:", res3)
# missing values :
#  Notice how ID=5 and ID=6 has NaN for name (no match in df1)

#index based join..........


# Create two DataFrames with index
dfl = pd.DataFrame({'Name': ['RD', 'Sachin', 'ABC']}, index=[1, 2, 3])
dfr = pd.DataFrame({'Score': [90, 85, 78]}, index=[2, 3, 4])

# Join on index
res = dfl.join(dfr, rsuffix='_right', lsuffix='_left')
print("Index-Based Join Result:", res)

# right or inner join by index based
res_inner = dfl.join(dfr, how='right')
print("Right Join Based on Index:", res_inner)
