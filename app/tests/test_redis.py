from config.redis import cliente_redis

def test_redis():
    try:
        generador = cliente_redis()
        cliente = next(generador)
        cliente.set("prueba_conexion", "prueba_exitosa", ex=10)
        valor = cliente.get("prueba_conexion")
        print(f"Valor obtenido de Redis: {valor}")
        cliente.delete("prueba_conexion")
    except Exception as e:
        print(f"Error al conectar con Redis: {e}")
        return
if __name__ == "__main__":
    test_redis()