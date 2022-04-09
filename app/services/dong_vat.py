from re import A
from sqlalchemy import false
from app.models.schemas import dong_vat as _dong_vat_schemas
from fastapi import HTTPException, status, UploadFile
from typing import List, Optional
from app.utils import (
    file_utils as _file_utils,
    image_utils as _image_utils
)
from app.db.repositories.dong_vat.create_dong_vat import create_dong_vat
from app.db.repositories.dong_vat.get_all_dong_vat import get_all_dong_vat
from app.db.repositories.dong_vat.delete_dong_vat import delete_dong_vat
from app.db.repositories.dong_vat.update_dong_vat import update_dong_vat
from app.db.repositories.image.create_image import create_image
from app.db.repositories.image.get_image_by_id import get_image_by_id
from app.db.repositories.dong_vat.get_all_by_name_all import get_all_by_name_all


class dong_vatServices():

    def create_dong_vat(dong_vat_in: _dong_vat_schemas.DongVatCreate, files: List[UploadFile]):
        respon = create_dong_vat(dong_vat_in)
        if respon is None:
            raise get_dong_vat_create_exception()
        
        image_responses = []
        for index, file in enumerate(files, start=1):
            image_db = _image_utils.create_product_image(
                respon.id_dong_vat, file,
                index
            )
            image_responses.append(image_db)
            create_image(image_db, respon.id_dong_vat)
        
        return respon

    def get_all_dong_vat(name: Optional[str] = None):
        # respon = get_all_dong_vat()
        if name is None:
            all_dong_vat = get_all_dong_vat()
        else:
            all_dong_vat = get_all_by_name_all(name)
        all = []
        for dong_vat in all_dong_vat:
            dong_vat = {**dong_vat.__dict__}
            all_image = get_list_path_by_id_product_detail(dong_vat.get("id_dong_vat"))
            dong_vat.update({"list_image": all_image})
            all.append(dong_vat)
        return all 

    def delete_dong_vat(id_dong_vat: int):
        respon = delete_dong_vat(id_dong_vat)
        if respon is None:
            raise get_dong_vat_exception()
        raise get_dong_vat_done()

    def update_dong_vat(dong_vat_in: _dong_vat_schemas.DongVatUpdate):
        respon = update_dong_vat(dong_vat_in)
        if respon is None:
            raise get_dong_vat_exception()
        return respon

    def get_filter(_in: _dong_vat_schemas.DongVatFilter):
        return

    def tes():        
        dong_vat_in = _dong_vat_schemas.DongVatCreate(**{
            "nguoi_thu_mau": "nan",
            "ten_tieng_viet": "Trăn lưới",
            "ten_khoa_hoc": "Python molurus (Linnaeus, 1758)",
            "ten_dia_phuong": "Trăn đất",
            "sinh_thai": "Đặc điểm sinh thái học: Thường sống ở các rừng thưa, savan, cây bụi hay ven các rừng già, ở các đồi núi thấp có nhiều bụi rậm khô ráo. Chúng ưa sống gần các vực nước, đầm lầy. Có thể leo lên cây và thích cuốn mình vào những cành cây chìa ra trên mặt nước. ở đồng bằng Nam bộ, chúng ưa sống ở những nơi đầm lầy, rừng tràm, rừng sú vẹt ngập nước, đôi khi còn xâm nhập cả vào những khu vực có vườn cây. Chúng chủ yếu đi kiếm mồi vào ban đêm, nhiều nhất vào lúc xẩm tối. Trăn đất ăn những loài thú nhỏ (chủ yếu gặm nhấm, đôi khi cả hươu nai cỡ nhỏ, chim và những loài ếch nhái, bò sát). Sinh sản hàng năm. Ở khu vực Đồng Bằng Sông Cửu Long giao phối từ tháng 10 đến tháng giêng năm sau. Trăn chửa khoảng hai tháng đến ba tháng sáu ngày, đẻ từ 15 đến 60 quả trứng. Trăn mẹ ấp trứng bằng cách cuộn lấy ổ trứng. Sau khoảng hai tháng (56 - 85 ngày) thì trứng nở: Trăn sơ sinh dài khoảng 52 - 61cm và nặng khoảng 80 - 140g. Lột xác lần đầu khoảng 7 - 10 ngày sau khi nở.",
            "hinh_thai": "Đặc điểm chẩn loại:  Rắn lành cỡ rất lớn trong họ nhà Trăn Pythonidae, dài tới 8m (kích thước trung bình khoảng từ 4 - 6m). Đầu dài, nhỏ. Hai tấm vảy môi trên có trên mỗi tấm vảy một lỗ (lỗ môi là cơ quan cảm giác nhiệt). Có hai cựa nhỏ, hình móng nằm ở hai bên khe huyệt. Cựa trăn cái ngắn, ẩn sâu trong hốc bên khe huyệt. Đầu có màu nâu xám, mặt trên đầu có hoa văn hình mũi mác di từ cổ, mũi nhọn hướng về phía đầu mõm. Mặt trên lưng có màu xám nhạt hay vàng nhạt có một dãy những vết lớn dài, màu nâu đỏ viền đen. Mặt bụng màu vàng hay nâu vàng có những đốm nâu hay đen (Smith 1984).\nĐặc điểm hình thái:  Đầu hình tam giác, chiều dài gần 2 lần chiều rộng. Lỗ mũi tách biệt bởi 2 vảy mũi. Có 2 cặp vảy trước trán, cặp vảy phía sau nhỏ hơn; vảy trán phân chia. Vùng vảy chẩm và vùng vảy thái dương không đều. Có 10 – 13 vảy môi trên, vảy thứ VI hoặc thứ VII ở dưới mắt hoặc tách biệt với mắt bởi hàng vảy dưới mắt; 2 vảy môi trên đầu tiên có các hốc cảm nhiệt rõ ràng. Mắt được bao quanh bởi 2 hoặc 3 vảy trước mắt, 1 vảy trên mắt, 2 hoặc 3, hiếm khi 4 vảy sau mắt, 1, 2 hiếm khi 3 vảy dưới mắt. Các vảy bao quanh mắt, ngoại trừ vảy trên mắt thường hợp nhất hoặc được phân chia bởi đường đứt nhỏ. Vảy môi trên có 2 hố vảy sâu. 16-22 vảy hàm dưới. Vảy cằm  nhỏ và không đều. Rãnh môi dưới rõ ràng. Vảy trơn, 60-75 hàng vảy giữa thân. 256-270 vảy bụng; 65-70 vảy dưới đuôi. Vảy hậu môn phân chia.",
            "ngay_thu_mau": "2022-04-07",
            "dia_diem": "nan",
            "id_sinh_canh": 16,
            "id_phan_bo": 2,
            "id_tinh_trang_mau_vat": 2,
            "id_tinh_trang_bao_ton": 1,
            "id_gia_tri": 3,
            "id_ho": 3,
            "id_bo": 3,
            "id_lop": 2,
            "id_nganh": 1,
            "id_gioi": 1,
            "id_user": 1
        })
        respon = create_dong_vat(dong_vat_in)
        return respon

def get_dong_vat_exception():
    credentials_exception = HTTPException(
        detail= "Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception

def get_dong_vat_done():
    credentials_exception = HTTPException(
        detail= "Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception

def get_dong_vat_create_exception():
    credentials_exception = HTTPException(
        detail= "Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception

def get_list_path_by_id_product_detail(id_product_detail: int):
    list_image = get_image_by_id(id_product_detail)
    list_path = []
    for image in list_image:
        list_path.append(image.path)
    return list_path