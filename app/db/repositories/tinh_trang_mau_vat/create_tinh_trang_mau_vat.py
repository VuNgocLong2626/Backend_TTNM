from app.db.database import SessionLocal
from app.models.schemas.tinh_trang_mau_vat import TinhTrangMauVatCreate
from app.db.tables import TinhTrangMauVat


db = SessionLocal()


def create_tinh_trang_mau_vat(_in: TinhTrangMauVatCreate):
    tinh_trang_mau_vat_new = TinhTrangMauVat(**_in.dict())
    db.add(tinh_trang_mau_vat_new)
    try:
        db.flush()
        db.commit()
        return tinh_trang_mau_vat_new
    except:    
        return None 