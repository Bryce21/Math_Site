import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
import pprint
import math_work
import itertools
import numpy as np
from numpy.linalg import inv

border1 = ''
border2 = ''
border3 = ''

answer_options = {
    '1': {
        '1': 'answer_matrix_output_div_1x1',
        '2': 'answer_matrix_output_div_1x2',
        '3': 'answer_matrix_output_div_1x3',
        '4': 'answer_matrix_output_div_1x4',
        '5': 'answer_matrix_output_div_1x5'
    },
    '2': {
        '1': 'answer_matrix_output_div_2x1',
        '2': 'answer_matrix_output_div_2x2',
        '3': 'answer_matrix_output_div_2x3',
        '4': 'answer_matrix_output_div_2x4',
        '5': 'answer_matrix_output_div_2x5'
    },
    '3': {
        '1': 'answer_matrix_output_div_3x1',
        '2': 'answer_matrix_output_div_3x2',
        '3': 'answer_matrix_output_div_3x3',
        '4': 'answer_matrix_output_div_3x4',
        '5': 'answer_matrix_output_div_3x5'
    },
    '4': {
        '1': 'answer_matrix_output_div_4x1',
        '2': 'answer_matrix_output_div_4x2',
        '3': 'answer_matrix_output_div_4x3',
        '4': 'answer_matrix_output_div_4x4',
        '5': 'answer_matrix_output_div_4x5'
    },
    '5': {
        '1': 'answer_matrix_output_div_5x1',
        '2': 'answer_matrix_output_div_5x2',
        '3': 'answer_matrix_output_div_5x3',
        '4': 'answer_matrix_output_div_5x4',
        '5': 'answer_matrix_output_div_5x5'
    }
}

dropdown_options = []
for x in range(1, 6):
    dict = {'label': x, 'value': x}
    dropdown_options.append(dict)

layout = html.Div([
    html.Div(style={'display': 'none'}, id='hidden_div_1'),
    # Header div

    # Div containing everything matrix
    html.Div([
        # Details on matrix goes here
        html.Div([
            html.P(['Generate a ', html.A(['matrix'], href='https://en.wikipedia.org/wiki/Matrix'), ]),
        ]),

        html.Div([
            html.Div([
                html.Label('Row: '),
                dcc.Dropdown(
                    options=dropdown_options,
                    id='row_dropdown',

                ),
                html.Label('Column: '),
                dcc.Dropdown(
                    options=dropdown_options,
                    id='column_dropdown',

                ),
                # When dealing with matrices of different sizes will need something like this
                # dcc.RadioItems(
                #     options=[
                #         {'label': 'Two matrices of same size', 'value': 'two_matrices'},
                #     ],
                #     value='two_matrices',
                #     id="two_matrices_checklist"
                # ),

                html.Button(id='generate_matrix_submit_button', children='Ok'),
                html.Div(id='generate_matrix_output_div')

            ]),

        ]),

    ], className='centered', id="matrix_div")

])


def generate_table(row_number, column_number, table_id):
    tr_list = []
    row_id = 0
    for r in range(row_number):
        row = []
        row_id += 1
        col_id = 0
        for c in range(column_number):
            col_id += 1
            id = 't' + str(table_id) + '_r' + str(row_id) + '_c' + str(col_id)
            row.append(html.Td(dcc.Input(type='number', id=id, placeholder=id)))
        tr_list.append(html.Tr(row))
    return tr_list


def generate_table_from_data(row_number, column_number, data):
    tr_list = []
    for r in range(row_number):
        row = []
        for c in range(column_number):
            row.append(html.Td(dcc.Input(type='number', value=data[r][c])))
        tr_list.append(html.Tr(row))
    return tr_list


def new_table(row_number, column_number):
    output_id = answer_options.get(str(row_number)).get(str(column_number))
    return html.Div([
        html.Div([
            html.Div([
                html.P('Matrix 1'),
                html.Table(generate_table(row_number, column_number, 1),
                           id='table1')
            ]),

            html.Div([
                html.P('Matrix 2'),
                html.Table(generate_table(row_number, column_number, 2),
                           id='table2')
            ])

        ]),
        html.Div(id=output_id, children='Answer here'),
        html.Br(),
        html.Div([
            dcc.RadioItems(
                options=[
                    {'label': 'Add', 'value': 'add'},
                    {'label': 'Subtract', 'value': 'sub'},
                    {'label': 'Multiply', 'value': 'mul'},
                    {'label': 'Invert Matrix One', 'value': 'inv'}
                ],
                value='add',
                id='answer_matrix_radio'
            ),

            html.Button(id='answer_matrix_submit_button', type='submit', children='Compute Matrix'),

        ])

    ], style={})


@app.callback(Output('generate_matrix_output_div', 'children'),
              [Input('generate_matrix_submit_button', 'n_clicks')],
              [State('row_dropdown', 'value'),
               State('column_dropdown', 'value')])
def generate_matrix(click, row_number, column_number):
    if click is None:
        return
    return html.Div([
        new_table(row_number, column_number)
    ])


def pull_out_matrixes(column, start, end, *args):
    col_count = 0
    row_count = 0
    matrix = []
    row_list = []
    for keys in args[start:end]:
        col_count += 1
        if col_count <= column:
            row_list.append(keys)
        if col_count == column:
            col_count = 0
            row_count += 1
            matrix.append(row_list)
            row_list = []
    return matrix


# Answer the matrix in here
def generate_output_callback(row, column):
    def output_callback(click, *args):
        # This function can display different outputs depending on
        # the values of the dynamic controls
        if click is None:
            return
        matrix1 = np.array(pull_out_matrixes(column, 0, int(len(args) / 2), *args))
        matrix2 = np.array(pull_out_matrixes(column, int(len(args) / 2), int(len(args)), *args))

        what_to_do = args[int(len(args) - 1)]

        if what_to_do == 'sub':
            what_to_display = html.Table(
                generate_table_from_data(row, column, (matrix1 - matrix2))
            )
        elif what_to_do == 'mul':
            what_to_display = html.Table(
                generate_table_from_data(row, column, (np.dot(matrix1, matrix2)))
            )
        elif what_to_do == 'inv':
            # requires a square matrix so need to have same size row and column
            if row == column:
                try:
                    what_to_display = html.Table(
                        generate_table_from_data(row, column, inv(matrix1))
                    )
                except:
                    what_to_display = "Matrix is not invertable."
            else:
                what_to_display = "Matrix has to be square in order to be inverted!"
        else:
            what_to_display = html.Table(
                generate_table_from_data(row, column, (matrix1 + matrix2))
            )

        return html.Div([
            html.Hr(),
            "Answer: ",
            what_to_display
        ])

    return output_callback


for value1, value2 in itertools.product(
        # For each dropdown (One defining # of rows, the other defining # of columns
        [o['value'] for o in layout['row_dropdown'].options],
        [o['value'] for o in layout['column_dropdown'].options]):
    app.callback(
        # Get the output from dictionary depending on what the current row and column number is
        Output(answer_options.get(str(value1)).get(str(value2)), 'children'),
        # Input will always be the same - a button
        [Input('answer_matrix_submit_button', 'n_clicks')],
        # Have to generate states representing the dcc.Inputs based on what the current row/col count is. +1 because it's a list
        [State('t{}_r{}_c{}'.format(t, r, c), 'value') for t in range(1, 3) for r in
         range(1, value1 + 1) for c in range(1, value2 + 1)] + [State('answer_matrix_radio', 'value')])(
        generate_output_callback(value1, value2)
    )
