from fastapi import APIRouter, HTTPException
from app.models.cliente import Client, Clientcreate, Clientt
from app.database import list_clients

router = APIRouter(
    prefix="/clientes",
    responses={404: {"description": "No encontrado"}}
)


@router.get("/clientes", tags=["clientes"])
async def Listar_clientes():
    return {"clients": list_clients}    

@router.post("/clientes", response_model=Client, tags=["clientes"])
async def create_clients(date_client: Clientcreate):

    Client_val = Clientt.model_validate(date_client.model_dump()) #el model dump convierte el objeto date_client en un diccionario para que pueda ser validado por el modelo Clientt

    Client_val.id = len(list_clients) + 1 #asignamos un id al cliente que se va a crear, el id es igual al tamaño de la lista de clientes + 1
    
    list_clients.append(Client_val) #agregamos el cliente a la lista de clientes
    return Client_val

#reto: crear un nuevo endponint y que me remote un solo cliente 
@router.get("/clientes/{id}", response_model=Client, tags=["clientes"])
async def get_client(id: int):
    for client in list_clients:
        if client.id == id:
            return client
    return {"message": "client not found"}

@router.delete("/clientes/{id}", response_model=Client, tags=["clientes"])
async def delete_client(id: int):
    for client in list_clients:
        if client.id == id:
            list_clients.remove(client) #remove elimina el cliente de la lista de clientes
            return {"message": "client deleted"}
    return {"message": "client not found"}

@router.put("/clientes/{id}", response_model=Client, tags=["clientes"])
async def update_client(id: int, date_client: Clientcreate):
    for client in list_clients:
        if client.id == id:
            cli_val = Clientt.model_validate(date_client.model_dump()) #validamos el cliente que se va a actualizar
            client.name = cli_val.name
            client.age = cli_val.age
            client.description = cli_val.description
            return client