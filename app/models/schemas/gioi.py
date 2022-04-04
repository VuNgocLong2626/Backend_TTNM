from app.models.domain import (
                                base as _base,
                                gioi as _gioi_domain)


class GioiCreate(
    _gioi_domain.GioiName
):
    pass


class GioiDetail(
    _base.GioiId,
    _gioi_domain.GioiName
):
    pass

    class Config:
        orm_mode = True


class GioiUpdate(
    _base.GioiId,
    _gioi_domain.GioiName
):
    pass