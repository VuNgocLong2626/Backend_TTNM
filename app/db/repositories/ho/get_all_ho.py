from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Ho


db = SessionLocal()


def get_all_ho():
    db.close()
    respon = db.query(Ho).all()
    return respon