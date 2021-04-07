import dash_core_components as dcc
import dash_html_components as html

# from app import app

import pandas as pd

data = pd.read_csv('data/avocado.csv')
data = data.query("type=='conventional' and region=='Albany'")
data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

layout = html.Div(
    children=[
        html.H1(children="Avocado Analytics"),
        html.P(
            children="Analyze the behevior of avocado prices"
            " and the number of avocados sold in the US"
            " between 2015 to 2018"
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        'type': "lines"
                    },
                ],
                "layout": {'title': 'Average Price of Avocados'},
            },
        ),
        dcc.Graph(
            figure={
                "data" : [
                    {
                        "x" : data["Date"],
                        "y" : data["Total Volume"],
                        'type': "lines",
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)
