from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Nganh


db = SessionLocal()


def get_all_nganh():
    db.close()
    respon = db.query(Nganh).all()
    return respon