'''
 Autor:     Mario Muñoz Jiménez
 Creado:    08.04.2022
 Archivo:   main.py
'''

from dotenv import load_dotenv
from flask import Flask
from pony.orm import Database
from pony.flask import Pony
import os

load_dotenv()
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>API Backend - Página de Bienvenida</h1>"

app.config.update(dict(
    DEBUG = False,
    PONY = {
        'provider': 'postgres',
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASS'),
        'host': 'localhost',
        'database': os.getenv('DB_NAME')
    }
))

db = Database()
from entities import Posicion
from entities import Clientes
from entities import Vehiculos
from entities import Pedidos
db.bind(**app.config['PONY'])
db.generate_mapping(create_tables=True)

Pony(app)

from routes.clientes import app_clientes
app.register_blueprint(app_clientes)

from routes.vehiculos import app_vehiculos
app.register_blueprint(app_vehiculos)

from routes.pedidos import app_pedidos
app.register_blueprint(app_pedidos)
