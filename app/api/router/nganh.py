from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from app.services.nganh import NganhServices
from app.models.schemas import nganh as _nganh_schemas


router = router = APIRouter(
    prefix="/nganh",
    tags=["Nganh"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=_nganh_schemas.nganhDetail)
async def create_nganh(_in: _nganh_schemas.NganhCreate):
    respon = NganhServices.create_nganh(_in)
    return respon

@router.get("/", response_model=List[_nganh_schemas.nganhDetail])
async def get_all_nganh():
    respon = NganhServices.get_all_nganh()
    return respon

@router.put("/", response_model=_nganh_schemas.nganhDetail)
async def update_nganh(_in: _nganh_schemas.NganhUpdate):
    respon = NganhServices.update_nganh(_in)
    return respon

@router.delete("/")
async def delete_nganh(id_nganh: int):
    respon = NganhServices.delete_nganh(id_nganh)