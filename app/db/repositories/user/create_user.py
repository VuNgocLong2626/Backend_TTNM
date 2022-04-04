from app.db.database import SessionLocal
from app.models.schemas.user import UserCreate
from app.db.tables import User


db = SessionLocal()


def create_user(_in: UserCreate):
    user_new = User(**_in.dict())
    db.add(user_new)
    try:
        db.flush()
        db.commit()
        return user_new
    except:    
        return None