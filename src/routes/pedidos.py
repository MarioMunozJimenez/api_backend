'''
 Autor:     Mario Muñoz Jiménez
 Creado:    08.04.2022
 Archivo:   pedidos.py
'''

from flask import Flask, request, Blueprint
from pony import orm
from main import db
import json
from entities import Pedidos

app_pedidos = Blueprint('pedidos', __name__)

@app_pedidos.route('/pedidos', methods=['GET'])
def get_orders():
    """
    Devuelve todos los pedidos
    """
    orders_list = orm.select(o for o in db.Pedidos)
    return str(orders_list.show())

@app_pedidos.route('/pedidos', methods=['POST'])
def post_order():
    """
    json body con los campos --> crea un pedido
    """
    new_order = db.Pedidos(
        id_vehiculo=request.json["id_vehiculo"],
        id_posicion=request.json["id_posicion"],
        id_cliente=request.json["id_cliente"],
        historico_posicion=request.json["historico_posicion"],
        peso_pedido=request.json["peso_pedido"],
        fragil=request.json["fragil"],
        dir_destino=request.json["dir_destino"],
        en_reparto=request.json["en_reparto"],
        entregado=request.json["entregado"]
    )
    return str(new_order)

@app_pedidos.route('/pedidos/<id>', methods=['GET'])
def get_order(id):
    """
    Devuelve pedido con id = <id>
    """
    one_order = orm.select(o for o in db.Pedidos if o.id == id)
    return str(one_order.show())

@app_pedidos.route('/pedidos/<id>', methods=['DELETE'])
def delete_order(id):
    """
    Borra pedido con id = <id>
    """
    deleted_order = orm.delete(o for o in db.Pedidos if o.id == id)
    return deleted_order

@app_pedidos.route('/pedidos/<id>', methods=['PUT'])
def update_order(id):
    """
    Actualizar el pedido con id = <id> - json body con los campos a actualizar
    """
    updated_order = db.Pedidos(
        id=id,
        id_vehiculo=request.json["id_vehiculo"],
        id_posicion=request.json["id_posicion"],
        id_cliente=request.json["id_cliente"],
        historico_posicion=request.json["historico_posicion"],
        peso_pedido=request.json["peso_pedido"],
        fragil=request.json["fragil"],
        dir_destino=request.json["dir_destino"],
        en_reparto=request.json["en_reparto"],
        entregado=request.json["entregado"]
    )
    return str(updated_order)

@app_pedidos.route('/pedidos/en-reparto', methods=['GET'])
def get_delivery_orders():
    """
    Devuelve todos los pedidos que están en reparto
    """
    delivery_orders_list = orm.select(o for o in db.Pedidos if o.en_reparto==True)
    return str(delivery_orders_list.show())

@app_pedidos.route('/pedidos/almacen', methods=['GET'])
def get_storage_orders():
    """
    Devuelve todos los pedidos que están en almacén
    """
    storage_orders_list = orm.select(o for o in db.Pedidos if o.en_reparto==False)
    return str(storage_orders_list.show())

@app_pedidos.route('/pedidos/entregados', methods=['GET'])
def get_delivered_orders():
    """
    Devuelve todos los pedidos que han sido entregados
    """
    delivered_orders_list = orm.select(o for o in db.Pedidos if o.entregado==True)
    return str(delivered_orders_list.show())

@app_pedidos.route('/pedidos/<id>/posicion', methods=['GET'])
def get_position_delivery():
    """
    Devuelve la posicion del pedido con id = <id>
    """
    delivery_position = request.json["historico_posicion"]
    return str(delivery_position)

@app_pedidos.route('/pedidos/<id>/posicion', methods=['POST'])
def post_position(id):
    """
    json body con los campos --> añade la posición del pedido id = <id>
    """
    new_position = db.Pedidos(
        historico_posicion=request.json["historico_posicion"]
    )
    return str(new_position)

@app_pedidos.route('/pedidos/<id>/posicion', methods=['PUT'])
def update_position(id):
    """
    actualiza la posición del pedido id = <id>
    """
    updated_position = db.Pedidos(
        id=id,
        historico_posicion=request.json["historico_posicion"]
    )
    return str(updated_position)

