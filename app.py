import os
import dash
import dash_bootstrap_components as dbc

assets_path = os.getcwd() + '/app_ui/assets'
external_stylesheets = [
    dbc.themes.DARKLY,
    dbc.icons.FONT_AWESOME,
]

app = app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    prevent_initial_callbacks=True,
    assets_folder=assets_path,
)

app.title = 'Demo App'
