from fastapi import APIRouter, HTTPException, Depends, Request, status

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
            detail=f"Error al clear nuevo cliente: {e}",
        )


@router.get("/clientes/")
async def obtener_clientes(
    servicio_cliente: ServicioClientePort = Depends(obtener_servicio_cliente),
    status_code=status.HTTP_200_OK,
):
    try:
        clientes = servicio_cliente.obtener_clientes()

        if clientes is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Lista de clientes no encontrada",
            )

        return clientes

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al buscar clientes: {e}",
        )


@router.get("/clientes/{cliente_id}")
async def obtener_cliente(
    id: int,
    servicio_cliente: ServicioClientePort = Depends(obtener_servicio_cliente),
    status_code=status.HTTP_200_OK,
):
    try:
        cliente = servicio_cliente.buscar_cliente_por_id(id)

        if cliente is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
            )

        return cliente
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al buscar el cliente: {e}",
        )


@router.put("/clientes/{cliente_id}")
async def actualizar_cliente(
    id: str,
    datos: ActualizarCliente,
    servicio_cliente: ServicioClientePort = Depends(obtener_servicio_cliente),
    status_code=status.HTTP_201_CREATED,
):
    try:
        cliente = servicio_cliente.actualizar(
            id,
            datos.nombre,
            datos.email,
            datos.direccion,
            datos.tipo,
        )

        if cliente is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No se pudo actualizar el cliente",
            )

        return cliente
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar el cliente: {e}",
        )


@router.delete("/clientes/{cliente_id}")
async def eliminar_cliente(
    request: Request,
    servicio_cliente: ServicioClientePort = Depends(obtener_servicio_cliente),
):
    raise HTTPException(status_code=501, detail="No implementado")
