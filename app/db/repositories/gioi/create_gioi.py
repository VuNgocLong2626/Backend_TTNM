from app.db.database import SessionLocal
from app.models.schemas.gioi import GioiCreate
from app.db.tables import Gioi


db = SessionLocal()


def create_gioi(_in: GioiCreate):
    gioi_new = Gioi(**_in.dict())
    db.add(gioi_new)
    try:
        db.flush()
        db.commit()
        return gioi_new
    except:    
        return None