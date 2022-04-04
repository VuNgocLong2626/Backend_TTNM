from app.db.database import SessionLocal
from app.models.schemas.phan_bo import phan_boUpdate
from app.db.tables import PhanBo


db = SessionLocal()


def update_phan_bo(_in: phan_boUpdate):
    try:
        db.query(PhanBo).\
        filter(PhanBo.id_phan_bo == _in.id_phan_bo).\
        update({
                PhanBo.name: _in.name
            })
        db.commit()
        return _in
    except:
        return None