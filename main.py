from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from database import Base, engine
from routers import movies, compus
from middlewares.jwt_handler import JWTBearer
from utils.jwt_manager import create_token

class User(BaseModel):
    email: str
    password: str

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mi App", version="0.0.2")

app.include_router(movies.router)
app.include_router(compus.router)

@app.get("/", tags=["Home"])
def root():
    return {"message": "Que rollo plebes"}

@app.post("/login", tags=["auth"])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "purosentado":
        token = create_token(user.dict())
        return JSONResponse(content=token)
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")
