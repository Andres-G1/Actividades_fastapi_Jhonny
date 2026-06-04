from pydantic import BaseModel
import datetime

class Bill(BaseModel):
    date: datetime.date = datetime.date.today()
    id_client: int
    totalvalue: float

class createbill(Bill):
    pass

class updatebill(Bill):
    id: int | None = None

class transactions(BaseModel):
    unitari_value: float
    cantidad: int
    bill_id: int

class transactioncreate(transactions):
    pass

class transactiont(transactions):
    id: int | None = None
