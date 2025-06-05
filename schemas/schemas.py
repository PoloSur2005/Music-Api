from pydantic import BaseModel, Field
from typing import Optional

class MovieSchema(BaseModel):
    id: Optional[int]
    title: str = Field(min_length=1, max_length=50)
    overview: str = Field(min_length=1, max_length=200)
    year: int = Field(le=2025, ge=1900)
    rating: float = Field(le=10, ge=0)
    category: str = Field(min_length=1, max_length=25)

    class Config:
        from_attributes = True

class CompuSchema(BaseModel):
    compu_id: Optional[int] = None
    Marca: str = Field(min_length=1, max_length=50)
    Modelo: str = Field(min_length=1, max_length=200)
    Color: str = Field(min_length=1, max_length=50)
    Ram: int = Field(gt=0)
    Almacenamiento: int = Field(gt=0)

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "Marca": "HP",
                "Modelo": "Spectre x360",
                "Color": "Plata",
                "Ram": 16,
                "Almacenamiento": 512
            }
        }

