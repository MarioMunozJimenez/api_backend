from tokenize import Double
from pony.orm import *
from main import db
from entities import Posicion

class Pedidos(db.Entity):
    _table_ = "Pedidos"
    id = PrimaryKey(int, auto=True)
    id_vehiculo = Required(int)
    id_posicion = Required(int)
    id_cliente = Required(int)
    historico_posicion = Required(Posicion)
    peso_pedido = Required(float)
    fragil = Required(bool)
    dir_destino = Required(str)
    en_reparto = Required(bool)
    entregado = Required(bool)
