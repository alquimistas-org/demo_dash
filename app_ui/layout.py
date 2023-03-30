from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app
from app_ui.components.hello_component import HelloComponent


app_layout = html.Div([

    dbc.Row([
        dbc.Col(
            html.Img(
                src=app.get_asset_url('python.svg'),
                id='initial_image',
                style={
                    "height": "100px",
                    "width": "auto",
                    "margin-bottom": "25px",
                },
            ),
            width=2,
        ),
        dbc.Col(html.H5("Demo App", className="display-3")),
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                options=['Lucas', 'Agus', 'Nati', 'Guille', 'Mati'],
                value='Agus',
                id='demo_dropdown'
            ),
        ]),
        dbc.Col([
            html.Div(id='output_in_line'),
        ]),
    ]),

    html.Br(),

    dbc.Row([
        HelloComponent(
            input_id='input_with_classes',
            output_id='output_with_classes'
        ).create()
    ]),
])
