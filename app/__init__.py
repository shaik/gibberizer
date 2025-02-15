"""
Flask application initialization.
"""
from flask import Flask
from pathlib import Path


def create_app(test_config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Ensure the data directory exists
    data_dir = Path(app.root_path).parent / "data"
    data_dir.mkdir(exist_ok=True)
    
    if test_config is None:
        # Load config from config.py if it exists
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)
    
    # Register routes
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app
