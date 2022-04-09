from fastapi import APIRouter, Depends, UploadFile, File
from typing import List
from app.utils.read_file_xlxs import read
from app.utils.athu import get_current_user

router = router = APIRouter(
    prefix="/file",
    tags=["File"],
    responses={404: {"description": "Not found"}}
)

@router.post("/")
async def read_excel(user: dict = Depends(get_current_user), _in: UploadFile = File(None)):
    respon = read(user, _in)
    return respon