from app.db.database import SessionLocal
from app.db.tables import DongVat


db = SessionLocal()


def delete_dong_vat(id_DongVat: int):
    try:
        db.query(DongVat).filter(DongVat.id_dong_vat == id_DongVat).delete()
        db.commit()
        return True
    except:
        return None