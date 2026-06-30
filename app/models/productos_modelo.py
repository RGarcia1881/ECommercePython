from sqlmodel import Field, SQLModel, Session, create_engine, select

class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    precio: float
    iva: float
    stock: int