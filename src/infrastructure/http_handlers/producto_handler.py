from fastapi import APIRouter, HTTPException, Depends, Request

from src.infrastructure.dependencies.dependencias_producto import (
    obtener_servicio_prodcuto,
)
from src.application.servicio_producto_port import ServicioProductoPort
from src.infrastructure.http_handlers.models.producto import (
    CrearProducto,
    ActualizarProducto,
)

router = APIRouter()


@router.post("/productos/")
async def crear_producto(
    producto: CrearProducto,
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
    producto_id: int,
    servicio_producto: ServicioProductoPort = Depends(obtener_servicio_prodcuto),
):
    producto = servicio_producto.obtener_producto(producto_id)
    return producto


@router.put("/productos/{producto_id}")
async def actualizar_producto(
    producto_id: int,
    producto: ActualizarProducto,
    servicio_producto: ServicioProductoPort = Depends(obtener_servicio_prodcuto),
):
    producto_actualizado = servicio_producto.actualizar_producto(
        producto_id, producto.nombre, producto.precio
    )
    return producto_actualizado


@router.delete("/productos/{producto_id}")
async def eliminar_producto(
    producto_id: int,
    servicio_producto: ServicioProductoPort = Depends(obtener_servicio_prodcuto),
):
    producto_eliminado = servicio_producto.eliminar_producto(producto_id)
    return producto_eliminado
