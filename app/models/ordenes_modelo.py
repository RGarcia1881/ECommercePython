from sqlmodel import Field, SQLModel
from datetime import datetime

class ordenes(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    id_usuario: int = Field(foreign_key="usuario.id", nullable=False)
    fecha: datetime = Field(default_factory=datetime.now)
    total: float
    estado: str = Field(default="En proceso")