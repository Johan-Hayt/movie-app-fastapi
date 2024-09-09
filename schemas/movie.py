#BaseModel: Manejo de Esquemas de datos, Field: Validación de datos
from pydantic import BaseModel, Field 
from typing import Optional

#Clase para definir Esquema de datos
class Movies(BaseModel):
    id: Optional[int] = None
    title: str = Field(
        min_length = 5,
        max_length = 15)
    overview: str = Field(
        min_length=5, 
        max_length = 50)
    year: int = Field(le = 2023)
    rating: float = Field(
        ge = 0.0, 
        le= 10.0)
    category: str = Field(
        min_length = 5,
        max_length = 15)

    class Config: # valores por defecto
        json_schema_extra = {
            "example" : {
                "id":1,
                "title":"Título",
                "overview": "Descripción",
                "year": 2022, 
                "rating": 9.8,
                "category": "Drama"
            } 
        }
