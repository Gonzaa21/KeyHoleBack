import mysql.connector
from flask import g

def get_db():
    if "db" not in g:
        g.db = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_password",
            database="nombre_de_tu_db"
        )
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db(app):
    app.teardown_appcontext(close_db)
