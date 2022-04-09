import pandas as pd
import time
from fastapi import UploadFile, File
from google_drive_downloader import GoogleDriveDownloader as gdd
import re
from app.db.repositories.gioi.get_gioi_by_name import get_gioi_by_name
from app.db.repositories.gioi.create_gioi import create_gioi
from app.db.repositories.nganh.get_nganh_by_name import get_nganh_by_name
from app.db.repositories.nganh.create_nganh import create_nganh
from app.db.repositories.lop.get_lop_by_name import get_lop_by_name
from app.db.repositories.lop.create_lop import create_lop
from app.db.repositories.bo.get_bo_by_name import get_bo_by_name
from app.db.repositories.bo.create_bo import create_bo
from app.db.repositories.ho.get_ho_by_name import get_ho_by_name
from app.db.repositories.ho.create_ho import create_ho
from app.db.repositories.gia_tri.get_gia_tri_by_name import get_giai_tri_by_name
from app.db.repositories.gia_tri.create_gia_tri import create_gia_tri
from app.db.repositories.tinh_trang_bao_ton.get_tinh_trang_bao_ton_by_name import get_tinh_trang_bao_ton_by_name
from app.db.repositories.tinh_trang_bao_ton.create_tinh_trang_bao_ton import create_tinh_trang_bao_ton
from app.db.repositories.phan_bo.get_phan_bo_by_name import get_phan_bo_by_name
from app.db.repositories.phan_bo.create_phan_bo import create_phan_bo
from app.db.repositories.tinh_trang_mau_vat.get_tinh_trang_mau_vat_by_name import get_tinh_trang_mau_vat_by_name
from app.db.repositories.tinh_trang_mau_vat.create_tinh_trang_mau_vat import create_tinh_trang_mau_vat
from app.db.repositories.sinh_canh.get_sinh_canh_by_name import get_sinh_canh_by_name
from app.db.repositories.sinh_canh.create_sinh_canh import create_sinh_canh
from app.models.schemas import dong_vat as _dong_vat_schemas
from app.models.schemas import user as _user_schemas
from datetime import date
import datetime
from app.db.repositories.dong_vat.create_dong_vat import create_dong_vat
from app.db.repositories.image.create_image import create_image


