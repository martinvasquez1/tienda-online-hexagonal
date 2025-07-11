from fastapi import APIRouter, HTTPException, Depends, Request

from src.application.servicio_pedido_port import ServicioPedidoPort
from src.infrastructure.dependencies.dependencias_pedido import (
    obtener_servicio_pedido,
)

from src.infrastructure.http_handlers.exceptions.exceptions_cliente import (
    ClienteNoEncontrado,
)
from src.infrastructure.http_handlers.exceptions.exceptions_pedido import (
    PedidoNoEncontrado,
)


router = APIRouter()


@router.post("/clientes/{cliente_id}/pedidos")
async def crear_pedido(
    cliente_id: int,
    servicio_pedido: ServicioPedidoPort = Depends(obtener_servicio_pedido),
):
    try:
        nuevo_pedido = servicio_pedido.crear_pedido(cliente_id)
        return nuevo_pedido
    except ClienteNoEncontrado as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/clientes/{cliente_id}/pedidos")
async def obtener_pedidos(
    cliente_id: int,
    servicio_pedido: ServicioPedidoPort = Depends(obtener_servicio_pedido),
):
    try:
        pedidos = servicio_pedido.obtener_pedidos(cliente_id)
        return pedidos
    except ClienteNoEncontrado as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/clientes/{cliente_id}/pedidos/{pedido_id}")
async def obtener_pedido(
    cliente_id: int,
    pedido_id: int,
    servicio_pedido: ServicioPedidoPort = Depends(obtener_servicio_pedido),
):
    try:
        pedido = servicio_pedido.obtener_pedido(cliente_id, pedido_id)
        return pedido
    except ClienteNoEncontrado as e:
        raise HTTPException(status_code=404, detail=str(e))
    except PedidoNoEncontrado as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/pedidos/{pedido_id}")
async def actualizar_pedido(
    request: Request,
    servicio_pedido: ServicioPedidoPort = Depends(obtener_servicio_pedido),
):
    raise HTTPException(status_code=501, detail="No implementado")


@router.delete("/pedidos/{pedido_id}")
async def eliminar_pedido(
    request: Request,
    servicio_pedido: ServicioPedidoPort = Depends(obtener_servicio_pedido),
):
    raise HTTPException(status_code=501, detail="No implementado")
