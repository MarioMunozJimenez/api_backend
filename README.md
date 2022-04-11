# api_backend

<body bgcolor="#336655">

#### API Backend Development Challenge
---

## Escenario

- Una empresa de paquetería ha creado una nueva función para sus clientes, que les permite rastrear en tiempo real dónde se encuentra su pedido y en qué vehículo. Actualmente, ya cuenta con una aplicación móvil y un sitio web, por lo que se le pide que cree una nueva API Backend con la que los vehículos puedan conectarse y añadir pedidos a su reparto y los usuarios puedan obtener la posición actual de su pedido y el vehículo que realizará la entrega indicando el número de pedido.
&nbsp;
- Puede trabajar con puntos de datos del Sistema de Posicionamiento Global (coordenadas geográficas).

---

## Instalación

Configuración y puesta en marcha del entorno de desarrollo virtual ([venv](https://docs.python.org/3/library/venv.html)).

```bash
pip3 install virtualenv
python3 -m venv venv
```
Se lanza __venv__ de la siguiente forma (para Windows PowerShell).

```bash
.\venv\Scripts\activate
```
Una vez establecido el entorno virtual se procede a la instalación de los paquetes esenciales.

Instalación __[Flask](https://flask.palletsprojects.com/en/2.1.x/installation/)__.
```bash
pip install flask
```
Se configura la variable de entorno 'FLASK_APP' para que reconozca nuestro programa principal.
```bash
$env:FLASK_APP = "main"
```

Instalación de __[dotenv](https://pypi.org/project/python-dotenv/)__ de Python. Lee los valores en un archivo .env y los establece como variables de entorno.
```bash
pip3 install python-dotenv
```

Se descargan e instalan los paquetes de __[Pony ORM](https://docs.ponyorm.org/firststeps.html)__, para poder trabajar con el contenido de las bases de datos en forma de objetos reconocidos en Python.
```bash
pip install pony
```
Se usa a su vez el driver Psycopg para adaptar __[PostgreSQL](https://www.postgresql.org/)__ en el lenguaje Python. PostgreSQL permite establecer y gestionar las bases de datos relacionales del proyecto.
```bash
pip install psycopg2
```

También se requiere el uso de __[Docker](https://docs.docker.com/get-docker/)__ (Docker Desktop para Windows) y __[Postman](https://www.postman.com/downloads/)__, para la configuración y manejo de contenedores de aplicaciones como para el uso de métodos de servicios REST (operaciones CRUD) respectivamente.


---
## Referencia API

##### Obtener todos los vehículos

```http
  GET /vehiculos
```

##### Crear un nuevo vehículo

```http
  POST /vehiculos
```

##### Obtener el vehículo con \<id> determinado

```http
  GET /vehiculos/<id>
```

##### Borrar el vehículo con \<id> determinado

```http
  DELETE /vehiculos/<id>
```

##### Actualizar el vehículo con \<id> determinado

```http
  PUT /vehiculos/<id>
```

##### Obtener los vehículos en reparto

```http
  GET /vehiculos/reparto
```

##### Asignar un pedido a un vehículo

```http
  POST /vehiculos/<id>/pedido/<id_pedido>
```

##### Obtener todos los clientes

```http
  GET /clientes
```

##### Crear un nuevo cliente

```http
  POST /clientes
```

##### Obtener el cliente con \<id> determinado

```http
  GET /clientes/<id>
```

##### Borrar el cliente con \<id> determinado

```http
  DELETE /clientes/<id>
```

##### Actualizar el cliente con \<id> determinado

```http
  PUT /clientes/<id>
```

##### Obtener todos los pedidos

```http
  GET /pedidos
```

##### Crear un nuevo pedido

```http
  POST /pedidos
```

##### Obtener el pedido con \<id> determinado

```http
  GET /pedidos/<id>
```

##### Borrar el pedido con \<id> determinado

```http
  DELETE /pedidos/<id>
```

##### Actualizar el pedido con \<id> determinado

```http
  PUT /pedidos/<id>
```

##### Obtener solo los pedidos en reparto

```http
  GET /pedidos/en-reparto
```

##### Obtener solo los pedidos en el almacén

```http
  GET /pedidos/almacen
```

##### Obtener solo los pedidos entregados

```http
  GET /pedidos/entregados
```

##### Obtener la posición del pedido con \<id> determinado

```http
  GET /pedidos/<id>/posicion
```

##### Añadir posición al pedido con \<id> determinado

```http
  POST /pedidos/<id>/posicion
```

##### Actualizar la posición del pedido con \<id> determinado

```http
  PUT /pedidos/<id>/posicion
```
---

## Estructura de la base de datos

![UML Backend Database](https://i.imgur.com/nrDFw32.png)

---
