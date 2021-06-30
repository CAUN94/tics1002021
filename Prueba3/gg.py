import pandas as pd


df = pd.read_csv('athlete_events.csv')
df = df[(df['Sex'] == 'M') & (df['Year'] >= 1980)]

print(df['Weight'].mean())