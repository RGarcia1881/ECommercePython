from pydantic import BaseModel, Field

class Checkout(BaseModel):
    usuario_id: int

class DetalleSalida(BaseModel):
    producto_id: int
    cantidad: int
    precio: float
    iva: float
    total_linea: float

    class Config:
        from_attributes = True

class CheckoutSalida(BaseModel):
    mensaje: str
    orden_id: int
    usuario_id: int
    total: float
    detalles: list[DetalleSalida]

    class Config:
        from_attributes = True