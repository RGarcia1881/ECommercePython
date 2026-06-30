from sqlmodel import select
from config.redis import cliente_redis
from config.bd import get_session
from models.productos_modelo import productos
from schemas.carrito_esquema import Carrito

def procesar_checkout(usuario_id: int):
    gen_redis = cliente_redis()
    gen_postgres = get_session()

    try:
        cliente = next(gen_redis)
        session = next(gen_postgres)

        clave_carrito = f"carrito:{usuario_id}"
        carrito_redis = cliente.hgetall(clave_carrito)

        if not carrito_redis:
            raise ValueError("El carrito está vacío.")

        ids = [int(p_id) for p_id in carrito_redis.keys()]
        productos_db = session.exec(select(productos).where(productos.id.in_(ids))).all()

        items_a_procesar = []
        for p in productos_db:
            cant = Carrito.model_validate_json(carrito_redis[str(p.id)]).cantidad
            
            if p.stock < cant:
                raise ValueError(f"Stock insuficiente para el producto: {p.nombre}. Disponible: {p.stock}, Solicitado: {cant}")
            
            items_a_procesar.append((p, cant))

        for p, cant in items_a_procesar:
            p.stock -= cant
            session.add(p)

        session.commit()

        cliente.delete(clave_carrito)

        return {"status": "success", "mensaje": "Checkout completado con éxito y stock actualizado."}

    except Exception as e:
        session.rollback()
        raise e

    finally:
        try: next(gen_redis)
        except StopIteration: pass
        try: next(gen_postgres)
        except StopIteration: pass