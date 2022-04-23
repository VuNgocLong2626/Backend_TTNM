from app.models.schemas.dong_vat import DongVatFilter
from app.db.database import SessionLocal
from app.db.tables import DongVat, Gioi, Nganh, Lop, Bo, Ho, GiaTri, TinhTrangBaoTon, PhanBo, TinhTrangMauVat, SinhCanh 


db = SessionLocal()


def get_filter_dong_vat(filter_in: DongVatFilter):

    _fillter = db.query(DongVat, Gioi, Nganh, Lop, Bo, Ho, GiaTri, TinhTrangBaoTon, TinhTrangMauVat, PhanBo, SinhCanh)\
        .join(Gioi).join(Nganh).join(Lop).join(Bo).join(Ho).join(GiaTri).join(TinhTrangBaoTon)\
        .join(PhanBo).join(TinhTrangMauVat).join(SinhCanh)\
        
    
    respon = ""
    if len(filter_in.list_ho):
        _fillter = _fillter.filter(DongVat.id_ho.in_(filter_in.list_ho))    
    if len(filter_in.list_bo):
        _fillter = _fillter.filter(DongVat.id_bo.in_(filter_in.list_bo))
    if len(filter_in.list_lop):
        _fillter = _fillter.filter(DongVat.id_lop.in_(filter_in.list_lop))
    if len(filter_in.list_nganh):
        _fillter = _fillter.filter(DongVat.id_nganh.in_(filter_in.list_nganh))
    if len(filter_in.list_gioi):
        _fillter = _fillter.filter(DongVat.id_gioi.in_(filter_in.list_gioi))
    return _fillter.all()

    # if filter_in.list_bo is None:
    #     if filter_in.list_gioi is None:
    #         if filter_in.list_ho is None:
    #             if filter_in.list_lop:

    #                 #get not bo and gioi ho lop
    #                 respon = 3
    #             elif filter_in.list_nganh:

    #                 #get not bo and gioi ho nganh
    #                 respon = 4
    #             #get not bo and gioi ho
    #             respon = 2
    #         elif filter_in.list_lop:
    #             #get not bo and gioi lop
    #             respon = 2
    #         elif filter_in.list_nganh:
    #             #get not bo and gioi nganh
    #             respon = 2
    #         #get not bo and gioi
    #         respon = 1
    #     elif filter_in.list_ho is None:

    #         #get not bo and ho
    #         respon = 1
    #     elif filter_in.list_lop is None:

    #         #get not bo and lop
    #         respon = 1
    #     elif filter_in.list_nganh is None:

    #         #get not bo and nganh
    #         respon = 1
    #     #get not bo
    #     respon = 0
    # elif filter_in.list_gioi is None:
    #     respon = 0
    # elif filter_in.list_ho is None:
    #     respon = 0
    # elif filter_in.list_lop is None:
    #     respon = 0
    # elif filter_in.list_nganh is None:
    #     respon = 0
    # # db.close()
    # # respon = db.query(DongVat).all()n
    return respon