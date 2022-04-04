from pydantic import BaseModel, Field
from typing import Optional


class UserId(BaseModel):
    id_user: int = Field(None, alias='id_user')


class ImageId(BaseModel):
    id_image: int = Field(None, alias='id_image')


class GioiId(BaseModel):
    id_gioi: int = Field(None, alias='id_gioi')


class NganhId(BaseModel):
    id_nganh: int = Field(None, alias='id_nganh')


class LopId(BaseModel):
    id_lop: int = Field(None, alias='id_lop')


class BoId(BaseModel):
    id_bo: int = Field(None, alias='id_bo')


class HoId(BaseModel):
    id_ho: int = Field(None, alias='id_ho')


class GiatriId(BaseModel):
    id_gia_tri: int = Field(None, alias='id_gia_tri')


class TinhTrangBaoTonId(BaseModel):
    id_tinh_trang_bao_ton: int = Field(None, alias='id_tinh_trang_bao_ton')


class PhanBoId(BaseModel):
    id_phan_bo: int = Field(None, alias='id_phan_bo')


class TinhTrangMauVatId(BaseModel):
    id_tinh_trang_mau_vat: int = Field(None, alias='id_tinh_trang_mau_vat')


class SinhCanhId(BaseModel):
    id_sinh_canh: int = Field(None, alias='id_sinh_canh')


class DongVatId(BaseModel):
    id_dong_vat: int = Field(None, alias='id_dong_vat')
