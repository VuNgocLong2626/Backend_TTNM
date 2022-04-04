from sqlalchemy import (Boolean,
                        Column, Float,
                        Integer,
                        String,
                        ForeignKey,
                        DateTime,
                        UnicodeText,
                        null)
from app.db.database import Base
from sqlalchemy.orm import relationship


class Gioi(Base):
    __tablename__ = "gioi"

    id_gioi = Column(Integer, primary_key=True, index=True)

    name = Column(String(250))

    dong_vat = relationship("DongVat",
                        back_populates="gioi",
                        cascade="all, delete",
                        passive_deletes=True)


class Nganh(Base):
    __tablename__ = "nganh"

    id_nganh = Column(Integer, primary_key=True, index=True)

    name = Column(String(250))

    dong_vat = relationship("DongVat",
                        back_populates="nganh",
                        cascade="all, delete",
                        passive_deletes=True)


class Lop(Base):
    __tablename__ = "lop"

    id_lop = Column(Integer, primary_key=True, index=True)

    name = Column(String(250))

    dong_vat = relationship("DongVat",
                        back_populates="lop",
                        cascade="all, delete",
                        passive_deletes=True)


class Bo(Base):
    __tablename__ = "bo"

    id_bo = Column(Integer, primary_key=True, index=True)

    name = Column(String(250))

    dong_vat = relationship("DongVat",
                        back_populates="bo",
                        cascade="all, delete",
                        passive_deletes=True)


class Ho(Base):
    __tablename__ = "ho"

    id_ho = Column(Integer, primary_key=True, index=True)

    name = Column(String(250))

    dong_vat = relationship("DongVat",
                        back_populates="ho",
                        cascade="all, delete",
                        passive_deletes=True)


class GiaTri(Base):
    __tablename__ = "gia_tri"

    id_gia_tri = Column(Integer, primary_key=True, index=True)

    name = Column(String(250))

    dong_vat = relationship("DongVat",
                        back_populates="gia_tri",
                        cascade="all, delete",
                        passive_deletes=True)


class TinhTrangBaoTon(Base):
    __tablename__ = "tinh_trang_bao_ton"

    id_tinh_trang_bao_ton = Column(Integer, primary_key=True, index=True)

    name = Column(String(250))

    dong_vat = relationship("DongVat",
                        back_populates="tinh_trang_bao_ton",
                        cascade="all, delete",
                        passive_deletes=True)


class PhanBo(Base):
    __tablename__ = "phan_bo"

    id_phan_bo = Column(Integer, primary_key=True, index=True)

    name = Column(String(250))

    dong_vat = relationship("DongVat",
                        back_populates="phan_bo",
                        cascade="all, delete",
                        passive_deletes=True)


class TinhTrangMauVat(Base):
    __tablename__ = "tinh_trang_mau_vat"

    id_tinh_trang_mau_vat = Column(Integer, primary_key=True, index=True)

    name = Column(String(250))

    dong_vat = relationship("DongVat",
                        back_populates="tinh_trang_mau_vat",
                        cascade="all, delete",
                        passive_deletes=True)


class SinhCanh(Base):
    __tablename__ = "sinh_canh"

    id_sinh_canh = Column(Integer, primary_key=True, index=True)

    name = Column(String(250))

    dong_vat = relationship("DongVat",
                        back_populates="sinh_canh",
                        cascade="all, delete",
                        passive_deletes=True)


class User(Base):
    __tablename__ = "user"

    id_user = Column(Integer, primary_key=True, index=True)

    tk = Column(String(250))
    mk = Column(String(250))
    hten = Column(String(250))

    dong_vat = relationship("DongVat",
                        back_populates="user",
                        cascade="all, delete",
                        passive_deletes=True)


class DongVat(Base):
    __tablename__ = "dong_vat"

    id_dong_vat = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey(
        'user.id_user', ondelete="CASCADE"))
    id_gioi = Column(Integer, ForeignKey(
        'gioi.id_gioi', ondelete="CASCADE"))
    id_nganh = Column(Integer, ForeignKey(
        'nganh.id_nganh', ondelete="CASCADE"))
    id_lop = Column(Integer, ForeignKey(
        'lop.id_lop', ondelete="CASCADE"))
    id_bo = Column(Integer, ForeignKey(
        'bo.id_bo', ondelete="CASCADE"))
    id_ho = Column(Integer, ForeignKey(
        'ho.id_ho', ondelete="CASCADE"))
    id_gia_tri = Column(Integer, ForeignKey(
        'gia_tri.id_gia_tri', ondelete="CASCADE"))
    id_tinh_trang_bao_ton = Column(Integer, ForeignKey(
        'tinh_trang_bao_ton.id_tinh_trang_bao_ton', ondelete="CASCADE"))
    id_phan_bo = Column(Integer, ForeignKey(
        'phan_bo.id_phan_bo', ondelete="CASCADE"))
    id_tinh_trang_mau_vat = Column(Integer, ForeignKey(
        'tinh_trang_mau_vat.id_tinh_trang_mau_vat', ondelete="CASCADE"))
    id_sinh_canh = Column(Integer, ForeignKey(
        'sinh_canh.id_sinh_canh', ondelete="CASCADE"))

    ten_khoa_hoc = Column(String(250))
    ten_tieng_viet = Column(String(250))
    ten_dia_phuong = Column(String(250))
    dia_diem = Column(UnicodeText)
    hinh_thai = Column(UnicodeText)
    sinh_thai = Column(UnicodeText)
    ngay_thu_mau = Column(DateTime)

    user = relationship("User", back_populates="dong_vat")
    gioi = relationship("Gioi", back_populates="dong_vat")
    nganh = relationship("Nganh", back_populates="dong_vat")
    lop = relationship("Lop", back_populates="dong_vat")
    bo = relationship("Bo", back_populates="dong_vat")
    ho = relationship("Ho", back_populates="dong_vat")
    gia_tri = relationship("GiaTri", back_populates="dong_vat")
    tinh_trang_bao_ton = relationship("TinhTrangBaoTon", back_populates="dong_vat")
    phan_bo = relationship("PhanBo", back_populates="dong_vat")
    tinh_trang_mau_vat = relationship("TinhTrangMauVat", back_populates="dong_vat")
    sinh_canh = relationship("SinhCanh", back_populates="dong_vat")
    image = relationship("Image",
                                back_populates="dong_vat",
                                cascade="all, delete",
                                passive_deletes=True)




class Image(Base):
    __tablename__ = "image"

    id_image = Column(Integer, primary_key=True, index=True)
    id_dong_vat = Column(Integer, ForeignKey(
    'dong_vat.id_dong_vat', ondelete="CASCADE"))

    path = Column(String(250))

    dong_vat = relationship("DongVat", back_populates="image")