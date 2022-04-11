'''
 Autor:     Mario Muñoz Jiménez
 Creado:    08.04.2022
 Archivo:   Pedidos.py
'''

from array import array
from pony.orm import *
from main import db
from entities import Posicion

class Pedidos(db.Entity):
    _table_ = "Pedidos"
    id = PrimaryKey(int, auto=True)
    id_vehiculo = Required(int)
    id_posicion = Required(int)
    id_cliente = Required(int)
    historico_posicion = Required(str)
    peso_pedido = Required(float)
    fragil = Required(bool)
    dir_destino = Required(str)
    en_reparto = Required(bool)
    entregado = Required(bool)
