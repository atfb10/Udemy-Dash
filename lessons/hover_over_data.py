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
from json import dumps
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import base64

# read in data
df = pd.read_csv('wheels.csv')

# Create app
app = dash.Dash()

def encode_image(image_file):
    with open(image_file, 'rb') as f:
        encoded = base64.b64encode(f.read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
    html.Div(dcc.Graph(id='wheels-plot',
             figure={'data': [go.Scatter(
                 x=df['color'],
                 y=df['wheels'],
                 dy=1,
                 mode='markers',
                 marker={'size':15}
             )],
             'layout':go.Layout(title='Test', hovermode='closest')}
             ),
             style={'width':'30%', 'float':'left'}),
    
    html.Div(html.Img(id='hover-data', src='children', height=300), 
             style={'paddingTop': 35}),
])

@app.callback(Output('hover-data', 'src'), [Input('wheels-plot', 'hoverData')]) # NOTE: 'hoverData' is a property that belongs to any dcc graph!
def callback_img(hoverData):
    wheel = hoverData['points'][0]['y']
    color = hoverData['points'][0]['x']
    path = 'Images/'
    return encode_image(path+df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server()