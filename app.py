import dash
import dash_bootstrap_components as dbc

app = app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.DARKLY,
        dbc.icons.FONT_AWESOME,
    ],
    prevent_initial_callbacks=True,
)

app.title = 'Demo App'
