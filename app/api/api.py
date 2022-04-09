from fastapi import APIRouter
from app.api.router import dong_vat, user, gioi, nganh, lop, bo, ho, gia_tri, file, tinh_trang_mau_vat, tinh_trang_bao_ton, phan_bo, sinh_canh


router = APIRouter()


router.include_router(user.router)
router.include_router(gioi.router)
router.include_router(nganh.router)
router.include_router(lop.router)
router.include_router(bo.router)
router.include_router(ho.router)
router.include_router(gia_tri.router)
router.include_router(tinh_trang_mau_vat.router)
router.include_router(tinh_trang_bao_ton.router)
router.include_router(phan_bo.router)
router.include_router(file.router)
router.include_router(sinh_canh.router)
router.include_router(dong_vat.router)