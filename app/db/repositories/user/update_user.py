from app.db.database import SessionLocal
from app.models.schemas.user import UserUpdate
from app.db.tables import User


db = SessionLocal()


def update_user(_in: UserUpdate):
    try:
        db.query(User).\
        filter(User.id_user == _in.id_user).\
        update({
                User.mk: _in.mk
            })
        db.commit()
        return _in
    except:
        return None