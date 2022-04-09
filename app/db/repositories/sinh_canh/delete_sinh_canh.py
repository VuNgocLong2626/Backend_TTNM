from app.db.database import SessionLocal
from app.db.tables import SinhCanh


db = SessionLocal()


def delete_sinh_canh(id_sinh_canh: int):
    try:
        db.query(SinhCanh).filter(SinhCanh.id_sinh_canh == id_sinh_canh).delete()
        db.commit()
        return True
    except:
        return None