from jwt import encode, decode #importando librería JWT para autenticación con token de rutas

def create_token(datos: dict)-> str:
    token:str = encode(payload = datos, key= "secret_key", algorithm= "HS256")
    return token  

def validate_token(token)->dict:
    data: dict = decode(token, key= "secret_key", algorithms=['HS256'])
    return data