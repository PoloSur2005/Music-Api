import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

sqlite_file_name = "../database.sqlite"

base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False},  # Importante para SQLite + FastAPI
    echo=True
)

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

