from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import create_token, validate_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        try:
            data = validate_token(auth.credentials)
        except Exception as e:
            raise HTTPException(status_code=403, detail=str(e))
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales inválidas")
        return data
