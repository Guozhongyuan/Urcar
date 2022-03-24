import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from views import query
from views import page_1, page_2

# -----------------------------------------------------------------------------# 
import json
from utils.contrast import CarContrast
tool = CarContrast()

import pandas as pd
data = pd.read_csv('assets/car.csv')

all_data = dict()

for i in range(1):
    info = dict(data.iloc[i])
    for j in info.keys():
        info[j] = str(info[j])
    all_data[info['car_ID']] = info

all_addresses = dict()
for id in all_data.keys():
    address = tool.new(all_data[id])
    all_addresses[id] = [address]

tool.addresses = all_addresses

# -----------------------------------------------------------------------------# 

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
)

app.layout = dbc.Container(
    [
        dcc.Location(id='url', refresh=False),

        dcc.Link('query', href='/query', refresh=False, style={'margin-left': '0px'}),
        # html.Br(),
        dcc.Link('页面B', href='/pageB', refresh=False, style={'margin-left': '20px'}),
        # html.Br(),
        dcc.Link('页面C', href='/pageC', refresh=False, style={'margin-left': '20px'}),

        html.Hr(),  # 分隔线

        html.Div(id='render-page-content'),

    ],
    style={
        'paddingTop': '20px'
    }
)


@app.callback(
    Output('render-page-content', 'children'),
    Input('url', 'pathname')
)
def render_page_content(pathname):
    if pathname == '/':
        return 'Welcome'

    elif pathname == '/query':
        return query.layout

    elif pathname == '/pageB':
        return page_1.layout

    elif pathname == '/pageC':
        return page_2.layout

    else:
        return '404 NOT FOUND'


if __name__ == '__main__':
    app.run_server(debug=True)
