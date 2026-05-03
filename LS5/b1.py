def lay_cau_hoi(stt):
    """Trả về chuỗi câu hỏi theo số thứ tự."""
    if stt == 1:
        return "Thủ đô của Việt Nam?"
    elif stt == 2:
        return "Python là ngôn ngữ gì?"
    elif stt == 3:
        return "1 KB = ? byte"
    elif stt == 4:
        return "Ai phát minh ra Python?"
    elif stt == 5:
        return "HTML dùng để làm gì?"
    else:
        return ""


def lay_dap_an_a(stt):
    """Trả về đáp án A."""
    if stt == 1:
        return "HCM"
    elif stt == 2:
        return "Biên dịch"
    elif stt == 3:
        return "100"
    elif stt == 4:
        return "Bill Gates"
    elif stt == 5:
        return "Lập trình"
    return ""


def lay_dap_an_b(stt):
    """Trả về đáp án B."""
    if stt == 1:
        return "Đà Nẵng"
    elif stt == 2:
        return "Thông dịch"
    elif stt == 3:
        return "500"
    elif stt == 4:
        return "Guido van Rossum"
    elif stt == 5:
        return "Cơ sở dữ liệu"
    return ""


def lay_dap_an_c(stt):
    """Trả về đáp án C."""
    if stt == 1:
        return "Hà Nội"
    elif stt == 2:
        return "Máy"
    elif stt == 3:
        return "1000"
    elif stt == 4:
        return "Elon Musk"
    elif stt == 5:
        return "Tạo trang web"
    return ""


def lay_dap_an_d(stt):
    """Trả về đáp án D."""
    if stt == 1:
        return "Huế"
    elif stt == 2:
        return "Assembly"
    elif stt == 3:
        return "1024"
    elif stt == 4:
        return "Steve Jobs"
    elif stt == 5:
        return "Đồ hoạ"
    return ""


def lay_dap_an_dung(stt):
    """Trả về đáp án đúng (A/B/C/D)."""
    if stt == 1:
        return "C"
    elif stt == 2:
        return "B"
    elif stt == 3:
        return "D"
    elif stt == 4:
        return "B"
    elif stt == 5:
        return "C"
    return ""


def kiem_tra(tra_loi, dap_an):
    """Kiểm tra đáp án."""
    return tra_loi.upper() == dap_an.upper()


def xep_hang(diem, tong):
    """Xếp hạng dựa trên điểm."""
    phan_tram = diem / tong * 100

    if phan_tram == 100:
        return "🏆 Hoàn hảo!"
    elif phan_tram >= 80:
        return "⭐ Giỏi!"
    elif phan_tram >= 60:
        return "👍 Khá!"
    elif phan_tram >= 40:
        return "🤔 Trung bình"
    else:
        return "😅 Cần cố gắng hơn"


# === CHƯƠNG TRÌNH CHÍNH ===
print("🧠 QUIZ KIẾN THỨC TỔNG QUÁT")
print("═" * 40)

so_cau = 5
diem = 0
ket_qua = ""

for stt in range(1, so_cau + 1):
    cau_hoi = lay_cau_hoi(stt)
    a = lay_dap_an_a(stt)
    b = lay_dap_an_b(stt)
    c = lay_dap_an_c(stt)
    d = lay_dap_an_d(stt)
    dap_an = lay_dap_an_dung(stt)

    print(f"\nCâu {stt}/{so_cau}: {cau_hoi}")
    print(f"  A. {a}    B. {b}")
    print(f"  C. {c}    D. {d}")

    tra_loi = input("Đáp án của bạn: ")

    if kiem_tra(tra_loi, dap_an):
        print("✅ Chính xác!")
        diem = diem + 1
        ket_qua = ket_qua + "✅ "
    else:
        print(f"❌ Sai! Đáp án đúng: {dap_an}")
        ket_qua = ket_qua + "❌ "

# In kết quả
phan_tram = diem / so_cau * 100
hang = xep_hang(diem, so_cau)

print("\n" + "═" * 40)
print("📊 KẾT QUẢ")
print("═" * 40)
print(f"  {ket_qua}")
print("─" * 40)
print(f"  Điểm: {diem}/{so_cau} ({phan_tram:.0f}%)")
print(f"  Xếp hạng: {hang}")
print("═" * 40)