from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.user import UserLogin
from app.db.tables import User


db = SessionLocal()


def get_user(user_in: UserLogin):
    db.close()
    respon = db.query(User).filter(User.tk == user_in.tk).first()
    return respon