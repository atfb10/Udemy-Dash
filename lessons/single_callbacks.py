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
    dcc.Input(id='my-id', value='Initial Text', type='text'),
    html.Div(id='my-div')
])

@app.callback(Output(component_id='my-div', component_property='children'), [Input(component_id='my-id', component_property='value')])
def update_output_div(input_value: str):
    return f"you entered: {input_value}"

# Run
if __name__ == '__main__':
    app.run_server()