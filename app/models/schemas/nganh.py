from app.models.domain import (
                                base as _base,
                                nganh as _nganh_domain)


class NganhCreate(
    _nganh_domain.NganhName
):
    pass


class nganhDetail(
    _base.NganhId,
    _nganh_domain.NganhName
):
    pass

    class Config:
        orm_mode = True


class NganhUpdate(
    _base.NganhId,
    _nganh_domain.NganhName
):
    pass