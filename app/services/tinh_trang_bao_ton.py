from sqlalchemy import false
from app.models.schemas import tinh_trang_bao_ton as _tinh_trang_bao_ton_schemas
from fastapi import HTTPException, status
from app.db.repositories.tinh_trang_bao_ton.create_tinh_trang_bao_ton import create_tinh_trang_bao_ton
from app.db.repositories.tinh_trang_bao_ton.get_all_tinh_trang_bao_ton import get_all_tinh_trang_bao_ton
from app.db.repositories.tinh_trang_bao_ton.delete_tinh_trang_bao_ton import delete_tinh_trang_bao_ton
from app.db.repositories.tinh_trang_bao_ton.update_tinh_trang_bao_ton import update_tinh_trang_bao_ton


class tinh_trang_bao_tonServices():

    def create_tinh_trang_bao_ton(tinh_trang_bao_ton_in: _tinh_trang_bao_ton_schemas.TinhTrangBaoTonCreate):
        respon = create_tinh_trang_bao_ton(tinh_trang_bao_ton_in)
        if respon is None:
            raise get_tinh_trang_bao_ton_create_exception()
        return respon

    def get_all_tinh_trang_bao_ton():
        respon = get_all_tinh_trang_bao_ton()
        return respon 

    def delete_tinh_trang_bao_ton(id_tinh_trang_bao_ton: int):
        delete_tinh_trang_bao_ton(id_tinh_trang_bao_ton)
        raise get_tinh_trang_bao_ton_done()

    def update_tinh_trang_bao_ton(tinh_trang_bao_ton_in: _tinh_trang_bao_ton_schemas.TinhTrangBaoTonUpdate):
        respon = update_tinh_trang_bao_ton(tinh_trang_bao_ton_in)
        if respon is None:
            raise get_tinh_trang_bao_ton_exception()
        return respon


def get_tinh_trang_bao_ton_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_tinh_trang_bao_ton_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_tinh_trang_bao_ton_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception