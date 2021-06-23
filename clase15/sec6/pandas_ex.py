import pandas as pd

df = pd.read_csv('clase15/sec6/athlete_events.csv')

# print(df)

# print(df.describe())

# print(df.head())

# print(df.iloc[4])
# print(df.iloc[4]['Age'])

# print(df.iloc[0,1])
# print(df.iloc[0,2])
# print(df.iloc[0,3])

# print(df[['Name','Age','Team']][10:20])


# print(df[(df['Team']== 'Chile') & (df['Age'] > 25) & (df['Medal'] == 'Gold')][['Name','Age']])

# print(df[((df['Age'] == 32) | (df['Age'] == 31) ) & (df['Medal'] == 'Silver')][['Name','Age']])


grupos = df.groupby('Team')
print(grupos['Weight','Height','Age'].agg(['min','max','mean','count','sum']))

print(df[(df["Team"]== "Chile")][["Name","Age"]][2:10])