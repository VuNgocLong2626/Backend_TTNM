from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import TinhTrangMauVat


db = SessionLocal()


def get_tinh_trang_mau_vat_by_name(name: str):
    db.close()
    respon = db.query(TinhTrangMauVat).filter(TinhTrangMauVat.name == name).first()
    return respon