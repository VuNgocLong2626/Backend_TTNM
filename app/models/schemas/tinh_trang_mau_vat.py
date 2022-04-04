from app.models.domain import (
                                base as _base,
                                tinh_trang_mau_vat as _tinh_trang_mau_vat_domain)


class TinhTrangMauVatCreate(
    _tinh_trang_mau_vat_domain.TinhTrangMauVatName
):
    pass


class TinhTrangMauVatDetail(
    _base.TinhTrangMauVatId,
    _tinh_trang_mau_vat_domain.TinhTrangMauVatName
):
    pass

    class Config:
        orm_mode = True


class TinhTrangMauVatUpdate(
    _base.TinhTrangMauVatId,
    _tinh_trang_mau_vat_domain.TinhTrangMauVatName
):
    pass