from fastapi import APIRouter, Depends, UploadFile
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from app.services.dong_vat import dong_vatServices
from app.models.schemas import dong_vat as _dong_vat_schemas
from datetime import date
from typing import Optional
from app.utils.athu import get_current_user


router = router = APIRouter(
    prefix="/dong-vat",
    tags=["Dong Vat"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=_dong_vat_schemas.DongVatDetail)
async def create_dong_vat(
    id_gioi: int,
    id_nganh: int,
    id_lop: int,
    id_bo: int,
    id_ho: int,
    id_gia_tri: int,
    id_tinh_trang_bao_ton: int,
    id_phan_bo: int,
    id_tinh_trang_mau_vat: int,
    id_sinh_canh: int,
    ten_khoa_hoc: str,
    ten_tieng_viet: str,
    ten_dia_phuong: str,
    nguoi_thu_mau: str,
    dia_diem: str,
    hinh_thai: str,
    sinh_thai: str,
    ngay_thu_mau: date,
    file: List[UploadFile],
    user: dict = Depends(get_current_user)
    ):
    _in = _dong_vat_schemas.DongVatCreate(**{
        "id_user": user.id_user,
        "id_gioi": id_gioi,
        "id_nganh": id_nganh,
        "id_lop": id_lop,
        "id_bo": id_bo,
        "id_ho": id_ho,
        "id_gia_tri": id_gia_tri,
        "id_tinh_trang_bao_ton": id_tinh_trang_bao_ton,
        "id_phan_bo": id_phan_bo,
        "id_tinh_trang_mau_vat": id_tinh_trang_mau_vat,
        "id_sinh_canh": id_sinh_canh,
        "ten_khoa_hoc": ten_khoa_hoc,
        "ten_tieng_viet": ten_tieng_viet,
        "ten_dia_phuong": ten_dia_phuong,
        "nguoi_thu_mau": nguoi_thu_mau,
        "dia_diem": dia_diem,
        "hinh_thai": hinh_thai,
        "sinh_thai": sinh_thai,
        "ngay_thu_mau": ngay_thu_mau
    })
    respon = dong_vatServices.create_dong_vat(_in, file)
    return respon

@router.get("/")
async def get_all_dong_vat(name: Optional[str] = None):
    respon = dong_vatServices.get_all_dong_vat(name)
    return respon

@router.put("/", response_model=_dong_vat_schemas.DongVatDetail)
async def update_dong_vat(_in: _dong_vat_schemas.DongVatUpdate):
    respon = dong_vatServices.update_dong_vat(_in)
    return respon

@router.delete("/")
async def delete_dong_vat(id_dong_vat: int):
    respon = dong_vatServices.delete_dong_vat(id_dong_vat)

@router.get("/test", response_model=_dong_vat_schemas.DongVatDetail)
async def get_test():
    respon = dong_vatServices.tes()
    return respon

@router.post("/filter/")
async def get_filter(_in: _dong_vat_schemas.DongVatFilter):
    respon = dong_vatServices.get_filter(_in)
    return respon