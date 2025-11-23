from fastapi import APIRouter, HTTPException
from app.services.clima_service import obtener_clima

router = APIRouter()
@router.get("/")
def clima(ciudad :str):
    resultado = obtener_clima
    if resultado is None:
        raise HTTPException(status_code=404,detail="No se encontrado")
    return resultado