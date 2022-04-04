from app.models.domain import (
                                base as _base,
                                lop as _lop_domain)


class LopCreate(
    _lop_domain.LopName
):
    pass


class LopDetail(
    _base.LopId,
    _lop_domain.LopName
):
    pass

    class Config:
        orm_mode = True


class LopUpdate(
    _base.LopId,
    _lop_domain.LopName
):
    pass