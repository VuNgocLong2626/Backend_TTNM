from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from app.services.gia_tri import gia_triServices
from app.models.schemas import gia_tri as _gia_tri_schemas


router = router = APIRouter(
    prefix="/gia-tri",
    tags=["Gia tri"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=_gia_tri_schemas.GiaTriDetail)
async def create_gia_tri(_in: _gia_tri_schemas.GiaTriCreate):
    respon = gia_triServices.create_gia_tri(_in)
    return respon

@router.get("/", response_model=List[_gia_tri_schemas.GiaTriDetail])
async def get_all_gia_tri():
    respon = gia_triServices.get_all_gia_tri()
    return respon

@router.put("/", response_model=_gia_tri_schemas.GiaTriDetail)
async def update_gia_tri(_in: _gia_tri_schemas.GiaTriUpdate):
    respon = gia_triServices.update_gia_tri(_in)
    return respon

@router.delete("/")
async def delete_gia_tri(id_gia_tri: int):
    respon = gia_triServices.delete_gia_tri(id_gia_tri)