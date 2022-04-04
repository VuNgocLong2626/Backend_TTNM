from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from app.services.tinh_trang_bao_ton import tinh_trang_bao_tonServices
from app.models.schemas import tinh_trang_bao_ton as _tinh_trang_bao_ton_schemas


router = router = APIRouter(
    prefix="/tinh-trang-bao-ton",
    tags=["Tinh trang bao ton"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=_tinh_trang_bao_ton_schemas.TinhTrangBaoTonDetail)
async def create_tinh_trang_bao_ton(_in: _tinh_trang_bao_ton_schemas.TinhTrangBaoTonCreate):
    respon = tinh_trang_bao_tonServices.create_tinh_trang_bao_ton(_in)
    return respon

@router.get("/", response_model=List[_tinh_trang_bao_ton_schemas.TinhTrangBaoTonDetail])
async def get_all_tinh_trang_bao_ton():
    respon = tinh_trang_bao_tonServices.get_all_tinh_trang_bao_ton()
    return respon

@router.put("/", response_model=_tinh_trang_bao_ton_schemas.TinhTrangBaoTonDetail)
async def update_tinh_trang_bao_ton(_in: _tinh_trang_bao_ton_schemas.TinhTrangBaoTonUpdate):
    respon = tinh_trang_bao_tonServices.update_tinh_trang_bao_ton(_in)
    return respon

@router.delete("/")
async def delete_tinh_trang_bao_ton(id_tinh_trang_bao_ton: int):
    respon = tinh_trang_bao_tonServices.delete_tinh_trang_bao_ton(id_tinh_trang_bao_ton)

