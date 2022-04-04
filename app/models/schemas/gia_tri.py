from app.models.domain import (
                                base as _base,
                                giai_tri as _giai_tri_domain)


class GiaTriCreate(
    _giai_tri_domain.GiaTriName
):
    pass


class GiaTriDetail(
    _base.GiatriId,
    _giai_tri_domain.GiaTriName
):
    pass

    class Config:
        orm_mode = True


class GiaTriUpdate(
    _base.GiatriId,
    _giai_tri_domain.GiaTriName
):
    pass