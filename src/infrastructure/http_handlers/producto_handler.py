from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/productos/")
async def crear_producto():
    raise HTTPException(status_code=501, detail="No implementado")


@router.get("/productos/")
async def obtener_productos():
    raise HTTPException(status_code=501, detail="No implementado")


@router.get("/productos/{producto_id}")
async def obtener_producto():
    raise HTTPException(status_code=501, detail="No implementado")


@router.put("/productos/{producto_id}")
async def actualizar_producto():
    raise HTTPException(status_code=501, detail="No implementado")


@router.delete("/productos/{producto_id}")
async def eliminar_producto():
    raise HTTPException(status_code=501, detail="No implementado")
