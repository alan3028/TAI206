from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# URL del servicio FastAPI dentro de Docker
FASTAPI_URL = "http://fastapi_app:5000/v1/usuarios/"

# Mostrar tabla
@app.route("/")
def index():
    response = request.get(FASTAPI_URL)
    data = response.json()
    usuarios = data["data"]
    return render_template("index.html", usuarios=usuarios)

# Agregar citas
@app.route("/agregar", methods=["POST"])
def agregar():
    nuevo_usuario = {
        "id": int(request.form["id"]),
        "nombre": request.form["nombre"],
        "edad": int(request.form["edad"])
    }
    request.post(FASTAPI_URL, json=nuevo_usuario)
    return redirect("/")

# Eliminar citas 
@app.route("/eliminar/<int:id>")
def eliminar(id):
    request.delete(FASTAPI_URL + str(id))
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
