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