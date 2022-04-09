from app.db.database import SessionLocal
from app.models.schemas.gia_tri import GiaTriCreate
from app.db.tables import GiaTri
from typing import Optional


db = SessionLocal()


def create_gia_tri(_in: Optional[GiaTriCreate] = None, name: Optional[str] = None):
    db.close()
    if name is None:
        gia_tri_new = GiaTri(**_in.dict())
    else:
        gia_tri_new = GiaTri(**{
            "name": name
        })
    db.add(gia_tri_new)
    try:
        db.flush()
        db.commit()
        return gia_tri_new
    except:    
        return None