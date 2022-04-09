from app.db.database import SessionLocal
from app.models.schemas.tinh_trang_bao_ton import TinhTrangBaoTonCreate
from app.db.tables import TinhTrangBaoTon
from typing import Optional


db = SessionLocal()


def create_tinh_trang_bao_ton(_in: Optional[TinhTrangBaoTonCreate] = None, name: Optional[str] = None):
    db.close()
    if name is None:
        tinh_trang_bao_ton_new = TinhTrangBaoTon(**_in.dict())
    else:
        tinh_trang_bao_ton_new = TinhTrangBaoTon(**{
            "name": name
        })
    db.add(tinh_trang_bao_ton_new)
    try:
        db.flush()
        db.commit()
        return tinh_trang_bao_ton_new
    except:    
        return None