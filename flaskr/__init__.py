from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY:DATABASE_URI'] = 'sqlite:///tutorial_Canciones.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
