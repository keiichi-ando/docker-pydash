import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from src import maps, graph, selector, menu

external_stylesheets = ['/static/bulma.min.css']
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True)

app.layout = html.Div([
    menu.get_menu(),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# index_layout = html.Div([
#     # represents the URL bar, doesn't render anything
#     dcc.Location(id='url', refresh=False),

#     dcc.Link('Navigate to "/"', href='/'),
#     html.Br(),
#     dcc.Link('Navigate to "/maps"', href='/maps'),

#     # content will be rendered in this element
#     html.Div(id='page-content')
# ])


@ app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == '/':
        return []  # index_layout

    elif pathname == '/selector':
        return selector.layout
    elif pathname == '/graph':
        return graph.layout

    return maps.layout


if __name__ == '__main__':
    app.run_server(debug=True)
