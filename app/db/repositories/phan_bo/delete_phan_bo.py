from app.db.database import SessionLocal
from app.db.tables import PhanBo


db = SessionLocal()


def delete_phan_bo(id_PhanBo: int):
    try:
        db.query(PhanBo).filter(PhanBo.id_phan_bo == id_PhanBo).delete()
        db.commit()
        return True
    except:
        return None