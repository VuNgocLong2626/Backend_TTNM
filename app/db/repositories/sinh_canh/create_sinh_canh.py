from app.db.database import SessionLocal
from app.models.schemas.sinh_canh import SinhCanhCreate
from app.db.tables import SinhCanh
from typing import Optional


db = SessionLocal()


def create_sinh_canh(_in: Optional[SinhCanhCreate] = None, name: Optional[str] = None):
    db.close()
    if name is None:
        sinh_canh_new = SinhCanh(**_in.dict())
    else:
        sinh_canh_new = SinhCanh(**{
            "name": name
        })
    db.add(sinh_canh_new)
    try:
        db.flush()
        db.commit()
        return sinh_canh_new
    except:    
        return None