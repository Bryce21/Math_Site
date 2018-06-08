import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
import math_work
import wolframalpha
import config

app_id = config.keys.get('wolfram_api_key')
client = wolframalpha.Client(app_id)

layout = html.Div([

    html.H3("Calculus"),
    html.Div([
        html.P("Calculus is the study of...")
    ]),
    html.Details([
        html.Summary("How to use this page:"),
        html.P(
            "The entry field below will submit whatever math problem is entered to wolfram alpha in an API call. "
            "It's very easy, but some special rules have to be followed in order for Wolfram to be able to make sense of the input."),
        html.P("Following are some examples of how to properly use the API in order to solve your math problem."),
        html.Hr(),
        html.P("For example, to use differentiation, type in 'differentiate 'your math problem here''."),
        html.P("In that same vein, to solve an algebra problem you'd replace 'differentiate' with 'solve'."),
        html.P("You're probably able to guess that integration would be: 'integrate 'your math problem''."),
        html.Hr(),
    ]),


    html.H3("Common Calculus problems: "),

    dcc.Input(
        type="text",
        id="wolfram_api_input",
        placeholder="Put problem here"
    ),
    html.Br(),
    html.Button(children="Submit", id="wolfram_submit_button"),
    html.Div(id="wolfram_output_div")
])


@app.callback(Output('wolfram_output_div', 'children'),
              [Input('wolfram_submit_button', 'n_clicks')],
              [State('wolfram_api_input', 'value')])
def binomial_submittion(click, wolfram_query):
    # To prevent an error when callbacks are called on page load.
    if click is None or wolfram_query is None:
        return
    return math_work.send_query_to_wolfram(wolfram_query, client)
