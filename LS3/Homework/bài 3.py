def lay_gia_nhien_lieu(loai):
    if loai == "ron95":
        return 25670
    elif loai == "ron92":
        return 23820
    elif loai == "diesel":
        return 21350
    else:
        return -1


def tinh_giam_gia_lit(so_lit):
    if so_lit >= 50:
        return 800
    elif so_lit >= 30:
        return 500
    else:
        return 0


def tinh_tien(loai, so_lit):
    gia = lay_gia_nhien_lieu(loai)
    if gia == -1:
        return -1, -1

    tien_goc = gia * so_lit
    giam_moi_lit = tinh_giam_gia_lit(so_lit)
    tien_sau_giam = (gia - giam_moi_lit) * so_lit

    return tien_goc, tien_sau_giam


def tinh_tich_luy(tien, co_the_tv):
    if co_the_tv:
        return tien * 0.01
    return 0


def tinh_phu_thu(tien, hinh_thuc):
    if hinh_thuc == "the":
        return tien * 0.01
    return 0


def ten_nhien_lieu(loai):
    if loai == "ron95":
        return "Xăng RON 95"
    elif loai == "ron92":
        return "Xăng RON 92"
    elif loai == "diesel":
        return "Dầu Diesel"
    else:
        return "Không xác định"


def in_hoa_don_xang(ten_khach, loai, so_lit, co_the_tv, hinh_thuc):
    tien_goc, tien_sau_giam = tinh_tien(loai, so_lit)

    if tien_goc == -1:
        print("❌ Loại nhiên liệu không hợp lệ!")
        return

    phu_thu = tinh_phu_thu(tien_sau_giam, hinh_thuc)    
    tong = tien_sau_giam + phu_thu
    diem = tinh_tich_luy(tong, co_the_tv)

    print("╔════════════════════════════════════╗")
    print("║          HÓA ĐƠN XĂNG             ║")
    print("╠════════════════════════════════════╣")
    print(f"║ Khách hàng : {ten_khach:<20}║")
    print(f"║ Nhiên liệu : {ten_nhien_lieu(loai):<20}║")
    print(f"║ Số lít     : {so_lit:<20}║")
    print(f"║ Tiền gốc   : {tien_goc:,.0f} đ{' '*(10-len(format(tien_goc, ',.0f')))}║")
    print(f"║ Sau giảm   : {tien_sau_giam:,.0f} đ{' '*(10-len(format(tien_sau_giam, ',.0f')))}║")
    print(f"║ Phụ thu    : {phu_thu:,.0f} đ{' '*(10-len(format(phu_thu, ',.0f')))}║")
    print(f"║ Tổng tiền  : {tong:,.0f} đ{' '*(10-len(format(tong, ',.0f')))}║")
    print(f"║ Tích lũy   : {diem:,.0f} điểm{' '*(7-len(format(diem, ',.0f')))}║")
    print("╚════════════════════════════════════╝")


# 🔹 Chương trình chính
ten = input("Nhập tên khách: ")
loai = input("Loại (ron95/ron92/diesel): ").lower()
so_lit = float(input("Số lít: "))
co_the = input("Có thẻ thành viên? (y/n): ").lower() == "y"
hinh_thuc = input("Thanh toán (tien_mat/the): ").lower()

in_hoa_don_xang(ten, loai, so_lit, co_the, hinh_thuc)