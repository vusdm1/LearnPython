so_du = 5000000
print("Mô phỏng rút tiền ATM")
print("=" * 38)

pin = input("Nhập mã PIN: ")

if pin == "1234":
    tien_rut = int(input("Nhập số tiền bạn cần rút: "))
    
    if tien_rut % 50000 != 0:
        print("Số tiền phải chia hết cho 50,000 VNĐ")
    elif tien_rut > so_du:
        print("Tiền rút không được vượt quá số dư")
    elif tien_rut <= 0:
        print("Số tiền không hợp lệ")
    else:
        so_du -= tien_rut
        print("Rút tiền thành công!")
        print("Số dư còn lại:", so_du, "VNĐ")
else:
    print("Nhập sai mã PIN! xin vui lòng thử lại")