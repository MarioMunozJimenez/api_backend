from pony.orm import *
from main import db

class Clientes(db.Entity):
    _table_ = "Clientes"
    id = PrimaryKey(int, auto=True)
    nombre = Required(str)
    apellidos = Required(str)
    email = Required(str, unique=True)
    direccion = Required(str)
    telefono = Required(str, unique=True)
    localidad = Required(str)

    def lugar_de_envio(self):
        return "%s, %s" % (self.direccion, self.localidad)
    