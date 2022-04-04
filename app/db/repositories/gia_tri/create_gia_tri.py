from app.db.database import SessionLocal
from app.models.schemas.gia_tri import GiaTriCreate
from app.db.tables import GiaTri


db = SessionLocal()


def create_gia_tri(_in: GiaTriCreate):
    gia_tri_new = GiaTri(**_in.dict())
    db.add(gia_tri_new)
    try:
        db.flush()
        db.commit()
        return gia_tri_new
    except:    
        return None