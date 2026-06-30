from pydantic_settings import BaseSettings, SettingsConfigDict

class Configuracion(BaseSettings):

    POSTGRES_USUARIO: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PUERTO: int
    POSTGRES_BD: str
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

ajustes = Configuracion()