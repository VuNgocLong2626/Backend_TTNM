from app.db.database import SessionLocal
from app.db.tables import TinhTrangBaoTon


db = SessionLocal()


def delete_tinh_trang_bao_ton(id_tinh_trang_bao_ton: int):
    try:
        db.query(TinhTrangBaoTon).filter(TinhTrangBaoTon.id_tinh_trang_bao_ton == id_tinh_trang_bao_ton).delete()
        db.commit()
        return True
    except:
        return None