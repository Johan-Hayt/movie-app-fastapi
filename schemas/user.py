from pydantic import BaseModel

#Clase para definir Esquema de Credenciales de Usuario
class Users(BaseModel):
    email : str
    password: str
