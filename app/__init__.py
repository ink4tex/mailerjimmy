import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(  #Esto es para saber que llaves se tiene que utilizar en la aplicacion y para obtener las variables de entorno
        SENDGRID_KEY = os.environ.get('SENDGRID_API_KEY'), #SENDGRID_KEY Es una API de servicio de correos que es gratis, deja mandar 100 correos al dia.. Esta Variable que va a obtener el valor que posee el sistema operativo
        SECRET_KEY = os.environ.get('SECRET_KEY'),
        DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PORT = os.environ.get('FLASK_DATABASE_PORT'),
        DATABASE_USER = os.environ.get('FLASK_DATABASE_USER'),
        DATABASE_PASSWORD = os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE = os.environ.get('FLASK_DATABASE')
    )
    
    from . import db
    db.init_app(app)

    return app
