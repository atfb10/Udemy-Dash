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

# read in data
df = pd.read_csv('mpg.csv')

# Create app
app = dash.Dash()

# 'mpg' 'hp', 'displacement'
feature_list = df.columns

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id='xaxis',
                     options=[{'label': i, 'value': i} for i in feature_list],
                     value='displacement')
    ], style={'width': '48%', 'display': 'inline-block'}),
    
    html.Div([
        dcc.Dropdown(id='yaxis',
                     options=[{'label': i, 'value':i} for i in feature_list],
                     value='mpg')
    ], style={'width':'48%', 'display':'inline-block'}),

    dcc.Graph(id='feature-graphic')
], style={'padding':10})

@app.callback(Output('feature-graphic', 'figure'), [Input('xaxis', 'value'), Input('yaxis', 'value')])
def update_graph(xaxis_name: str, yaxis_name: str) -> dict:
    return {'data': [go.Scatter(x=df[xaxis_name], y=df[yaxis_name], text=df['name'], mode='markers', marker={'size':5, 'color':'green', 'opacity':'.5', 'line':{'width':.5, 'color':'white'}})],
            'layout': go.Layout(title='My Dashboard for MPG', xaxis={'title': xaxis_name}, yaxis={'title': yaxis_name}, hovermode='closest')}

if __name__ == '__main__':
    app.run_server()