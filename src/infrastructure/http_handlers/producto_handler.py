from fastapi import APIRouter, HTTPException, Depends, Request

from src.infrastructure.dependencies.dependencias_producto import (
    obtener_servicio_prodcuto,
)
from src.application.servicio_producto_port import ServicioProductoPort
from src.infrastructure.http_handlers.models.producto import Producto

router = APIRouter()


@router.post("/productos/")
async def crear_producto(
    producto: Producto,
    servicio_producto: ServicioProductoPort = Depends(obtener_servicio_prodcuto),
):
    nuevo_producto = servicio_producto.crear_producto(producto.nombre, producto.precio)
    return nuevo_producto


@router.get("/productos/")
async def obtener_productos(
    servicio_producto: ServicioProductoPort = Depends(obtener_servicio_prodcuto),
):
    productos = servicio_producto.obtener_productos()
    return productos


@router.get("/productos/{producto_id}")
async def obtener_producto(
    request: Request,
    servicio_producto: ServicioProductoPort = Depends(obtener_servicio_prodcuto),
):
    raise HTTPException(status_code=501, detail="No implementado")


@router.put("/productos/{producto_id}")
async def actualizar_producto(
    request: Request,
    servicio_producto: ServicioProductoPort = Depends(obtener_servicio_prodcuto),
):
    raise HTTPException(status_code=501, detail="No implementado")


@router.delete("/productos/{producto_id}")
async def eliminar_producto(
    request: Request,
    servicio_producto: ServicioProductoPort = Depends(obtener_servicio_prodcuto),
):
    raise HTTPException(status_code=501, detail="No implementado")
