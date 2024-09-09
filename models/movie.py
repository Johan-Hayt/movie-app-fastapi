"""
Crear la carpeta models:
     |___models
         |--- __init__py
         |--- movie.py    


"""
from config.database import Base #Importamos instancia de la base creada en database.py
from sqlalchemy import Column, Integer, String, Float #Importamos los tipos de datos para crear la tabla


class Movie(Base): #Creamos una clase que hereda de la clase Base
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year= Column(Integer)
    rating = Column(Float)
    category = Column(String)