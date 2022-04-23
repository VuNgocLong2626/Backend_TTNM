from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import DongVat, Gioi, Nganh, Lop, Bo, Ho, GiaTri, TinhTrangBaoTon, PhanBo, TinhTrangMauVat, SinhCanh 


db = SessionLocal()


def get_all_dong_vat_detail(id_dong_vat: int):
    db.close()
    respon = db.query(DongVat.id_dong_vat, Gioi, Nganh, Lop, Bo, Ho, GiaTri, TinhTrangBaoTon, TinhTrangMauVat, PhanBo, SinhCanh).join(Gioi).join(Nganh).join(Lop).join(Bo).join(Ho).join(GiaTri).join(TinhTrangBaoTon).join(PhanBo).join(TinhTrangMauVat).join(SinhCanh).filter(DongVat.id_dong_vat == id_dong_vat).first()
    return respon