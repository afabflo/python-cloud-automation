from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"mensaje: Hola Jesus GIL"}
# uvicorn 02_apis_python.clima.main:app --reload