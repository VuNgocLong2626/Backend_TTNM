from app.db.database import SessionLocal
from app.models.schemas.nganh import NganhCreate
from app.db.tables import Nganh
from typing import Optional


db = SessionLocal()


def create_nganh(_in: Optional[NganhCreate] = None, name: Optional[str] = None ):
    db.close()
    if name is None:
        nganh_new = Nganh(**_in.dict())
    else:
        nganh_new = Nganh(**{
            "name": name
        })
    db.add(nganh_new)
    try:
        db.flush()
        db.commit()
        return nganh_new
    except:    
        return None