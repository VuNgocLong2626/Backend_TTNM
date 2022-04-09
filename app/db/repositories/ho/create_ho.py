from app.db.database import SessionLocal
from app.models.schemas.ho import HoCreate
from app.db.tables import Ho
from typing import Optional


db = SessionLocal()


def create_ho(_in: Optional[HoCreate] = None, name: Optional[str] = None):
    db.close()
    if name is None:
        ho_new = Ho(**_in.dict())
    else:
        ho_new = Ho(**{
            "name": name
        })
    db.add(ho_new)
    try:
        db.flush()
        db.commit()
        return ho_new
    except:    
        return None