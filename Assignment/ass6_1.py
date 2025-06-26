# ************************************ Assignment 6 ***********************************************

import pandas as pd
# question 1 ********************
data = {'dates': pd.to_datetime(['2025-04-22','2025-06-21','2025-06-22','2025-02-20','2025-06-22']), 'col1': ['course1','course2','course3','course4','course5']}
df = pd.DataFrame(data)
#print(df)
ts = pd.Series(df['col1'].values, index=df['dates'],)
print(ts)


