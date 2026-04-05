print("Tính điện tiền điện theo bậc thang")
print("="*38)
kwh = float(input("Nhập số kWh tiêu thụ: "))
tien=0
if kwh <+50:
    tien = kwh * 1678
elif kwh <= 100:
    tien = 50 * 1678 + (kwh - 50) * 1734
elif kwh <= 200:
    tien = 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
elif kwh <= 300:
    tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + (kwh - 200) * 2536
elif kwh <= 400:
    tien = (50 * 1678 + 50 * 1734 + 100 * 2014 +
            100 * 2536 + (kwh - 300) * 2834)
else:
    tien = (50 * 1678 + 50 * 1734 + 100 * 2014 +
            100 * 2536 + 100 * 2834 + (kwh - 400) * 2927)
print("Tổng tiền điện là:", int(tien), "đ")