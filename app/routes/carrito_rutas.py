from fastapi import APIRouter, HTTPException, status
from schemas.carrito_esquema import CarritoSalida
from services import carrito_servicio

router = APIRouter(prefix="/carrito", tags=["Carrito"])

@router.get("/{usuario_id}", response_model=CarritoSalida)
def ver_carrito(usuario_id: int):
    return carrito_servicio.obtener_carrito(usuario_id)

@router.post("/{usuario_id}/agregar")
def agregar_item(usuario_id: int, producto_id: int, cantidad: int):
    try:
        return carrito_servicio.agregar_producto_carrito(usuario_id, producto_id, cantidad)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.delete("/{usuario_id}/eliminar/{producto_id}")
def eliminar_item(usuario_id: int, producto_id: int):
    return carrito_servicio.eliminar_producto_carrito(usuario_id, producto_id)

@router.post("/{usuario_id}/vaciar")
def vaciar(usuario_id: int):
    return carrito_servicio.vaciar_carrito(usuario_id)