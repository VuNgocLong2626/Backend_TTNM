from app.db.database import SessionLocal
from app.models.schemas.gioi import GioiUpdate
from app.db.tables import Gioi


db = SessionLocal()


def update_gioi(_in: GioiUpdate):
    try:
        db.query(Gioi).\
        filter(Gioi.id_gioi == _in.id_gioi).\
        update({
                Gioi.name: _in.name
            })
        db.commit()
        return _in
    except:
        return None