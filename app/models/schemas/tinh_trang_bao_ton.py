from app.models.domain import (
                                base as _base,
                                tinh_trang_bao_ton as _tinh_trang_bao_ton_domain)


class TinhTrangBaoTonCreate(
    _tinh_trang_bao_ton_domain.TinhTrangBaoTonName
):
    pass


class TinhTrangBaoTonDetail(
    _base.TinhTrangBaoTonId,
    _tinh_trang_bao_ton_domain.TinhTrangBaoTonName
):
    pass

    class Config:
        orm_mode = True


class TinhTrangBaoTonUpdate(
    _base.TinhTrangBaoTonId,
    _tinh_trang_bao_ton_domain.TinhTrangBaoTonName
):
    pass