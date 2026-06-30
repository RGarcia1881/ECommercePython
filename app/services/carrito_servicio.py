from sqlmodel import select
from config.redis import cliente_redis
from config.bd import get_session
from models.productos_modelo import productos
from schemas.carrito_esquema import Carrito, ItemCarritoSalida, CarritoSalida

def agregar_producto_carrito(usuario_id: int, producto_id: int, cantidad: int):
    gen_redis = cliente_redis()
    gen_postgres = get_session()

    try:
        cliente = next(gen_redis)
        session = next(gen_postgres)

        producto = session.get(productos, producto_id)
        if not producto:
            raise ValueError(f"Producto con ID {producto_id} no encontrado.")
       
        clave_carrito = f"carrito:{usuario_id}"
        existente = cliente.hget(clave_carrito, str(producto_id))

        if existente:
            carrito_item = Carrito.model_validate_json(existente)
            carrito_item.cantidad += cantidad
        else:
            carrito_item = Carrito(producto_id=producto_id, cantidad=cantidad)

        cliente.hset(clave_carrito, str(producto_id), carrito_item.model_dump_json())
        return {"status": "success", "mensaje": "Producto guardado en el carrito"}

    finally:
        try: next(gen_redis)
        except StopIteration: pass
        try: next(gen_postgres)
        except StopIteration: pass


def eliminar_producto_carrito(usuario_id: int, producto_id: int):
    gen_redis = cliente_redis()
    try:
        cliente = next(gen_redis)
        clave_carrito = f"carrito:{usuario_id}"

        resultado = cliente.hdel(clave_carrito, str(producto_id))
        
        if resultado == 0:
            return {"status": "info", "mensaje": "El producto no estaba en el carrito"}
            
        return {"status": "success", "mensaje": "Producto eliminado del carrito"}
        
    finally:
        try: next(gen_redis)
        except StopIteration: pass


def vaciar_carrito(usuario_id: int):
    gen_redis = cliente_redis()
    try:
        cliente = next(gen_redis)
        clave_carrito = f"carrito:{usuario_id}"

        cliente.delete(clave_carrito)
        return {"status": "success", "mensaje": "Carrito vaciado por completo"}
        
    finally:
        try: next(gen_redis)
        except StopIteration: pass


def obtener_carrito(usuario_id: int) -> CarritoSalida:
    gen_redis = cliente_redis()
    gen_postgres = get_session()

    try:
        cliente = next(gen_redis)
        session = next(gen_postgres)

        clave_carrito = f"carrito:{usuario_id}"
        carrito_redis = cliente.hgetall(clave_carrito)
        
        articulos, subtotal, total_iva = [], 0.0, 0.0

        if carrito_redis:
            ids = [int(p_id) for p_id in carrito_redis.keys()]
            productos_db = session.exec(select(productos).where(productos.id.in_(ids))).all()

            for p in productos_db:
                cant = Carrito.model_validate_json(carrito_redis[str(p.id)]).cantidad
                sub_l = p.precio * cant
                iva_l = sub_l * p.iva

                subtotal += sub_l
                total_iva += iva_l
                
                articulos.append(
                    ItemCarritoSalida(
                        producto_id=p.id,
                        nombre_producto=p.nombre,
                        precio_unitario=p.precio,
                        cantidad=cant,
                        subtotal=sub_l,
                        iva=iva_l,
                        total=sub_l + iva_l
                    )
                )

        return CarritoSalida(
            usuario_id=usuario_id,
            items=articulos,
            subtotal=subtotal,
            iva=total_iva,
            total=subtotal + total_iva
        )

    finally:
        try: next(gen_redis)
        except StopIteration: pass
        try: next(gen_postgres)
        except StopIteration: pass