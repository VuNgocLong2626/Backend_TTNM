from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import PhanBo


db = SessionLocal()


def get_all_phan_bo():
    db.close()
    respon = db.query(PhanBo).all()
    return respon