from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from app.services.gioi import GioiServices
from app.models.schemas import gioi as _gioi_schemas


router = router = APIRouter(
    prefix="/gioi",
    tags=["Gioi"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=_gioi_schemas.GioiDetail)
async def create_gioi(_in: _gioi_schemas.GioiCreate):
    respon = GioiServices.create_gioi(_in)
    return respon

@router.get("/", response_model=List[_gioi_schemas.GioiDetail])
async def get_all_gioi():
    respon = GioiServices.get_all_gioi()
    return respon

@router.put("/", response_model=_gioi_schemas.GioiDetail)
async def update_gioi(_in: _gioi_schemas.GioiUpdate):
    respon = GioiServices.update_gioi(_in)
    return respon

@router.delete("/")
async def delete_gioi(id_gioi: int):
    respon = GioiServices.delete_gioi(id_gioi)