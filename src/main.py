from fastapi import FastAPI
import uvicorn

from adapter.http_handlers.pedido_handler import router as producto_router
from adapter.http_handlers.producto_handler import router as pedido_router

app = FastAPI()

app.include_router(producto_router)
app.include_router(pedido_router)
