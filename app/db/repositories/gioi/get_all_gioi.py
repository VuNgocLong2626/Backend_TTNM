from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Gioi


db = SessionLocal()


def get_all_gioi():
    db.close()
    respon = db.query(Gioi).all()
    return respon