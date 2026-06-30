from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes import carrito_rutas, productos_rutas, checkout_rutas
from sqlmodel import SQLModel
from config.bd import conexion as engine

@asynccontextmanager
async def ciclo_vida(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(
    title="RBMusic API",
    version="1.0.0",
    description="API optimizada para la gestión de productos, carritos y checkout",
    lifespan=ciclo_vida
)
app.include_router(productos_rutas)
app.include_router(carrito_rutas)
app.include_router(checkout_rutas)

@app.get("/")
def raiz():
    return {
        "sistema": "RBMusic API",
        "estado": "En línea",
        "documentacion": "/docs"
    }