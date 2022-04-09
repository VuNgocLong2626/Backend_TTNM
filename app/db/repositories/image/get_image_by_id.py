from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Image


db = SessionLocal()


def get_image_by_id(id_dong_vat: int):
    db.close()
    respon = db.query(Image).filter(Image.id_dong_vat == id_dong_vat).all()
    return respon