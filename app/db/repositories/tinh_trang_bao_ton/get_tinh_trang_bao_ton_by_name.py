from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import TinhTrangBaoTon


db = SessionLocal()


def get_tinh_trang_bao_ton_by_name(name: str):
    db.close()
    respon = db.query(TinhTrangBaoTon).filter(TinhTrangBaoTon.name == name).first()
    return respon