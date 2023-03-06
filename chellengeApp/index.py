from dash import html, Input, Output, dcc
from app import app
from pages import home, page1, iptable, action
import dash_bootstrap_components as dbc

# Navbar layout
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.A(
                            dbc.Row(
                                [
                                    dbc.Col(
                                        html.Img(src="/assets/logo.png", height="30px")
                                    ),
                                    dbc.Col(dbc.NavbarBrand("Home Secu-Data", className="ml-2")),
                                ],
                                align="center",
                                className="no-gutters",
                            ),
                            href="/",
                        ),
                        width="auto",
                    ),
                    dbc.Col(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Page 1", href="/page1")),
                                dbc.NavItem(dbc.NavLink("Iptable", href="/iptable")),
                                dbc.NavItem(dbc.NavLink("Action", href="/action")),
                            ],
                            navbar=True,
                        ),
                        width=True,
                        className="ml-auto",
                    ),
                ],
                align="center",
            ),
        ],
        fluid=True,
    ),
    color="dark",
    dark=True,
)

# App layout with navbar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/page1':
        return page1.layout()
    elif pathname == '/iptable':
        return iptable.layout()
    elif pathname == '/action':
        return action.layout()
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
