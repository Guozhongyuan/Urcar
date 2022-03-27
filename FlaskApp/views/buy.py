from dash import Dash, dcc, html, Input, Output, callback

import dash_bootstrap_components as dbc

from dash import dash_table

from app import tool
import pandas as pd

df = tool.df
col_n = ['car_ID', 'CarCompany', 'CarName', 'fueltype', 'enginetype', 'curbweight', 'carbody', 'carlength',  'doornumber', 'enginelocation', 'price']
df = pd.DataFrame(df, columns = col_n)
data_show = df.to_dict('records')

layout = dbc.Container(
    [
        dash_table.DataTable(
            data=data_show,
            columns=[
                {'name': column, 'id': column}
                for column in df.columns
            ],
            # 自定义条件筛选单元格样式
            style_filter={
                'background-color': '#e3f2fd'
            },
            style_table={
                'height': '500px',
                'overflow-y': 'auto'
            },
            style_header={
                'font-family': 'Times New Roman',
                'font-weight': 'bold',
                'text-align': 'center'
            },
            style_data={
                'font-family': 'Times New Roman',
                'text-align': 'center'
            },
            filter_action="native",
            fill_width=True,
            fixed_rows={'headers': True},
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Form(
                        [
                            dbc.Input(type="text", id='input-buyer'),
                            dbc.FormText("input car id"),
                        ]
                    ),
                    width=5
                ),
                dbc.Col(
                    dbc.Form(
                        [
                            dbc.Input(type="text", id='input-account'),
                            dbc.FormText("input account address"),
                        ]
                    ),
                    width=5
                ),
                dbc.Col(
                    dbc.Button('BUY', id='buy-button'),
                    width=2
                )
            ],
            style={'margin-left': '60px'}
        ),
    ],

    style={
            'margin-top': '50px',
            'max-width': '1000px'
    },
)