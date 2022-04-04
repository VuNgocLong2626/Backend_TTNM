from sqlalchemy import false
from app.models.schemas import gia_tri as _gia_tri_schemas
from fastapi import HTTPException, status
from app.db.repositories.gia_tri.create_gia_tri import create_gia_tri
from app.db.repositories.gia_tri.get_all_gia_tri import get_all_gia_tri
from app.db.repositories.gia_tri.delete_gia_tri import delete_gia_tri
from app.db.repositories.gia_tri.update_gia_tri import update_gia_tri


class gia_triServices():

    def create_gia_tri(gia_tri_in: _gia_tri_schemas.GiaTriCreate):
        respon = create_gia_tri(gia_tri_in)
        if respon is None:
            raise get_gia_tri_create_exception()
        return respon

    def get_all_gia_tri():
        respon = get_all_gia_tri()
        return respon 

    def delete_gia_tri(id_gia_tri: int):
        respon = delete_gia_tri(id_gia_tri)
        if respon is None:
            raise get_gia_tri_exception()
        raise get_gia_tri_done()

    def update_gia_tri(gia_tri_in: _gia_tri_schemas.GiaTriUpdate):
        respon = update_gia_tri(gia_tri_in)
        if respon is None:
            raise get_gia_tri_exception()
        return respon


def get_gia_tri_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_gia_tri_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_gia_tri_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception