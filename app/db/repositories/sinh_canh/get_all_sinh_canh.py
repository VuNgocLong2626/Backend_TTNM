from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import SinhCanh


db = SessionLocal()


def get_all_sinh_canh():
    db.close()
    respon = db.query(SinhCanh).all()
    return respon