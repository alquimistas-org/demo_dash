from dash import html
import dash_bootstrap_components as dbc
from app import app


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
])
