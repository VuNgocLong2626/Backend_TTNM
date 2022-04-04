from app.db.database import SessionLocal
from app.models.schemas.gia_tri import GiaTriUpdate
from app.db.tables import GiaTri


db = SessionLocal()


def update_gia_tri(_in: GiaTriUpdate):
    try:
        db.query(GiaTri).\
        filter(GiaTri.id_gia_tri == _in.id_gia_tri).\
        update({
                GiaTri.name: _in.name
            })
        db.commit()
        return _in
    except:
        return None