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
- `modelos/facture.py`: modelo de factura.
- `modelos/transaction.py`: modelo de transacción.