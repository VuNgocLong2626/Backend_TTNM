from sqlalchemy import false
from app.models.schemas import bo as _bo_schemas
from fastapi import HTTPException, status
from app.db.repositories.bo.create_bo import create_bo
from app.db.repositories.bo.get_all_bo import get_all_bo
from app.db.repositories.bo.delete_bo import delete_bo
from app.db.repositories.bo.update_bo import update_bo


class boServices():

    def create_bo(bo_in: _bo_schemas.BoCreate):
        respon = create_bo(bo_in)
        if respon is None:
            raise get_bo_create_exception()
        return respon

    def get_all_bo():
        respon = get_all_bo()
        return respon 

    def delete_bo(id_bo: int):
        respon = delete_bo(id_bo)
        if respon is None:
            raise get_bo_exception()
        raise get_bo_done()

    def update_bo(bo_in: _bo_schemas.BoUpdate):
        respon = update_bo(bo_in)
        if respon is None:
            raise get_bo_exception()
        return respon


def get_bo_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_bo_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_bo_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception