from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class Client(SQLModel):
    name: str
    age: int
    description: str | None = None

class Clientcreate(Client):
    pass

class Clientt(Client Table=True):
    id: int |None = None