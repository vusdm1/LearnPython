eng1 = "hello";  vie1 = "xin chào"
eng2 = "goodbye"; vie2 = "tạm biệt"
eng3 = "thank"; vie3 = "cảm ơn" 
eng4 = "sorry"; vie4 = "xin lỗi"
eng5 = "love"; vie5 = "yêu thương"
eng6 = "friend"; vie6 = "bạn bè"
eng7 = "school"; vie7 = "trường học"
eng8 = "teacher"; vie8 = "giáo viên"
eng9 = "student"; vie9 = "học sinh"
eng10 = "python"; vie10 = "con trăn / ngôn ngữ lập trình"

def tra_tu(eng):
    if eng == eng1:
        return vie1
    elif eng == eng2:
        return vie2
    elif eng == eng3:
        return vie3
    elif eng == eng4:
        return vie4
    elif eng == eng5:
        return vie5
    elif eng == eng6:
        return vie6
    elif eng == eng7:
        return vie7
    elif eng == eng8:
        return vie8
    elif eng == eng9:
        return vie9
    elif eng == eng10:
        return vie10
    else:
        return "Không tìm thấy từ cần tra"
    

def in_menu():
    print("\n📖 TỪ ĐIỂN ANH-VIỆT MINI")
    print("1. Tra từ")
    print("2. Xem tất cả từ vựng")
    print("3. Kiểm tra từ vựng")
    print("0. Thoát")


def hien_thi_tat_ca():
    print("\n📚 TẤT CẢ TỪ VỰNG:")
    print(eng1, "→", vie1)
    print(eng2, "→", vie2)
    print(eng3, "→", vie3)
    print(eng4, "→", vie4)
    print(eng5, "→", vie5)
    print(eng6, "→", vie6)
    print(eng7, "→", vie7)
    print(eng8, "→", vie8)
    print(eng9, "→", vie9)
    print(eng10, "→", vie10)

def kiem_tra(): 
    diem = 0
    print("\n🧠 KIỂM TRA TỪ VỰNG")

    ans= input('Câu 1: "xin chào" tiếng Anh là gì?')
    if ans == "hello": print("✅ Đúng!"); diem += 1
    else: print("❌ Sai! Đáp án: hello")

    ans = input('Câu 2: "bạn bè" tiếng Anh là gì? ')
    if ans == "friend": print("✅ Đúng!"); diem += 1
    else: print("❌ Sai! Đáp án: friend")

    ans = input('Câu 3: "trường học" tiếng Anh là gì? ')
    if ans == "school": print("✅ Đúng!"); diem += 1
    else: print("❌ Sai! Đáp án: school")

    ans = input('Câu 4: "giáo viên" tiếng Anh là gì? ')
    if ans == "teacher": print("✅ Đúng!"); diem += 1
    else: print("❌ Sai! Đáp án: teacher")

    ans = input('Câu 5: "cảm ơn" tiếng Anh là gì? ')
    if ans == "thank": print("✅ Đúng!"); diem += 1
    else: print("❌ Sai! Đáp án: thank")
   
    print(f"\n🎉 Bạn đã đạt được {diem}/5 điểm!")

def main():
    while True:
        in_menu()
        chon = input("Chọn: ")
        if chon == "1":
            tu = input ("Nhập từ tiếng Anh cần tra: ")
            kq = tra_tu(tu)
            if kq == "Không tìm thấy từ cần tra":
                print("❌", kq)   
            else:
                print("✅", tu, "→", kq)
        elif chon == "2":
            hien_thi_tat_ca()
        elif chon == "3":
            kiem_tra()
        elif chon == "0":
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
