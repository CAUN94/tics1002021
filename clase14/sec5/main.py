import pandas as pd

df = pd.read_csv('/Users/cristobalugarte/code/tics100/clase14/sec5/athlete_events.csv')

print('All')
print(df)
print()

print('Describe')
print(df.describe())
print()

print('Head')
print(df.head(10))
print()

print('Iloc 0')
print(df.iloc[0])
print()

print('Iloc 200')
print(df.iloc[200])
print()

print('Iloc [0,1]')
print(df.iloc[0,1])
print()

print('Names')
print(df['Name'])
print()

print('Ages')
print(df['Age'])
print()

print('Names 0')
print(df['Name'][0])
print()

print('Names 100 al 119')
print(df['Name'][100:120])
print()

print('Names Age Team')
print(df[['Name','Age','Team']])
print()

print('Names Age Team 20 al 30')
print(df[['Name','Age','Team']][20:31])
print()

print('Names Age Team del compadre 10')
print(df[['Name','Age','Team']].iloc[10])
print()

print('Names')
print(df['Name'].unique())
# for name in df['Name'].unique():
#     print(name)
print()


print('Years')
print(df['Year'].unique())
# for year in df['Year'].unique():
#     print(year)
print()

print('Medallas de Oro')
golde_medals = df[df['Medal'] == 'Gold']
golden_medals_name = golde_medals['Name']
golden_medals_name_no_repeat = golden_medals_name.unique()
# print(list(golden_medals_name_no_repeat))
print(golden_medals_name_no_repeat)
print()

print('Medallaro')
medals = df[(df['Medal'] == 'Gold') | (df['Medal'] == 'Silver') | (df['Medal'] == 'Bronze')]
medals_name = medals['Name']
medals_name_no_repeat = medals_name.unique()
# print(list(golden_medals_name_no_repeat))
print(golden_medals_name_no_repeat)
print()

print('Chilenos Medallas')
chileans = df[(df['Team'] == 'Chile') & (df['Medal'].fillna('None') != 'None')]
chileans_name = chileans['Name']
chileans_name_no_repeat = chileans_name.unique()
print(chileans_name_no_repeat)

print('Chilenos Medallas Oro')
gold_chileans = df[(df['Team'] == 'Chile') & (df['Medal'] == 'Gold')]
gold_chileans_name = gold_chileans['Name']
gold_chileans_name_no_repeat = gold_chileans_name.unique()
print(gold_chileans_name_no_repeat)






