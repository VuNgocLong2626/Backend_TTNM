from app.db.database import SessionLocal
from app.models.schemas.bo import BoUpdate
from app.db.tables import Bo


db = SessionLocal()


def update_bo(_in: BoUpdate):
    try:
        db.query(Bo).\
        filter(Bo.id_bo == _in.id_bo).\
        update({
                Bo.name: _in.name
            })
        db.commit()
        return _in
    except:
        return None