import pandas as pd
#part(a)...........
df = pd.DataFrame({'id': [1, 2], 'name': ['RD', 'Sachin']})

# Using iterrows()
for index, row in df.iterrows():
    print(f"Row {index}: id={row['id']}, name={row['name']}")

# Using itertuples()
for row in df.itertuples():
    print(f"id={row.id}, name={row.name}")

# part(b)...........
df = pd.DataFrame({'id': [1, 2, 3], 'marks': [90, 70, 85]})

# Select rows where marks > 80
high_marks = df[df['marks'] > 80]
print(high_marks)

# part(c)...........
df = pd.DataFrame({'id': [1, 2, 3], 'name': ['RD', 'Sachin', 'Shanker']})

# Select the second row (index 1)
print(df.iloc[1])
print(df.iloc[1, 0])          #print element of second(index 1) row and first(index 0) column

# part(d)...........
df = pd.DataFrame({'id': [1, 2, 3], 'name': ['RD', 'Sachin', 'Shanker']})

# Show first 2 rows of 'name' column
df_row = df.iloc[0:2, 1]
print(df_row)            #print(df.loc['name']) is incorrect

#part(e)...........
df = pd.DataFrame({'id': [1, 2, 3], 'marks': [90, 60, 75]})
# Drop rows which contain marks = 75
df = df[df['marks'] != 75]
print(df)


#part(f)...........
df = pd.DataFrame({'id': [1, 2], 'name': ['RD', 'Sachin']})

# New row to insert
new_row = pd.DataFrame({'id': [3], 'name': ['Shanker']})

# Insert at position 1
df = pd.concat([df.iloc[:1], new_row, df.iloc[1:]]).reset_index(drop=True)
print(df)

#part(g)...........
df = pd.DataFrame({'id': [1, 2], 'name': ['RD', 'Sachin']})

# Convert each row to a list
row_list = df.values.tolist()
print(row_list)