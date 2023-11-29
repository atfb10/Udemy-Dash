import dash
from dash import (
    dcc,
    html
)
from dash.dependencies import (
    Input,
    Output,
    State
)
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import json

app = dash.Dash()

df = pd.read_csv('mpg.csv')
# Add a random "jitter" to model_year to spread out the plot
df['year'] = np.random.randint(-4,5,len(df))*0.10 + df['model_year']

app.layout = html.Div([
    dcc.Graph(
        id='mpg_scatter',
        figure={
            'data': [go.Scatter(
                x = df['year']+1900,  # our "jittered" data
                y = df['mpg'],
                text = df['name'],
                hoverinfo = ['text', 'y'],
                mode = 'markers'
            )],
            'layout': go.Layout(
                title = 'MPG Data',
                xaxis = {'title': 'model year'},
                yaxis = {'title': 'miles per gallon'},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()