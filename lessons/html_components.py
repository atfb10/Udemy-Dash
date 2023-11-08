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

app.layout = html.Div(['This is the outermost div',
                       html.Div('This is an inner div!', style={'color':'red'}),
                       html.Div('Another inner div!', style={'color': 'blue', 'border': '2px black solid'})],
                      style={'color': 'green', 'border':'2px blue solid'})

# Run
if __name__ == '__main__':
    app.run_server()