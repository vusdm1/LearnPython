print("            🏥CHƯƠNG TRÌNH TÍNH CHỈ SỐ BMI.                     ")
print("================================================================")
ten= input("👤 Nhập tên của bạn" )
can_nang= float(input("Cân nặng (kg): "))
chieu_cao = float(input("Chiều cao (cm): "))
chieu_cao_m = chieu_cao / 100
bmi = can_nang / (chieu_cao_m ** 2)

print(f"\n📊 Kết quả của {ten}:")
print(f"   Cân nặng  : {can_nang} kg")
print(f"   Chiều cao : {chieu_cao_m:.2f} m")
print(f"   Chỉ số BMI: {bmi:.1f}")
print(f"\n💡 Tham khảo:")
print(f"   BMI < 18.5     : Thiếu cân")
print(f"   18.5 ≤ BMI < 25: Bình thường")
print(f"   25 ≤ BMI < 30  : Thừa cân")
print(f"   BMI ≥ 30       : Béo phì")

print("================================================================")
print()

print(f"🎉 Chào {ten}, chúc bạn học Python vui vẻ! 🎉")