from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import PhanBo


db = SessionLocal()


def get_phan_bo_by_name(name: str):
    db.close()
    respon = db.query(PhanBo).filter(PhanBo.name == name).first()
    return respon