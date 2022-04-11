'''
 Autor:     Mario Muñoz Jiménez
 Creado:    08.04.2022
 Archivo:   Posicion.py
'''

from pony.orm import *
from main import db
import datetime as date

class Posicion(db.Entity):
    _table_ = "Posicion"
    id = PrimaryKey(int, auto=True)
    latitud = Required(float)
    longitud = Required(float)
    altitud = Required(float)
    ultima_actualizacion = Required(date.datetime)
