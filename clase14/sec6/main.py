import pandas as pd

df = pd.read_csv('/Users/cristobalugarte/code/tics100/clase14/athlete_events.csv')

print('Describe')
print(df.describe())
print()

print('Head(10)')
print(df.head(10))
print()

print('Iloc')
print(df.iloc[0])
print()

print('Iloc only one value')
print(df.iloc[0,1])
print(df.iloc[0,6])
print()

print('DF Name')
print(df['Name'])
print()

print('DF Year')
print(df['Year'])
print()

print('SubFrame Name')
print(df['Name'][0:10])
print()

print('SubDataFrame Name, Team')
data = df[['Name','Team']]
print(data.head(10))
print()

print('SubDataFrame Name, Team Iloc[0]')
print(data.iloc[0])
print()

print('Filas')
print(df.shape[0])
print()

print('Columnas')
print(df.shape[1])
print()

print('Atletas unicos')
unique_athelets = df['Name'].unique()
print(unique_athelets)
# print(list(unique_athelets))
print(len(unique_athelets))
print()

print('Medallas de Oro')
gold_medals = df[df['Medal'] == 'Gold']
gold_medals_unique = gold_medals['Name'].unique()
print(gold_medals_unique)
# print(list(unique_athelets))
print(len(gold_medals_unique))

# for name in gold_medals_unique:
#     print(name)

print()

print('Medallero')
gold_medals = df[(df['Medal'] == 'Gold') | (df['Medal'] == 'Silver') | (df['Medal'] == 'Bronze')]
gold_medals_unique = gold_medals['Name'].unique()
print(gold_medals_unique)
# print(list(unique_athelets))
print(len(gold_medals_unique))

# for name in gold_medals_unique:
#     print(name)

print()

print('Consulta')
gold_medals = df[(df['Team'] == 'Chile') & (df['Year'] >= 2000) & (df['Medal'] == 'Gold')]
gold_medals_unique = gold_medals['Name'].unique()
print(gold_medals_unique)
# print(list(unique_athelets))
print(len(gold_medals_unique))

# for name in gold_medals_unique:
#     print(name)

print()

print('Filtros')
medal_winners = df[(df['Medal'].fillna('None') != 'None')]
print(medal_winners)
# print(list(unique_athelets))
print(len(medal_winners))

# for name in gold_medals_unique:
#     print(name)

print()

print('Comparar')
medal_winners1 = df[(df['Medal'].fillna('None') != 'None')]
medal_winners2 = df[(df['Medal'] == 'Gold') | (df['Medal'] == 'Silver') | (df['Medal'] == 'Bronze')]

print(medal_winners1.equals(medal_winners2))

print()

