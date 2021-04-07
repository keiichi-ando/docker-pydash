import dash_html_components as html


def get_menu():
    menu = html.Div(
        html.Nav([
            html.Div([
                html.A([
                    html.Img(
                        src="https://dash.plotly.com/assets/images/logo-dash.png", width="90")
                ], href='/', className="nav-item"),
            ], className='navbar-brand'),
            html.Div([
                html.Div([
                    html.A(' Home ', href="/", className="navbar-item"),
                    html.A(' Map ', href="/maps", className="navbar-item"),
                    html.A(' Graph ', href="/graph",
                           className="navbar-item"),
                    html.A(' Graph (Avocado) ', href="/graph/avocado",
                           className="navbar-item"),

                ], className="navbar-start")
            ], id="navbarBasic", className="navbar-menu")

        ], className='navbar is-primary is-transparent')
    )
    # html.Nav([, className='navbar-brand'], id="navbarBasic", className='navbar')
    return menu
