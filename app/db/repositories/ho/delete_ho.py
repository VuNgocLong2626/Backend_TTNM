from app.db.database import SessionLocal
from app.db.tables import Ho


db = SessionLocal()


def delete_ho(id_ho: int):
    try:
        db.query(Ho).filter(Ho.id_ho == id_ho).delete()
        db.commit()
        return True
    except:
        return None