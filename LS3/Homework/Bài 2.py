def nhap_diem(ten_cot):
    while True:
        try:
            diem = float(input(f"Nhập điểm {ten_cot}: "))
            if 0 <= diem <= 10:
                return diem
            else:
                print(" Điểm phải từ 0 đến 10!")
        except ValueError:
            print(" Vui lòng nhập số!")


def tinh_dtb_he_so(mieng, muoi_lam, mot_tiet, thi):
    return (mieng + muoi_lam + 2*mot_tiet + 3*thi) / 7


def xep_loai(dtb):
    if dtb >= 9:
        return "Xuất sắc "
    elif dtb >= 8:
        return "Giỏi "
    elif dtb >= 6.5:
        return "Khá "
    elif dtb >= 5:
        return "Trung bình "
    elif dtb >= 3.5:
        return "Yếu "
    else:
        return "Kém "


def nhan_xet(mieng, thi, dtb):
    if thi >= 8 and dtb >= 7:
        return "📈 Tiến bộ rõ rệt!"
    elif thi < mieng - 2:
        return "📉 Cần ôn tập kỹ hơn!"
    else:
        return "Bình thường"


def in_phieu_diem(ten_hs, ten_mon, mieng, muoi_lam, mot_tiet, thi):
    dtb = tinh_dtb_he_so(mieng, muoi_lam, mot_tiet, thi)
    loai = xep_loai(dtb)
    nx = nhan_xet(mieng, thi, dtb)

    print("\n===== PHIẾU ĐIỂM =====")
    print(f"Học sinh : {ten_hs}")
    print(f"Môn học  : {ten_mon}")
    print(f"Miệng    : {mieng}")
    print(f"15 phút  : {muoi_lam}")
    print(f"1 tiết   : {mot_tiet}")
    print(f"Thi CK   : {thi}")
    print(f"ĐTB      : {dtb:.2f}")
    print(f"Xếp loại : {loai}")
    print(f"Nhận xét : {nx}")


ten = input("Nhập tên học sinh: ")
mon = input("Nhập môn học: ")

mieng = nhap_diem("miệng")
muoi_lam = nhap_diem("15 phút")
mot_tiet = nhap_diem("1 tiết")
thi = nhap_diem("thi cuối kỳ")

in_phieu_diem(ten, mon, mieng, muoi_lam, mot_tiet, thi)