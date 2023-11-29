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
    html.Div([
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
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='mpg_line',
                  figure={
                      'data': [go.Scatter(x=[0, 1],
                                          y=[0,1],
                                          mode='lines'),],
                      'layout:': go.Layout(title='Acceleration', margin={'l':0})
                  })
    ], style={'width': '20%', 'height':'50%', 'display': 'inline-block'})
])

@app.callback(Output('mpg_line', 'figure'), [Input('mpg_scatter', 'hoverData')])
def callback_graph(hoverData):
    vehicle_index = hoverData['points'][0]['pointIndex']
    figure_dict = {'data': [go.Scatter(x=[0, 1],
                                       y=[0, 60/df.iloc[vehicle_index]['acceleration']],
                                       mode='lines')], # Represent how long it takes to go from 0 to 60 in seconds
                   'layout': go.Layout(title=df.iloc[vehicle_index]['name'], margin={'l':0}, height=300, xaxis={'visible':False}, yaxis={'visible':False, 'range':[0, 60/df['acceleration'].min()]})}
    
    return figure_dict 

if __name__ == '__main__':
    app.run_server()