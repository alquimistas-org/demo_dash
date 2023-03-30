from app import app
from app_ui.layout import app_layout

app.layout = app_layout

if __name__ == "__main__":
    app.run_server()
