from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Gioi


db = SessionLocal()


def get_gioi_by_name(name: str):
    db.close()
    respon = db.query(Gioi).filter(Gioi.name == name).first()
    return respon