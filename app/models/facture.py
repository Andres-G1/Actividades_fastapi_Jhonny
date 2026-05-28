from pydantic import BaseModel
import datetime

class Facture(BaseModel):
    date: datetime.date = datetime.date.today()
    id_client: int
    totalvalue: float

class createfacture(Facture):
    pass

class updatefacture(Facture):
    id: int | None = None

class transactions(BaseModel):
    unitari_value: float
    cantidad: int
    facture_id: int

class transactioncreate(transactions):
    pass

class transactiont(transactions):
    id: int | None = None