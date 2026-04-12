# 🐍 GIÁO TRÌNH PYTHON — BUỔI 4

## **VÒNG LẶP FOR VÀ WHILE: LÀM VIỆC LẶP LẠI MỘT CÁCH THÔNG MINH**

> _"Máy tính giỏi nhất ở việc lặp lại — và vòng lặp là cách ta ra lệnh cho nó."_

| Thông tin buổi học     | Chi tiết                                                                          |
| ---------------------- | --------------------------------------------------------------------------------- |
| **Buổi**               | 04                                                                                |
| **Chủ đề**             | Vòng lặp `for`, `while`, lệnh `break`, `continue`, `range()`                     |
| **Thời lượng**         | ~2 - 3 giờ (bao gồm thực hành)                                                   |
| **Yêu cầu**           | Đã nắm kiến thức về biến, kiểu dữ liệu, câu điều kiện, hàm                      |
| **Mục tiêu tổng quát** | Biết dùng vòng lặp để tự động hóa các công việc lặp đi lặp lại                    |

---

# 📌 MỤC LỤC

- [Module 1: Vì sao cần vòng lặp?](#module-1-vì-sao-cần-vòng-lặp)
- [Module 2: Vòng lặp `for` và `range()`](#module-2-vòng-lặp-for-và-range)
- [Module 3: Vòng lặp `while`](#module-3-vòng-lặp-while)
- [Module 4: `break` và `continue`](#module-4-break-và-continue)
- [Module 5: Vòng lặp lồng nhau](#module-5-vòng-lặp-lồng-nhau)
- [Module 6: Kết hợp vòng lặp với hàm](#module-6-kết-hợp-vòng-lặp-với-hàm)
- [📚 Phương pháp học vòng lặp hiệu quả](#-phương-pháp-học-vòng-lặp-hiệu-quả)
- [📝 Bài tập thực hành](#-bài-tập-thực-hành)

---

---

# Module 1: Vì sao cần vòng lặp?

## 🎯 Mục tiêu

> Hiểu rằng vòng lặp giúp ta **tự động hóa** việc lặp lại mà không cần viết code trùng lặp.

---

## 1.1. Vấn đề khi chưa có vòng lặp

Giả sử ta muốn in "Xin chào!" 5 lần:

```python
print("Xin chào!")
print("Xin chào!")
print("Xin chào!")
print("Xin chào!")
print("Xin chào!")
```

Nếu muốn in 100 lần thì sao? 1000 lần? → **Không thể viết bằng tay!**

## 1.2. Giải pháp: Vòng lặp

```python
for i in range(5):
    print("Xin chào!")
```

> 💡 Vòng lặp giúp ta nói với máy tính: **"Hãy làm việc này N lần"** chỉ trong vài dòng code.

## 1.3. Hai loại vòng lặp trong Python

| Loại       | Khi nào dùng?                                        |
| ---------- | ---------------------------------------------------- |
| **`for`**  | Khi biết trước số lần lặp (đếm từ 1 đến 10, duyệt danh sách...) |
| **`while`** | Khi chưa biết trước, lặp cho đến khi điều kiện sai   |

**Ví dụ đời thường:**

- `for`: "Hãy ăn đúng **5** muỗng cơm" → biết trước số lần
- `while`: "Hãy ăn **cho đến khi no**" → không biết trước bao nhiêu lần

---

### ✅ Kiểm tra nhanh Module 1

Tình huống nào nên dùng `for`, tình huống nào nên dùng `while`?

1. In bảng cửu chương từ 1 đến 9
2. Hỏi mật khẩu cho đến khi nhập đúng
3. Tính tổng các số từ 1 đến 100

<details>
<summary>👀 Xem đáp án</summary>

1. `for` — biết trước số lần (1 đến 9)
2. `while` — không biết trước bao nhiêu lần nhập sai
3. `for` — biết trước dãy số (1 đến 100)

</details>

---

---

# Module 2: Vòng lặp `for` và `range()`

## 🎯 Mục tiêu

> Biết dùng `for` kết hợp với `range()` để lặp theo số lần xác định.

---

## 2.1. Cú pháp cơ bản

```python
for bien_dem in range(so_lan):
    # Khối lệnh sẽ lặp lại
    print("Lặp")
```

**Giải thích:**

- `for` là từ khóa bắt đầu vòng lặp
- `bien_dem` là biến tự động đếm từ 0
- `range(so_lan)` tạo ra dãy số từ 0 đến `so_lan - 1`
- Khối lệnh bên trong phải **thụt đầu dòng**

## 2.2. Ví dụ đầu tiên

```python
for i in range(5):
    print(f"Lần thứ {i}")
```

**Kết quả:**

```
Lần thứ 0
Lần thứ 1
Lần thứ 2
Lần thứ 3
Lần thứ 4
```

> ⚠️ `range(5)` bắt đầu từ **0** và kết thúc ở **4** (tổng cộng 5 lần).

## 2.3. Hiểu `range()` chi tiết

`range()` có 3 cách sử dụng:

### Cách 1: `range(n)` — từ 0 đến n-1

```python
for i in range(4):
    print(i)   # 0, 1, 2, 3
```

### Cách 2: `range(start, stop)` — từ start đến stop-1

```python
for i in range(1, 6):
    print(i)   # 1, 2, 3, 4, 5
```

### Cách 3: `range(start, stop, step)` — có bước nhảy

```python
for i in range(0, 10, 2):
    print(i)   # 0, 2, 4, 6, 8

for i in range(10, 0, -1):
    print(i)   # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

## 2.4. Ví dụ thực hành: Tính tổng các số từ 1 đến N

```python
n = int(input("Nhập N: "))
tong = 0

for i in range(1, n + 1):
    tong = tong + i

print(f"Tổng từ 1 đến {n} = {tong}")
```

**Chạy thử:**

```
Nhập N: 5
Tổng từ 1 đến 5 = 15
```

> 💡 Biến `tong` được gọi là **biến tích lũy** (accumulator) — một kỹ thuật cực kỳ quan trọng!

## 2.5. Ví dụ thực hành: Đếm số chẵn, số lẻ

```python
n = int(input("Nhập N: "))
dem_chan = 0
dem_le = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        dem_chan = dem_chan + 1
    else:
        dem_le = dem_le + 1

print(f"Từ 1 đến {n}:")
print(f"  Số chẵn: {dem_chan}")
print(f"  Số lẻ : {dem_le}")
```

**Chạy thử:**

```
Nhập N: 10
Từ 1 đến 10:
  Số chẵn: 5
  Số lẻ : 5
```

## 2.6. Ví dụ thực hành: In bảng cửu chương

```python
so = int(input("Nhập số cần in bảng cửu chương: "))

print(f"\n📋 BẢNG CỬU CHƯƠNG {so}")
print("-" * 20)

for i in range(1, 11):
    ket_qua = so * i
    print(f"  {so} x {i:>2} = {ket_qua:>3}")
```

**Chạy thử:**

```
Nhập số cần in bảng cửu chương: 7

📋 BẢNG CỬU CHƯƠNG 7
--------------------
  7 x  1 =   7
  7 x  2 =  14
  7 x  3 =  21
  7 x  4 =  28
  7 x  5 =  35
  7 x  6 =  42
  7 x  7 =  49
  7 x  8 =  56
  7 x  9 =  63
  7 x 10 =  70
```

## 2.7. Lặp qua chuỗi

`for` cũng có thể duyệt qua từng ký tự trong chuỗi:

```python
ten = "PYTHON"

for ky_tu in ten:
    print(ky_tu, end=" ")
```

**Kết quả:**

```
P Y T H O N
```

> 💡 `end=" "` giúp in trên cùng một dòng, cách nhau bằng dấu cách.

## 2.8. Ví dụ thực hành: Đếm nguyên âm trong chuỗi

```python
chuoi = input("Nhập một chuỗi: ")
nguyen_am = "aeiouAEIOU"
dem = 0

for ky_tu in chuoi:
    if ky_tu in nguyen_am:
        dem = dem + 1

print(f"Chuỗi '{chuoi}' có {dem} nguyên âm.")
```

**Chạy thử:**

```
Nhập một chuỗi: Xin chao Python
Chuỗi 'Xin chao Python' có 5 nguyên âm.
```

---

### ✅ Kiểm tra nhanh Module 2

Đoán kết quả:

```python
tong = 0
for i in range(1, 6):
    tong = tong + i * i
print(tong)
```

<details>
<summary>👀 Xem đáp án</summary>

```
55
```

Giải thích: 1² + 2² + 3² + 4² + 5² = 1 + 4 + 9 + 16 + 25 = 55

</details>

---

---

# Module 3: Vòng lặp `while`

## 🎯 Mục tiêu

> Biết dùng `while` để lặp khi **chưa biết trước** số lần lặp.

---

## 3.1. Cú pháp cơ bản

```python
while dieu_kien:
    # Khối lệnh lặp lại khi điều kiện còn True
    pass
```

**Quy trình hoạt động:**

1. Kiểm tra `dieu_kien`
2. Nếu `True` → chạy khối lệnh → quay lại bước 1
3. Nếu `False` → thoát vòng lặp

## 3.2. Ví dụ đầu tiên

```python
dem = 1

while dem <= 5:
    print(f"Lần thứ {dem}")
    dem = dem + 1

print("Kết thúc!")
```

**Kết quả:**

```
Lần thứ 1
Lần thứ 2
Lần thứ 3
Lần thứ 4
Lần thứ 5
Kết thúc!
```

> ⚠️ **Rất quan trọng:** Phải luôn cập nhật biến điều kiện (`dem = dem + 1`), nếu không vòng lặp sẽ chạy **vĩnh viễn** (vòng lặp vô hạn)!

## 3.3. Ví dụ: Vòng lặp vô hạn (cẩn thận!)

```python
# ❌ ĐỪNG CHẠY CODE NÀY — vòng lặp vĩnh viễn!
# while True:
#     print("Lặp mãi mãi...")
```

> 💡 Nếu vô tình chạy vòng lặp vô hạn, nhấn `Ctrl + C` để dừng chương trình.

## 3.4. Ví dụ thực hành: Hỏi mật khẩu

```python
mat_khau_dung = "python123"

mat_khau = input("Nhập mật khẩu: ")

while mat_khau != mat_khau_dung:
    print("❌ Sai mật khẩu! Thử lại.")
    mat_khau = input("Nhập mật khẩu: ")

print("✅ Đăng nhập thành công!")
```

**Chạy thử:**

```
Nhập mật khẩu: abc
❌ Sai mật khẩu! Thử lại.
Nhập mật khẩu: hello
❌ Sai mật khẩu! Thử lại.
Nhập mật khẩu: python123
✅ Đăng nhập thành công!
```

## 3.5. Ví dụ thực hành: Menu chương trình

```python
print("📋 CHƯƠNG TRÌNH QUẢN LÝ")
print("1. Xem thông tin")
print("2. Thêm dữ liệu")
print("3. Thoát")

lua_chon = ""

while lua_chon != "3":
    lua_chon = input("\nChọn chức năng (1-3): ")

    if lua_chon == "1":
        print("→ Đang xem thông tin...")
    elif lua_chon == "2":
        print("→ Đang thêm dữ liệu...")
    elif lua_chon == "3":
        print("→ Tạm biệt!")
    else:
        print("❌ Lựa chọn không hợp lệ!")
```

## 3.6. Ví dụ thực hành: Nhập điểm cho đến khi nhập -1

```python
print("📊 NHẬP ĐIỂM HỌC SINH")
print("(Nhập -1 để kết thúc)\n")

tong = 0
dem = 0

diem = float(input("Nhập điểm: "))

while diem != -1:
    if diem < 0 or diem > 10:
        print("⚠️ Điểm không hợp lệ! Bỏ qua.")
    else:
        tong = tong + diem
        dem = dem + 1

    diem = float(input("Nhập điểm: "))

if dem > 0:
    dtb = tong / dem
    print(f"\n📋 Kết quả:")
    print(f"  Số học sinh: {dem}")
    print(f"  Tổng điểm : {tong}")
    print(f"  ĐTB       : {dtb:.2f}")
else:
    print("\n⚠️ Không có điểm nào được nhập!")
```

**Chạy thử:**

```
📊 NHẬP ĐIỂM HỌC SINH
(Nhập -1 để kết thúc)

Nhập điểm: 8.5
Nhập điểm: 7.0
Nhập điểm: 9.2
Nhập điểm: -1

📋 Kết quả:
  Số học sinh: 3
  Tổng điểm : 24.7
  ĐTB       : 8.23
```

## 3.7. So sánh `for` và `while`

| Tiêu chí        | `for`                        | `while`                        |
| --------------- | ---------------------------- | ------------------------------ |
| Khi nào dùng    | Biết trước số lần lặp        | Không biết trước               |
| Biến đếm        | Tự động quản lý              | Phải tự tăng/giảm              |
| Rủi ro          | Ít rủi ro                    | Dễ bị vòng lặp vô hạn          |
| Phổ biến hơn    | Khi duyệt dãy số, chuỗi     | Khi chờ điều kiện, nhập liệu  |

---

### ✅ Kiểm tra nhanh Module 3

Đoạn code sau in ra gì?

```python
so = 1
while so <= 20:
    if so % 3 == 0:
        print(so, end=" ")
    so = so + 1
```

<details>
<summary>👀 Xem đáp án</summary>

```
3 6 9 12 15 18
```

In ra các số chia hết cho 3 trong phạm vi từ 1 đến 20.

</details>

---

---

# Module 4: `break` và `continue`

## 🎯 Mục tiêu

> Biết dùng `break` để thoát vòng lặp sớm và `continue` để bỏ qua lượt lặp hiện tại.

---

## 4.1. Lệnh `break` — Thoát vòng lặp ngay lập tức

```python
for i in range(1, 11):
    if i == 6:
        print("Gặp số 6 — dừng lại!")
        break
    print(f"Số: {i}")
```

**Kết quả:**

```
Số: 1
Số: 2
Số: 3
Số: 4
Số: 5
Gặp số 6 — dừng lại!
```

> 💡 `break` giống như nút **DỪNG KHẨN CẤP** — khi gặp điều kiện đặc biệt, thoát ngay.

## 4.2. Ví dụ: Tìm số đầu tiên chia hết cho 7

```python
for i in range(1, 100):
    if i % 7 == 0:
        print(f"Số đầu tiên chia hết cho 7 là: {i}")
        break
```

**Kết quả:**

```
Số đầu tiên chia hết cho 7 là: 7
```

## 4.3. Ví dụ: Đăng nhập giới hạn 3 lần

```python
mat_khau_dung = "kite2026"
so_lan = 0

while so_lan < 3:
    mk = input(f"Nhập mật khẩu (lần {so_lan + 1}/3): ")

    if mk == mat_khau_dung:
        print("✅ Đăng nhập thành công!")
        break

    print("❌ Sai mật khẩu!")
    so_lan = so_lan + 1

if so_lan == 3:
    print("🔒 Tài khoản bị khóa sau 3 lần nhập sai!")
```

**Chạy thử (nhập đúng lần 2):**

```
Nhập mật khẩu (lần 1/3): abc
❌ Sai mật khẩu!
Nhập mật khẩu (lần 2/3): kite2026
✅ Đăng nhập thành công!
```

**Chạy thử (nhập sai 3 lần):**

```
Nhập mật khẩu (lần 1/3): a
❌ Sai mật khẩu!
Nhập mật khẩu (lần 2/3): b
❌ Sai mật khẩu!
Nhập mật khẩu (lần 3/3): c
❌ Sai mật khẩu!
🔒 Tài khoản bị khóa sau 3 lần nhập sai!
```

## 4.4. Lệnh `continue` — Bỏ qua lượt lặp hiện tại

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Bỏ qua số chẵn
    print(f"Số lẻ: {i}")
```

**Kết quả:**

```
Số lẻ: 1
Số lẻ: 3
Số lẻ: 5
Số lẻ: 7
Số lẻ: 9
```

> 💡 `continue` giống như nói **"Bỏ qua cái này, qua cái tiếp theo"** — vòng lặp vẫn chạy tiếp.

## 4.5. Ví dụ: Tính tổng nhưng bỏ qua số chia hết cho 3

```python
tong = 0

for i in range(1, 21):
    if i % 3 == 0:
        continue  # Bỏ qua số chia hết cho 3
    tong = tong + i

print(f"Tổng các số từ 1-20 (bỏ qua số chia hết cho 3) = {tong}")
```

**Kết quả:**

```
Tổng các số từ 1-20 (bỏ qua số chia hết cho 3) = 147
```

## 4.6. So sánh `break` và `continue`

| Lệnh        | Tác dụng                                   | Ví dụ ứng dụng                     |
| ------------ | ------------------------------------------ | ---------------------------------- |
| `break`      | Dừng toàn bộ vòng lặp, thoát ra ngoài      | Tìm thấy kết quả → dừng tìm        |
| `continue`   | Bỏ qua phần còn lại, chuyển sang lượt tiếp | Dữ liệu không hợp lệ → bỏ qua      |

### Hình ảnh minh họa

```
for i in range(5):     │  for i in range(5):
    if i == 3:         │      if i == 3:
        break          │          continue
    print(i)           │      print(i)
                       │
→ In: 0 1 2            │  → In: 0 1 2 4
  (Dừng hẳn)           │    (Bỏ qua 3, chạy tiếp)
```

---

### ✅ Kiểm tra nhanh Module 4

Đoán kết quả:

```python
for i in range(1, 10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i, end=" ")
```

<details>
<summary>👀 Xem đáp án</summary>

```
1 2 4 5 6
```

- Khi `i == 3`: `continue` → bỏ qua, không in
- Khi `i == 7`: `break` → dừng hẳn
- Kết quả: 1, 2, (bỏ 3), 4, 5, 6, (dừng tại 7)

</details>

---

---

# Module 5: Vòng lặp lồng nhau

## 🎯 Mục tiêu

> Biết đặt một vòng lặp bên trong vòng lặp khác để xử lý bài toán 2 chiều.

---

## 5.1. Khái niệm

Vòng lặp lồng nhau (nested loop) là vòng lặp nằm bên trong vòng lặp khác.

```python
for i in range(3):       # Vòng ngoài: chạy 3 lần
    for j in range(4):   # Vòng trong: mỗi lần chạy 4 lần
        print(f"({i},{j})", end=" ")
    print()  # Xuống dòng sau mỗi hàng
```

**Kết quả:**

```
(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
```

> 💡 Tổng số lần chạy = **vòng ngoài × vòng trong** = 3 × 4 = 12 lần.

## 5.2. Ví dụ: In hình chữ nhật bằng dấu sao

```python
dong = int(input("Nhập số dòng: "))
cot = int(input("Nhập số cột: "))

for i in range(dong):
    for j in range(cot):
        print("* ", end="")
    print()
```

**Chạy thử (dòng=3, cột=5):**

```
* * * * *
* * * * *
* * * * *
```

## 5.3. Ví dụ: In tam giác sao

```python
n = int(input("Nhập số tầng: "))

for i in range(1, n + 1):
    for j in range(i):
        print("* ", end="")
    print()
```

**Chạy thử (n=5):**

```
*
* *
* * *
* * * *
* * * * *
```

## 5.4. Ví dụ thực hành: In toàn bộ bảng cửu chương 2-9

```python
print("📋 BẢNG CỬU CHƯƠNG ĐẦY ĐỦ (2 → 9)")
print("=" * 50)

for so in range(2, 10):
    print(f"\n--- Bảng {so} ---")
    for i in range(1, 11):
        print(f"  {so} x {i:>2} = {so * i:>3}")
```

## 5.5. Ví dụ thực hành: Kiểm tra số nguyên tố

```python
def la_so_nguyen_to(n):
    """Kiểm tra n có phải số nguyên tố không."""
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# In các số nguyên tố từ 1 đến 50
print("Các số nguyên tố từ 1 đến 50:")
for so in range(1, 51):
    if la_so_nguyen_to(so):
        print(so, end=" ")
```

**Kết quả:**

```
Các số nguyên tố từ 1 đến 50:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

---

### ✅ Kiểm tra nhanh Module 5

Đoạn code sau in ra hình gì?

```python
for i in range(4):
    for j in range(4 - i):
        print("*", end=" ")
    print()
```

<details>
<summary>👀 Xem đáp án</summary>

```
* * * *
* * *
* *
*
```

Tam giác ngược — số sao giảm dần.

</details>

---

---

# Module 6: Kết hợp vòng lặp với hàm

## 🎯 Mục tiêu

> Biết viết hàm có vòng lặp bên trong, tạo chương trình gọn gàng và tái sử dụng.

---

## 6.1. Hàm tính giai thừa

```python
def giai_thua(n):
    """Tính n! = 1 × 2 × 3 × ... × n"""
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua = ket_qua * i
    return ket_qua


so = int(input("Nhập số: "))
print(f"{so}! = {giai_thua(so)}")
```

**Chạy thử:**

```
Nhập số: 5
5! = 120
```

## 6.2. Hàm tính lũy thừa (không dùng **)

```python
def luy_thua(co_so, so_mu):
    """Tính co_so ^ so_mu bằng vòng lặp."""
    ket_qua = 1
    for i in range(so_mu):
        ket_qua = ket_qua * co_so
    return ket_qua


print(luy_thua(2, 10))   # 1024
print(luy_thua(3, 4))    # 81
```

## 6.3. Hàm đảo ngược chuỗi

```python
def dao_nguoc(chuoi):
    """Đảo ngược chuỗi bằng vòng lặp."""
    ket_qua = ""
    for ky_tu in chuoi:
        ket_qua = ky_tu + ket_qua
    return ket_qua


print(dao_nguoc("PYTHON"))   # NOHTYP
print(dao_nguoc("Xin chào")) # oàhc niX
```

## 6.4. Hàm kiểm tra Palindrome

```python
def la_palindrome(chuoi):
    """Kiểm tra chuỗi có đọc xuôi ngược giống nhau không."""
    chuoi_nguoc = dao_nguoc(chuoi)
    return chuoi == chuoi_nguoc


print(la_palindrome("madam"))   # True
print(la_palindrome("python"))  # False
print(la_palindrome("12321"))   # True
```

## 6.5. Ví dụ tổng hợp: Chương trình kiểm tra mật khẩu mạnh

```python
def dem_chu_hoa(s):
    """Đếm số chữ cái viết hoa."""
    dem = 0
    for ky_tu in s:
        if ky_tu >= "A" and ky_tu <= "Z":
            dem = dem + 1
    return dem


def dem_chu_so(s):
    """Đếm số chữ số."""
    dem = 0
    for ky_tu in s:
        if ky_tu >= "0" and ky_tu <= "9":
            dem = dem + 1
    return dem


def kiem_tra_mat_khau(mk):
    """Kiểm tra mật khẩu mạnh/yếu."""
    if len(mk) < 8:
        return "Yếu — Cần ít nhất 8 ký tự"

    if dem_chu_hoa(mk) == 0:
        return "Trung bình — Thiếu chữ hoa"

    if dem_chu_so(mk) == 0:
        return "Trung bình — Thiếu chữ số"

    return "Mạnh ✅"


# Chạy thử
mk = input("Nhập mật khẩu: ")
print(f"Đánh giá: {kiem_tra_mat_khau(mk)}")
```

**Chạy thử:**

```
Nhập mật khẩu: abc
Đánh giá: Yếu — Cần ít nhất 8 ký tự

Nhập mật khẩu: abcdefgh
Đánh giá: Trung bình — Thiếu chữ hoa

Nhập mật khẩu: Abcdefgh
Đánh giá: Trung bình — Thiếu chữ số

Nhập mật khẩu: Abcdef12
Đánh giá: Mạnh ✅
```

---

---

# 📚 Phương pháp học vòng lặp hiệu quả

## 1. Quy tắc "Giấy trước, Code sau"

Trước khi viết code, hãy viết ra giấy:

1. Biến nào cần khởi tạo trước vòng lặp?
2. Vòng lặp chạy từ đâu đến đâu?
3. Mỗi lượt lặp làm gì?
4. Sau khi vòng lặp kết thúc, kết quả nằm ở biến nào?

## 2. Bảng theo dõi (Trace table)

Cách tốt nhất để hiểu vòng lặp là **lập bảng theo dõi**:

```python
tong = 0
for i in range(1, 5):
    tong = tong + i
```

| Lượt | `i`  | `tong` trước | `tong` sau |
| ---- | ---- | ----------- | ---------- |
| 1    | 1    | 0           | 1          |
| 2    | 2    | 1           | 3          |
| 3    | 3    | 3           | 6          |
| 4    | 4    | 6           | 10         |

## 3. Sai lầm phổ biến cần tránh

- Quên cập nhật biến điều kiện trong `while` → vòng lặp vô hạn
- Nhầm `range(n)` (0 đến n-1) với `range(1, n+1)` (1 đến n)
- Đặt biến tích lũy **bên trong** vòng lặp thay vì **bên ngoài**
- `break` dừng **toàn bộ** vòng lặp, không chỉ 1 lượt
- Vòng lặp lồng nhau: `break` chỉ thoát vòng lặp **trong nhất**

## 4. Mẹo debug vòng lặp

- Thêm `print()` bên trong vòng lặp để xem giá trị từng bước
- Giới hạn số vòng lặp khi test (thay 1000 bằng 5)
- Dùng bảng theo dõi cho 3-4 lượt đầu

---

---

# 📝 Bài tập thực hành

> 🎯 Mỗi bài tập đều có **Input/Output mẫu** để bạn tự kiểm tra kết quả.
>
> 📄 **Lời giải** được đặt riêng trong file: `Buoi_04_Loi_Giai.md`

---

## 🟢 CƠ BẢN

---

### 📌 Bài 1: Đếm ngược phóng tên lửa _(Cơ bản)_

```
📋 Mô tả:
Viết chương trình đếm ngược từ N về 0, sau đó in "🚀 Phóng!".

📝 Yêu cầu:
- Nhập số N (số nguyên dương)
- Dùng vòng lặp đếm ngược từ N về 0
- Khi về 0, in thêm "🚀 Phóng!"

📌 Test case 1:
   Input:  N = 5
   Output:
   5
   4
   3
   2
   1
   0
   🚀 Phóng!

📌 Test case 2:
   Input:  N = 3
   Output:
   3
   2
   1
   0
   🚀 Phóng!
```

---

### 📌 Bài 2: Tổng các chữ số _(Cơ bản)_

```
📋 Mô tả:
Nhập một số nguyên dương, tính tổng các chữ số của nó.

📝 Yêu cầu:
- Nhập số nguyên dương N
- Dùng vòng lặp while để tách từng chữ số và cộng lại
- Gợi ý: N % 10 lấy chữ số cuối, N // 10 bỏ chữ số cuối

📌 Test case 1:
   Input:  N = 123
   Output: Tổng các chữ số của 123 = 6

📌 Test case 2:
   Input:  N = 9876
   Output: Tổng các chữ số của 9876 = 30

📌 Test case 3:
   Input:  N = 5
   Output: Tổng các chữ số của 5 = 5
```

---

### 📌 Bài 3: In các số chia hết cho cả 3 và 5 _(Cơ bản)_

```
📋 Mô tả:
In ra tất cả các số từ 1 đến N chia hết cho cả 3 VÀ 5.

📝 Yêu cầu:
- Nhập số N
- Dùng vòng lặp for và lệnh continue để bỏ qua số không thỏa mãn
- Cuối cùng in tổng số lượng các số tìm được

📌 Test case 1:
   Input:  N = 50
   Output:
   15 30 45
   Tổng cộng: 3 số

📌 Test case 2:
   Input:  N = 100
   Output:
   15 30 45 60 75 90
   Tổng cộng: 6 số

📌 Test case 3:
   Input:  N = 10
   Output:
   (không có số nào)
   Tổng cộng: 0 số
```

---

### 📌 Bài 4: Bảng cửu chương tùy chọn _(Cơ bản)_

```
📋 Mô tả:
Viết hàm in bảng cửu chương cho một số bất kỳ, từ bội 1 đến bội N.

📝 Yêu cầu:
- Viết hàm in_cuu_chuong(so, n) → in bảng cửu chương của 'so' từ 1 đến n
- Nhập số và n từ bàn phím

📌 Test case 1:
   Input:  so = 7, n = 5
   Output:
   📋 BẢNG CỬU CHƯƠNG 7
   7 x 1 =  7
   7 x 2 = 14
   7 x 3 = 21
   7 x 4 = 28
   7 x 5 = 35

📌 Test case 2:
   Input:  so = 12, n = 3
   Output:
   📋 BẢNG CỬU CHƯƠNG 12
   12 x 1 = 12
   12 x 2 = 24
   12 x 3 = 36
```

---

## 🟡 TRUNG BÌNH

---

### 📌 Bài 5: Máy ATM rút tiền _(Trung bình)_

```
📋 Bối cảnh:
Viết chương trình mô phỏng máy ATM đơn giản.

📝 Yêu cầu:
- Số dư ban đầu: 5,000,000 đồng
- Cho phép rút nhiều lần (dùng while)
- Mỗi lần rút: kiểm tra đủ số dư không
- Số tiền rút phải là bội số của 50,000
- Nhập 0 để thoát
- Sau mỗi giao dịch, in số dư còn lại

📌 Test case:
   Số dư: 5,000,000đ
   
   Nhập số tiền rút: 1000000
   ✅ Rút thành công! Số dư: 4,000,000đ
   
   Nhập số tiền rút: 500000
   ✅ Rút thành công! Số dư: 3,500,000đ
   
   Nhập số tiền rút: 75000
   ❌ Số tiền phải là bội số của 50,000đ!
   
   Nhập số tiền rút: 5000000
   ❌ Số dư không đủ! Số dư hiện tại: 3,500,000đ
   
   Nhập số tiền rút: 0
   👋 Cảm ơn đã sử dụng dịch vụ! Số dư cuối: 3,500,000đ
```

---

### 📌 Bài 6: Số hoàn hảo _(Trung bình)_

```
📋 Mô tả:
Số hoàn hảo là số mà tổng các ước (trừ chính nó) bằng chính nó.
Ví dụ: 6 = 1 + 2 + 3, nên 6 là số hoàn hảo.

📝 Yêu cầu:
1. Viết hàm tong_uoc(n) → trả về tổng các ước của n (không tính chính n)
2. Viết hàm la_so_hoan_hao(n) → trả về True/False
3. Nhập N, in tất cả số hoàn hảo từ 1 đến N

📌 Test case 1:
   Input:  N = 30
   Output:
   Các số hoàn hảo từ 1 đến 30:
   6 (= 1 + 2 + 3)
   28 (= 1 + 2 + 4 + 7 + 14)

📌 Test case 2:
   Input:  N = 500
   Output:
   Các số hoàn hảo từ 1 đến 500:
   6 (= 1 + 2 + 3)
   28 (= 1 + 2 + 4 + 7 + 14)
   496 (= 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248)

📌 Test case 3:
   Input:  N = 5
   Output:
   Các số hoàn hảo từ 1 đến 5:
   (Không tìm thấy số hoàn hảo nào)
```

---

### 📌 Bài 7: Chương trình đoán số (nhiều lượt) _(Trung bình)_

```
📋 Bối cảnh:
Nâng cấp trò chơi đoán số từ Buổi 3: giờ người chơi được đoán
nhiều lần cho đến khi đoán đúng hoặc hết lượt.

📝 Yêu cầu:
1. Số bí mật: cố định = 37 (vì chưa học random)
2. Người chơi có tối đa 7 lượt đoán
3. Mỗi lượt: nhập số → so sánh → gợi ý "Cao hơn" hoặc "Thấp hơn"
4. Nếu đoán đúng: in "Chính xác!" + số lượt đã dùng → break
5. Nếu hết lượt: in "Thua rồi!" + cho biết đáp án

📌 Test case 1 (đoán đúng lần 3):
   🎮 TRÒ CHƠI ĐOÁN SỐ (1-100)
   Bạn có 7 lượt đoán. Chúc may mắn!
   
   Lượt 1/7 — Nhập số: 50
   📈 Số bí mật THẤP HƠN 50
   
   Lượt 2/7 — Nhập số: 25
   📉 Số bí mật CAO HƠN 25
   
   Lượt 3/7 — Nhập số: 37
   🎯 CHÍNH XÁC! Bạn đoán đúng sau 3 lượt!

📌 Test case 2 (hết lượt):
   ...
   Lượt 7/7 — Nhập số: 40
   📈 Số bí mật THẤP HƠN 40
   
   ❌ Hết lượt! Số bí mật là 37. Chúc bạn may mắn lần sau!
```

---

### 📌 Bài 8: Phân tích số nguyên tố _(Trung bình)_

```
📋 Mô tả:
Viết chương trình phân tích một số thành tích các thừa số nguyên tố.

📝 Yêu cầu:
1. Viết hàm phan_tich(n) → in ra các thừa số nguyên tố
2. Gợi ý: chia liên tục cho 2, rồi 3, rồi 5, 7... cho đến khi n = 1

📌 Test case 1:
   Input:  N = 12
   Output: 12 = 2 x 2 x 3

📌 Test case 2:
   Input:  N = 100
   Output: 100 = 2 x 2 x 5 x 5

📌 Test case 3:
   Input:  N = 17
   Output: 17 = 17 (là số nguyên tố)

📌 Test case 4:
   Input:  N = 360
   Output: 360 = 2 x 2 x 2 x 3 x 3 x 5
```

---

## 🔴 NÂNG CAO

---

### 📌 Bài 9: Hệ thống quản lý điểm lớp học _(Nâng cao)_

```
📋 Bối cảnh:
Giáo viên cần nhập điểm cho N học sinh, tính điểm trung bình lớp,
tìm điểm cao nhất, thấp nhất, và xếp loại từng học sinh.

📝 Yêu cầu:
1. Viết hàm nhap_diem_hs(stt) → nhập điểm 1 HS, kiểm tra 0-10, trả về điểm
   (nếu sai, yêu cầu nhập lại — dùng while)
2. Viết hàm xep_loai(diem) → trả về xếp loại (Giỏi/Khá/TB/Yếu/Kém)
3. Viết hàm in_ket_qua(stt, diem, loai) → in kết quả 1 HS
4. Chương trình chính:
   - Nhập N (số học sinh)
   - Dùng for lặp N lần, mỗi lần nhập điểm + in kết quả
   - Tích lũy: tổng điểm, điểm cao nhất, thấp nhất, đếm từng loại
   - Cuối cùng: in báo cáo tổng kết lớp

📌 Test case (N=3):
   📊 QUẢN LÝ ĐIỂM LỚP HỌC
   Nhập số học sinh: 3
   
   --- Học sinh 1 ---
   Nhập điểm: 8.5
   → HS 1: 8.5 điểm — Giỏi 🥇
   
   --- Học sinh 2 ---
   Nhập điểm: 12
   ⚠️ Điểm không hợp lệ! Nhập lại.
   Nhập điểm: 6.0
   → HS 2: 6.0 điểm — Trung bình 🥉
   
   --- Học sinh 3 ---
   Nhập điểm: 9.5
   → HS 3: 9.5 điểm — Xuất sắc 🌟
   
   ════════════════════════════════
   📋 BÁO CÁO TỔNG KẾT LỚP
   ════════════════════════════════
   Sĩ số       : 3
   ĐTB lớp     : 8.00
   Điểm cao nhất: 9.5
   Điểm thấp nhất: 6.0
   ────────────────────────────────
   Xuất sắc/Giỏi: 2 (66.7%)
   Khá          : 0 (0.0%)
   Trung bình   : 1 (33.3%)
   Yếu/Kém     : 0 (0.0%)
   ════════════════════════════════
```

---

### 📌 Bài 10: Trò chơi Fizz Buzz nâng cao _(Nâng cao)_

```
📋 Bối cảnh:
FizzBuzz là một bài kiểm tra lập trình kinh điển.
Phiên bản nâng cao cho phép người dùng tùy chọn 2 số.

📝 Yêu cầu:
1. Nhập 2 số A và B (số nguyên dương), và giới hạn N
2. Với mỗi số từ 1 đến N:
   - Chia hết cho cả A và B → in "FizzBuzz ⚡"
   - Chia hết cho A → in "Fizz 🔵"
   - Chia hết cho B → in "Buzz 🔴"
   - Không chia hết → in số đó
3. Cuối cùng thống kê:
   - Số lần Fizz, Buzz, FizzBuzz
   - Phần trăm mỗi loại

📌 Test case (A=3, B=5, N=20):
   Input: A=3, B=5, N=20
   Output:
   1  2  Fizz 🔵  4  Buzz 🔴  Fizz 🔵  7  8
   Fizz 🔵  Buzz 🔴  11  Fizz 🔵  13  14  FizzBuzz ⚡
   16  17  Fizz 🔵  19  Buzz 🔴
   
   📊 Thống kê:
   Fizz     : 5 lần (25.0%)
   Buzz     : 3 lần (15.0%)
   FizzBuzz : 1 lần (5.0%)
   Số thường: 11 (55.0%)
```

---

### 📌 Bài 11: Vẽ hình bằng dấu sao _(Nâng cao)_

```
📋 Mô tả:
Viết các hàm vẽ hình hình học bằng dấu sao.

📝 Yêu cầu:
1. Viết hàm ve_tam_giac(n) → tam giác cân
2. Viết hàm ve_hinh_thoi(n) → hình thoi
3. Viết hàm ve_chu_x(n) → chữ X
4. Cho người dùng chọn hình muốn vẽ từ menu

📌 Test case 1 — Tam giác cân (n=5):
       *
      ***
     *****
    *******
   *********

📌 Test case 2 — Hình thoi (n=5):
       *
      ***
     *****
    *******
   *********
    *******
     *****
      ***
       *

📌 Test case 3 — Chữ X (n=5):
   *       *
    *     *
      * *
    *     *
   *       *
```

---

### 📌 Bài 12: Máy bán hàng tự động _(Nâng cao)_

```
📋 Bối cảnh:
Viết chương trình mô phỏng máy bán hàng tự động.

Danh sách sản phẩm:
- Mã 1: Nước suối    — 8,000đ
- Mã 2: Trà xanh     — 12,000đ
- Mã 3: Cà phê lon    — 15,000đ
- Mã 4: Bánh mì       — 20,000đ
- Mã 5: Snack         — 10,000đ

📝 Yêu cầu:
1. Viết hàm lay_ten_sp(ma) → tên sản phẩm
2. Viết hàm lay_gia_sp(ma) → giá sản phẩm
3. Viết hàm in_menu() → in menu sản phẩm đẹp
4. Chương trình vòng lặp:
   - Hiển thị menu
   - Người dùng chọn sản phẩm + số lượng
   - Tích lũy tổng tiền
   - Nhập 0 để thanh toán
   - In hóa đơn hoàn chỉnh: danh sách đã mua + tổng tiền
   - Hỏi tiền khách đưa → tính tiền thối

📌 Test case:
   🏪 MÁY BÁN HÀNG TỰ ĐỘNG
   ┌──────────────────────────┐
   │ 1. Nước suối    8,000đ   │
   │ 2. Trà xanh    12,000đ   │
   │ 3. Cà phê lon  15,000đ   │
   │ 4. Bánh mì     20,000đ   │
   │ 5. Snack       10,000đ   │
   │ 0. Thanh toán             │
   └──────────────────────────┘
   
   Chọn sản phẩm: 2
   Số lượng: 2
   ✅ Đã thêm: Trà xanh x2 = 24,000đ
   
   Chọn sản phẩm: 4
   Số lượng: 1
   ✅ Đã thêm: Bánh mì x1 = 20,000đ
   
   Chọn sản phẩm: 0
   
   ═══════════════════════════════
   📋 HÓA ĐƠN
   ═══════════════════════════════
   Trà xanh      x2    24,000đ
   Bánh mì       x1    20,000đ
   ───────────────────────────────
   TỔNG CỘNG:          44,000đ
   ═══════════════════════════════
   
   Tiền khách đưa: 50000
   💰 Tiền thối: 6,000đ
   Cảm ơn quý khách! 🙏
```

---

## 🟣 THỬ THÁCH

---

### 📌 Bài 13: Trò chơi Hangman mini _(Thử thách)_

```
📋 Bối cảnh:
Viết trò chơi đoán từ (Hangman) đơn giản.
Máy tính chọn sẵn một từ, người chơi đoán từng chữ cái.

📝 Yêu cầu:
1. Từ bí mật cố định: "python" (có thể đổi)
2. Hiển thị từ dạng ẩn: "_ _ _ _ _ _"
3. Người chơi được đoán tối đa 6 lần sai
4. Mỗi lượt: nhập 1 chữ cái
   - Nếu có trong từ → mở chữ cái đó
   - Nếu không → tăng số lần sai
   - Nếu đoán chữ cái đã đoán rồi → cảnh báo
5. Thắng: mở hết tất cả chữ cái
6. Thua: sai 6 lần

📌 Test case:
   🎮 TRÒ CHƠI ĐOÁN TỪ (HANGMAN)
   Từ bí mật có 6 chữ cái.
   Bạn được sai tối đa 6 lần.
   
   Từ: _ _ _ _ _ _     Sai: 0/6
   Đoán chữ: p
   ✅ Đúng rồi!
   
   Từ: p _ _ _ _ _     Sai: 0/6
   Đoán chữ: a
   ❌ Sai rồi!
   
   Từ: p _ _ _ _ _     Sai: 1/6
   Đoán chữ: y
   ✅ Đúng rồi!
   
   Từ: p y _ _ _ _     Sai: 1/6
   Đoán chữ: t
   ✅ Đúng rồi!
   
   Từ: p y t _ _ _     Sai: 1/6
   ...
   
   Từ: p y t h o n     Sai: 2/6
   🎉 CHÚC MỪNG! Bạn đã đoán đúng từ "python"!
```

---

### 📌 Bài 14: In số La Mã _(Thử thách)_

```
📋 Mô tả:
Viết hàm đổi số nguyên (1-3999) sang số La Mã.

Bảng quy đổi:
M=1000, CM=900, D=500, CD=400, C=100, XC=90,
L=50, XL=40, X=10, IX=9, V=5, IV=4, I=1

📝 Yêu cầu:
1. Viết hàm doi_la_ma(so) → trả về chuỗi số La Mã
2. Gợi ý: dùng while, chia so cho từng giá trị từ lớn đến nhỏ
3. Cho phép nhập nhiều số (dùng while, nhập 0 để thoát)

📌 Test case 1:
   Input:  2024
   Output: MMXXIV

📌 Test case 2:
   Input:  49
   Output: XLIX

📌 Test case 3:
   Input:  3999
   Output: MMMCMXCIX

📌 Test case 4:
   Input:  8
   Output: VIII
```

---

## 📌 Checklist tổng kết Buổi 4

| #   | Nội dung                                                    | Trạng thái |
| --- | ----------------------------------------------------------- | ---------- |
| 1   | Hiểu vì sao cần vòng lặp                                   | ⬜         |
| 2   | Biết dùng `for` với `range()` (1, 2, 3 tham số)             | ⬜         |
| 3   | Biết dùng `while` với điều kiện dừng                         | ⬜         |
| 4   | Phân biệt được khi nào dùng `for`, khi nào dùng `while`     | ⬜         |
| 5   | Biết dùng `break` để thoát vòng lặp sớm                     | ⬜         |
| 6   | Biết dùng `continue` để bỏ qua 1 lượt lặp                   | ⬜         |
| 7   | Biết viết vòng lặp lồng nhau                                | ⬜         |
| 8   | Biết kết hợp vòng lặp với hàm                               | ⬜         |
| 9   | Biết dùng biến tích lũy (accumulator) trong vòng lặp         | ⬜         |
| 10  | Hoàn thành ít nhất 5/14 bài tập                             | ⬜         |

---

> **📢 Hẹn gặp lại ở Buổi 5!**
>
> Ở buổi tiếp theo, chúng ta sẽ **luyện tập tổng hợp** — kết hợp tất cả kiến thức từ Buổi 1 đến Buổi 4 để xây dựng các **dự án mini** hoàn chỉnh! 🚀

---

_© 2026 — Giáo trình Python | Biên soạn cho lớp học KITE_
