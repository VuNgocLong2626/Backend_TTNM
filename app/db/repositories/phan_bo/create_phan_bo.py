from app.db.database import SessionLocal
from app.models.schemas.phan_bo import PhanBoCreate
from app.db.tables import PhanBo


db = SessionLocal()


def create_phan_bo(_in: PhanBoCreate):
    phan_bo_new = PhanBo(**_in.dict())
    db.add(phan_bo_new)
    try:
        db.flush()
        db.commit()
        return phan_bo_new
    except:    
        return None