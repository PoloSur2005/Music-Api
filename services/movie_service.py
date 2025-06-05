from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List

from models.movie import Movie
from schemas.schemas import MovieSchema


def get_all_movies(db: Session) -> List[Movie]:
    return db.query(Movie).all()


def get_movies_by_category(db: Session, category: str) -> List[Movie]:
    movies = db.query(Movie).filter(Movie.category.ilike(category)).all()
    if not movies:
        raise HTTPException(status_code=404, detail="No se encontraron películas en esa categoría")
    return movies


def get_movie_by_id(db: Session, movie_id: int) -> Movie:
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    return movie


def create_movie(db: Session, movie_data: MovieSchema) -> Movie:
    new_movie = Movie(**movie_data.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie


def update_movie(db: Session, movie_id: int, movie_data: MovieSchema) -> Movie:
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    for key, value in movie_data.dict(exclude_unset=True).items():
        setattr(db_movie, key, value)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def delete_movie(db: Session, movie_id: int) -> str:
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    title = movie.title
    db.delete(movie)
    db.commit()
    return title
