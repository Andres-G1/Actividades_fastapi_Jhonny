# Proyecto Python de Facturas y Clientes

## Qué eh hecho hasta el momento

- Nos enseñaron las dos  formas de instalar fastapi, tanto con pip como con uv.
- Al final decidi usar uv, para usar uv toca primero instalarlo con pip install uv.
- Seguido de eso se inicia el proyecto con uv init.
- Despues se hace la instalacion del framework el cual es fastapi de la siguiente forma uv add 'fastapi[standard]'.
- por ultimo se modifica el `main.py` con lo que se necesita en este caso funcion del cliente, factura y transaccion se crean los metodos de ver, eliminar, agregar, editar, buscar por id.

## Estructura actual del proyecto

- `main.py`: define los endpoints de FastAPI y la lógica de creación/listado.
- `modelos/cliente.py`: modelo de cliente.
- `modelos/bill.py`: modelo de factura.
- `modelos/transaction.py`: modelo de transacción.

## Estructura de carpetas

- Creamos una carpeta a `app`.
- Dentro de esa carpeta se organiza el achivo `main.py` y creamos  otro llamado `database.py`.
- Dentro de esta carpeta agregamos dos carpetas `Models` y `Routers`.
- En `Modeles` ubicamos los archivos donde tenemos las clases de cliente y factura.
- En `Routers` ubicamos el archivo `clientes.py`.

## Ordenamiento de carpetas y Conexion con la BD

- Creamos la carpeta `router` dentro de la carpeta `app`.
- Dentro de esa carpeta creamos los archivos `cliente.py`, `bill.py` y `transactions.py`.
- Importamos con `from flask import APIRouter`.
- Limpiamos el main.py en este solo vamos a colocar `app.include_router(clientes.router)` o `(Bills.router) `.
- Por ultimo añadimos con uv sqlite y en el archivo `databse.py` lo configuramos.

## Conexion de los modelos con la base de datos

- Terminamos de hacer la conexion de la base de datos primero creamos 
`Sesion_dependencia` dentro del archivo `database.py`.
- Seguido de esto en los models `cliente.py`, `bill.py` y `transactions.py`,
los conectamos con `sqlmodel` en el cual vamos de paso a dejar el `Field`, `Relationship`, para los campos que vamos a llenar y de paso dejamos para hacer las relaciones de los modelos.
- En los archivos de `Router`, para subir los cambios hacemos uso de `add,commit,refresh` no en todos,
pero si en los create, alter y delete, en el caso del delete `delete`.
- Hacemos las relaciones del modelo `client` con el modelo `bill` y `bill` con `Transactions`, en el caso de client para que nos pueda mostrar el nombre del cliente en la factura y en el caso de trasaccion para poder,
ver las transacciones del cliente mas lo que gasta la persona.