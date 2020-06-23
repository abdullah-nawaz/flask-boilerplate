"""Flask CLI/Application entry point."""
import os

from src.flask_boilerplate import create_app, db

app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {"db": db}
