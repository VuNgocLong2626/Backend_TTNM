from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import DongVat
from app.models.schemas import dong_vat as _dong_vat_schemas

db = SessionLocal()


def get_all_dong_vat(_in: _dong_vat_schemas.DongVatFilter):
    db.close()
    if _in.list_gioi is None:
        k = 0
    else:
        return
    respon = db.query(DongVat).all()
    return respon