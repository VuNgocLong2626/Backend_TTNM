from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import TinhTrangBaoTon


db = SessionLocal()


def get_all_tinh_trang_bao_ton():
    db.close()
    respon = db.query(TinhTrangBaoTon).all()
    return respon