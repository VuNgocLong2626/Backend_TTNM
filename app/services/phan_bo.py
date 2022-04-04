from sqlalchemy import false
from app.models.schemas import phan_bo as _phan_bo_schemas
from fastapi import HTTPException, status
from app.db.repositories.phan_bo.create_phan_bo import create_phan_bo
from app.db.repositories.phan_bo.get_all_phan_bo import get_all_phan_bo
from app.db.repositories.phan_bo.delete_phan_bo import delete_phan_bo
from app.db.repositories.phan_bo.update_phan_bo import update_phan_bo


class phan_boServices():

    def create_phan_bo(phan_bo_in: _phan_bo_schemas.PhanBoCreate):
        respon = create_phan_bo(phan_bo_in)
        if respon is None:
            raise get_phan_bo_create_exception()
        return respon

    def get_all_phan_bo():
        respon = get_all_phan_bo()
        return respon 

    def delete_phan_bo(id_phan_bo: int):
        delete_phan_bo(id_phan_bo)
        raise get_phan_bo_done()

    def update_phan_bo(phan_bo_in: _phan_bo_schemas.phan_boUpdate):
        respon = update_phan_bo(phan_bo_in)
        if respon is None:
            raise get_phan_bo_exception()
        return respon


def get_phan_bo_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_phan_bo_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_phan_bo_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception