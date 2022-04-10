from flask import Flask, request, Blueprint
from pony import orm
from main import db
import json
from entities import Clientes

app_clientes = Blueprint('clientes', __name__)

@app_clientes.route('/clientes', methods=['GET'])
def get_clients():
    """
    Devuelve todos los clientes
    """
    clients_list = orm.select(c for c in db.Clientes)
    return str(clients_list.to_json)

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
    return str(new_client)

@app_clientes.route('/clientes/<id>', methods=['GET'])
def get_client(id):
    """
    Devuelve cliente con id = <id>
    """
    print(request.json["id"])
    one_client = orm.select(c for c in db.Clientes if c.id == id)
    return one_client

@app_clientes.route('/clientes/<id>', methods=['DELETE'])
def delete_client(id):
    """
    Borra cliente con id = <id>
    """
    print(request.json["id"])
    deleted_client = orm.delete(c for c in db.Clientes if c.id == id)
    return deleted_client

@app_clientes.route('/clientes/<id>', methods=['PUT'])
def update_client(id):
    """
    Actualizar el cliente con id = <id> - json body con los campos a actualizar
    """
    updated_client = db.Clientes(
        id=id,
        nombre=request.json["nombre"],
        apellidos=request.json["apellidos"],
        email=request.json["email"],
        direccion=request.json["direccion"],
        telefono=request.json["telefono"],
        localidad=request.json["localidad"]
    )
    return str(updated_client)
