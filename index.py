import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app

import math_work

border1 = ''
border2 = ''
border3 = ''

dropdown_options = []
for x in range(1, 11):
    dict = {'label': x, 'value': x}
    dropdown_options.append(dict)

app.layout = html.Div([
    # Header div
    html.Div([
        # header
        html.H1('Math site', id='h1_header', style={'border': border2}),
        # Info on site div
        html.Div([
            html.P(
                'This site is designed to aggregate all kinds of useful tools and information for the math student to one place')
        ], style={'border': border3})
    ], style={'border': border1}),
    html.Br(),
    # Div containing everything to do with Binomial equations
    html.Div([
        # Info on binomial equations div
        html.Div([
            html.P(['A ', html.A(['binomial distribution'], href='https://en.wikipedia.org/wiki/Binomial_distribution'),
                    ' is a probability problem that addresses the likely hood of getting m successes of n yes or no trials. Some example use cases: Coin flips. Dice roll']),
        ], style={'border': border2}),
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
                ], style={'border': border2}),
            ]),

        ])
    ], style={'border': border1}),
    html.Br(),
    # Everything to do with birthday problem
    html.Div([
        # Info on binomial equations div
        html.Div([
            html.P(['The ', html.A(['birthday problem'], href='https://en.wikipedia.org/wiki/Birthday_problem'),
                    ' is a probability problem...']),
        ], style={'border': border2}),
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
                    ], style={'border': border2}),

                ]),

            ], id='birthday_details')
        ])
    ], style={'border': border1}),
    html.Br(),
    # Div containing everything matrix
    html.Div([
        # Details on matrix goes here
        html.Div([
            html.P(['Generate a ', html.A(['matrix'], href='https://en.wikipedia.org/wiki/Matrix'), ]),
        ]),

        html.Div([
            html.Details([
                html.Summary('Matrix'),
                # Input goes here
                html.Div([
                    # Row dropdown
                    html.Label('Number of rows'),
                    dcc.Dropdown(
                        id='row_dropdown',
                        options=dropdown_options,
                    ),
                    html.Label('Number of columns'),
                    dcc.Dropdown(
                        id='column_dropdown',
                        options=dropdown_options,
                    ),
                ]),
                # Output goes here
                html.Div([
                    # Matrix one
                    html.Div([], id='output_area_matrix_1'),
                    # Matrix two
                    html.Div([], id='output_area_matrix_2')
                ])
            ])
        ]),

    ])

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
              [State('number_of_people_field', 'value')])
def birth_day_problem(click, value):
    if click is None or value is None:
        return
    return str(math_work.same_birthday_probability(value))


@app.callback(Output('output_area_matrix_1', 'children'),
              [Input('row_dropdown', 'value'),
               Input('column_dropdown', 'value')])
def generate_matrix(row_number, column_number):
    # To prevent an error when callbacks are called on page load.
    if row_number is None or column_number is None:
        return
    table = new_table(row_number, column_number)
    return table


def new_table(row_number, column_number):
    print('generating table')
    # Generates a table, representing a matrix, with row_number rows and column number columns

    tr_list = []

    row_id = 0
    for r in range(row_number):
        row = []
        row_id += 1
        col_id = 0
        for c in range(column_number):
            col_id += 1
            id = 'r'+str(row_id)+'c'+str(col_id)
            print(id)
            row.append(html.Td(dcc.Input(type='text', id=id)))
        tr_list.append(html.Tr(row))

    return html.Table(
        tr_list
    )


if __name__ == '__main__':
    app.run_server(debug=True)
