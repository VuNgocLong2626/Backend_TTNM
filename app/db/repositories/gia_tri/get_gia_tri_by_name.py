from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import GiaTri


db = SessionLocal()


def get_giai_tri_by_name(name: str):
    db.close()
    respon = db.query(GiaTri).filter(GiaTri.name == name).first()
    return respon