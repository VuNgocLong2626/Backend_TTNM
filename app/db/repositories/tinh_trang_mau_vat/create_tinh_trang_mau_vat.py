from app.db.database import SessionLocal
from app.models.schemas.tinh_trang_mau_vat import TinhTrangMauVatCreate
from app.db.tables import TinhTrangMauVat
from typing import Optional


db = SessionLocal()


def create_tinh_trang_mau_vat(_in: Optional[TinhTrangMauVatCreate] = None, name: Optional[str] = None):
    db.close()
    if name is None:
        tinh_trang_mau_vat_new = TinhTrangMauVat(**_in.dict())
    else:
        tinh_trang_mau_vat_new = TinhTrangMauVat(**{
            "name": name
        })
    db.add(tinh_trang_mau_vat_new)
    try:
        db.flush()
        db.commit()
        return tinh_trang_mau_vat_new
    except:    
        return None 