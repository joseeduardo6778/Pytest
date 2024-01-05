import pytest
from src.app import app
from src.persona import Persona


@pytest.fixture #clases que estan en app se hace un test

#se hace la conexion para la base de datos 
def client():
    with app.test_client() as client:
        yield client
#se hace la prueba del index
def test_index(client):
    #se obtiene la vista
    response = client.get('/')
    #se verificar que en el index se encuentre un h1 y se verifica que sirva la conexion
    assert response.status_code == 200 # es un código de respuesta del servidor HTTP que nos ofrecerá el estatus correcto
    assert b"Trabajo Linea de Profundizacion" in response.data

#Se hace la prueba agregar persona
def test_agregar_persona(client):
    #se envia una secuencia de datos 
    response = client.post('/guardar_personas', data={
        'nombre': 'lucas',
        'apellido': 'castillo',
        'telefono': '3023555342',
        'correo': 'lucascas@example.com',
        'fecha_nacimiento': '1992-01-05'
    })
    #se verifica el envio de este mismo
    assert response.status_code == 302 #el recurso solicitado ha sido movido temporalmente a la URL 

#Se hace la prueba de eliminar personas
def test_eliminar_persona(client):
    # Supongamos que tienes una persona con la id en tu base de datos y se elimina
    response = client.get('/eliminar_persona/6512facf25ad5c3d5c7e9ef4')
    assert response.status_code == 302  #El recurso solicitado ha sido movido temporalmente a la URL

#Se hace la prueba de editar
def test_editar_persona(client):
    #se edita el documento jhon con los siguientes datos
    response = client.post('/editar_persona/John', data={
        'nombre': 'Jane',
        'apellido': 'Doe',
        'telefono': '987654321',
        'correo': 'jane@example.com',
        'fecha_nacimiento': '1990-02-02'
    })
    assert response.status_code == 302  # Debe redirigir después de editar una persona

def test_buscar_documentos(client):
    #Se busca el documento de la clase Personas con el nombre que se le da en parametros
    response = client.post('/buscar', data={
        'opciones': 'nombre',
        'valor_busqueda': 'Jose'
    })
    assert response.status_code == 200  # es un código de respuesta del servidor HTTP que nos ofrecerá el estatus correcto




