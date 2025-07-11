from fastapi import APIRouter, HTTPException, Depends, Request

from src.infrastructure.dependencies.dependencias_pedido import (
    obtener_servicio_pedido,
)
from src.application.servicio_pedido_port import ServicioPedidoPort

router = APIRouter()


@router.post("/clientes/{cliente_id}/pedidos")
async def crear_pedido(
    cliente_id: int,
    servicio_pedido: ServicioPedidoPort = Depends(obtener_servicio_pedido),
):
    nuevo_pedido = servicio_pedido.crear_pedido(cliente_id)
    return nuevo_pedido


@router.get("/pedidos/")
async def obtener_pedidos(
    request: Request,
    servicio_pedido: ServicioPedidoPort = Depends(obtener_servicio_pedido),
):
    raise HTTPException(status_code=501, detail="No implementado")


@router.get("/pedidos/{pedido_id}")
async def obtener_pedido(
    request: Request,
    servicio_pedido: ServicioPedidoPort = Depends(obtener_servicio_pedido),
):
    raise HTTPException(status_code=501, detail="No implementado")


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
