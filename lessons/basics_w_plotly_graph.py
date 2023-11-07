import dash
from dash import (
    dcc,
    html
)
import plotly.graph_objs as go
import numpy as np

# Spin up dash up
app = dash.Dash()

# Create data
np.random.seed(seed=42)
x = np.random.randint(1, 101, 100)
y = np.random.randint(1, 101, 100)

app.layout = html.Div([
    dcc.Graph(id='scatterplot',
              figure= {'data': [
                  go.Scatter(
                      x=x,
                      y=y,
                      mode='markers',
                      marker={
                          'size':12,
                          'color': 'rgb(51, 204, 153)',
                          'symbol': 'pentagon',
                          'line': {'width':2}
                      }
                  )
              ],
                       'layout': go.Layout(title='Scatter Example',
                                           xaxis={'title':'Some X title'},
                                           yaxis={'title': 'I am y'})}),
    dcc.Graph(id='scatterplot2',
              figure= {'data': [
                  go.Scatter(
                      x=x,
                      y=y,
                      mode='markers',
                      marker={
                          'size':10,
                          'color': 'rgb(51, 1, 153)',
                          'line': {'width':5}
                      }
                  )
              ],
                       'layout': go.Layout(title='Scatter Example2',
                                           xaxis={'title':'Some X title'},
                                           yaxis={'title': 'I am y'})})
])

if __name__ == '__main__':
    app.run_server()