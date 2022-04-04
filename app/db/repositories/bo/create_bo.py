from app.db.database import SessionLocal
from app.models.schemas.bo import BoCreate
from app.db.tables import Bo


db = SessionLocal()


def create_bo(_in: BoCreate):
    bo_new = Bo(**_in.dict())
    db.add(bo_new)
    try:
        db.flush()
        db.commit()
        return bo_new
    except:    
        return None