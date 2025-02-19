from flask import Flask
from flask_cors import CORS

from .db import init_db

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.config.from_object("app.config")

    init_db(app)

    from .routes import main
    app.register_blueprint(main)

    return app
