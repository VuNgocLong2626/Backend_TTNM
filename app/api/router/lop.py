from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from app.services.lop import lopServices
from app.models.schemas import lop as _lop_schemas


router = router = APIRouter(
    prefix="/lop",
    tags=["Lop"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=_lop_schemas.LopDetail)
async def create_lop(_in: _lop_schemas.LopCreate):
    respon = lopServices.create_lop(_in)
    return respon

@router.get("/", response_model=List[_lop_schemas.LopDetail])
async def get_all_lop():
    respon = lopServices.get_all_lop()
    return respon

@router.put("/", response_model=_lop_schemas.LopDetail)
async def update_lop(_in: _lop_schemas.LopUpdate):
    respon = lopServices.update_lop(_in)
    return respon

@router.delete("/")
async def delete_lop(id_lop: int):
    respon = lopServices.delete_lop(id_lop)