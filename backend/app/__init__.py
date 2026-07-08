from flask import Flask
from .routes import api

def create_app():
    app=Flask(__name__) #__name__ îi spune lui Flask unde se află fișierele proiectului

    app.config['SECRET_KEY'] = "adam18" 

    app.register_blueprint(api, url_prefix="/api")
    return app
