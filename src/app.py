from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient
import certifi
from src.persona import Persona #pruebas con pytest
#from persona import Persona  #cuando se va aejecutar el servidor

MONGO = 'mongodb+srv://jose:Ucundinamarca@cluster0.7cia1qn.mongodb.net/?retryWrites=true&w=majority'
certificado = certifi.where()
client = MongoClient(MONGO, tlsCAFile=certificado)
con_bd = client["bd_personas"]

app = Flask(__name__)

@app.route('/guardar_personas', methods=['POST'])
def agregarPersona():
    personas = con_bd['Personas']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    correo = request.form['correo']
    fecha_nacimiento = request.form['fecha_nacimiento']

    if nombre and apellido and telefono and correo and fecha_nacimiento:
        persona = Persona(nombre, apellido, telefono, correo, fecha_nacimiento)
        personas.insert_one(persona.formato_doc())
        return redirect(url_for('index'))
    else:
        return "Error"
    
@app.route('/eliminar_persona/<string:nombre_persona>')
def eliminar(nombre_persona):
    personas = con_bd['Personas']
    personas.delete_one({'_id': ObjectId (nombre_persona)})
    return redirect(url_for('index'))

@app.route('/editar_persona/<string:nombre_persona>', methods=['POST'])
def editar(nombre_persona):
    personas = con_bd['Personas']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    correo = request.form['correo']
    fecha_nacimiento = request.form['fecha_nacimiento']

    if nombre and apellido and telefono and correo and fecha_nacimiento:
        personas.update_one({'nombre':nombre_persona},{'$set':{'nombre':nombre, 'apellido':apellido, 'telefono':telefono, 'correo':correo, 'fecha_nacimiento':fecha_nacimiento}})
        return redirect(url_for('index'))
    else:
        return "Error de actualizacion"

@app.route('/buscar', methods=['POST'])
def buscar_documentos():
    personas = con_bd['Personas']
    opcion_seleccionada = request.form.get("opciones")
    valor_busqueda = request.form.get("valor_busqueda")

    resultados = personas.find({opcion_seleccionada: valor_busqueda})

    return render_template("index.html", resultados=resultados)

@app.route('/')
def index():
    personas = con_bd['Personas']
    personas = personas.find()
    return render_template('index.html', personas = personas)

if __name__ == '__main__':
    app.run(debug=True)