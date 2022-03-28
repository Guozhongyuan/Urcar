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
        html.Hr(),  # 分割线

        html.H1('Show Car Information',className="display-4 ",style={'margin-left': '220px',}),

        html.Br(),

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
                'height': '600px',
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
        html.Hr(),  # 分割线
    ],

    style={
            'margin-top': '50px',
            'max-width': '1000px'
    },
)