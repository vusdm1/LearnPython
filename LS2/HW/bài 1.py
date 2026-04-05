can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao_cm = float(input("Nhập chiều cao (cm): "))
chieu_cao_m = chieu_cao_cm / 100
bmi = can_nang / (chieu_cao_m ** 2)

print("BMI của bạn là:", round(bmi, 2))

if bmi < 18.5:
    print("Phân loại: Thiếu cân")
elif bmi < 25:
    print("Phân loại: Bình thường")
elif bmi < 30:
    print("Phân loại: Thừa cân")
else:
    print("Phân loại: Béo phì")