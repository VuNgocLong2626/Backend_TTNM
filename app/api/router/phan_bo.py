from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from app.services.phan_bo import phan_boServices
from app.models.schemas import phan_bo as _phan_bo_schemas


router = router = APIRouter(
    prefix="/phan-bo",
    tags=["Phan bo"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=_phan_bo_schemas.phan_boDetail)
async def create_phan_bo(_in: _phan_bo_schemas.PhanBoCreate):
    respon = phan_boServices.create_phan_bo(_in)
    return respon

@router.get("/", response_model=List[_phan_bo_schemas.phan_boDetail])
async def get_all_phan_bo():
    respon = phan_boServices.get_all_phan_bo()
    return respon

@router.put("/", response_model=_phan_bo_schemas.phan_boDetail)
async def update_phan_bo(_in: _phan_bo_schemas.phan_boUpdate):
    respon = phan_boServices.update_phan_bo(_in)
    return respon

@router.delete("/")
async def delete_phan_bo(id_phan_bo: int):
    respon = phan_boServices.delete_phan_bo(id_phan_bo)