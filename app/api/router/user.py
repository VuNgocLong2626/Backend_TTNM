from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.services.user import UserServices
from app.models.schemas import (
                                user as _user_schemas
                                )
from app.utils.athu import get_current_user

router = router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}}
)

@router.post("/login-form")
async def login_form(form_data: OAuth2PasswordRequestForm = Depends()):
    respon = UserServices.login_form(form_data)
    return respon

@router.post("/sgin-up")
async def create_user(user_in: _user_schemas.UserCreate):
    respon = UserServices.create_user(user_in)
    return respon

@router.get("/")
async def get_token(user: dict = Depends(get_current_user)):
    return user

@router.get("/get-all/")
async def get_all_user(user: dict = Depends(get_current_user)):
    respon = UserServices.get_all_user()
    return respon
