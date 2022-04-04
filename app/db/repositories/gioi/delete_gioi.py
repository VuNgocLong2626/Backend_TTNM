from app.db.database import SessionLocal
from app.db.tables import Gioi


db = SessionLocal()


def delete_gioi(id_gioi: int):
    try:
        db.query(Gioi).filter(Gioi.id_gioi == id_gioi).delete()
        db.commit()
        return True
    except:
        return None