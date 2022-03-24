import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from init import tool
from views import add, query, buy


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
)

app.layout = dbc.Container(
    [
        dcc.Location(id='url', refresh=False),

        dcc.Link('QUERY', href='/query', refresh=False, style={'margin-left': '0px'}),
        # html.Br(),
        dcc.Link('ADD', href='/add', refresh=False, style={'margin-left': '40px'}),
        # html.Br(),
        dcc.Link('BUY', href='/buy', refresh=False, style={'margin-left': '40px'}),

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

    elif pathname == '/add':
        return add.layout

    elif pathname == '/buy':
        return buy.layout

    else:
        return '404 NOT FOUND'


if __name__ == '__main__':
    app.run_server(debug=True)
