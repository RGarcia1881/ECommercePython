from sqlmodel import select
from config.bd import get_session
from models.productos_modelo import productos

def crear_producto(datos_producto) -> dict:
    gen_postgres = get_session()
    try:
        session = next(gen_postgres)
        session.add(datos_producto)
        session.commit()
        session.refresh(datos_producto)
        
        return {"status": "success", "mensaje": "Producto creado con éxito.", "id": datos_producto.id}
    except Exception as e:
        session.rollback()
        raise e
    finally:
        try: next(gen_postgres)
        except StopIteration: pass

def obtener_producto_por_id(producto_id: int):
    gen_postgres = get_session()
    try:
        session = next(gen_postgres)
        return session.get(productos, producto_id)
    finally:
        try: next(gen_postgres)
        except StopIteration: pass

def listar_productos():
    gen_postgres = get_session()
    try:
        session = next(gen_postgres)
        return session.exec(select(productos)).all()
    finally:
        try: next(gen_postgres)
        except StopIteration: pass

def actualizar_stock_producto(producto_id: int, nuevo_stock: int) -> dict:
    gen_postgres = get_session()
    try:
        session = next(gen_postgres)
        
        producto = session.get(productos, producto_id)
        if not producto:
            raise ValueError(f"Producto con ID {producto_id} no encontrado.")
            
        producto.stock = nuevo_stock
        session.add(producto)
        session.commit()
        
        return {"status": "success", "mensaje": "Stock actualizado correctamente."}
    except Exception as e:
        session.rollback()
        raise e
    finally:
        try: next(gen_postgres)
        except StopIteration: pass

def eliminar_producto(producto_id: int) -> dict:
    gen_postgres = get_session()
    try:
        session = next(gen_postgres)
        
        producto = session.get(productos, producto_id)
        if not producto:
            raise ValueError(f"Producto con ID {producto_id} no encontrado.")
            
        session.delete(producto)
        session.commit()
        
        return {"status": "success", "mensaje": "Producto eliminado del catálogo."}
    except Exception as e:
        session.rollback()
        raise e
    finally:
        try: next(gen_postgres)
        except StopIteration: pass