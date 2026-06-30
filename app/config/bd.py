from sqlmodel import SQLModel, create_engine, Session
from config.configuracion import ajustes

URL_BD=(
    f"postgresql://{ajustes.POSTGRES_USUARIO}:{ajustes.POSTGRES_PASSWORD}"
    f"@{ajustes.POSTGRES_HOST}:{ajustes.POSTGRES_PUERTO}/{ajustes.POSTGRES_BD}"
)

estatus_conexion = { "conectado": False}
conexion = create_engine(URL_BD, estatus_conexion=estatus_conexion)
