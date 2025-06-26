import pandas as pd
# Create three DataFrames
dfA = pd.DataFrame({'ID': [1, 2], 'Name': ['RD', 'Sachin']})
dfB = pd.DataFrame({'ID': [3, 4], 'Name': ['ABC', 'XYZ']})
dfC = pd.DataFrame({'ID': [2, 3, 4], 'Score': [95, 80, 88]})

# Concatenate dfA and dfB vertically
concat_df = pd.concat([dfA, dfB], ignore_index=True)
print("\n Concatenated dfA and dfB:\n", concat_df)

# Merge with dfC on 'ID'
merged = pd.merge(concat_df, dfC, on='ID', how='left')
print("\n Merged with dfC:\n", merged)


# difference between df.join and pd.merge:

# ..df.join Joins on the index by default and pd.merge Joins on common columns by default
#..df.join Index-to-index join and pd.merge Column-to-column join using like on="column name"
#..df.join limited keys support and pd.merge fully supports multiple keys (like, on=['A','B'])