from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Nganh


db = SessionLocal()


def get_nganh_by_name(name: str):
    db.close()
    respon = db.query(Nganh).filter(Nganh.name == name).first()
    return respon