from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField
from wtforms.validators import DataRequired

class ConsultaForm(FlaskForm):
    fecha_objetivo = DateField('Fecha objetivo', validators=[DataRequired()])
    lat = FloatField('Latitud', validators=[DataRequired()])
    lon = FloatField('Longitud', validators=[DataRequired()])
    actividad = StringField('Actividad (opcional)')
    submit = SubmitField('Consultar clima')