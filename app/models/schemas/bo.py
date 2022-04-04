from app.models.domain import (
                                base as _base,
                                bo as _bo_domain)


class BoCreate(
    _bo_domain.BoName
):
    pass


class BoDetail(
    _base.BoId,
    _bo_domain.BoName
):
    pass

    class Config:
        orm_mode = True


class BoUpdate(
    _base.BoId,
    _bo_domain.BoName
):
    pass