from app.db.database import SessionLocal
from app.models.schemas.gioi import GioiCreate
from app.db.tables import Gioi
from typing import Optional


db = SessionLocal()


def create_gioi(_in: Optional[GioiCreate] = None, name: Optional[str] = None):
    db.close()
    if name is None:
        gioi_new = Gioi(**_in.dict())
    else:
        gioi_new = Gioi(**{
            "name":name
        })
    db.add(gioi_new)
    try:
        db.flush()
        db.commit()
        return gioi_new
    except:    
        return None