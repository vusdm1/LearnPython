def tao_phep_tinh(stt):
    """Trả về (a, b, phép_tính, đáp_án)."""
    if stt == 1:
        return 15, 27, "+", 42
    elif stt == 2:
        return 83, 45, "-", 38
    elif stt == 3:
        return 12, 6, "×", 72
    elif stt == 4:
        return 96, 8, "÷", 12
    elif stt == 5:
        return 17, 38, "+", 55
    elif stt == 6:
        return 100, 67, "-", 33
    elif stt == 7:
        return 15, 9, "×", 135
    elif stt == 8:
        return 144, 12, "÷", 12
    elif stt == 9:
        return 256, 189, "+", 445
    elif stt == 10:
        return 1000, 573, "-", 427
    return 0, 0, "", 0


def xep_loai_thi(dung, tong):
    """Xếp loại bài thi."""
    phan_tram = dung / tong * 100

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


def bat_dau_thi(so_cau):
    """Điều phối bài thi."""
    print("\n── BẮT ĐẦU THI ──\n")

    dung = 0
    sai = 0
    streak = 0
    streak_max = 0

    for i in range(1, so_cau + 1):
        a, b, phep, dap_an = tao_phep_tinh(i)

        tra_loi = int(input(f"Câu {i}: {a} {phep} {b} = ? "))

        if tra_loi == dap_an:
            dung = dung + 1
            streak = streak + 1
            if streak > streak_max:
                streak_max = streak
            print(f"✅ Chính xác! (+10 điểm) 🔥 Streak: {streak}")
        else:
            sai = sai + 1
            streak = 0
            print(f"❌ Sai! Đáp án đúng: {dap_an}. Streak reset!")

        print()

    return dung, sai, streak_max


def in_ket_qua_thi(dung, sai, tong, streak_max):
    """In bảng kết quả."""
    tong_diem = dung * 10
    diem_toi_da = tong * 10
    loai = xep_loai_thi(dung, tong)

    print("═" * 35)
    print("📊 KẾT QUẢ BÀI THI")
    print("═" * 35)
    print(f"  Số câu đúng    : {dung}/{tong}")
    print(f"  Số câu sai     : {sai}/{tong}")
    print(f"  Tổng điểm      : {tong_diem}/{diem_toi_da}")
    print(f"  Streak cao nhất: {streak_max} 🔥")
    print(f"  Xếp loại       : {loai}")
    print("═" * 35)


# === CHƯƠNG TRÌNH CHÍNH ===
while True:
    print("\n📝 THI TRẮC NGHIỆM TOÁN HỌC")
    print("═" * 30)
    print("1. Thi 5 câu (Dễ)")
    print("2. Thi 10 câu (Đầy đủ)")
    print("0. Thoát")

    lc = input("Chọn: ")

    if lc == "0":
        print("👋 Tạm biệt!")
        break

    elif lc == "1":
        dung, sai, streak_max = bat_dau_thi(5)
        in_ket_qua_thi(dung, sai, 5, streak_max)

    elif lc == "2":
        dung, sai, streak_max = bat_dau_thi(10)
        in_ket_qua_thi(dung, sai, 10, streak_max)

    else:
        print("❌ Lựa chọn không hợp lệ!")