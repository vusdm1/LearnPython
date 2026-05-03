def tra_tu(tu):
    """Tra nghĩa tiếng Việt. Trả 'Không tìm thấy' nếu không có."""
    tu = tu.lower()

    if tu == "hello":
        return "xin chào"
    elif tu == "goodbye":
        return "tạm biệt"
    elif tu == "thank":
        return "cảm ơn"
    elif tu == "sorry":
        return "xin lỗi"
    elif tu == "love":
        return "yêu thương"
    elif tu == "friend":
        return "bạn bè"
    elif tu == "school":
        return "trường học"
    elif tu == "teacher":
        return "giáo viên"
    elif tu == "student":
        return "học sinh"
    elif tu == "python":
        return "con trăn / ngôn ngữ lập trình"
    else:
        return "Không tìm thấy"


def lay_tu_tieng_anh(stt):
    """Trả về từ tiếng Anh theo thứ tự (dùng cho kiểm tra)."""
    if stt == 1:
        return "hello"
    elif stt == 2:
        return "friend"
    elif stt == 3:
        return "teacher"
    elif stt == 4:
        return "sorry"
    elif stt == 5:
        return "school"
    return ""


def in_menu():
    """In menu chức năng."""
    print("\n📖 TỪ ĐIỂN ANH-VIỆT MINI")
    print("─" * 30)
    print("1. Tra từ")
    print("2. Xem tất cả từ vựng")
    print("3. Kiểm tra từ vựng")
    print("0. Thoát")


def xem_tat_ca():
    """In tất cả từ vựng."""
    print("\n📚 TẤT CẢ TỪ VỰNG:")
    print("─" * 35)
    print(f"  {'hello':<12} → xin chào")
    print(f"  {'goodbye':<12} → tạm biệt")
    print(f"  {'thank':<12} → cảm ơn")
    print(f"  {'sorry':<12} → xin lỗi")
    print(f"  {'love':<12} → yêu thương")
    print(f"  {'friend':<12} → bạn bè")
    print(f"  {'school':<12} → trường học")
    print(f"  {'teacher':<12} → giáo viên")
    print(f"  {'student':<12} → học sinh")
    print(f"  {'python':<12} → con trăn / ngôn ngữ LP")
    print("─" * 35)


def kiem_tra_tu_vung():
    """Kiểm tra từ vựng - 5 câu."""
    print("\n📝 KIỂM TRA TỪ VỰNG (5 câu)")
    print("─" * 30)

    diem = 0

    for i in range(1, 6):
        tu = lay_tu_tieng_anh(i)
        nghia = tra_tu(tu)

        tra_loi = input(f'\nCâu {i}: "{nghia}" tiếng Anh là gì? ')

        if tra_loi.lower() == tu:
            print("✅ Đúng!")
            diem = diem + 1
        else:
            print(f"❌ Sai! Đáp án: {tu}")

    phan_tram = diem / 5 * 100
    print(f"\n📊 Kết quả: {diem}/5 ({phan_tram:.0f}%)")


# === CHƯƠNG TRÌNH CHÍNH ===
while True:
    in_menu()
    lc = input("\nChọn: ")

    if lc == "0":
        print("👋 Tạm biệt!")
        break
    elif lc == "1":
        tu = input("Nhập từ tiếng Anh: ")
        nghia = tra_tu(tu)
        if nghia == "Không tìm thấy":
            print(f'→ Không tìm thấy từ "{tu}"!')
        else:
            print(f'→ "{tu}" = "{nghia}"')
    elif lc == "2":
        xem_tat_ca()
    elif lc == "3":
        kiem_tra_tu_vung()
    else:
        print("❌ Lựa chọn không hợp lệ!")