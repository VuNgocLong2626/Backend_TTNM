from app.db.database import SessionLocal
from app.models.schemas.lop import LopCreate
from app.db.tables import Lop
from typing import Optional


db = SessionLocal()


def create_lop(_in: Optional[LopCreate] = None, name: Optional[str] = None):
    db.close()
    if name is None:
        lop_new = Lop(**_in.dict())
    else:
        lop_new = Lop(**{
            "name": name
        })
    db.add(lop_new)
    try:
        db.flush()
        db.commit()
        return lop_new
    except:    
        return None