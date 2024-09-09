"""
Pasos para instalar y configurar ORM SQLalchemy.
1. Instalar extensión de VsCode: SQlite Viewer
2. Instalar librería SQLalchemy: pip install sqlalchemy
3. Crear la carpeta config:
     |___Config
         |--- __init__py
         |--- database.py    


"""

import os 
from sqlalchemy import create_engine  #Imnportar clase para crear una instancia de engine
from sqlalchemy.orm.session import sessionmaker #Importar clase para crear un instancia de una sesión 
from sqlalchemy.ext.declarative import declarative_base #Clase madre que sirve para manipular las tablas de la base de datos
from config.config import Settings

setting = Settings()

#Conexión a base de datos PostgreSQL parámetros:
POSTGRES_USER = setting.postgres_user
POSTGRES_PASSWORD = setting.postgres_password #contraseña
POSTGRES_DB = setting.postgres_db #nombre de la base de datos
POSTGRES_HOST = setting.postgres_host #nombre del host
POSTGRES_PORT = setting.postgres_port #nombre del puerto

#sqlite_file_name = "database.sqlite"    

#Variable que contiene la ruta del directorio actual
#base_dir = os.path.dirname(os.path.realpath(__file__))  

#Ruta o Url de la base de datos debe ser un string con el prefijo sqlite:///[ruta_absoluta_database]
#database_url = f"sqlite:///{os.path.join(base_dir,sqlite_file_name)}" 

#Ruta o Url de la base de datos postgresql
database_url = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

#Se crea una instancia de engine con argumento la ruta o url de la base de datos
engine = create_engine(database_url, echo= True)

#Se crea una session y se pasa como argumento la instancia de engine
session = sessionmaker(bind = engine)

Base = declarative_base()

