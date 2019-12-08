import pandas as pd

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def test01():
    df = pd.read_csv('box_since_2000.csv', sep=';')
    #print(df)
    weights = df['Weight']
    print(weights)


if __name__ == '__main__':
    test01()
