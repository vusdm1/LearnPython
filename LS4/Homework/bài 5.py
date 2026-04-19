balance = 5000000 

while True:
    print("\nSố dư hiện tại:", balance, "đ")
    
    withdraw = int(input("Nhập số tiền rút (0 để thoát): "))
    
    if withdraw == 0:
        print("👋 Cảm ơn đã sử dụng dịch vụ! Số dư cuối:", balance, "đ")
        break
    
    if withdraw % 50000 != 0:
        print("❌ Số tiền phải là bội số của 50,000đ!")
        continue
    
    if withdraw > balance:
        print("❌ Số dư không đủ! Số dư hiện tại:", balance, "đ")
        continue
    
    balance -= withdraw
    print("✅ Rút thành công! Số dư:", balance, "đ")