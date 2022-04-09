from app.db.database import SessionLocal
from app.models.schemas.dong_vat import DongVatCreate
from app.db.tables import DongVat
from typing import Optional


db = SessionLocal()


def create_dong_vat(_in: Optional[DongVatCreate] = None):
    db.close()
    dong_vat_new = DongVat(**_in.dict())
    db.add(dong_vat_new)
    try:
        db.flush()
        db.commit()
        return dong_vat_new
    except:    
        return None