from fastapi import APIRouter, HTTPException, status
from models.productos_modelo import productos
from app.services import producto_servicio  

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_nuevo_producto(item_producto: productos):
    try:
        return producto_servicio.crear_producto(item_producto)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{producto_id}")
def obtener_producto(producto_id: int):
    producto = producto_servicio.obtener_producto_por_id(producto_id)
    if not producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return producto

@router.get("/")
def listar_todos_los_productos():
    return producto_servicio.listar_productos()

@router.put("/{producto_id}/stock")
def actualizar_stock(producto_id: int, nuevo_stock: int):
    try:
        return producto_servicio.actualizar_stock_producto(producto_id, nuevo_stock)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.delete("/{producto_id}")
def eliminar_producto_por_id(producto_id: int):
    try:
        return producto_servicio.eliminar_producto(producto_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))