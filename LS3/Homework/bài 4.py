def gia_ve_co_ban(loai_phim):
    if loai_phim == "2d":
        return 65000
    elif loai_phim == "3d":
        return 95000
    elif loai_phim == "imax":
        return 150000
    else:
        return -1


def phu_thu_suat_chieu(suat):
    if suat == "sang":
        return 0
    elif suat == "chieu":
        return 10000
    elif suat == "toi":
        return 20000
    else:
        return 0


def giam_gia_doi_tuong(tuoi, la_hoc_sinh):
    if tuoi < 6:
        return 1.0   # miễn phí
    elif tuoi >= 60:
        return 0.3
    elif la_hoc_sinh:
        return 0.2
    else:
        return 0.0


def gia_combo(ma_combo):
    if ma_combo == "a":
        return 49000
    elif ma_combo == "b":
        return 79000
    else:
        return 0


def tinh_tien_ve(loai_phim, suat, tuoi, la_hs, so_ve, ma_combo):
    gia = gia_ve_co_ban(loai_phim)
    if gia == -1:
        return -1

    phu_thu = phu_thu_suat_chieu(suat)
    giam = giam_gia_doi_tuong(tuoi, la_hs)

    gia_1_ve = (gia + phu_thu) * (1 - giam)
    tien_ve = gia_1_ve * so_ve

    tien_combo = gia_combo(ma_combo)

    tong = tien_ve + tien_combo
    return tong, tien_ve, tien_combo


def ten_phim(loai):
    return {"2d": "Phim 2D", "3d": "Phim 3D", "imax": "IMAX"}.get(loai, "Không rõ")


def ten_suat(suat):
    return {"sang": "Suất sáng", "chieu": "Suất chiều", "toi": "Suất tối"}.get(suat, "")


def in_ve_phim(ten_khach, loai, suat, tuoi, la_hs, so_ve, ma_combo):
    kq = tinh_tien_ve(loai, suat, tuoi, la_hs, so_ve, ma_combo)

    if kq == -1:
        print("❌ Loại phim không hợp lệ!")
        return

    tong, tien_ve, tien_combo = kq

    print("╔════════════════════════════════════╗")
    print("║           VÉ XEM PHIM             ║")
    print("╠════════════════════════════════════╣")
    print(f"║ Khách hàng : {ten_khach:<20}║")
    print(f"║ Loại phim  : {ten_phim(loai):<20}║")
    print(f"║ Suất chiếu : {ten_suat(suat):<20}║")
    print(f"║ Số vé      : {so_ve:<20}║")
    print(f"║ Tiền vé    : {tien_ve:,.0f} đ{' '*(10-len(format(tien_ve, ',.0f')))}║")
    print(f"║ Combo      : {tien_combo:,.0f} đ{' '*(10-len(format(tien_combo, ',.0f')))}║")
    print(f"║ Tổng tiền  : {tong:,.0f} đ{' '*(10-len(format(tong, ',.0f')))}║")
    print("╚════════════════════════════════════╝")


# 🔹 Chương trình chính
print("=== MENU RẠP PHIM ===")
print("Loại phim: 2d / 3d / imax")
print("Suất: sang / chieu / toi")
print("Combo: a / b / none")

ten = input("Tên khách: ")
loai = input("Loại phim: ").lower()
suat = input("Suất chiếu: ").lower()
tuoi = int(input("Tuổi: "))
la_hs = input("Học sinh? (y/n): ").lower() == "y"
so_ve = int(input("Số vé: "))
combo = input("Combo (a/b/none): ").lower()

in_ve_phim(ten, loai, suat, tuoi, la_hs, so_ve, combo)