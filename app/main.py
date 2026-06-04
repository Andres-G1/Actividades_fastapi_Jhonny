from fastapi import FastAPI
from models.cliente import Client, Clientcreate, Clientt
from models.facture import Facture, createfacture, updatefacture, transactions, transactioncreate, transactiont

app = FastAPI()

list_clients: list[Client] = []
facture: list[Facture] = []
transaction: list[transactions] = []

#models

@app.get("/clientes")
async def Listar_clientes():
    return {"clients": list_clients}

@app.post("/clientes", response_model=Client)
async def create_clients(date_client: Clientcreate):

    Client_val = Clientt.model_validate(date_client.model_dump()) #el model dump convierte el objeto date_client en un diccionario para que pueda ser validado por el modelo Clientt

    Client_val.id = len(list_clients) + 1 #asignamos un id al cliente que se va a crear, el id es igual al tamaño de la lista de clientes + 1
    
    list_clients.append(Client_val) #agregamos el cliente a la lista de clientes
    return Client_val

#reto: crear un nuevo endponint y que me remote un solo cliente 
@app.get("/clientes/{id}", response_model=Client)
async def get_client(id: int):
    for client in list_clients:
        if client.id == id:
            return client
    return {"message": "client not found"}

@app.delete("/clientes/{id}", response_model=Client)
async def delete_client(id: int):
    for client in list_clients:
        if client.id == id:
            list_clients.remove(client) #remove elimina el cliente de la lista de clientes
            return {"message": "client deleted"}
    return {"message": "client not found"}

@app.put("/clientes/{id}", response_model=Client)
async def update_client(id: int, date_client: Clientcreate):
    for client in list_clients:
        if client.id == id:
            cli_val = Clientt.model_validate(date_client.model_dump()) #validamos el cliente que se va a actualizar
            client.name = cli_val.name
            client.age = cli_val.age
            client.description = cli_val.description
            return client


'''
Create models (transaction, facture,)
Facture/(id, date, client, totalvalue)
transaction(id, description, facture)
'''
# FACTURES ENDPOINTS
@app.get("/facturas")
async def list_factures():
    return {"factures": facture}

@app.post("/facturas/{id_client}", response_model=Facture)
async def create_facture(data_facture: createfacture):
    if data_facture.id_client not in [client.id for client in list_clients]: #verificamos que el id del cliente exista en la lista de clientes
        return {"message": "client not found"}

    facture_val = updatefacture.model_validate(data_facture.model_dump()) #validamos la factura que se va a crear

    facture_val.id = len(facture) + 1 #asignamos un id a la factura que se va a crear, el id es igual al tamaño de la lista de facturas + 1
    
    facture.append(facture_val) #agregamos la factura a la lista de facturas
        #return the facture_val with the information about the client whit this id_client
    return facture_val

@app.get("/facturas/{id}", response_model=Facture)
async def get_facture(id: int):
    for fac in facture:
        if fac.id == id:
            return fac
    return {"message": "facture not found"}

@app.delete("/facturas/{id}")
async def delete_facture(id: int):
    for fac in facture:
        if fac.id == id:
            facture.remove(fac)
            return {"message": "facture deleted"}
    return {"message": "facture not found"}

@app.put("/facturas/{id}", response_model=Facture)
async def update_facture(id: int, data_facture: createfacture):
    for fac in facture:
        if fac.id == id:
            facture_val = updatefacture.model_validate(data_facture.model_dump()) #validamos la factura que se va a actualizar
            fac.date = facture_val.date
            fac.id_client = facture_val.id_client
            fac.totalvalue = facture_val.totalvalue
            return fac
    return {"message": "facture not found"}

# TRANSACTIONS ENDPOINTS
@app.get("/transactions")
async def list_transactions():
    return {"transactions": transaction}

@app.post("/transactions", response_model=transactions)
async def create_transaction(data_transaction: transactioncreate):
    if data_transaction.facture_id not in [fac.id for fac in facture]: #verificamos que el id de la factura exista en la lista de facturas
        return {"message": "facture not found"}

    transaction_val = transactiont.model_validate(data_transaction.model_dump()) #validamos la transaccion que se va a crear

    transaction_val.id = len(transaction) + 1 #asignamos un id a la transaccion que se va a crear, el id es igual al tamaño de la lista de transacciones + 1
    
    transaction.append(transaction_val)
    return transaction_val

@app.get("/transactions/{id}", response_model=transactions)
async def get_transaction(id: int):
    for transac in transaction:
        if transac.id == id:
            return transac
    return {"message": "transaction not found"}

@app.delete("/transactions/{id}")
async def delete_transaction(id: int):
    for transac in transaction:
        if transac.id == id:
            transaction.remove(transac)
            return {"message": "transaction deleted"}
    return {"message": "transaction not found"}

@app.put("/transactions/{id}", response_model=transactions)
async def update_transaction(id: int, data_transaction: transactioncreate): 
    for transac in transaction:
        if transac.id == id:
            transaction_val = transactiont.model_validate(data_transaction.model_dump()) #validamos la transaccion que se va a actualizar
            transac.unitari_value = transaction_val.unitari_value
            transac.cantidad = transaction_val.cantidad
            transac.facture_id = transaction_val.facture_id
            return transac
    return {"error":"Transaction not found"}