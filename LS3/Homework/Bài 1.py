def tinh_phi_gui_xe(loai_xe, so_gio):
    phi = 0

    # 🚲 Xe đạp
    if loai_xe == "xd":
        if so_gio <= 2:
            phi = 0
        else:
            phi = (so_gio - 2) * 2000

    # 🏍️ Xe máy
    elif loai_xe == "xm":
        if so_gio == 1:
            phi = 5000
        elif so_gio <= 4:
            phi = 5000 + (so_gio - 1) * 3000
        else:
            phi = 5000 + 3 * 3000 + (so_gio - 4) * 5000

    # 🚗 Ô tô
    elif loai_xe == "ot":
        if so_gio == 1:
            phi = 20000
        elif so_gio <= 3:
            phi = 20000 + (so_gio - 1) * 10000
        else:
            phi = 20000 + 2 * 10000 + (so_gio - 3) * 15000

    return phi


def ap_dung_giam_gia(phi, ban_dem, la_vip):
    giam = 0

    if ban_dem:
        giam += phi * 0.3   # giảm 30%

    if la_vip:
        giam += phi * 0.1   # giảm thêm 10%

    return phi - giam, giam


def ten_loai_xe(ma_xe):
    if ma_xe == "xd":
        return "Xe đạp"
    elif ma_xe == "xm":
        return "Xe máy"
    elif ma_xe == "ot":
        return "Ô tô"
    else:
        return "Không xác định"


def in_ve_xe(ten_khach, loai_xe, so_gio, ban_dem, la_vip):
    phi_goc = tinh_phi_gui_xe(loai_xe, so_gio)
    thanh_tien, giam = ap_dung_giam_gia(phi_goc, ban_dem, la_vip)


    print("║       VÉ GIỮ XE THÔNG MINH      ║")
    print(f"║ Khách hàng : {ten_khach}║")
    print(f"║ Loại xe    : {ten_loai_xe(loai_xe)}║")
    print(f"║ Thời gian  : {so_gio} giờ{' '*(12-len(str(so_gio)))}║")
    print(f"║ Phí gốc    : {phi_goc:,.0f} đồng{' '*(7-len(format(phi_goc, ',.0f')))}║")
    print(f"║ Giảm giá   : {giam:,.0f} đồng{' '*(7-len(format(giam, ',.0f')))}║")
    print(f"║ Thành tiền : {thanh_tien:,.0f} đồng{' '*(7-len(format(thanh_tien, ',.0f')))}║")
    print("╚══════════════════════════════════╝")


# 🔹 Chương trình chính
ten = input("Nhập tên khách hàng: ")
loai = input("Nhập loại xe (xd/xm/ot): ").lower()
gio = int(input("Nhập số giờ gửi: "))
ban_dem = input("Gửi ban đêm? (y/n): ").lower() == "y"
vip = input("Khách VIP? (y/n): ").lower() == "y"

in_ve_xe(ten, loai, gio, ban_dem, vip)