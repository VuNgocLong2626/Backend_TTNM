from app.db.database import SessionLocal
from app.models.schemas.phan_bo import PhanBoCreate
from app.db.tables import PhanBo
from typing import Optional


db = SessionLocal()


def create_phan_bo(_in: Optional[PhanBoCreate] = None, name: Optional[str] = None):
    db.close()
    if name is None:
        phan_bo_new = PhanBo(**_in.dict())
    else:
        phan_bo_new = PhanBo(**{
            "name": name
        })
    db.add(phan_bo_new)
    try:
        db.flush()
        db.commit()
        return phan_bo_new
    except:    
        return None