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
import pandas as pd
import numpy as np


# Create app
app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='number-id', value=1, style={'font-size':24}),
    html.Button(id='submit', n_clicks=0, children='Submit Here', style={'font-size':24}),
    html.H1(id='number-out')
])

@app.callback(Output('number-out', 'children'), [Input('submit', 'n_clicks')], [State('number-id', 'value')])
def output(n_clicks:int, number:int) -> int:
    return f'{number} was typed in and submit btn has been clicked {n_clicks} total times'

if __name__ == '__main__':
    app.run_server()