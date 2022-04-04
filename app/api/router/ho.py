from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from app.services.ho import hoServices
from app.models.schemas import ho as _ho_schemas


router = router = APIRouter(
    prefix="/ho",
    tags=["Ho"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=_ho_schemas.hoDetail)
async def create_ho(_in: _ho_schemas.HoCreate):
    respon = hoServices.create_ho(_in)
    return respon

@router.get("/", response_model=List[_ho_schemas.hoDetail])
async def get_all_ho():
    respon = hoServices.get_all_ho()
    return respon

@router.put("/", response_model=_ho_schemas.hoDetail)
async def update_ho(_in: _ho_schemas.hoUpdate):
    respon = hoServices.update_ho(_in)
    return respon

@router.delete("/")
async def delete_ho(id_ho: int):
    respon = hoServices.delete_ho(id_ho)