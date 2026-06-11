from fastapi import FastAPI
from app.routers import clientes, bill, transactions, list_clients, bills, transaction

app = FastAPI()

#Router Client

app.include_router(clientes.router)

#Router Bill

app.include_router(bill.router)

#Router Transactions

app.include_router(transactions.router)

'''
Create models (transaction, Bill,)
Bill(id, date, client, totalvalue)
transaction(id, description, facture)
'''
"Bill == Factura"
"Git log == Para ver el historial de cambios"
"Git log --oneline == Para ver el historial de cambios en una sola linea"
"Git checkout codigo ==para cambiar a un commit especifico"