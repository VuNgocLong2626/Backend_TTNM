from app.db.database import SessionLocal
from app.db.tables import User


db = SessionLocal()


def delete_user(id_User: int):
    try:
        db.query(User).filter(User.id_user == id_User).delete()
        db.commit()
        return True
    except:
        return None