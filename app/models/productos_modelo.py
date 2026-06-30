from sqlmodel import Field, SQLModel

class productos(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    precio: float
    iva: float
    stock: int