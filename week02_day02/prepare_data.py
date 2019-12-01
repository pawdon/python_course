import pandas as pd


df = pd.read_csv('athlete_events_since_2000.csv', sep=';')
print(df['Sport'].unique())
