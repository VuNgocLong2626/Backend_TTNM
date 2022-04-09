from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Bo


db = SessionLocal()


def get_bo_by_name(name: str):
    db.close()
    respon = db.query(Bo).filter(Bo.name == name).first()
    return respon