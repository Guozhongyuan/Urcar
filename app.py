import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State
import time
# -----------------------------------------------------------------------------# 
import json
from utils.contrast import CarContrast
tool = CarContrast()

import pandas as pd
data = pd.read_csv('car.csv')

all_data = dict()

for i in range(10):
    info = dict(data.iloc[i])
    for j in info.keys():
        info[j] = str(info[j])
    all_data[info['car_ID']] = info

all_addresses = dict()
list_addresses = list()
for id in all_data.keys():
    address = tool.new(all_data[id])
    all_addresses[id] = [address]
    list_addresses.append([id, address])

df_save = pd.DataFrame(columns=['id', 'address'], data=list_addresses)
df_save.to_csv('address.csv', header=True, index=False)

time.sleep(1)
# -----------------------------------------------------------------------------# 
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Br(),

        dbc.Container(
            [
                html.Img(
                    src='assets/car_2.jpg',
                    style={'width': '100%'}
                ),

                html.Hr(),  # 分割线

                # 车辆选择控件
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label('Car ID :'),
                                dcc.Dropdown(
                                    id='car_list',
                                    options=[
                                        {'label': item[0], 'value': item[0]}
                                        for item in list_addresses
                                    ])
                            ]
                        )
                    ]
                ),

                html.Br(),  # 空格

                # 查看内容选择控件
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label('Search : ', html_for='car_attributes'),
                                dcc.Dropdown(
                                    id='car_attributes',
                                    multi=True,
                                    options=[
                                        {'label': item, 'value': item}
                                        for item in ['Initial Info', 'Repair Info']
                                    ])
                            ],
                        )
                    ]
                ),

                html.Hr(),

                # 提交查询按钮
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Button('Query', id='query'),
                        ),
                    ]
                ),

                dbc.Tabs(
                    id='car_attributes_list',
                    style={'margin-top': '20px'},
                )
            ],
            style={
            'margin-top': '10px',
            'max-width': '600px'
            }
        )
    ]
)

@app.callback(
    Output('car_attributes_list', 'children'),
    Input('query', 'n_clicks'),
    [State('car_list', 'value'),
     State('car_attributes', 'value')]
)
def render_content(n_clicks, car_id, car_attributes):
    '''
    根据用户控件输入结果，进行相应查询结果的渲染
    :param n_clicks: 查询按钮点击次数
    :param car_id: 已选择的车辆对应id
    :param car_attributes: 已选择要展示的内容范围
    :return:
    '''

    # 当按钮被新一轮点击后
    if n_clicks:
        # 当car_id与car_attributes不为空时
        if car_id and car_attributes:

            # 获取该车辆全部信息
            car_info = tool.getInfo(all_addresses[car_id][0])
 
            # 初始化Tabs返回结果
            tabs = []
            if 'Initial Info' in car_attributes:
                # 渲染Initial Info面板内容
                tabs.append(
                    dbc.Tab(
                        [
                            html.H2(car_info['CarName']),
                            html.P(json.dumps(car_info))
                        ],
                        label='Initial Info'
                    )
                )

            if 'Repair Info' in car_attributes:
                # 渲染Repair Info面板内容
                tabs.append(
                    dbc.Tab(
                        [
                            html.H2('Modify record'),
                            html.P(json.dumps(car_info)),
                        ],
                        label='Repair Info'
                    )
                )

            # 返回渲染结果
            return tabs

    return dash.no_update

if __name__ == '__main__':
    app.run_server(debug=False)