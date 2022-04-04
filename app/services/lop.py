from sqlalchemy import false
from app.models.schemas import lop as _lop_schemas
from fastapi import HTTPException, status
from app.db.repositories.lop.create_lop import create_lop
from app.db.repositories.lop.get_all_lop import get_all_lop
from app.db.repositories.lop.delete_lop import delete_lop
from app.db.repositories.lop.update_lop import update_lop


class lopServices():

    def create_lop(lop_in: _lop_schemas.LopCreate):
        respon = create_lop(lop_in)
        if respon is None:
            raise get_lop_create_exception()
        return respon

    def get_all_lop():
        respon = get_all_lop()
        return respon 

    def delete_lop(id_lop: int):
        respon = delete_lop(id_lop)
        if respon is None:
            raise get_lop_exception()
        raise get_lop_done()

    def update_lop(lop_in: _lop_schemas.LopUpdate):
        respon = update_lop(lop_in)
        if respon is None:
            raise get_lop_exception()
        return respon


def get_lop_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_lop_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_lop_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception