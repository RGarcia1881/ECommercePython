from pydantic import BaseModel, Field

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    iva: float = Field(default=0.16)
    stock: int

class ProductoSalida(Producto):
    pass

class CrearProducto(Producto):
    pass