from fastapi import APIRouter, HTTPException, status
from services import checkout_servicio

router = APIRouter(prefix="/checkout", tags=["Checkout"])

@router.post("/{usuario_id}")
def finalizar_compra(usuario_id: int):
    try:
        return checkout_servicio.procesar_checkout(usuario_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno en el servidor")