from app.db.database import SessionLocal
from app.models.schemas.ho import hoUpdate
from app.db.tables import Ho


db = SessionLocal()


def update_ho(_in: hoUpdate):
    try:
        db.query(Ho).\
        filter(Ho.id_ho == _in.id_ho).\
        update({
                Ho.name: _in.name
            })
        db.commit()
        return _in
    except:
        return None