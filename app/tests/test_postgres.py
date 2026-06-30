from sqlmodel import SQLModel, select, func
from app.config.bd import get_session, conexion
from app.models.usuarios_modelo import usuarios

def test_bd():

    try:
        SQLModel.metadata.create_all(conexion)
        print("Tablas creadas correctamente.")
    except Exception as e:
        print(f"Error al crear las tablas: {e}")
        return
    
    try:
        generador = get_session()
        session = next(generador)

        conteo=session.exec(select(func.count(usuarios.id))).one()
        print(f"Cantidad de usuarios en la base de datos: {conteo}")
    
    except Exception as e:
        print(f"Error al obtener la sesión: {e}")
        return
    
if __name__ == "__main__":
    test_bd()