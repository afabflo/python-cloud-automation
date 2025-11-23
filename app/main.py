from fastapi import FastAPI
from api.clima_router import router as clima_router

app = FastAPI(
    title="API de afabflo",
    description = "Servicio de backend con FastAPI",
    version = "1.0.0"
)
#routers

# uvicorn app.clima.main:app --reload