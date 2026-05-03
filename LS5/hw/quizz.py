def laycauhoi(stt):
    if stt == 1:
        return "Thủ đô của Việt Nam?"
    if stt == 2:
        return "Python là ngôn ngữ gì?"
    if stt == 3:
        return "1 KB = ? byte"
    if stt == 4:
        return "Ai phát minh Python?"
    if stt == 5:
        return "HTML dùng để?"
    else:
        return ""
    
def lay_dap_an_a(stt):
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

def kiem_tra(tra_loi, dap_an):
    return tra_loi.lower() == dap_an.lower()

def dap_an_dung(stt):
    if stt ==1 :
        return "C"
    if stt == 2:
        return "B"
    if stt == 3:
        return "D"
    if stt == 4:
        return "B"
    if stt == 5:
        return "C"
    return()

def xep_hang(diem, tong):
    phan_tram = (diem / tong) * 100
    
    if phan_tram == 100:
        return "🏆 Xuất sắc!"
    elif phan_tram >= 80:
        return "⭐ Giỏi!"
    elif phan_tram >= 60:
        return "👍 Khá!"
    elif phan_tram >= 40:
        return "😐 Trung bình"
    else:
        return "😅 Cần cố gắng hơn"
    
print("🧠 QUIZ KIẾN THỨC TỔNG QUÁT")
print("========================================")

SO_CAU = 5
DIEM = 0
KET_QUA = ""

for stt in range(1, SO_CAU + 1):
    cau_hoi = laycauhoi(stt)
    a = lay_dap_an_a(stt)
    b = lay_dap_an_b(stt)
    c = lay_dap_an_c(stt)
    d = lay_dap_an_d(stt)

for stt in range(1, SO_CAU + 1):
    cau_hoi = laycauhoi(stt)
    a = lay_dap_an_a(stt)
    b = lay_dap_an_b(stt)
    c = lay_dap_an_c(stt)
    d = lay_dap_an_d(stt)

    dap_an = dap_an_dung(stt)

    print(f"Câu {stt}/{SO_CAU}: {cau_hoi}")
    print(f" A. {a}     B. {b}")
    print(f" C. {c}     D. {d}")
    
    tra_loi = input("Đáp án của bạn (A/B/C/D): ")

    if kiem_tra(tra_loi, dap_an):
        print("✅ Chính xác!")
        DIEM += 1
        KET_QUA = KET_QUA + "✅"
    else:
        print(f"❌ Sai rồi! Đáp án đúng là: {dap_an}")
        KET_QUA = KET_QUA + "❌"

hang = xep_hang(DIEM, SO_CAU)

print("=" * 40)
print("📊 KẾT QUẢ")
print("=" * 40)
print(KET_QUA)
print("-" * 40)
print(f"Điểm: {DIEM}/{SO_CAU} ({DIEM / SO_CAU * 100:.0f}%)")
print(f"Xếp hạng: {hang}")
print("=" * 40)