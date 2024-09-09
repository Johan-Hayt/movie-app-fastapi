from fastapi import APIRouter

from fastapi import  Body, Path, Query, Depends    #Path validación "parámetro de ruta",  Query validación "parámetros Query".
from fastapi.responses import  JSONResponse
from typing import List
from config.database import session   #Importamos instancias de configuración para manipulación de la base de datos
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movies


movie_router = APIRouter()

@movie_router.get('/movies' , tags=['Movies'], response_model= List[Movies], status_code= 200 )#Estabalecer Ruta Protegida
def get_movies():
    db = session() #Abre una session para interactuar con la base de datos
    result = MovieService(db).get_movies()  #Realiza la consulta de la tabla MovieModel de la base de datos
    return JSONResponse(status_code = 200, content=jsonable_encoder(result))  #el metodo jsonable_encoder permite transformar un objeto a un json para ser representado.

#Parámetros de Ruta
@movie_router.get('/movies/{id}', tags=['Movies'], response_model= List[Movies], status_code=200)
def get_movie(id: int = Path(ge = 1, le= 2000)):
    db = session()
    result = MovieService(db).get_movies_id(id)   #Filtramos la tabla por id
    return JSONResponse(status_code=200, content=jsonable_encoder(result)) if result else JSONResponse(status_code=404, content={"message":"ID NOT FOUND!"})


#Parámetros Query
@movie_router.get('/movies/', tags= ['Movies'], response_model=List[Movies], status_code=200)
def get_movies_by_category(category: str = Query(min_length = 5, max_length = 15)):
    db = session()
    result = MovieService(db).get_movies_cat(category) 
    return JSONResponse(status_code=200, content =jsonable_encoder(result)) if result else JSONResponse(status_code=404, content={"message": "ITEM NO FOUND!"})
    

@movie_router.post('/movies', tags=['Movies'],response_model = dict, status_code=201)
def add_movie(movie: Movies)-> dict:
    db = session()  #Se crea una nueva session para interactuar con la base de datos
    MovieService(db).post_movie(movie)
    return  JSONResponse(status_code= 201, content={"message": "A movie was creted"}) 

@movie_router.put('/movies/{id}', tags =['Movies'], response_model= dict, status_code=201)
def update_movie(id: int = Path(ge = 1, le= 2000), movie: Movies = Body(...))->dict:
    db = session()
    result = MovieService(db).get_movies_id(id)
    if not result:
        return  JSONResponse(status_code = 404, content={"message":"ID NOT FOUND!"}) 

    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code= 201, content={"message": "The movie was updated"})


@movie_router.delete('/movies/{id}', tags= ['Movies'], response_model= dict, status_code= 200)
def delete_movie(id: int = Path(ge = 1, le= 2000))->dict:
    db = session()
    result = MovieService(db).get_movies_id(id)
    if not result:
        return  JSONResponse(status_code = 404, content={"message":"ID NOT FOUND!"})
    
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code= 200, content={"message": "A movie was deleted"})