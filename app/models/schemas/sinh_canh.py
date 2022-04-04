from app.models.domain import (
                                base as _base,
                                sinh_canh as _sinh_canh_domain)


class SinhCanhCreate(
    _sinh_canh_domain.SinhCanhName
):
    pass


class SinhCanhDetail(
    _base.SinhCanhId,
    _sinh_canh_domain.SinhCanhName
):
    pass

    class Config:
        orm_mode = True


class SinhCanhUpdate(
    _base.SinhCanhId,
    _sinh_canh_domain.SinhCanhName
):
    pass