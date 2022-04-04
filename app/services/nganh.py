from sqlalchemy import false
from app.models.schemas import nganh as _nganh_schemas
from fastapi import HTTPException, status
from app.db.repositories.nganh.create_nganh import create_nganh
from app.db.repositories.nganh.get_all_nganh import get_all_nganh
from app.db.repositories.nganh.delete_nganh import delete_nganh
from app.db.repositories.nganh.update_nganh import update_nganh


class NganhServices():

    def create_nganh(nganh_in: _nganh_schemas.NganhCreate):
        respon = create_nganh(nganh_in)
        if respon is None:
            raise get_nganh_create_exception()
        return respon

    def get_all_nganh():
        respon = get_all_nganh()
        return respon 

    def delete_nganh(id_nganh: int):
        delete_nganh(id_nganh)
        raise get_nganh_done()

    def update_nganh(nganh_in: _nganh_schemas.NganhUpdate):
        respon = update_nganh(nganh_in)
        if respon is None:
            raise get_nganh_exception()
        return respon


def get_nganh_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_nganh_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_nganh_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception