from sqlalchemy import false
from app.models.schemas import ho as _ho_schemas
from fastapi import HTTPException, status
from app.db.repositories.ho.create_ho import create_ho
from app.db.repositories.ho.get_all_ho import get_all_ho
from app.db.repositories.ho.delete_ho import delete_ho
from app.db.repositories.ho.update_ho import update_ho


class hoServices():

    def create_ho(ho_in: _ho_schemas.HoCreate):
        respon = create_ho(ho_in)
        if respon is None:
            raise get_ho_create_exception()
        return respon

    def get_all_ho():
        respon = get_all_ho()
        return respon 

    def delete_ho(id_ho: int):
        respon = delete_ho(id_ho)
        if respon is None:
            raise get_ho_exception()
        raise get_ho_done()

    def update_ho(ho_in: _ho_schemas.hoUpdate):
        respon = update_ho(ho_in)
        if respon is None:
            raise get_ho_exception()
        return respon


def get_ho_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_ho_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_ho_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception