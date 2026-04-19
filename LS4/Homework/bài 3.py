n = int(input("Nhập N:  "))
tong=0
for i in range(1, n+1):
    if i % 3 !=0 or i % 5 !=0:
        continue
    print(i)
    tong +=1
    if tong == 0:
        print("(không có số nào)")

print(f"Tổng Cộng: {tong} số")