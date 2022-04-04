from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import User


db = SessionLocal()


def get_all_user():
    db.close()
    respon = db.query(User).all()
    return respon