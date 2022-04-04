from app.db.database import SessionLocal
from app.models.schemas.tinh_trang_bao_ton import TinhTrangBaoTonCreate
from app.db.tables import TinhTrangBaoTon


db = SessionLocal()


def create_tinh_trang_bao_ton(_in: TinhTrangBaoTonCreate):
    tinh_trang_bao_ton_new = TinhTrangBaoTon(**_in.dict())
    db.add(tinh_trang_bao_ton_new)
    try:
        db.flush()
        db.commit()
        return tinh_trang_bao_ton_new
    except:    
        return None