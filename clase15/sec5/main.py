import pandas as pd

df = pd.read_csv('clase15/sec5/athlete_events.csv')

# print(df)

# print(df.describe())

print(df.head())
print()
print()
# print(df.iloc[8])
# print(df.iloc[20,6])

# print(df[['City','Year']][0:1])

# print(df[['City','Year','Team']].iloc[0,1])

# print(df['City'].unique())

# for city in df['City'].unique():
#     print(city)



# print(df[(df['Medal'] == 'Gold') & (df['Team'] == 'Chile') & (df['Age'] > 25)][['Name','Age','City','Year','Sport','Event']])


# print(df[((df['Event'] == "Tennis Men's Singles") & (df['Event'] == "Tennis Men's Doubles")) &   ((df['Medal'] == 'Gold') | (df['Medal'] == 'Silver') | (df['Medal'] == 'Bronze') )][['Name','Age','City','Year','Medal','Event']])

# print(df[((df['Event'] == "Tennis Men's Singles") & (df['Event'] == "Tennis Men's Doubles")) &   ((df['Medal'].fillna('None') != 'None')  )][['Name','Age','City','Year','Medal','Event']])

# grupos = df.groupby(['Season','Year'])

# print(grupos['Weight', 'Height','Age'].agg(['min','max','count','mean']))

# desde_1996 = df[df['Year']>=1996].groupby('Season')
# print(desde_1996['Weight', 'Height'].agg(['mean']))

grupos = df[(df['Year']>1999) & (df['Season']=='Summer') & (df['Medal'].fillna('None'))].groupby(['Year'])

print(grupos['Age','Weight'].agg(['min','max','mean']))


