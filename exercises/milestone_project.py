# Importing necessary libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import yfinance as yf  # Use yfinance as an alternative to pandas_datareader
from datetime import datetime

# Set your IEX Cloud API key
# You can get a free key by signing up at https://iexcloud.io/cloud-login#/register/
IEX_CLOUD_API_KEY = 'pk_f8f7e7934a3347f78963cd67f0e8307a'

# Initializing the Dash web application
app = dash.Dash()

# Defining the layout of the Dash application
app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a stock symbol:'),
    dcc.Input(id='my_stock_picker', value='TSLA'),
    dcc.Graph(id='my_graph',
              figure={'data': [{'x': [1, 2], 'y': [3, 1]}],
                      'layout': {'title': 'Default Title'}})
])

@app.callback(Output('my_graph', 'figure'), [Input('my_stock_picker', 'value')])
def update_graph(stock_ticker):
    # Check if an API key is provided
    if not IEX_CLOUD_API_KEY:
        return {
            'data': [{'x': [1, 2], 'y': [3, 1]}],
            'layout': {'title': 'API key missing'}
        }

    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 11, 30)

    # Fetch stock data using yfinance
    df = yf.download(stock_ticker, start=start_date, end=end_date)

    figure = {
        'data': [{'x': df.index, 'y': df['Close']}],
        'layout': {'title': stock_ticker}
    }
    return figure

if __name__ == '__main__':
    app.run_server()
