from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Ho


db = SessionLocal()


def get_ho_by_name(name: str):
    db.close()
    respon = db.query(Ho).filter(Ho.name == name).first()
    return respon