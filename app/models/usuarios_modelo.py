from sqlmodel import Field, SQLModel, Session, create_engine, select

class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    correo: str