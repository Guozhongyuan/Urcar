import dash
from dash import dcc, html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import tool
import json

layout = html.Div(
    [
        html.Br(),

        dbc.Container(
            [
                html.Img(
                    src='assets/car.jpg',
                    style={
                        'width': '50%',
                        'height': '50%',
                        'margin-left': '180px',
                        }
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
                                        {'label': key, 'value': key}
                                        for key in tool.addresses.keys()
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
                            dbc.Button('Query', id='query-button'),
                        ),
                    ]
                ),

                # show text
                # html.Div(id='output-value'),

                dbc.Tabs(
                    id='output-value',
                    style={'margin-top': '20px'},
                )

            ],
            style={
            'margin-top': '-20px',
            'max-width': '800px'
            }
        ),

    ]
)

@callback(
    Output('output-value', 'children'),
    Input('query-button', 'n_clicks'),
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
            car_info = tool.getInfo(tool.addresses[car_id][0])

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
                            html.H2('Records'),
                            html.P(json.dumps(car_info)),
                        ],
                        label='Repair Info'
                    )
                )

            # 返回渲染结果
            return tabs

    return dash.no_update