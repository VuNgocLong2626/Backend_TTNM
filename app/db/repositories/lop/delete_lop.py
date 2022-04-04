from app.db.database import SessionLocal
from app.db.tables import Lop


db = SessionLocal()


def delete_lop(id_Lop: int):
    try:
        db.query(Lop).filter(Lop.id_lop == id_Lop).delete()
        db.commit()
        return True
    except:
        return None