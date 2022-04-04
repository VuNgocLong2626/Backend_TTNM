from app.models.domain import (
                                base as _base,
                                ho as _ho_domain)


class HoCreate(
    _ho_domain.HoName
):
    pass


class hoDetail(
    _base.HoId,
    _ho_domain.HoName
):
    pass

    class Config:
        orm_mode = True


class hoUpdate(
    _base.HoId,
    _ho_domain.HoName
):
    pass