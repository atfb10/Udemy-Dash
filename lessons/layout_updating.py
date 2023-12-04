import dash
from dash import (
    dcc,
    html
)
import dash_core_components as dcc
from dash.dependencies import (
    Input,
    Output
)

app = dash.Dash()



'''
EXAMPLE 1: Update on refresh

# crash_free = 0

# def refresh_layout():
#     global crash_free
#     crash_free += 1
#     return html.H1(f'Crash free for {crash_free} refreshes')

# app.layout = refresh_layout
'''

'''
Example 2: Update on Interval
'''
app.layout = html.Div([
    html.H1(id='live-update-text'),
    dcc.Interval(id='interval-component',
                 interval=2000,
                 n_intervals=0)
])

@app.callback(Output('live-update-text', 'children'), [Input('interval-component', 'n_intervals')])
def update_layout(n):
    return f'Crash free for {n} refreshes'

if __name__ == '__main__':
    app.run_server()