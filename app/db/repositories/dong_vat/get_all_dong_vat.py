from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import DongVat


db = SessionLocal()


def get_all_dong_vat():
    db.close()
    respon = db.query(DongVat).all()
    return respon