from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from app.services.sinh_canh import sinh_canhServices
from app.models.schemas import sinh_canh as _sinh_canh_schemas


router = router = APIRouter(
    prefix="/sinh-canh",
    tags=["Sinh canh"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=_sinh_canh_schemas.SinhCanhDetail)
async def create_sinh_canh(_in: _sinh_canh_schemas.SinhCanhCreate):
    respon = sinh_canhServices.create_sinh_canh(_in)
    return respon

@router.get("/", response_model=List[_sinh_canh_schemas.SinhCanhDetail])
async def get_all_sinh_canh():
    respon = sinh_canhServices.get_all_sinh_canh()
    return respon

@router.put("/", response_model=_sinh_canh_schemas.SinhCanhDetail)
async def update_sinh_canh(_in: _sinh_canh_schemas.SinhCanhUpdate):
    respon = sinh_canhServices.update_sinh_canh(_in)
    return respon

@router.delete("/")
async def delete_sinh_canh(id_sinh_canh: int):
    respon = sinh_canhServices.delete_sinh_canh(id_sinh_canh)