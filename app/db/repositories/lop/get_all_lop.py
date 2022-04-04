from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Lop


db = SessionLocal()


def get_all_lop():
    db.close()
    respon = db.query(Lop).all()
    return respon