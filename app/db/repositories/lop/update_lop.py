from app.db.database import SessionLocal
from app.models.schemas.lop import LopUpdate
from app.db.tables import Lop


db = SessionLocal()


def update_lop(_in: LopUpdate):
    try:
        db.query(Lop).\
        filter(Lop.id_lop == _in.id_lop).\
        update({
                Lop.name: _in.name
            })
        db.commit()
        return _in
    except:
        return None