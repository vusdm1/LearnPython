
def lay_ten_sp(ma):
    if ma == 1:
        return "Nước suối"
    elif ma == 2:
        return "Trà xanh"
    elif ma == 3:
        return "Cà phê lon"
    elif ma == 4:
        return "Bánh mì"
    elif ma == 5:
        return "Snack"
    else:
        return None


def lay_gia_sp(ma):
    if ma == 1:
        return 8000
    elif ma == 2:
        return 12000
    elif ma == 3:
        return 15000
    elif ma == 4:
        return 20000
    elif ma == 5:
        return 10000
    else:
        return 0


def in_menu():
    print("🏪 MÁY BÁN HÀNG TỰ ĐỘNG")
    print("┌──────────────────────────┐")
    print("│ 1. Nước suối    8,000đ   │")
    print("│ 2. Trà xanh    12,000đ   │")
    print("│ 3. Cà phê lon  15,000đ   │")
    print("│ 4. Bánh mì     20,000đ   │")
    print("│ 5. Snack       10,000đ   │")
    print("│ 0. Thanh toán             │")
    print("└──────────────────────────┘")



gio_hang = []  
tong_tien = 0

while True:
    in_menu()
    ma = int(input("Chọn sản phẩm: "))

    if ma == 0:
        break

    ten = lay_ten_sp(ma)
    gia = lay_gia_sp(ma)

    if ten is None:
        print("❌ Mã không hợp lệ!")
        continue

    so_luong = int(input("Số lượng: "))
    thanh_tien = gia * so_luong

    gio_hang.append((ten, so_luong, thanh_tien))
    tong_tien += thanh_tien

    print(f"✅ Đã thêm: {ten} x{so_luong} = {thanh_tien:,}đ")



print("\n═══════════════════════════════")
print("📋 HÓA ĐƠN")
print("═══════════════════════════════")

for ten, sl, tt in gio_hang:
    print(f"{ten:<12} x{sl:<3} {tt:>10,}đ")

print("───────────────────────────────")
print(f"TỔNG CỘNG:{tong_tien:>15,}đ")
print("═══════════════════════════════")



tien_khach = int(input("\nTiền khách đưa: "))

if tien_khach < tong_tien:
    print("❌ Không đủ tiền!")
else:
    tien_thoi = tien_khach - tong_tien
    print(f"💰 Tiền thối: {tien_thoi:,}đ")
    print("Cảm ơn quý khách! 🙏")