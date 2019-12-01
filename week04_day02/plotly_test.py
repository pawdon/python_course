import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot


def test_scatter():
    x = np.linspace(0, 3 * np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    trace1 = go.Scatter(  # linia wykresu
        x=x,
        y=y1,
        mode='markers+lines',
        line=dict(color='#008000',
                  dash='dot'),
        name='sinus',
        showlegend=False,
    )

    trace2 = go.Scatter(  # linia wykresu
        x=x,
        y=y2,
        mode='markers+lines',
        line=dict(color='rgba(0,0,255,0.2)',
                  width=5),
        marker=dict(symbol='x',
                    size=10,
                    color='rgb(0,255,255)',
                    line=dict(color='rgb(255,0,0)',
                              width=2)),
        name='cosinus'
    )

    layout = go.Layout()  # okno
    figure = go.Figure(data=[trace1, trace2], layout=layout)  # wszystko razem
    plot(figure, auto_open=True, filename='test.html')


if __name__ == '__main__':
    test_scatter()
