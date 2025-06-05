from database import Base
from sqlalchemy import Column, Integer, String, Float

class Compu(Base):
    __tablename__ = "Compus"

    compu_id = Column(Integer, primary_key=True)
    Marca = Column(String)
    Modelo = Column(String)
    Color = Column(String)
    Ram = Column(Float)
    Almacenamiento = Column(Float)
