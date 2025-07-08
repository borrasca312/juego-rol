from flask import Flask
from routes import usuario_routes, raza_routes

app = Flask(__name__)


app.register_blueprint(usuario_routes.bp)
app.register_blueprint(raza_routes.bp)

if __name__ == "__main__":
    app.run(debug=True)
