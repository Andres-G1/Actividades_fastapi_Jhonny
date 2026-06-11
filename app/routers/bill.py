from fastapi import APIRouter, HTTPException
from app.models.bill import Bill, createbill, updatebill
from app.database import bills, list_clients

router = APIRouter(
    prefix="/bill",
    tags=["bill"],
    responses={404: {"description": "No encontrado"}}
)

bills: list[Bill] = []

# BILLS ENDPOINTS
@router.get("/facturas", tags=["bill"])
async def list_bills():
    return {"bills": bills}

@router.post("/facturas/{id_client}", response_model=Bill, tags=["bill"])
async def create_bill(data_bill: createbill):
    if data_bill.id_client not in [client.id for client in list_clients]: #verificamos que el id del cliente exista en la lista de clientes
        return {"message": "client not found"}

    bill_val = updatebill.model_validate(data_bill.model_dump()) #validamos la factura que se va a crear

    bill_val.id = len(bills) + 1 #asignamos un id a la factura que se va a crear, el id es igual al tamaño de la lista de facturas + 1
    
    bills.append(bill_val) #agregamos la factura a la lista de facturas
        #return the bill_val with the information about the client whit this id_client
    return bill_val

@router.get("/facturas/{id}", response_model=Bill, tags=["bill"])
async def get_bill(id: int):
    for bil in bills:
        if bil.id == id:
            return bil
    return {"message": "bill not found"}

@router.delete("/facturas/{id}", tags=["bill"])
async def delete_bill(id: int):
    for bil in bills:
        if bil.id == id:
            bills.remove(bil)
            return {"message": "bill deleted"}
    return {"message": "bill not found"}

@router.put("/facturas/{id}", response_model=Bill, tags=["bill"])
async def update_bill(id: int, data_bill: createbill):
    for bil in bills:
        if bil.id == id:
            bill_val = updatebill.model_validate(data_bill.model_dump()) #validamos la factura que se va a actualizar
            bil.date = bill_val.date
            bil.id_client = bill_val.id_client
            bil.totalvalue = bill_val.totalvalue
            return bil
    return {"message": "bill not found"}