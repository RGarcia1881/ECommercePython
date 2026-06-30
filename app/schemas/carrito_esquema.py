from pydantic import BaseModel

class Carrito(BaseModel):
    producto_id: int
    cantidad: int

class ItemCarritoSalida(BaseModel):
    producto_id: int
    cantidad: int
    nombre: str
    precio: float
    iva: float
    total_linea: float

class CarritoSalida(BaseModel):
    usuario_id: int
    orden_id: int
    items: list[ItemCarritoSalida]
    subtotal: float
    iva: float
    total: float
