import redis
from app.config.configuracion import ajustes

redis_pool = redis.ConnectionPool(
    host=ajustes.REDIS_HOST,
    port=ajustes.REDIS_PORT,
    password=ajustes.REDIS_PASSWORD,
    decode_responses=True
)

def cliente_redis():
    cliente = redis.Redis(connection_pool=redis_pool)
    try:
        yield cliente
    finally:
        pass