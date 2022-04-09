from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.image import ImageCreate
from app.db.tables import Image


db = SessionLocal()


def create_image(image: str, id_dong_vat: int):
    db.close()
    image_in = ImageCreate(**{
        "path": image,
        "id_dong_vat": id_dong_vat
        })
        
    image_new = Image(**image_in.dict())
    db.add(image_new)
    try:
        db.flush()
        db.commit()
        return image_new
    except:    
        return None