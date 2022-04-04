from app.db.database import SessionLocal
from app.models.schemas.lop import LopCreate
from app.db.tables import Lop


db = SessionLocal()


def create_lop(_in: LopCreate):
    lop_new = Lop(**_in.dict())
    db.add(lop_new)
    try:
        db.flush()
        db.commit()
        return lop_new
    except:    
        return None