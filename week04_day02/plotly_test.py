import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot


def test_scatter():
    x = np.linspace(0, 3 * np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    label1 = [f'y={i}' for i in y2]

    trace1 = go.Scatter(  # linia wykresu
        x=x,
        y=y1,
        mode='markers+lines',
        line=dict(color='#008000',
                  dash='dot'),
        name='sinus',
        showlegend=False,
        hovertext=label1,
        hoverinfo='text'
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

    layout = go.Layout(  # okno
        title='Moje wykresy',
        # height=1080,
        # width=1920
        yaxis=dict(range=(-1.2, 1.2))
    )
    figure = go.Figure(data=[trace1, trace2], layout=layout)  # wszystko razem
    plot(figure, auto_open=True, filename='test.html')



def test_plotly3d():
    # x = np.linspace(-10, 10, 7)
    # y = np.linspace(-5, 3, 4)

    x = np.array([-2, 1, 0, 1, 2])
    y = np.array([-3, -1, 1, 3])

    print(x, '\n')
    print(y, '\n')

    X, Y = np.meshgrid(x, y)
    print(X, '\n')
    print(Y, '\n')

    Z = X ** 2 + Y ** 3  # moja funkcja
    print(Z, '\n')

    trace1 = go.Heatmap(
        x=x,  # 1D
        y=y,  # 1D
        z=Z,  # 2D
        colorscale='Viridis'
    )

    layout = go.Layout()
    figure = go.Figure(data=[trace1], layout=layout)  # wszystko razem
    plot(figure, auto_open=True, filename='test.html')



def test_plotly3d_ver2():
    t = np.linspace(0, 10, 50)
    x, y, z = np.cos(t), np.sin(t), t
    trace1 = go.Scatter3d(
        x=x,
        y=y,
        z=z
    )

    layout = go.Layout()
    figure = go.Figure(data=[trace1], layout=layout)  # wszystko razem
    plot(figure, auto_open=True, filename='test.html')


if __name__ == '__main__':
    test_plotly3d_ver2()
