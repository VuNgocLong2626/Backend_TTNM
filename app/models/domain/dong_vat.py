from pydantic import BaseModel, Field
from datetime import date


class DongVatTenKhoaHoc(BaseModel):
    ten_khoa_hoc: str = Field(alias='ten_khoa_hoc')


class DongVatTenTiengViet(BaseModel):
    ten_tieng_viet: str = Field(alias='ten_tieng_viet')


class DongVatTenDiaPhuong(BaseModel):
    ten_dia_phuong: str = Field(alias='ten_dia_phuong')


class DongVatDiaDiem(BaseModel):
    dia_diem: str = Field(alias='dia_diem')


class DongVatHinhThai(BaseModel):
    hinh_thai: str = Field(alias='hinh_thai')


class DongVatSinhThai(BaseModel):
    sinh_thai: str = Field(alias='sinh_thai')


class DongVatNgayMauThu(BaseModel):
    ngay_thu_mau: date = Field(alias='ngay_thu_mau')


class DongVatNguoiThuMau(BaseModel):
    nguoi_thu_mau: str = Field(alias='nguoi_thu_mau')