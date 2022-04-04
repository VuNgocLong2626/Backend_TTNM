from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from app.services.bo import boServices
from app.models.schemas import bo as _bo_schemas


router = router = APIRouter(
    prefix="/bo",
    tags=["Bo"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=_bo_schemas.BoDetail)
async def create_bo(_in: _bo_schemas.BoCreate):
    respon = boServices.create_bo(_in)
    return respon

@router.get("/", response_model=List[_bo_schemas.BoDetail])
async def get_all_bo():
    respon = boServices.get_all_bo()
    return respon

@router.put("/", response_model=_bo_schemas.BoDetail)
async def update_bo(_in: _bo_schemas.BoUpdate):
    respon = boServices.update_bo(_in)
    return respon

@router.delete("/")
async def delete_bo(id_bo: int):
    respon = boServices.delete_bo(id_bo)