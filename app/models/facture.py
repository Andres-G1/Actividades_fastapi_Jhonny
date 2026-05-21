from pydantic import BaseModel
from .cliente import Client
import datetime

class Facture(BaseModel):
    id: int | None = None
    date: datetime.date = datetime.date.today()
    client: Client
    totalvalue: float