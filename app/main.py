from fastapi import FastAPI
from models.cliente import Client, Clientcreate, Clientt
from models.bill import Bill, createbill, updatebill, transactions, transactioncreate, transactiont

app = FastAPI()

list_clients: list[Client] = []
bills: list[Bill] = []
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
Create models (transaction, Bill,)
Bill(id, date, client, totalvalue)
transaction(id, description, facture)
'''
# BILLS ENDPOINTS
@app.get("/facturas")
async def list_bills():
    return {"bills": bills}

@app.post("/facturas/{id_client}", response_model=Bill)
async def create_bill(data_bill: createbill):
    if data_bill.id_client not in [client.id for client in list_clients]: #verificamos que el id del cliente exista en la lista de clientes
        return {"message": "client not found"}

    bill_val = updatebill.model_validate(data_bill.model_dump()) #validamos la factura que se va a crear

    bill_val.id = len(bills) + 1 #asignamos un id a la factura que se va a crear, el id es igual al tamaño de la lista de facturas + 1
    
    bills.append(bill_val) #agregamos la factura a la lista de facturas
        #return the bill_val with the information about the client whit this id_client
    return bill_val

@app.get("/facturas/{id}", response_model=Bill)
async def get_bill(id: int):
    for bil in bills:
        if bil.id == id:
            return bil
    return {"message": "bill not found"}

@app.delete("/facturas/{id}")
async def delete_bill(id: int):
    for bil in bills:
        if bil.id == id:
            bills.remove(bil)
            return {"message": "bill deleted"}
    return {"message": "bill not found"}

@app.put("/facturas/{id}", response_model=Bill)
async def update_bill(id: int, data_bill: createbill):
    for bil in bills:
        if bil.id == id:
            bill_val = updatebill.model_validate(data_bill.model_dump()) #validamos la factura que se va a actualizar
            bil.date = bill_val.date
            bil.id_client = bill_val.id_client
            bil.totalvalue = bill_val.totalvalue
            return bil
    return {"message": "bill not found"}

# TRANSACTIONS ENDPOINTS
@app.get("/transactions")
async def list_transactions():
    return {"transactions": transaction}

@app.post("/transactions", response_model=transactions)
async def create_transaction(data_transaction: transactioncreate):
    if data_transaction.bill_id not in [bil.id for bil in bills]: #verificamos que el id de la factura exista en la lista de facturas
        return {"message": "bill not found"}

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
            transac.bill_id = transaction_val.bill_id
            return transac
    return {"error":"Transaction not found"}


"Bill == Factura"