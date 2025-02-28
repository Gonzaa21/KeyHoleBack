from flask import Flask
from flask_cors import CORS
from .db import init_db, db

def create_app():
    app = Flask(__name__)
    # Connection to frontend
    CORS(app)
    
    # Configuration
    app.config.from_object("src.config")
    
    # Database
    init_db(app)
    
    # Endpoints
    from .routes import main
    app.register_blueprint(main)

    return app
