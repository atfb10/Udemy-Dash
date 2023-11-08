import dash
from dash import (
    dcc,
    html
)
import pandas as pd
import numpy as np
import plotly.graph_objs as go

# Create app
app = dash.Dash()

app.layout = html.Div([
    html.Label('Dropdown'), 
    dcc.Dropdown(options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Bishop', 'value': 'Bish'}
        ],
        value='Bish'),

    html.Label('Slider'),
    dcc.Slider(min=0, max=10, step=1, value=0, marks={i: i for i in range(0, 10)}),

    html.P(html.Label('Some Radio Items')),
    dcc.RadioItems(options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Bishop', 'value': 'Bish'}
        ],
        value='NYC')
])

# Run
if __name__ == '__main__':
    app.run_server()