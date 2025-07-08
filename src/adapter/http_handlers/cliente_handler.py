from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/clientes/")
async def crear_cliente():
    raise HTTPException(status_code=501, detail="No implementado")


@router.get("/clientes/")
async def obtener_clientes():
    raise HTTPException(status_code=501, detail="No implementado")


@router.get("/clientes/{cliente_id}")
async def obtener_cliente():
    raise HTTPException(status_code=501, detail="No implementado")


@router.put("/clientes/{cliente_id}")
async def actualizar_cliente():
    raise HTTPException(status_code=501, detail="No implementado")


@router.delete("/clientes/{cliente_id}")
async def eliminar_cliente():
    raise HTTPException(status_code=501, detail="No implementado")
