from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from app.services.tinh_trang_mau_vat import tinh_trang_mau_vatServices
from app.models.schemas import tinh_trang_mau_vat as _tinh_trang_mau_vat_schemas


router = router = APIRouter(
    prefix="/tinh-trang-mau-vat",
    tags=["Tinh trang mau vat"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=_tinh_trang_mau_vat_schemas.TinhTrangMauVatDetail)
async def create_tinh_trang_mau_vat(_in: _tinh_trang_mau_vat_schemas.TinhTrangMauVatCreate):
    respon = tinh_trang_mau_vatServices.create_tinh_trang_mau_vat(_in)
    return respon

@router.get("/", response_model=List[_tinh_trang_mau_vat_schemas.TinhTrangMauVatDetail])
async def get_all_tinh_trang_mau_vat():
    respon = tinh_trang_mau_vatServices.get_all_tinh_trang_mau_vat()
    return respon

@router.put("/", response_model=_tinh_trang_mau_vat_schemas.TinhTrangMauVatDetail)
async def update_tinh_trang_mau_vat(_in: _tinh_trang_mau_vat_schemas.TinhTrangMauVatUpdate):
    respon = tinh_trang_mau_vatServices.update_tinh_trang_mau_vat(_in)
    return respon

@router.delete("/")
async def delete_tinh_trang_mau_vat(id_tinh_trang_mau_vat: int):
    respon = tinh_trang_mau_vatServices.delete_tinh_trang_mau_vat(id_tinh_trang_mau_vat)