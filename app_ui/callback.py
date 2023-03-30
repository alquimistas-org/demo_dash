from app import app
from dash import Input, Output


@app.callback(
    Output('output_in_line', 'children'),
    Input('demo_dropdown', 'value')
)
def update_output_in_line(value):
    return f'You have selected:  {value}'


@app.callback(
    Output('output_with_classes', 'children'),
    Input('input_with_classes', 'value')
)
def update_output_in_class(value):
    return f'You are writing: {value}'
