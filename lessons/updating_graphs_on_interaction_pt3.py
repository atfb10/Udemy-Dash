# Importing necessary libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# Initializing the Dash web application
app = dash.Dash()

# Reading the dataset containing MPG data
df = pd.read_csv('mpg.csv')

# Adding random "jitter" to model_year to spread out the plot
df['year'] = np.random.randint(-4, 5, len(df)) * 0.10 + df['model_year']

# Defining the layout of the Dash application
app.layout = html.Div([

    # Scatterplot of year & miles per gallon
    html.Div([
        dcc.Graph(
            id='mpg_scatter',
            figure={
                'data': [go.Scatter(
                    x=df['year'] + 1900,  # Our "jittered" data
                    y=df['mpg'],
                    text=df['name'],
                    hoverinfo=['text', 'y'],
                    mode='markers'
                )],
                'layout': go.Layout(
                    title='MPG Data',
                    xaxis={'title': 'model year'},
                    yaxis={'title': 'miles per gallon'},
                    hovermode='closest'
                )
            }
        )
    ], style={'width': '50%', 'display': 'inline-block'}),

    # Line "scatterplot" of time to get to 60 miles an hour
    html.Div([
        dcc.Graph(id='mpg_line',
                  figure={
                      'data': [go.Scatter(x=[0, 1],
                                          y=[0, 1],
                                          mode='lines'), ],
                      'layout': go.Layout(title='Acceleration', margin={'l': 0})
                  })
    ], style={'width': '20%', 'height': '50%', 'display': 'inline-block'}),

    # Markdown component to display vehicle statistics
    html.Div([
        dcc.Markdown(id='mpg_stats')
    ], style={'width': '20%', 'height': '50%', 'display': 'inline-block'})
])

# Callback to update the line plot based on the selected data point in the scatter plot
@app.callback(Output('mpg_line', 'figure'), [Input('mpg_scatter', 'hoverData')])
def callback_graph(hoverData):
    vehicle_index = hoverData['points'][0]['pointIndex']
    
    # Creating a dictionary for the line plot figure
    figure_dict = {
        'data': [go.Scatter(x=[0, 1],
                            y=[0, 60 / df.iloc[vehicle_index]['acceleration']],  # Representing time to go from 0 to 60 in seconds
                            mode='lines',
                            line={'width': 2 * df.iloc[vehicle_index]['cylinders']})],
        'layout': go.Layout(title=df.iloc[vehicle_index]['name'],
                            margin={'l': 0},
                            height=300,
                            xaxis={'visible': False},
                            yaxis={'visible': False, 'range': [0, 60 / df['acceleration'].min()]})}
    
    return figure_dict

# Callback to update the vehicle statistics based on the selected data point in the scatter plot
@app.callback(Output('mpg_stats', 'children'), [Input('mpg_scatter', 'hoverData')])
def callback_stats(hoverData):
    vehicle_index = hoverData['points'][0]['pointIndex']
    
    # Creating a formatted string with vehicle statistics
    stats = """
        **Vehicle Stats**
        * {} cylinders
        * {} cc displacement
        * 0 to 60mph in {} seconds
    """.format(df.iloc[vehicle_index]['cylinders'],
               df.iloc[vehicle_index]['displacement'],
               df.iloc[vehicle_index]['acceleration'])
    
    return stats

# Running the Dash web application
if __name__ == '__main__':
    app.run_server()
