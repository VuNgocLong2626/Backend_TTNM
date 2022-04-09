from app.db.database import SessionLocal
from app.db.tables import TinhTrangMauVat


db = SessionLocal()


def delete_tinh_trang_mau_vat(id_TinhTrangMauVat: int):
    try:
        db.query(TinhTrangMauVat).filter(TinhTrangMauVat.id_tinh_trang_mau_vat == id_TinhTrangMauVat).delete()
        db.commit()
        return True
    except:
        return None