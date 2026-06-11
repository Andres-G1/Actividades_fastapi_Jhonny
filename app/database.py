from sqlmodel import SQLModel, Session, create_engine

sqlite_nombre = "bd_clientes.sqlite3"

sqlite_url = f"sqlite:///{sqlite_nombre}"
motor_bd =  create_engine(sqlite_url)

def obtener_sesion():
    with Session(motor_bd) as mi_sesion:
        yield mi_sesion

def crear_bd_y_tablas():
    SQLModel.metadata.create_all(motor_bd)

#https://sqlmodel.tiangolo.com/