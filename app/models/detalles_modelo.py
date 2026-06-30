from sqlmodel import Field, SQLModel

class Detalles(SQLModel, table=True):
    __tablename__ = "detalles"
    id: int | None = Field(default=None, primary_key=True)
    orden_id: int = Field(foreign_key="orden.id", nullable=False)
    producto_id: int = Field(foreign_key="producto.id")
    cantidad: int
    precio: float
    iva: float
    total_linea: float