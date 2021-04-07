import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app

import plotly.express as px
import pandas as pd

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

layout = html.Div(
    children=[
        html.H1("Hello Dash"),

        html.Div(children='''
            Dash: A web appliation framework for Python.
        '''),

        dcc.Graph(
            id="example-graph",
            figure=fig
        ),
        # callback
        html.H6("Change the value in the text box to see callbacks in action!"),
        html.Div(["Input: ",
                  dcc.Input(id='my-input', value='initial value', type='text')]),
        html.Br(),
        html.Div(id='my-output'),

    ]
)

# for callback
@app.callback(Output(component_id='my-output', component_property='children'),Input(component_id='my-input', component_property='value'))
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)
