import dash
from dash import (
    dcc,
    html
)
from dash.dependencies import (
    Input,
    Output
)
import pandas as pd
import numpy as np
import plotly.graph_objs as go

'''
Callback steps
1. create function to return output
2. Decorate function w/ @app.callback decorator
    > Set an Output to a component id
    > Set an Input to a component id
3. Connect the desired properties
'''

# Create app
app = dash.Dash()

app.layout = html.Div([
    dcc.RangeSlider(id='slider', min=-10, max=10, marks={i:str(i) for i in range(-10, 11)}, value=[-1, 1]),
    html.H1(id='product')
])

@app.callback(Output('product', 'children'), [Input('slider', 'value')])
def update_value(value_list) -> float:
    return value_list[0] * value_list[1]

# Run
if __name__ == '__main__':
    app.run_server()