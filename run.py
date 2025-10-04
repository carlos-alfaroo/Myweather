from app import create_app, db
from app.models import Usuario, Consulta, Pronostico, FuenteClima, PeticionAPI, Recomendacion, ErrorLog 
print("Inicializando app...")  # <-- prueba
app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
