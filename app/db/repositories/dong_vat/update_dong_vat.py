from app.db.database import SessionLocal
from app.models.schemas.dong_vat import DongVatUpdate
from app.db.tables import DongVat


db = SessionLocal()


def update_dong_vat(_in: DongVatUpdate):
    try:
        db.query(DongVat).\
        filter(DongVat.id_dong_vat == _in.id_dong_vat).\
        update({
                DongVat.id_user: _in.id_user,
                DongVat.id_gia_tri: _in.id_gia_tri
            })
        db.commit()
        return _in
    except:
        return None