import pandas as pd


def test():
    with open('athlete_events_since_2000.csv', 'r') as f:
        keys = f.readline().strip().split(';')
        print(len(keys))
        for line in f:
            values = line.strip().split(';')
            if len(values) != len(keys):
                print(values)


def prepare():
    df = pd.read_csv('athlete_events.csv')
    df = df[df['Year'] >= 2000]
    df.to_csv('athlete_events_since_2000.csv', index=False, sep=';')


test()
