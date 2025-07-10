from fastapi import APIRouter, HTTPException, Depends, Request

from src.infrastructure.dependencies.dependencias_cliente import (
    obtener_servicio_cliente,
)
from src.application.servicio_cliente_port import ServicioClientePort
from src.domain.entities.Cliente import Cliente, TipoCliente


router = APIRouter()


@router.post("/clientes/")
async def crear_cliente(
    request: Request,
    servicio_cliente: ServicioClientePort = Depends(obtener_servicio_cliente),
):
    raise HTTPException(status_code=501, detail="No implementado")


@router.get("/clientes/")
async def obtener_clientes(
    request: Request,
    servicio_cliente: ServicioClientePort = Depends(obtener_servicio_cliente),
):
    nuevo_cliente = servicio_cliente.registrar_cliente(
        "Pepe", "pepe@pepe.com", "Francias", TipoCliente.FRECUENTE.value
    )

    return nuevo_cliente


@router.get("/clientes/{cliente_id}")
async def obtener_cliente(
    request: Request,
    servicio_cliente: ServicioClientePort = Depends(obtener_servicio_cliente),
):
    raise HTTPException(status_code=501, detail="No implementado")


@router.put("/clientes/{cliente_id}")
async def actualizar_cliente(
    request: Request,
    servicio_cliente: ServicioClientePort = Depends(obtener_servicio_cliente),
):
    raise HTTPException(status_code=501, detail="No implementado")


@router.delete("/clientes/{cliente_id}")
async def eliminar_cliente(
    request: Request,
    servicio_cliente: ServicioClientePort = Depends(obtener_servicio_cliente),
):
    raise HTTPException(status_code=501, detail="No implementado")
