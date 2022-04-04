from app.db.database import SessionLocal
from app.models.schemas.nganh import NganhUpdate
from app.db.tables import Nganh


db = SessionLocal()


def update_nganh(_in: NganhUpdate):
    try:
        db.query(Nganh).\
        filter(Nganh.id_nganh == _in.id_nganh).\
        update({
                Nganh.name: _in.name
            })
        db.commit()
        return _in
    except:
        return None