from sqlmodel import Field, SQLModel

class usuarios(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    correo: str