from app.db.database import SessionLocal
from app.db.tables import GiaTri


db = SessionLocal()


def delete_gia_tri(id_GiaTri: int):
    try:
        db.query(GiaTri).filter(GiaTri.id_gia_tri == id_GiaTri).delete()
        db.commit()
        return True
    except:
        return None