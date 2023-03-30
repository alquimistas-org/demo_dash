from dash import html
import dash_bootstrap_components as dbc


class HelloComponent:

    def __init__(self, input_id='input', output_id='output') -> None:
        self.input_id = input_id
        self.output_id = output_id

    def create(self) -> dbc.Col:
        layout = dbc.Col([
            dbc.Row(
                dbc.Input(
                    id=self.input_id,
                    placeholder="Type something...",
                    type="text"
                ),
            ),
            html.Br(),
            dbc.Row(
                html.P(id=self.output_id),
            ),
        ])
        return layout
