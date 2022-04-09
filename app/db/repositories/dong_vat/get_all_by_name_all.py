from sqlalchemy import false, or_
from app.db.database import SessionLocal
from app.db.tables import DongVat


db = SessionLocal()


def get_all_by_name_all(name: str):
    db.close()
    respon = db.query(DongVat).filter(or_(DongVat.ten_dia_phuong.like(f'%{name}%'), DongVat.ten_khoa_hoc.like(f'%{name}%'), DongVat.ten_tieng_viet.like(f'%{name}%'))).all()
    return respon