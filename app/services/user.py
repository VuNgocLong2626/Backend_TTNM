from sqlalchemy import false
from app.models.schemas import user as _user_schemas
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.db.repositories.user.create_user import create_user
from app.db.repositories.user.get_all_user import get_all_user
from app.db.repositories.user.delete_user import delete_user
from app.db.repositories.user.update_user import update_user
from app.db.repositories.user.get_user import get_user

from app.utils.athu import (
                                get_password_hash, 
                                create_access_token,
                                verify_password)


class UserServices():

    def login_form(form_data: OAuth2PasswordRequestForm = Depends()):
        user_in = _user_schemas.UserLogin(**{
            "tk": form_data.username,
            "mk": form_data.password
        })

        respon_user = get_user(user_in)
        if not respon_user:
            raise get_user_exception()

        athu_password = verify_password(user_in.mk, respon_user.mk)
        if not athu_password:
            raise get_user_exception()

        user_token = _user_schemas.UserToken(**{
                "hten": respon_user.hten, 
                "id_user": respon_user.id_user
            })
        token = create_access_token(user_token)
        return token

    def create_user(user_in: _user_schemas.UserCreate):
        try:

            hash_password = get_password_hash(user_in.mk)
            new_user = _user_schemas.UserCreate(**{
                "hten": user_in.hten,
                "mk": hash_password,
                "tk": user_in.tk,
            })
            user_out = create_user(new_user)
            if user_out is None:
                raise get_user_create_exception()
                
            user_token = _user_schemas.UserToken(**{
                "hten": user_out.hten, 
                "id_user": user_out.id_user
            })
            token = create_access_token(user_token)
            return token
        except:
            raise get_user_exception()

    def get_all_user():
        respon = get_all_user()
        return respon


def get_user_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_user_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_user_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception