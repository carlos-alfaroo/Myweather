from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    print("Configurando app...")
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave-secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clima.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicialización de extensiones
    db.init_app(app)
    csrf.init_app(app)

    print("Base de datos inicializada")

    # Registro de rutas (blueprint)
    from .routes import main
    app.register_blueprint(main)

    # Retornar la aplicación Flask (clave del error)
    return app
