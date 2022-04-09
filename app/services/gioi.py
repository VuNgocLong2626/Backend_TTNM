from sqlalchemy import false
from app.models.schemas import gioi as _gioi_schemas
from fastapi import HTTPException, status
from app.db.repositories.gioi.create_gioi import create_gioi
from app.db.repositories.gioi.get_all_gioi import get_all_gioi
from app.db.repositories.gioi.delete_gioi import delete_gioi
from app.db.repositories.gioi.update_gioi import update_gioi


class GioiServices():

    def create_gioi(gioi_in: _gioi_schemas.GioiCreate):
        respon = create_gioi(gioi_in)
        if respon is None:
            raise get_gioi_create_exception()
        return respon

    def get_all_gioi():
        respon = get_all_gioi()
        return respon 

    def delete_gioi(id_gioi: int):
        delete_gioi(id_gioi)
        raise get_gioi_done()

    def update_gioi(gioi_in: _gioi_schemas.GioiUpdate):
        respon = update_gioi(gioi_in)
        if respon is None:
            raise get_gioi_exception()
        return respon


def get_gioi_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_gioi_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_gioi_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception