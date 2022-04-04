from app.db.database import SessionLocal
from app.db.tables import Bo


db = SessionLocal()


def delete_bo(id_bo: int):
    try:
        db.query(Bo).filter(Bo.id_bo == id_bo).delete()
        db.commit()
        return True
    except:
        return None