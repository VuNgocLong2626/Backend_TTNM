from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import SinhCanh


db = SessionLocal()


def get_sinh_canh_by_name(name: str):
    db.close()
    respon = db.query(SinhCanh).filter(SinhCanh.name == name).first()
    return respon