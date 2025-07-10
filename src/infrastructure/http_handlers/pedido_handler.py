from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/pedidos/")
async def crear_pedido():
    raise HTTPException(status_code=501, detail="No implementado")


@router.get("/pedidos/")
async def obtener_pedidos():
    raise HTTPException(status_code=501, detail="No implementado")


@router.get("/pedidos/{pedido_id}")
async def obtener_pedido():
    raise HTTPException(status_code=501, detail="No implementado")


@router.put("/pedidos/{pedido_id}")
async def actualizar_pedido():
    raise HTTPException(status_code=501, detail="No implementado")


@router.delete("/pedidos/{pedido_id}")
async def eliminar_pedido():
    raise HTTPException(status_code=501, detail="No implementado")
