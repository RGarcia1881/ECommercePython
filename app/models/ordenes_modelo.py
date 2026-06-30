from sqlmodel import Field, SQLModel
from datetime import datetime

class Orden(SQLModel, table=True):
    __tablename__ = "orden"
    id: int | None = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuario.id", nullable=False)
    fecha: datetime = Field(default_factory=datetime.now)
    total: float
    estado: str = Field(default="En proceso")