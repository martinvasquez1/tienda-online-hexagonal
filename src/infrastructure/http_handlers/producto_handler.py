from fastapi import APIRouter, HTTPException, Depends, Request

from src.infrastructure.dependencies.dependencias_producto import (
    obtener_servicio_prodcuto,
)
from src.application.servicio_producto_port import ServicioProductoPort
from src.infrastructure.http_handlers.models.producto import (
    CrearProducto,
    ActualizarProducto,
)
from src.infrastructure.http_handlers.exceptions.exceptions_cliente import (
    ClienteNoEncontrado,
)
from src.infrastructure.http_handlers.exceptions.exceptions_pedido import (
    PedidoNoEncontrado,
)

router = APIRouter()


@router.post("/clientes/{cliente_id}/pedidos/{pedido_id}/productos")
async def crear_producto(
    cliente_id: int,
    pedido_id: int,
    producto: CrearProducto,
    servicio_producto: ServicioProductoPort = Depends(obtener_servicio_prodcuto),
):
    try:
        nuevo_producto = servicio_producto.crear_producto(
            cliente_id, pedido_id, producto.nombre, producto.precio, producto.stock
        )
        return nuevo_producto
    except ClienteNoEncontrado as e:
        raise HTTPException(status_code=404, detail=str(e))
    except PedidoNoEncontrado as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/clientes/{cliente_id}/pedidos/{pedido_id}/productos")
async def obtener_productos(
    cliente_id: int,
    pedido_id: int,
    servicio_producto: ServicioProductoPort = Depends(obtener_servicio_prodcuto),
):
    try:
        productos = servicio_producto.obtener_productos(cliente_id, pedido_id)
        return productos
    except ClienteNoEncontrado as e:
        raise HTTPException(status_code=404, detail=str(e))
    except PedidoNoEncontrado as e:
        raise HTTPException(status_code=404, detail=str(e))


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
        producto_id, producto.nombre, producto.precio, producto.stock
    )
    return producto_actualizado


@router.delete("/productos/{producto_id}")
async def eliminar_producto(
    producto_id: int,
    servicio_producto: ServicioProductoPort = Depends(obtener_servicio_prodcuto),
):
    producto_eliminado = servicio_producto.eliminar_producto(producto_id)
    return producto_eliminado
