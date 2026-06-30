from sqlmodel import SQLModel, create_engine, Session
from app.config.configuracion import ajustes

URL_BD=(
    f"postgresql://{ajustes.POSTGRES_USUARIO}:{ajustes.POSTGRES_PASSWORD}"
    f"@{ajustes.POSTGRES_HOST}:{ajustes.POSTGRES_PUERTO}/{ajustes.POSTGRES_BD}"
)

conexion = create_engine(URL_BD, echo=True)

def get_session():
    with Session(conexion) as session:
        yield session