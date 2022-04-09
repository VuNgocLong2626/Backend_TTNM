from sqlalchemy import false
from app.models.schemas import sinh_canh as _sinh_canh_schemas
from fastapi import HTTPException, status
from app.db.repositories.sinh_canh.create_sinh_canh import create_sinh_canh
from app.db.repositories.sinh_canh.get_all_sinh_canh import get_all_sinh_canh
from app.db.repositories.sinh_canh.delete_sinh_canh import delete_sinh_canh
from app.db.repositories.sinh_canh.update_sinh_canh import update_sinh_canh


class sinh_canhServices():

    def create_sinh_canh(sinh_canh_in: _sinh_canh_schemas.SinhCanhCreate):
        respon = create_sinh_canh(sinh_canh_in)
        if respon is None:
            raise get_sinh_canh_create_exception()
        return respon

    def get_all_sinh_canh():
        respon = get_all_sinh_canh()
        return respon 

    def delete_sinh_canh(id_sinh_canh: int):
        delete_sinh_canh(id_sinh_canh)
        raise get_sinh_canh_done()

    def update_sinh_canh(sinh_canh_in: _sinh_canh_schemas.SinhCanhUpdate):
        respon = update_sinh_canh(sinh_canh_in)
        if respon is None:
            raise get_sinh_canh_exception()
        return respon


def get_sinh_canh_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_sinh_canh_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_sinh_canh_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception