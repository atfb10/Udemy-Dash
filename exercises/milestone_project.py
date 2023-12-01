# Importing necessary libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import yfinance as yf  # Use yfinance as an alternative to pandas_datareader
from datetime import datetime
import pandas as pd

# Set your IEX Cloud API key
# You can get a free key by signing up at https://iexcloud.io/cloud-login#/register/
IEX_CLOUD_API_KEY = 'pk_f8f7e7934a3347f78963cd67f0e8307a'

# Initializing the Dash web application
app = dash.Dash()

nasdaq = pd.read_csv('NASDAQcompanylist.csv')
nasdaq = nasdaq.set_index('Symbol')
options = []
for ticker in nasdaq.index:
    mydict = {}
    mydict['label'] = str(nasdaq.loc[ticker]['Name'] + ' ' + ticker)
    mydict['value'] = ticker
    options.append(mydict)

# Defining the layout of the Dash application
app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.Div([
        html.H3('Enter a stock symbol:', style={'paddingRight': '30px'}),
        dcc.Dropdown(id='my_stock_picker', value=['TSLA'], options=options, multi=True),
    ], style={'display':'inline-block', 'verticalAlign': 'top'}),

    html.Div([
        html.H3('Select a start and end date:'),
        dcc.DatePickerRange(id='my_date_picker',
                            min_date_allowed=datetime(2015, 1, 1),
                            max_date_allowed=datetime.today(),
                            start_date = datetime(2023, 1, 1),
                            end_date = datetime.today())
    ], style={'display': 'inline-block', 'width': '30%'}),

    dcc.Graph(id='my_graph',
            figure={'data': [{'x': [1, 2], 'y': [3, 1]}],
                    'layout': {'title': 'Default Title'}})
])

@app.callback(Output('my_graph', 'figure'), [Input('my_stock_picker', 'value'), Input('my_date_picker', 'start_date'), Input('my_date_picker', 'end_date')])
def update_graph(stock_ticker, start_date, end_date):
    # Check if an API key is provided
    if not IEX_CLOUD_API_KEY:
        return {
            'data': [{'x': [1, 2], 'y': [3, 1]}],
            'layout': {'title': 'API key missing'}
        }

    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')

    traces = []

    for ticker in stock_ticker:
        df = yf.download(ticker, start=start, end=end)
        traces.append({'x': df.index, 'y': df['Close'], 'name':ticker})

    figure = {
        'data': traces,
        'layout': {'title': stock_ticker}
    }
    return figure

if __name__ == '__main__':
    app.run_server()
