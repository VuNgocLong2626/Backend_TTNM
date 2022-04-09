from app.db.database import SessionLocal
from app.models.schemas.sinh_canh import SinhCanhUpdate
from app.db.tables import SinhCanh


db = SessionLocal()


def update_sinh_canh(_in: SinhCanhUpdate):
    try:
        db.query(SinhCanh).\
        filter(SinhCanh.id_sinh_canh == _in.id_sinh_canh).\
        update({
                SinhCanh.name: _in.name
            })
        db.commit()
        return _in
    except:
        return None