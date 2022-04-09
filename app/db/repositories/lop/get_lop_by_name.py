from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Lop


db = SessionLocal()


def get_lop_by_name(name: str):
    db.close()
    respon = db.query(Lop).filter(Lop.name == name).first()
    return respon