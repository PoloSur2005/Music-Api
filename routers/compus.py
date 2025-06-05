from fastapi import APIRouter, Depends, Path, Query
from typing import List
from sqlalchemy.orm import Session

from schemas.schemas import CompuSchema
from database import get_db
from middlewares.jwt_handler import JWTBearer
from services import compu_service

router = APIRouter(
    prefix="/compus",
    tags=["Compus"],
    dependencies=[Depends(JWTBearer())]
)

@router.get("/", response_model=List[CompuSchema])
def get_compus(db: Session = Depends(get_db)):
    return compu_service.get_all_compus(db)

@router.get("/search", response_model=List[CompuSchema])
def get_compus_by_marca(marca: str = Query(..., min_length=2, max_length=50), db: Session = Depends(get_db)):
    return compu_service.get_compus_by_marca(db, marca)

@router.get("/{compu_id}", response_model=CompuSchema)
def get_compu(compu_id: int = Path(ge=1), db: Session = Depends(get_db)):
    return compu_service.get_compu_by_id(db, compu_id)

@router.post("/", response_model=CompuSchema, status_code=201)
def create_compu(compu_data: CompuSchema, db: Session = Depends(get_db)):
    return compu_service.create_compu(db, compu_data)

@router.put("/{compu_id}", response_model=CompuSchema)
def update_compu(compu_id: int, compu_data: CompuSchema, db: Session = Depends(get_db)):
    return compu_service.update_compu(db, compu_id, compu_data)

@router.delete("/{compu_id}", response_model=dict)
def delete_compu(compu_id: int, db: Session = Depends(get_db)):
    modelo = compu_service.delete_compu(db, compu_id)
    return {"message": f"Computadora eliminada: {modelo}"}
