from fastapi import FastAPI
from app.api.clima_router import router as clima_router


app = FastAPI(
    title="API de afabflo",
    description = "Servicio de backend con FastAPI",
    version = "1.0.0"
)
#routers
app.include_router(clima_router,prefix="/clima",tags=["clima"])
# uvicorn app.clima.main:app --reload
#http://127.0.0.1:8000/clima/?ciudad=Madrid
#clima podria ser el nombre prefix que quieras añadirle
#y ?ciudad=Nombre Ciudad es como si fuese query parameter osea el parametro de la funcion
@app.get("/")
def root():
    return{"Para buscar ciudad pon /clima/?ciudad=Madrid al lado de la ip"}