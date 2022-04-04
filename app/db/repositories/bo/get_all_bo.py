from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Bo


db = SessionLocal()


def get_all_bo():
    db.close()
    respon = db.query(Bo).all()
    return respon