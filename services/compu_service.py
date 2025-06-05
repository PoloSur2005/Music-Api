from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List

from models.compu import Compu
from schemas.schemas import CompuSchema


def get_all_compus(db: Session) -> List[Compu]:
    return db.query(Compu).all()


def get_compus_by_marca(db: Session, marca: str) -> List[Compu]:
    compus = db.query(Compu).filter(Compu.Marca.ilike(marca)).all()
    if not compus:
        raise HTTPException(status_code=404, detail="No se encontraron computadoras con esa marca")
    return compus


def get_compu_by_id(db: Session, compu_id: int) -> Compu:
    compu = db.query(Compu).filter(Compu.compu_id == compu_id).first()
    if not compu:
        raise HTTPException(status_code=404, detail="Computadora no encontrada")
    return compu


def create_compu(db: Session, compu_data: CompuSchema) -> Compu:
    new_compu = Compu(**compu_data.dict())
    db.add(new_compu)
    db.commit()
    db.refresh(new_compu)
    return new_compu


def update_compu(db: Session, compu_id: int, compu_data: CompuSchema) -> Compu:
    db_compu = get_compu_by_id(db, compu_id)
    for key, value in compu_data.dict(exclude_unset=True).items():
        setattr(db_compu, key, value)
    db.commit()
    db.refresh(db_compu)
    return db_compu


def delete_compu(db: Session, compu_id: int) -> str:
    compu = get_compu_by_id(db, compu_id)
    modelo = compu.Modelo
    db.delete(compu)
    db.commit()
    return modelo
