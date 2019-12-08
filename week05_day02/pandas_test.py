import pandas as pd

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def test01():
    df = pd.read_csv('box_since_2000.csv', sep=';')
    print(df)
    print(df.keys())
    weights = df['Weight']
    print(weights.mean(), weights.median())
    print(weights)
    bmi = df['Weight'] / (df['Height'] / 100) ** 2
    bmi = bmi
    print(bmi.dropna())

    mask_low_bmi = bmi < 20  # series bool
    print(mask_low_bmi)
    df_low_bmi = df[mask_low_bmi]
    print(df_low_bmi)

    events_low_bmi = df_low_bmi['Event'].unique()
    print(events_low_bmi)

    df_low_bmi_middleweight = df[(bmi < 20) & (df['Event'] == "Boxing Men's Middleweight")]
    print(df_low_bmi_middleweight)


if __name__ == '__main__':
    test01()
