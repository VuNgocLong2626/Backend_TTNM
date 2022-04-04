from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import TinhTrangMauVat


db = SessionLocal()


def get_all_tinh_trang_mau_vat():
    db.close()
    respon = db.query(TinhTrangMauVat).all()
    return respon