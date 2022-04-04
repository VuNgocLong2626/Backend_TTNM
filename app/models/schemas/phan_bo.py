from app.models.domain import (
                                base as _base,
                                phan_bo as _phan_bo_domain)


class PhanBoCreate(
    _phan_bo_domain.PhanBoName
):
    pass


class phan_boDetail(
    _base.PhanBoId,
    _phan_bo_domain.PhanBoName
):
    pass

    class Config:
        orm_mode = True


class phan_boUpdate(
    _base.PhanBoId,
    _phan_bo_domain.PhanBoName
):
    pass