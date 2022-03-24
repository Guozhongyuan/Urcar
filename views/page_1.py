from dash import Dash, dcc, html, Input, Output, callback

layout = html.Div([
    html.H1('Page 1'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'], 'LA', id='page-1-dropdown'),
    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Go to query', href='/query'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),
])

@callback(Output('page-1-content', 'children'),
              [Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return f'You have selected {value}'


