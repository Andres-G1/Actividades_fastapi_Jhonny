# TRANSACTIONS ENDPOINTS
from fastapi import APIRouter, HTTPException
from app.models.bill import transactions, transactioncreate, transactiont
from app.database import bills, transaction

router = APIRouter(
    prefix="/Transactions",
    responses={404: {"description": "No encontrado"}}
)

@router.get("/transactions", tags=["Transactions"])
async def list_transactions():
    return {"transactions": transaction}

@router.post("/transactions", response_model=transactions, tags=["Transactions"])
async def create_transaction(data_transaction: transactioncreate):
    if data_transaction.bill_id not in [bil.id for bil in bills]: #verificamos que el id de la factura exista en la lista de facturas
        return {"message": "bill not found"}

    transaction_val = transactiont.model_validate(data_transaction.model_dump()) #validamos la transaccion que se va a crear

    transaction_val.id = len(transaction) + 1 #asignamos un id a la transaccion que se va a crear, el id es igual al tamaño de la lista de transacciones + 1
    
    transaction.append(transaction_val)
    return transaction_val

@router.get("/transactions/{id}", response_model=transactions,  tags=["Transactions"])
async def get_transaction(id: int):
    for transac in transaction:
        if transac.id == id:
            return transac
    return {"message": "transaction not found"}

@router.delete("/transactions/{id}",  tags=["Transactions"])
async def delete_transaction(id: int):
    for transac in transaction:
        if transac.id == id:
            transaction.remove(transac)
            return {"message": "transaction deleted"}
    return {"message": "transaction not found"}

@router.put("/transactions/{id}", response_model=transactions,  tags=["Transactions"])
async def update_transaction(id: int, data_transaction: transactioncreate): 
    for transac in transaction:
        if transac.id == id:
            transaction_val = transactiont.model_validate(data_transaction.model_dump()) #validamos la transaccion que se va a actualizar
            transac.unitari_value = transaction_val.unitari_value
            transac.cantidad = transaction_val.cantidad
            transac.bill_id = transaction_val.bill_id
            return transac
    return {"error":"Transaction not found"}
