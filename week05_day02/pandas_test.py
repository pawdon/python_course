import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot


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

    df_bantam = df[df['Event'] == "Boxing Men's Bantamweight"]
    print(df_bantam['Weight'].min(), df_bantam['Weight'].max(), df_bantam['Weight'].mean())

    print()
    weight_cat = df['Event'].unique()
    cat_data = []
    for cat in weight_cat:
        df_cat_weight = df[df['Event'] == cat]['Weight']
        single_data = {'name': cat,
                       'min': df_cat_weight.min(),
                       'max': df_cat_weight.max(),
                       'mean': round(df_cat_weight.mean(), 2),
                       'count': df_cat_weight.shape[0]}
        cat_data.append(single_data)

    cat_data.sort(key=lambda x: x['min'])

    df_cat_data = pd.DataFrame(cat_data)

    pd.set_option('display.max_rows', 100)
    print(df_cat_data)

    mask_women_lightweight = df['Event'] == "Boxing Women's Lightweight"
    women_lightweight = df[mask_women_lightweight]
    print(women_lightweight)
    pd.set_option('display.max_rows', 10)


def plot_bar():
    df = pd.read_csv('box_since_2000.csv', sep=';')
    weight_cat = df['Event'].unique()
    cat_data = []
    for cat in weight_cat:
        if "Boxing Men's" in cat:
            df_cat_weight = df[df['Event'] == cat]['Weight']
            single_data = {'name': cat.replace("Boxing Men's", ""),
                           'min': df_cat_weight.min(),
                           'max': df_cat_weight.max(),
                           'mean': round(df_cat_weight.mean(), 2),
                           'count': df_cat_weight.shape[0]}
            cat_data.append(single_data)

    cat_data.sort(key=lambda x: x['min'])

    df_cat_data = pd.DataFrame(cat_data)

    pd.set_option('display.max_rows', 100)
    print(df_cat_data)

    categories = df_cat_data['name']

    trace_min = go.Bar(
        name='min',
        x=categories,
        y=df_cat_data['min'],
        marker=dict(color='#0000ff')
    )
    trace_mean = go.Bar(
        name='mean',
        x=categories,
        y=df_cat_data['mean'],
        marker=dict(color='#ffff00')
    )
    trace_max = go.Bar(
        name='max',
        x=categories,
        y=df_cat_data['max'],
        marker=dict(color='#888888', line=dict(color='#ff0000', width=4))
    )
    layout = go.Layout(title='Boxing categories', barmode='group')
    figure = go.Figure(data=[trace_min, trace_mean, trace_max], layout=layout)
    plot(figure, auto_open=True, filename='box.html')


if __name__ == '__main__':
    plot_bar()
