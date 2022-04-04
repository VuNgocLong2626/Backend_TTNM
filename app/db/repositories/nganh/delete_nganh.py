from app.db.database import SessionLocal
from app.db.tables import Nganh


db = SessionLocal()


def delete_nganh(id_nganh: int):
    try:
        db.query(Nganh).filter(Nganh.id_nganh == id_nganh).delete()
        db.commit()
        return True
    except:
        return None