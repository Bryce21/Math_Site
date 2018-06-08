import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import matrix_page, calculus_page, probability_page

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # Will be header div that will carry across for all pages
    html.Div([
        # header
        html.H1('Math site', id='h1_header'),
        # Info on site div
        html.Div([
            html.P(
                'This site is designed to aggregate all kinds of useful tools and information for the math student to one place.')
       ]),

        html.Div([
            # TODO Have external css target this class and add margin-left
            dcc.Link('Home', href="/", id="first_header_link",),
            dcc.Link('Linear Algebra', href='/Linear_algebra', className="header_links", style={"margin-left":"5%"}),
            dcc.Link('Calculus', href="/calculus", className="header_links", style={"margin-left": "5%"}),
            dcc.Link('Probability', href="/probability", className="header_links", style={"margin-left": "5%"}),
        ], style={"margin-bottom":"-20px"}),
        html.Hr(),

    ], id="header_div", style={"text-align":"center"}),
    # Body div
    html.Div(id='page_content'),

])


@app.callback(Output('page_content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname is None:
        return "Loading"
    elif pathname == '/Linear_algebra':
        return matrix_page.layout
    elif pathname == "/":
        return layout
    elif pathname == "/calculus":
        return calculus_page.layout
    elif pathname == "/probability":
        return probability_page.layout
    else:
        return "404"


# Main page overview aspect
layout = html.Div([
    "Overview of site would go here"
])

if __name__ == '__main__':
    app.run_server(debug=True)
