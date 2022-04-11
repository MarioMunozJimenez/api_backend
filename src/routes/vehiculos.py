'''
 Autor:     Mario Muñoz Jiménez
 Creado:    08.04.2022
 Archivo:   vehiculos.py
'''

from flask import Flask, request, Blueprint
from pony import orm
from main import db
import json
from entities import Vehiculos

app_vehiculos = Blueprint('vehiculos', __name__)

@app_vehiculos.route('/vehiculos', methods=['GET'])
def get_vehicles():
    """
    Devuelve todos los vehiculos
    """
    vehicles_list = orm.select(v for v in db.Vehiculos)
    return str(vehicles_list.show())

@app_vehiculos.route('/vehiculos', methods=['POST'])
def post_vehicle():
    """
    json body con los campos --> crea un vehiculo
    """
    new_vehicle = db.Vehiculos(
        tipo=request.json["tipo"],
        matricula=request.json["matricula"],
        peso_maximo=request.json["peso_maximo"],
        reparto=request.json["reparto"],
        lista_pedidos=request.json["lista_pedidos"]
    )
    return str(new_vehicle)

@app_vehiculos.route('/vehiculos/<id>', methods=['GET'])
def get_vehicle(id):
    """
    Devuelve vehiculo con id = <id>
    """
    one_vehicle = orm.select(v for v in db.Vehiculos if v.id == id)
    return str(one_vehicle.show())

@app_vehiculos.route('/vehiculos/<id>', methods=['DELETE'])
def delete_vehicle(id):
    """
    Borra vehiculo con id = <id>
    """
    deleted_vehicle = orm.delete(v for v in db.Vehiculos if v.id == id)
    return deleted_vehicle

@app_vehiculos.route('/vehiculos/<id>', methods=['PUT'])
def update_vehicle(id):
    """
    Actualizar el vehiculo con id = <id> - json body con los campos a actualizar
    """
    updated_vehicle = db.Vehiculos(
        id=id,
        tipo=request.json["tipo"],
        matricula=request.json["matricula"],
        peso_maximo=request.json["peso_maximo"],
        reparto=request.json["reparto"],
        lista_pedidos=request.json["lista_pedidos"]
    )
    return str(updated_vehicle)

@app_vehiculos.route('/vehiculos/reparto', methods=['GET'])
def get_delivery_vehicles():
    """
    Devuelve todos los vehiculos que están en reparto
    """
    delivery_vehicles_list = orm.select(v for v in db.Vehiculos if v.reparto==True)
    return str(delivery_vehicles_list.to_json)

@app_vehiculos.route('/vehiculos/<id>/pedido/<id_pedido>', methods=['POST'])
def delivery_for_vehicle(id):
    """
    asigna el pedido id_pedido al vehiculo id = <id>
    """
    vehicles_list = orm.select(v for v in db.Vehiculos)
    for v in vehicles_list:
        if(v.id == id):
            new_order_for_vehicle = db.Pedidos["id"]
    return str(new_order_for_vehicle)