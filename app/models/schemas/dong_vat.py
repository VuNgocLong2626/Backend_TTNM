from app.models.domain import (
                                base as _base,
                                dong_vat as _dong_vat_domain)


class DongVatCreate(
    _base.DongVatId,
    _base.UserId,
    _base.GioiId,
    _base.NganhId,
    _base.LopId,
    _base.BoId,
    _base.HoId,
    _base.GiatriId,
    _base.TinhTrangBaoTonId,
    _base.TinhTrangMauVatId,
    _base.PhanBoId,
    _base.SinhCanhId,
    _dong_vat_domain.DongVatDiaDiem,
    _dong_vat_domain.DongVatNgayMauThu,
    _dong_vat_domain.DongVatHinhThai,
    _dong_vat_domain.DongVatSinhThai,
    _dong_vat_domain.DongVatTenDiaPhuong,
    _dong_vat_domain.DongVatTenKhoaHoc,
    _dong_vat_domain.DongVatTenTiengViet
):
    pass