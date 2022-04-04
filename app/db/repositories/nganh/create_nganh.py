from app.db.database import SessionLocal
from app.models.schemas.nganh import NganhCreate
from app.db.tables import Nganh


db = SessionLocal()


def create_nganh(_in: NganhCreate):
    nganh_new = Nganh(**_in.dict())
    db.add(nganh_new)
    try:
        db.flush()
        db.commit()
        return nganh_new
    except:    
        return None