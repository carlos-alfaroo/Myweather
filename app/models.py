from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# --- Usuario ---
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    consultas = db.relationship('Consulta', backref='usuario', lazy=True)

# --- Consulta ---
class Consulta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    fecha_consulta = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_objetivo = db.Column(db.Date, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    actividad_opcional = db.Column(db.String(100))
    estado = db.Column(db.String(20), default='pendiente')  # pendiente, exitoso, error

    peticiones = db.relationship('PeticionAPI', backref='consulta', lazy=True)
    pronosticos = db.relationship('Pronostico', backref='consulta', lazy=True)
    recomendaciones = db.relationship('Recomendacion', backref='consulta', lazy=True)
    errores = db.relationship('ErrorLog', backref='consulta', lazy=True)

# --- Fuente de Clima ---
class FuenteClima(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    base_url = db.Column(db.String(200), nullable=False)

    peticiones = db.relationship('PeticionAPI', backref='fuente', lazy=True)

# --- Petición a API ---
class PeticionAPI(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consulta_id = db.Column(db.Integer, db.ForeignKey('consulta.id'), nullable=False)
    fuente_id = db.Column(db.Integer, db.ForeignKey('fuente_clima.id'), nullable=False)
    endpoint = db.Column(db.String(200))
    status_code = db.Column(db.Integer)
    duracion_ms = db.Column(db.Integer)
    error_msg = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# --- Pronóstico ---
class Pronostico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consulta_id = db.Column(db.Integer, db.ForeignKey('consulta.id'), nullable=False)
    hora_inicio = db.Column(db.DateTime)
    hora_fin = db.Column(db.DateTime)
    p_calor_extremo = db.Column(db.Float)
    p_frio_extremo = db.Column(db.Float)
    p_viento_fuerte = db.Column(db.Float)
    p_lluvia_intensa = db.Column(db.Float)
    p_incomodidad = db.Column(db.Float)

# --- Recomendación ---
class Recomendacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consulta_id = db.Column(db.Integer, db.ForeignKey('consulta.id'), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(50))  # equipo, horario, alternativa

# --- Error Log ---
class ErrorLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consulta_id = db.Column(db.Integer, db.ForeignKey('consulta.id'))
    origen = db.Column(db.String(50))  # api, red, app
    mensaje = db.Column(db.String(255))
    detalle = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)