from fastapi import APIRouter, Depends, Query, Path
from typing import List
from sqlalchemy.orm import Session

from schemas.schemas import MovieSchema
from database import get_db
from middlewares.jwt_handler import JWTBearer
from services import movie_service


router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
    dependencies=[Depends(JWTBearer())]
)

@router.get("/", response_model=List[MovieSchema])
def get_movies(db: Session = Depends(get_db)):
    return movie_service.get_all_movies(db)

@router.get("/category", response_model=List[MovieSchema])
def get_movies_by_category(category: str = Query(..., min_length=2, max_length=15), db: Session = Depends(get_db)):
    return movie_service.get_movies_by_category(db, category)

@router.get("/{id}", response_model=MovieSchema)
def get_movie(id: int = Path(ge=0), db: Session = Depends(get_db)):
    return movie_service.get_movie_by_id(db, id)

@router.post("/", response_model=MovieSchema)
def create_movie(movie: MovieSchema, db: Session = Depends(get_db)):
    return movie_service.create_movie(db, movie)

@router.put("/{id}", response_model=MovieSchema)
def update_movie(id: int, movie: MovieSchema, db: Session = Depends(get_db)):
    return movie_service.update_movie(db, id, movie)

@router.delete("/{id}", response_model=dict)
def delete_movie(id: int, db: Session = Depends(get_db)):
    title = movie_service.delete_movie(db, id)
    return {"message": f"Película eliminada: {title}"}

