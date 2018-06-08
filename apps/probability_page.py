import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
import pprint
import math_work

layout = html.Div([
    # What is probability
    # Common problems and walk through
    #
    html.H3("Probability"),
    html.Div([
        html.P("Probability is the study of...")
    ]),

    html.H3("Common probability problems: "),
    # Div containing everything to do with Binomial equations
    html.Div([
        # Info on binomial equations div
        html.Div([
            html.P(['A ', html.A(['binomial distribution'], href='https://en.wikipedia.org/wiki/Binomial_distribution'),
                    ' is a probability problem that addresses the likely hood of getting m successes of n yes or no trials. Some example use cases: Coin flips. Dice roll']),
        ], style={}),
        # Div that will contain the dropdown component
        html.Div([
            html.Details([
                html.Summary('Binomial Distribition'),
                html.Div([
                    html.P([
                        dcc.Input(id='number_of_successes_field', type='number',
                                  placeholder='Successes'),
                        html.Br(),
                        dcc.Input(id='number_of_tests_field', type='number', placeholder='Number of Tests'),
                        html.Br(),
                        dcc.Input(id='success_rate_field', type='number', placeholder='Rate of Success'),
                        html.Br(),
                        html.Button(id='submit_binomial', type='submit', children='ok'),
                        html.Div([], id='output_area_binomial')
                    ])
                ], style={}),
            ]),

        ])
    ], style={}, className='centered', id='binomial_div'),
    html.Br(),
    # Everything to do with birthday problem
    html.Div([
        # Info on binomial equations div
        html.Div([
            html.P(['The ', html.A(['birthday problem'], href='https://en.wikipedia.org/wiki/Birthday_problem'),
                    ' is a probability problem...']),
        ], style={}),
        # Div that will contain the dropdown component
        html.Div([
            html.Details([
                html.Summary('Birthday Problem'),
                html.Div([
                    html.Div([
                        html.P([
                            dcc.Input(id='number_of_people_field', type='number', placeholder='Number of people',
                                      value=''),
                            html.Br(),
                            html.Button(id='submit_birthday', type='submit', children='ok'),
                            html.Div(id='output_area_birthday')
                        ])
                    ], style={}),

                ]),

            ], id='birthday_details')
        ])
    ], style={}, id='bday_div', className='centered', ),
    html.Br(),

])


@app.callback(Output('output_area_binomial', 'children'),
              [Input('submit_binomial', 'n_clicks')],
              [State('number_of_successes_field', 'value'),
               State('number_of_tests_field', 'value'),
               State('success_rate_field', 'value')])
def binomial_submittion(click, success, total, rate_of_success):
    # To prevent an error when callbacks are called on page load.
    if success is None or total is None or rate_of_success is None:
        return
    ans = math_work.binomial(success, total, rate_of_success)
    return str(ans)


@app.callback(Output('output_area_birthday', 'children'),
              [Input('submit_birthday', 'n_clicks')],
              [State('number_of_people_field', 'value'), ])
def birth_day_problem(click, value):
    if click is None or value is None:
        return
    return str(math_work.same_birthday_probability(value))
