from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app import db
from app.models import Usuario, Consulta, Pronostico
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
    return render_template('resultado.html', consulta=consulta, pronost