def read(user: _user_schemas.UserToken ,file: UploadFile = File(None)):
    if not file.filename.endswith('.xlsx'):
        return "Not file Excel"
    df = pd.read_excel(file.file.read(), sheet_name=0)
    js = df.to_json(orient='records', lines=True)
    arr = []
    for row in range(len(df)):
        db = df.iloc[row]
        gioi = get_gioi_by_name(str(db.values[4]).strip())
        if not gioi:
            gioi = create_gioi(name=str(db.values[4]).strip())

        nganh = get_nganh_by_name(str(db.values[5]).strip())
        if not nganh:
            nganh = create_nganh(name=str(db.values[5]).strip())

        lop = get_lop_by_name(str(db.values[6]).strip())
        if not lop:
            lop = create_lop(name=str(db.values[6]).strip())

        bo = get_bo_by_name(str(db.values[7]).strip())
        if not bo:
            bo = create_bo(name=str(db.values[7]).strip())

        ho = get_ho_by_name(str(db.values[7]).strip())
        if not ho:
            ho = create_ho(name=str(db.values[7]).strip())

        gia_tri = get_giai_tri_by_name(str(db.values[16]).strip())
        if not gia_tri:
            gia_tri = create_gia_tri(name=str(db.values[16]).strip())

        tinh_trang_bao_ton = get_tinh_trang_bao_ton_by_name(str(db.values[18]).strip())
        if not tinh_trang_bao_ton:
            tinh_trang_bao_ton = create_tinh_trang_bao_ton(name=str(db.values[18]).strip())

        phan_bo = get_phan_bo_by_name(str(db.values[21]).strip())
        if not phan_bo:
            phan_bo = create_phan_bo(name=str(db.values[21]).strip())

        tinh_trang_mau_vat = get_tinh_trang_mau_vat_by_name(str(db.values[27]).strip())
        if not tinh_trang_mau_vat:
            tinh_trang_mau_vat = create_tinh_trang_mau_vat(name=str(db.values[27]).strip())

        sinh_canh = get_sinh_canh_by_name(str(db.values[28]).strip())
        if not sinh_canh:
            sinh_canh = create_sinh_canh(name=str(db.values[28]).strip())
        
        if not str(db.values[30]).strip() == "NaT": 
            ngay_thu_mau = datetime.datetime.strptime(str(db.values[30]).strip(), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        else:
            ngay_thu_mau = datetime.datetime.today().strftime('%Y-%m-%d')
        
        _in = _dong_vat_schemas.DongVatCreate(**{
        "id_user": user.id_user,
        "id_gioi": gioi.id_gioi,
        "id_nganh": nganh.id_nganh,
        "id_lop": lop.id_lop,
        "id_bo": bo.id_bo,
        "id_ho": ho.id_ho,
        "id_gia_tri": gia_tri.id_gia_tri,
        "id_tinh_trang_bao_ton": tinh_trang_bao_ton.id_tinh_trang_bao_ton,
        "id_phan_bo": phan_bo.id_phan_bo,
        "id_tinh_trang_mau_vat": tinh_trang_mau_vat.id_tinh_trang_mau_vat,
        "id_sinh_canh": sinh_canh.id_sinh_canh,
        "ten_khoa_hoc": str(db.values[1]).strip(),
        "ten_tieng_viet": str(db.values[2]).strip(),
        "ten_dia_phuong": str(db.values[3]).strip(),
        "nguoi_thu_mau": str(db.values[31]).strip(),
        "dia_diem": str(db.values[29]).strip(),
        "hinh_thai": str(db.values[14]).strip(),
        "sinh_thai": str(db.values[15]).strip(),
        "ngay_thu_mau": ngay_thu_mau
        })
        dong_vat= create_dong_vat(_in)
        url_1 = str(db.values[9]).strip()
        url_1 = dowload_load_image(url_1, dong_vat.id_dong_vat)
        if url_1:
            create_image(url_1, dong_vat.id_dong_vat)
        time.sleep(5)
        url_2 = str(db.values[10]).strip()
        url_2 = dowload_load_image(url_2, dong_vat.id_dong_vat)
        if url_2:
            create_image(url_2, dong_vat.id_dong_vat)
        time.sleep(5)
        url_3 = str(db.values[11]).strip()
        url_3 = dowload_load_image(url_3, dong_vat.id_dong_vat)
        if url_3:
            create_image(url_3, dong_vat.id_dong_vat)
        time.sleep(5)
        url_4 = str(db.values[12]).strip()
        url_4 = dowload_load_image(url_4, dong_vat.id_dong_vat)
        if url_4:
            create_image(url_4, dong_vat.id_dong_vat)
        time.sleep(5)
        url_5 = str(db.values[13]).strip()
        url_5 = dowload_load_image(url_5, dong_vat.id_dong_vat)
        if url_5:
            create_image(url_5, dong_vat.id_dong_vat)
        time.sleep(5)
        # arr.append(dowload_load_image(str(db.values[12]).strip()))
        # print(db.values[16])check_google_drive(str(db.values[12]).strip())
        # print(df.iloc[row].values[4])
        # print(df.iloc[row].values[31])

    respon = {
        "row": len(df)-1,
        "col": len(df.iloc[len(df)-1]),
        "date": dowload_load_image(url_1, 1)
    }

    # img_data = requests.get("https://drive.google.com/drive/u/1/folders/1Uo10QbdNXjSc2DaZcFfe-Y4o1M7eLnhd", stream=True).content
    # # print(img_data)
    # with open('image_name.jpg', 'wb') as handler:
    #     handler.write(img_data)

    # url = 'https://drive.google.com/drive/u/1/folders/1Uo10QbdNXjSc2DaZcFfe-Y4o1M7eLnhd'
    # output = '00000001.jpg'
    # gdown.download(url, output, quiet=False)

    # z = re.findall('(?<=id=)([^&\n]*)(?=&)?',k)[0]
    # Ok duoc
    # gdd.download_file_from_google_drive(file_id=z,
    #                                 dest_path='./data/02.jpg',
    #                                 unzip=True)
    # k = 'https://drive.google.com/file/d/1ho3UAHmYl_v901oVcA7kUpzyilSk-LXw/view'
    # z = re.findall('(\/file\/d\/)(.*?)(?:&|$)', k)
    # z = re.findall('\/file\/d\/([^&]*)', k)[0]
        # Ok duoc
    
    # gdd.download_file_from_google_drive(file_id=z.replace("/view", ""),
    #                                 dest_path='./data/031.jpg',
    #                                 unzip=True)
    return respon


def check_google_drive(check: str):
    if check == "nan":
        return False
    m = re.search('https?://([A-Za-z_0-9.-]+).*', check)
    if m is None:
        return False
    m = m.group(1)
    if m == 'drive.google.com':
        return True
    return False

def get_file_extension(filename: str):
    return filename.split(".")[-1]

def generate_ksuid() -> str:
    kid = str(datetime.datetime.now()).replace(" ", "")
    return kid

def get_new_filename(filename: str):
    ksuid = generate_ksuid()
    file_extension = get_file_extension(filename)
    return f'{ksuid}.{file_extension}'.replace(" ", "")

def dowload_load_image(url: str, id_dong_vat: int):
    chek = check_google_drive(url)
    if not chek:
        return False
    z = re.findall('(?<=id=)([^&\n]*)(?=&)?',url)

    if not z:
        z = re.findall('(\/file\/d\/)(.*?)(?:&|$)', url)[0]
    save_file = f'media/products/{id_dong_vat}/images'
    file_name = get_new_filename("jpg")
    file_location = f"{save_file}/{file_name}"
    
    gdd.download_file_from_google_drive(file_id=z[len(z)-1].replace("/view", ""),
                                    dest_path=file_location,
                                    unzip=True)
    return file_location