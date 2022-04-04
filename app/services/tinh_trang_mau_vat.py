from sqlalchemy import false
from app.models.schemas import tinh_trang_mau_vat as _tinh_trang_mau_vat_schemas
from fastapi import HTTPException, status
from app.db.repositories.tinh_trang_mau_vat.create_tinh_trang_mau_vat import create_tinh_trang_mau_vat
from app.db.repositories.tinh_trang_mau_vat.get_all_tinh_trang_mau_vat import get_all_tinh_trang_mau_vat
from app.db.repositories.tinh_trang_mau_vat.delete_tinh_trang_mau_vat import delete_tinh_trang_mau_vat
from app.db.repositories.tinh_trang_mau_vat.update_tinh_trang_mau_vat import update_tinh_trang_mau_vat


class tinh_trang_mau_vatServices():

    def create_tinh_trang_mau_vat(tinh_trang_mau_vat_in: _tinh_trang_mau_vat_schemas.TinhTrangMauVatCreate):
        respon = create_tinh_trang_mau_vat(tinh_trang_mau_vat_in)
        if respon is None:
            raise get_tinh_trang_mau_vat_create_exception()
        return respon

    def get_all_tinh_trang_mau_vat():
        respon = get_all_tinh_trang_mau_vat()
        return respon 

    def delete_tinh_trang_mau_vat(id_tinh_trang_mau_vat: int):
        respon = delete_tinh_trang_mau_vat(id_tinh_trang_mau_vat)
        if respon is None:
            raise get_tinh_trang_mau_vat_exception()
        raise get_tinh_trang_mau_vat_done()

    def update_tinh_trang_mau_vat(tinh_trang_mau_vat_in: _tinh_trang_mau_vat_schemas.TinhTrangMauVatUpdate):
        respon = update_tinh_trang_mau_vat(tinh_trang_mau_vat_in)
        if respon is None:
            raise get_tinh_trang_mau_vat_exception()
        return respon


def get_tinh_trang_mau_vat_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_tinh_trang_mau_vat_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_tinh_trang_mau_vat_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception