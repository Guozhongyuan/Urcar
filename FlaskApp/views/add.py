from dash import Dash, dcc, html, callback
import dash_bootstrap_components as dbc
from init import tool
from dash.dependencies import Input, Output, State

layout = html.Div(
    [
        html.Br(),  # 换行

        dbc.Container(
            [
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col([dbc.Label('1. Your identity')])
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.RadioItems(
                                options=[
                                    {"label": "Factory", "value": 1},
                                    {"label": "Shop", "value": 2},
                                    {"label": "Checker", "value": 3}
                                ],
                                inline=True
                            )
                        )
                    ]
                ),
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col([dbc.Label('2. Type of record')])
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.RadioItems(
                                options=[
                                    {"label": "Ex factory", "value": 1},
                                    {"label": "Repair", "value": 2},
                                    {"label": "Transaction", "value": 3},
                                    {"label": "Varify", "value": 4},
                                    {"label": "Destroy", "value": 5},
                                ],
                                inline=True
                            )
                        )
                    ]
                ),
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col([dbc.Label('3. Need what')])
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Checklist(
                                options=[
                                    {"label": "initial", "value": 1},
                                    {"label": "price", "value": 2},
                                    {"label": "odograph", "value": 3},
                                    {"label": "score", "value": 4},
                                    {"label": "others", "value": 5}
                                ],
                                inline=True
                            ),
                        )
                    ]
                ),
                html.Hr(),
                html.Br(),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Form(
                                [
                                    dbc.Input(type="text", id='input-carID'),
                                    dbc.FormText("input car id"),
                                ]
                            ),
                            width=5
                        ),
                        dbc.Col(
                            dbc.Form(
                                [
                                    dbc.Input(type="text", id='input-content'),
                                    dbc.FormText("input record content"),
                                ]
                            ),
                            width=5
                        ),
                        dbc.Col(
                            dbc.Button('ADD', id='add-button'),
                            width=2
                        )
                    ],
                ),
                # show
                html.Div(id='output-add'),
            ],
            style={
            'margin-top': '0px',
            'max-width': '800px'
            }
        )
    ]
)

@callback(
    Output('output-add', 'value'),
    Input('add-button', 'n_clicks'),
    [State('input-carID', 'value'),
    State('input-content', 'value')],
)
def refresh_output(n_clicks, carID, content):

    if n_clicks:
        address = tool.new(content)
        if carID not in tool.addresses.keys():
            tool.addresses[carID] = [address]
        else:
            tool.addresses[carID].append(address)
    return 'add one success'


