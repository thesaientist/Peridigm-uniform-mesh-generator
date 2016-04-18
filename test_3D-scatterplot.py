# Sample python script for plotting a 3D scatter plot using plotly

import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter3d(
    x=[0.5, -0.5, 2 , 5],
    y=[1, 2, 5, 3.5],
    z=[1, 1, 2, 2],
    mode='markers',
    marker=dict(
        size=8,
        line=dict(
            color='rgb(217,217,217)',
            width=0.2
        ),
        opacity=0.8
    )
)

data = [trace1]
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)

fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='simple-3D-scatterplot')
