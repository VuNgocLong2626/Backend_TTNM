from app.db.database import SessionLocal
from app.models.schemas.bo import BoCreate
from app.db.tables import Bo
from typing import Optional


db = SessionLocal()


def create_bo(_in: Optional[BoCreate] = None, name: Optional[str] = None):
    db.close()
    if name is None:
        bo_new = Bo(**_in.dict())
    else:
        bo_new = Bo(**{
            "name": name
        })
    db.add(bo_new)
    try:
        db.flush()
        db.commit()
        return bo_new
    except:    
        return None