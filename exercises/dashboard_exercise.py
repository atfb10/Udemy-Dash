import dash
from dash import (
    dcc,
    html
)
import plotly.graph_objs as go
import pandas as pd

'''
Plot x & y as scatterplot

Data Dictionary
D = date of recordings in month
X = duration of the current eruption in minutes
Y = waiting time until the next eruption in minutes
'''

# Read in data
df = pd.read_csv('OldFaithful.csv')

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id='scatterplot',
              figure= {'data': [
                  go.Scatter(
                      x=df['X'],
                      y=df['Y'],
                      mode='markers',
                  )
              ],
                       'layout': go.Layout(title='Waiting time by erurption duration',
                                           xaxis={'title':'Duration of Eruption'},
                                           yaxis={'title': 'Waiting time until next eruption'})})
])


if __name__ == '__main__':
    app.run_server()