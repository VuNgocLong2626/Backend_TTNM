from app.db.database import SessionLocal
from app.models.schemas.tinh_trang_bao_ton import TinhTrangBaoTonUpdate
from app.db.tables import TinhTrangBaoTon


db = SessionLocal()


def update_tinh_trang_bao_ton(_in: TinhTrangBaoTonUpdate):
    try:
        db.query(TinhTrangBaoTon).\
        filter(TinhTrangBaoTon.id_tinh_trang_bao_ton == _in.id_tinh_trang_bao_ton).\
        update({
                TinhTrangBaoTon.name: _in.name
            })
        db.commit()
        return _in
    except:
        return None