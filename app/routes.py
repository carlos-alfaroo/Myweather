from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app import db
from app.models import Usuario, Consulta, Pronostico, FuenteClima, PeticionAPI, Recomendacion, ErrorLog 
from app.forms import ConsultaForm
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    form = ConsultaForm()
    return render_template('index.html', form=form)

@main.route('/consultar', methods=['POST'])
def consultar():
    form = ConsultaForm()
    if form.validate_on_submit():
        nueva_consulta = Consulta(
            user_id=1,  # temporal (hasta tener sistema de login)
            fecha_consulta=datetime.utcnow(),
            fecha_objetivo=form.fecha_objetivo.data,
            lat=form.lat.data,
            lon=form.lon.data,
            actividad_opcional=form.actividad.data,
            estado='pendiente'
        )
        db.session.add(nueva_consulta)
        db.session.commit()
        flash('Consulta registrada con éxito.', 'success')
        return redirect(url_for('main.resultado', consulta_id=nueva_consulta.id))
    flash('Error al registrar la consulta.', 'danger')
    return redirect(url_for('main.index'))

@main.route('/resultado/<int:consulta_id>')
def resultado(consulta_id):
    consulta = Consulta.query.get_or_404(consulta_id)
    pronosticos = Pronostico.query.filter_by(consulta_id=consulta_id).all()
    return render_template('resultado.html', consulta=consulta, pronosticos=pronosticos)
  
# Endpoint para recibir lat/lon del mapa
@main.route('/get_location', methods=['POST'])
def get_location():
    data = request.get_json()
    lat = data.get('lat')
    lon = data.get('lon')
    print(f"Ubicación recibida: {lat}, {lon}")
    return jsonify({'status': 'success', 'lat': lat, 'lon': lon})



@main.route('/forecast')
def forecast():
    # Datos de ejemplo para mostrar
    data = {
        "location": "Blue Ridge, GA 30513",
        "date": "July 22, 2023",
        "risks": [
            {"label": "Very Hot", "value": 52, "desc": "Potentially hot, but not extreme."},
            {"label": "Very Cold", "value": 5, "desc": "Little to no chance of cold weather."},
            {"label": "Very Wet", "value": 82, "desc": "High chance of rain. You may want to bring an umbrella."},
            {"label": "Very Uncomfortable", "value": 4, "desc": "Mild discomfort possible."}
        ]
    }
    return render_template('forecast.html', data=data)

@main.route('/datasources')
def datasources():
    return render_template('datasources.html')

@main.route('/credits')
def credits():
    return render_template('credits.html')