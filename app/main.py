from fastapi import FastAPI
from .routers.clientes import router_client
from .routers.bill import router_bills 
from .routers.transactions import router_transactions  
from .database import crear_tablas

app = FastAPI(lifespan=crear_tablas)

#Router Client

app.include_router(router_client, tags=["client"])

#Router Bill

app.include_router(router_bills, tags=["bill"])

#Router Transactions

app.include_router(router_transactions, tags=["transaction"])

'''
Create models (transaction, Bill,)
Bill(id, date, client, totalvalue)
transaction(id, description, facture)
'''
"Bill == Factura"
"Git log == Para ver el historial de cambios"
"Git log --oneline == Para ver el historial de cambios en una sola linea"
"Git checkout codigo ==para cambiar a un commit especifico"