from app.models.domain import (
                                base as _base,
                                image as _image_domain)


class ImageCreate(
    _base.DongVatId,
    _image_domain.ImagePath
):
    pass


class ImageDetail(
    _base.ImageId,
    _base.DongVatId,
    _image_domain.ImagePath
):
    pass

    class Config:
        orm_mode = True


class ImageUpdate(
    _base.ImageId,
    _base.DongVatId,
    _image_domain.ImagePath
):
    pass