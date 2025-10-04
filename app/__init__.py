from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    from flask import Flask
    from .models import db

    print("Configurando app...")
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave-secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clima.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    print("Base de datos inicializada")

    # Temporal: comentar db.create_all() aquí
    # with app.app_context():
    #     db.create_all()
    #     print("Tablas creadas")

    from . import routes