from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm


router = router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}}
)

@router.post("/login-form")
async def login_form():
    return "ahihih"