from models.movie import Movie as MovieModel
from schemas.movie import Movies
#from fastapi import Query


class MovieService():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_movies(self):
        result = self.db.query(MovieModel).all()  #Realiza la consulta de la tabla MovieModel de la base de datos
        return result 
    
    def get_movies_id(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()  
        return result
    
    def get_movies_cat(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()  
        return result
    
    def post_movie(self,movie: Movies):
        new_movie = MovieModel(**movie.dict()) #Registrar todos los campos en la base de datos, es necesario pasarlo como dictionary, 
        self.db.add(new_movie)   #Resgitra los datos en la BD
        self.db.commit()
        return 
    
    def update_movie(self, id, movie: Movies):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first() 
        result.title = movie.title
        result.overview = movie.overview
        result.year = movie.year
        result.category = movie.category 
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)
        return 
    
    def delete_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        self.db.delete(result)
        self.db.commit()
        return 
    

        
    