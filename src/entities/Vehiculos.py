'''
 Autor:     Mario Muñoz Jiménez
 Creado:    08.04.2022
 Archivo:   Vehiculos.py
'''

from pony.orm import *
from entities.Pedidos import Pedidos
from main import db

class Vehiculos(db.Entity):
    _table_ = "Vehiculos"
    id = PrimaryKey(int, auto=True)
    tipo = Required(str)
    matricula = Required(str, unique=True)
    peso_maximo = Required(float)
    reparto = Required(bool)
    lista_pedidos = Optional(str)
    
    def info_de_vehiculo(self):
        return "[%d] Tipo de Vehiculo: %s \nMatricula: %s\nPeso Max.: %.2f Kg\n" % (self.id, self.tipo, self.matricula, self.peso_maximo)
    