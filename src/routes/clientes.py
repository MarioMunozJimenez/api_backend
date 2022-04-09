from flask import Flask, request, Blueprint
from pony import orm
from main import db
from entities import Clientes

app_clientes = Blueprint('clientes', __name__)

@app_clientes.route('/clientes', methods=['GET'])
def get_clients():
    """
    Devuelve todos los clientes
    """
    clients_list = orm.select(c for c in db.Clientes)
    return str(clients_list)

@app_clientes.route('/clientes', methods=['POST'])
def post_client():
    """
    json body con los campos --> crea un cliente
    """
    new_client = db.Clientes(
        nombre=request.json["nombre"],
        apellidos=request.json["apellidos"],
        email=request.json["email"],
        direccion=request.json["direccion"],
        telefono=request.json["telefono"],
        localidad=request.json["localidad"]
    )
    new_client.save()
    return new_client

@app_clientes.route('/clientes/:id', methods=['GET'])
def get_client():
    return "Devuelve cliente con id = :id"

@app_clientes.route('/clientes/:id', methods=['DELETE'])
def delete_client():
    return "Borra cliente con id = :id"

@app_clientes.route('/clientes/:id', methods=['PUT'])
def update_clients():
    return "Actualizar el cliente con id = :id - json body con los campos a actualizar"