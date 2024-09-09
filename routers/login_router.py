from fastapi import APIRouter
from fastapi.responses import  JSONResponse
from jwt_manager import create_token
from schemas.user import Users

login_router = APIRouter()


#Ruta para Login
@login_router.post("/login", tags = ["Auth"])
def login(user : Users):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)