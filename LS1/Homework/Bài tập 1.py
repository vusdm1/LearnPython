
print("================================================================")
print("          CHƯƠNG TRÌNH THU THẬP THÔNG TIN                     ")
print("================================================================")
print()

ho_ten = input("👤 Nhập tên của bạn: ").strip()
nam_sinh = int(input("📅 Nhập năm sinh: "))
thanh_pho = input("🏙️ Bạn đang sống ở đâu? ").strip()
chieu_cao_cm = float(input("📏 Chiều cao của bạn (cm): "))

nam_hien_tai = 2026
tuoi = nam_hien_tai - nam_sinh

chieu_cao_m = round(chieu_cao_cm / 100, 2)

print()
print("================================================================")
print("                  THÔNG TIN CÁ NHÂN                            ")
print("================================================================")

print(f"Họ tên          : {ho_ten}")
print(f"Tuổi            : {tuoi}")
print(f"Thành phố       : {thanh_pho}")
print(f"Chiều cao       : {chieu_cao_m:.2f} m")

print("================================================================")
print()

print(f"🎉 Chào {ho_ten}, chúc bạn học Python vui vẻ! 🎉")