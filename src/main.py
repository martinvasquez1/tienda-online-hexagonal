from fastapi import FastAPI
import uvicorn

from src.infrastructure.http_handlers.pedido_handler import router as producto_router
from src.infrastructure.http_handlers.producto_handler import router as pedido_router
from src.infrastructure.http_handlers.cliente_handler import router as cliente_router

app = FastAPI()

app.include_router(producto_router)
app.include_router(pedido_router)
app.include_router(cliente_router)
