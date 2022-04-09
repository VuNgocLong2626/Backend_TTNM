from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import DongVat


db = SessionLocal()


def get_giai_tri_by_name(name: str):
    db.close()
    respon = db.query(DongVat).filter(DongVat.ten_dia_phuong == name).first()
    return respon