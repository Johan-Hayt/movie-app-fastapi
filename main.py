#Comando terminal para ejecutar API
#uvicorn main:app --reload --port 5000 --host 0.0.0.0
#Para ingresar a la documentación se debe ir a http://0.0.0.0:5000/docs

from fastapi import FastAPI   
from fastapi.responses import HTMLResponse
from config.database import engine,Base    #Importamos instancias de configuración para manipulación de la base de datos
from middlewares.error_handler import ErrorHandler
from routers.movie_routers import movie_router
from routers.login_router import login_router
from pathlib import Path


def init_Config(app):
    #Cambia el nombre de la aplicación
    app.title = "Mi aplicación FastAPI"
    #Cambia la versión de la aplicación
    app.version = "0.0.1"

#Crea una instancia de FastAPI
app  = FastAPI()
#Establece título y versión de App 
init_Config(app)


app.add_middleware(ErrorHandler) #Añadiendo middleware al archivo main
Base.metadata.create_all(bind=engine) #Iniciar manejador de base de datos
app.include_router(movie_router)
app.include_router(login_router)


#Los Tags nos ayudan a agrupar rutas
@app.get("/", tags = ["Home"])
def message():
    return HTMLResponse("<h1>Hello World</h1>")


    