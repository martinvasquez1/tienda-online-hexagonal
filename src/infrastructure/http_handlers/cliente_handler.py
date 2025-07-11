from fastapi import APIRouter, HTTPException, Depends, status

from src.infrastructure.dependencies.dependencias_cliente import (
    obtener_servicio_cliente,
)
from src.application.servicio_cliente_port import ServicioClientePort
from src.infrastructure.http_handlers.models.cliente import (
    CrearCliente,
    ActualizarCliente,
)

router = APIRouter()


@router.post("/clientes/")
async def crear_cliente(
    cliente: CrearCliente,
    servicio_cliente: ServicioClientePort = Depends(obtener_servicio_cliente),
    status_code=status.HTTP_201_CREATED,
):
    try:
        nuevo_cliente = servicio_cliente.registrar_cliente(
            nombre=cliente.nombre,
            email=cliente.email,
            direccion=cliente.direccion,
            tipo=cliente.tipo,
        )
        return nuevo_cliente
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inesperado: {e}",
        )


@router.get("/clientes/")
async def obtener_clientes(
    servicio_cliente: ServicioClientePort = Depends(obtener_servicio_cliente),
    status_code=status.HTTP_200_OK,
):
    try:
        clientes = servicio_cliente.obtener_clientes()

        return clientes or []

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inesperado: {e}",
        )


@router.get("/clientes/{cliente_id}")
async def obtener_cliente(
    cliente_id: int,
    servicio_cliente: ServicioClientePort = Depends(obtener_servicio_cliente),
    status_code=status.HTTP_200_OK,
):
    try:
        cliente = servicio_cliente.obtener(cliente_id)

        return cliente or []
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inesperado: {e}",
        )


@router.put("/clientes/{cliente_id}")
async def actualizar_cliente(
    cliente_id: str,
    datos: ActualizarCliente,
    servicio_cliente: ServicioClientePort = Depends(obtener_servicio_cliente),
    status_code=status.HTTP_201_CREATED,
):
    try:
        cliente = servicio_cliente.actualizar(
            cliente_id,
            datos.nombre,
            datos.email,
            datos.direccion,
            datos.tipo,
        )

        return cliente or []

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inesperado: {e}",
        )


@router.delete("/clientes/{cliente_id}")
async def eliminar_cliente(
    cliente_id: str,
    servicio_cliente: ServicioClientePort = Depends(obtener_servicio_cliente),
    status_code=status.HTTP_204_NO_CONTENT,
):
    try:
        fueEliminado = servicio_cliente.eliminar_cliente(cliente_id)

        if not fueEliminado:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        return fueEliminado
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inesperado: {e}",
        )
