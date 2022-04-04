from app.db.database import SessionLocal
from app.models.schemas.ho import HoCreate
from app.db.tables import Ho


db = SessionLocal()


def create_ho(_in: HoCreate):
    ho_new = Ho(**_in.dict())
    db.add(ho_new)
    try:
        db.flush()
        db.commit()
        return ho_new
    except:    
        return None