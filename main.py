import fastapi
import sqlite3
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Crea la base de datos
conn = sqlite3.connect("sql/dispositivos.db")

app = fastapi.FastAPI()

origins = [
    "http://localhost:8080",
    "https://shm-frontend-c3f2dc0fa89c.herokuapp.com",
    "https://api-contactos-frontend-a3d16e92dede.herokuapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return "Conexion exitosa"

