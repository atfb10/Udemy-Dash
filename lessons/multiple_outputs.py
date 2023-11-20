import dash
from dash import (
    dcc,
    html
)
from dash.dependencies import (
    Input,
    Output
)
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import base64

# read in data
df = pd.read_csv('wheels.csv')

# Create app
app = dash.Dash()

def encode_img(image_file):
    with open(image_file, 'rb') as f:
        encoded = base64.b64encode(f.read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
    dcc.RadioItems(id='wheels',
                   options=[{'label': i, 'value': i} for i in df['wheels'].unique()],
                   value=1
                   ),
    html.Div(id='wheels-output'),
    html.Hr(),
    dcc.RadioItems(id='colors',
                   options=[{'label':i, 'value':i} for i in df['color'].unique()],
                   value='blue'
                   ),
    html.Div(id='colors-output'),
    html.Img(id='display-img', src='children', height=300)
], style={'fontFamily':'helvetica', 'fontSize':18})

@app.callback(Output('wheels-output', 'children'), [Input('wheels', 'value')])
def callback_a(wheels_value: int) -> str:
    return f'You chose {wheels_value}'

@app.callback(Output('colors-output', 'children'), [Input('colors', 'value')])
def callback_b(colors_value: str) -> str:
    return f'You chose {colors_value}'

@app.callback(Output('display-img', 'src'), [Input('wheels', 'value'), Input('colors', 'value')])
def callback_img(wheel:int, color:str):
    path = 'D:\\coding\\udemy\\dash\\lessons\\Images\\'
    return encode_img(path+df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server()