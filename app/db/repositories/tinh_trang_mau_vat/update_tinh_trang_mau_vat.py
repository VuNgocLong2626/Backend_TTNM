from app.db.database import SessionLocal
from app.models.schemas.tinh_trang_mau_vat import TinhTrangMauVatUpdate
from app.db.tables import TinhTrangMauVat


db = SessionLocal()


def update_tinh_trang_mau_vat(_in: TinhTrangMauVatUpdate):
    try:
        db.query(TinhTrangMauVat).\
        filter(TinhTrangMauVat.id_tinh_trang_mau_vat == _in.id_tinh_trang_mau_vat).\
        update({
                TinhTrangMauVat.name: _in.name
            })
        db.commit()
        return _in
    except:
        return None