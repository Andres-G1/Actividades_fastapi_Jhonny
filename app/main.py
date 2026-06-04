from fastapi import FastAPI
from app.routers import clientes, bill
from app.database import list_clients, bills, transaction

app = FastAPI()

#Router Client

app.include_router(clientes.router)

#Router Bill

app.include_router(bill.router)

@app.get("/")
async def raiz():
    return {"mensaje": "API funcionando correctamente"}
'''
Create models (transaction, Bill,)
Bill(id, date, client, totalvalue)
transaction(id, description, facture)
'''
"Bill == Factura"
"Git log == Para ver el historial de cambios"
"Git log --oneline == Para ver el historial de cambios en una sola linea"
"Git checkout codigo ==para cambiar a un commit especifico"