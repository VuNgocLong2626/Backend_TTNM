from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import GiaTri


db = SessionLocal()


def get_all_gia_tri():
    db.close()
    respon = db.query(GiaTri).all()
    return respon