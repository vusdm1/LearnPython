# 🐍 GIÁO TRÌNH PYTHON — BUỔI 2

## **CÂU LỆNH ĐIỀU KIỆN: DẠY CHƯƠNG TRÌNH "SUY NGHĨ"**

> _"Lập trình không chỉ là ra lệnh — mà là dạy máy tính cách đưa ra quyết định."_

| Thông tin buổi học     | Chi tiết                                                                      |
| ---------------------- | ----------------------------------------------------------------------------- |
| **Buổi**               | 02                                                                            |
| **Chủ đề**             | Câu lệnh điều kiện — `if`, `if-else`, `if-elif-else`, Toán tử so sánh & logic |
| **Thời lượng**         | ~2 - 3 giờ (bao gồm thực hành)                                                |
| **Yêu cầu**            | Đã hoàn thành Buổi 1 (Biến, Kiểu dữ liệu, Input/Output)                       |
| **Mục tiêu tổng quát** | Viết được chương trình có khả năng ra quyết định dựa trên điều kiện           |

---

# 📌 MỤC LỤC

- [Module 1: Toán tử so sánh (Comparison Operators)](#module-1-toán-tử-so-sánh-comparison-operators)
- [Module 2: Toán tử logic (Logical Operators)](#module-2-toán-tử-logic-logical-operators)
- [Module 3: Câu lệnh `if` đơn giản](#module-3-câu-lệnh-if-đơn-giản)
- [Module 4: Câu lệnh `if-else`](#module-4-câu-lệnh-if-else)
- [Module 5: Câu lệnh `if-elif-else`](#module-5-câu-lệnh-if-elif-else)
- [Module 6: Điều kiện lồng nhau (Nested if)](#module-6-điều-kiện-lồng-nhau-nested-if)
- [Module 7: Toán tử ba ngôi & Kỹ thuật nâng cao](#module-7-toán-tử-ba-ngôi--kỹ-thuật-nâng-cao)
- [📝 Bài tập thực hành tổng hợp](#-bài-tập-thực-hành-tổng-hợp)

---

---

# Module 1: Toán tử so sánh (Comparison Operators)

## 🎯 Mục tiêu

> Hiểu cách **so sánh** hai giá trị với nhau. Kết quả luôn là `True` hoặc `False`.

---

## 1.1. Tổng quan toán tử so sánh

| Toán tử | Ý nghĩa           | Ví dụ    | Kết quả |
| ------- | ----------------- | -------- | ------- |
| `==`    | Bằng nhau         | `5 == 5` | `True`  |
| `!=`    | Khác nhau         | `5 != 3` | `True`  |
| `>`     | Lớn hơn           | `10 > 7` | `True`  |
| `<`     | Nhỏ hơn           | `3 < 1`  | `False` |
| `>=`    | Lớn hơn hoặc bằng | `5 >= 5` | `True`  |
| `<=`    | Nhỏ hơn hoặc bằng | `4 <= 3` | `False` |

> ⚠️ **Nhắc lại**: `=` là **gán giá trị**, `==` là **so sánh**! Đây là lỗi **phổ biến nhất** của người mới.

## 1.2. Ví dụ thực hành

```python
a = 10
b = 20

print(a == b)   # False — 10 có bằng 20 không? Không!
print(a != b)   # True  — 10 có khác 20 không? Đúng!
print(a > b)    # False — 10 có lớn hơn 20 không? Không!
print(a < b)    # True  — 10 có nhỏ hơn 20 không? Đúng!
print(a >= 10)  # True  — 10 có lớn hơn hoặc bằng 10 không? Đúng!
print(a <= 5)   # False — 10 có nhỏ hơn hoặc bằng 5 không? Không!
```

## 1.3. So sánh chuỗi (String)

Python so sánh chuỗi theo **thứ tự bảng chữ cái** (mã Unicode/ASCII):

```python
print("apple" == "apple")   # True
print("apple" == "Apple")   # False — phân biệt HOA/thường!
print("apple" != "banana")  # True
print("a" < "b")            # True  — 'a' đứng trước 'b'
print("abc" < "abd")        # True  — so sánh từng ký tự
print("A" < "a")            # True  — chữ HOA có mã nhỏ hơn chữ thường
```

> 💡 **Mẹo**: Khi so sánh chuỗi không phân biệt HOA/thường, dùng `.lower()` hoặc `.upper()`:

```python
nhap_vao = "Python"
print(nhap_vao.lower() == "python")  # True
```

## 1.4. So sánh chuỗi (nâng cao)

Python hỗ trợ **so sánh chuỗi liên tiếp** (chained comparison) — rất tiện lợi:

```python
tuoi = 25

# Thay vì viết: tuoi >= 18 and tuoi <= 60
print(18 <= tuoi <= 60)  # True — tuổi từ 18 đến 60

diem = 7.5
print(5.0 <= diem <= 10.0)  # True — điểm từ 5 đến 10
```

---

### ✅ Kiểm tra nhanh Module 1

```python
# Đoán kết quả trước khi chạy:
print(10 == 10.0)    # ???
print("10" == 10)    # ???
print(1 == True)     # ???
print(0 == False)    # ???
```

<details>
<summary>👀 Xem đáp án</summary>

```python
print(10 == 10.0)    # True  — int và float có cùng giá trị
print("10" == 10)    # False — chuỗi khác số!
print(1 == True)     # True  — True tương đương 1
print(0 == False)    # True  — False tương đương 0
```

</details>

---

---

# Module 2: Toán tử logic (Logical Operators)

## 🎯 Mục tiêu

> Kết hợp **nhiều điều kiện** với nhau bằng `and`, `or`, `not`.

---

## 2.1. Ba toán tử logic

| Toán tử | Ý nghĩa      | Kết quả `True` khi             |
| ------- | ------------ | ------------------------------ |
| `and`   | **VÀ**       | **Cả hai** điều kiện đều đúng  |
| `or`    | **HOẶC**     | **Ít nhất một** điều kiện đúng |
| `not`   | **PHỦ ĐỊNH** | Đảo ngược giá trị              |

## 2.2. Toán tử `and` (VÀ)

> Chỉ `True` khi **TẤT CẢ** điều kiện đều đúng.

```
┌─────────┬─────────┬────────────────┐
│    A    │    B    │   A and B      │
├─────────┼─────────┼────────────────┤
│  True   │  True   │   ✅ True      │
│  True   │  False  │   ❌ False     │
│  False  │  True   │   ❌ False     │
│  False  │  False  │   ❌ False     │
└─────────┴─────────┴────────────────┘
```

```python
tuoi = 20
co_cmnd = True

# Cả HAI điều kiện phải đúng
print(tuoi >= 18 and co_cmnd)  # True — đủ tuổi VÀ có CMND
print(tuoi >= 18 and not co_cmnd)  # False — đủ tuổi NHƯNG không có CMND
```

**Ví dụ thực tế:**

```python
diem_toan = 7
diem_van = 6

# Đỗ khi cả hai môn đều >= 5
do_tot_nghiep = diem_toan >= 5 and diem_van >= 5
print(f"Đỗ tốt nghiệp: {do_tot_nghiep}")  # True
```

## 2.3. Toán tử `or` (HOẶC)

> `True` khi **ÍT NHẤT MỘT** điều kiện đúng.

```
┌─────────┬─────────┬────────────────┐
│    A    │    B    │   A or B       │
├─────────┼─────────┼────────────────┤
│  True   │  True   │   ✅ True      │
│  True   │  False  │   ✅ True      │
│  False  │  True   │   ✅ True      │
│  False  │  False  │   ❌ False     │
└─────────┴─────────┴────────────────┘
```

```python
la_sinh_vien = False
la_nguoi_cao_tuoi = True

# Chỉ cần MỘT trong hai là được giảm giá
duoc_giam_gia = la_sinh_vien or la_nguoi_cao_tuoi
print(f"Được giảm giá: {duoc_giam_gia}")  # True
```

## 2.4. Toán tử `not` (PHỦ ĐỊNH)

> Đảo ngược giá trị: `True` → `False` và `False` → `True`.

```python
troi_mua = True

print(not troi_mua)      # False — không mưa? Sai, đang mưa!
print(not (10 > 20))     # True  — not False = True
```

## 2.5. Kết hợp nhiều toán tử

```python
tuoi = 25
thu_nhap = 15_000_000
co_no = False

# Đủ điều kiện vay: tuổi >= 18 VÀ thu nhập >= 10 triệu VÀ không có nợ
du_dieu_kien = tuoi >= 18 and thu_nhap >= 10_000_000 and not co_no
print(f"Đủ điều kiện vay: {du_dieu_kien}")  # True
```

### Thứ tự ưu tiên toán tử logic

| Thứ tự | Toán tử | Ưu tiên    |
| ------ | ------- | ---------- |
| 1️⃣     | `not`   | Cao nhất   |
| 2️⃣     | `and`   | Trung bình |
| 3️⃣     | `or`    | Thấp nhất  |

```python
# Ví dụ thứ tự ưu tiên
print(True or False and False)       # True  → and chạy trước: False and False = False → True or False = True
print((True or False) and False)     # False → ngoặc trước: True and False = False

# Khuyên dùng: LUÔN dùng ngoặc () để rõ ràng!
```

---

---

# Module 3: Câu lệnh `if` đơn giản

## 🎯 Mục tiêu

> Thực hiện một hành động **chỉ khi** điều kiện là đúng (`True`).

---

## 3.1. Cú pháp

```python
if điều_kiện:
    # Code thực hiện khi điều kiện ĐÚNG
    # (Phải thụt đầu dòng 4 dấu cách hoặc 1 Tab)
```

**Sơ đồ hoạt động:**

```
        ┌──────────────────┐
        │  Kiểm tra điều   │
        │      kiện        │
        └────────┬─────────┘
                 │
          ┌──────┴──────┐
          │             │
       True ✅       False ❌
          │             │
    ┌─────┴─────┐       │
    │ Thực hiện │       │
    │ code bên  │       │
    │  trong if │       │
    └─────┬─────┘       │
          │             │
          └──────┬──────┘
                 │
        ┌────────┴────────┐
        │ Tiếp tục chương │
        │     trình       │
        └─────────────────┘
```

## 3.2. Ví dụ cơ bản

```python
tuoi = 20

if tuoi >= 18:
    print("Bạn đã đủ tuổi trưởng thành! 🎉")

print("Chương trình kết thúc.")
```

**Kết quả:** (vì `20 >= 18` là `True`)

```
Bạn đã đủ tuổi trưởng thành! 🎉
Chương trình kết thúc.
```

## 3.3. Thụt đầu dòng (Indentation) — CỰC KỲ QUAN TRỌNG!

> ⚠️ **Python dùng thụt đầu dòng để xác định khối code**, KHÔNG dùng ngoặc nhọn `{}` như Java/C++.

```python
diem = 8

# ✅ ĐÚNG — thụt 4 dấu cách
if diem >= 5:
    print("Đỗ!")           # ← nằm TRONG if
    print("Chúc mừng!")    # ← nằm TRONG if

print("Kết thúc.")         # ← nằm NGOÀI if (luôn chạy)
```

```python
# ❌ SAI — không thụt đầu dòng → IndentationError!
if diem >= 5:
print("Đỗ!")  # Lỗi! Thiếu thụt đầu dòng
```

```python
# ❌ SAI — thụt không đều → IndentationError!
if diem >= 5:
    print("Đỗ!")
      print("Chúc mừng!")  # Lỗi! Thụt không đều
```

> 💡 **Quy ước**: Luôn dùng **4 dấu cách** (space) cho mỗi cấp thụt đầu dòng. VS Code sẽ tự động làm điều này khi bạn nhấn Tab.

## 3.4. Nhiều lệnh trong khối `if`

```python
nhiet_do = 38.5

if nhiet_do >= 37.5:
    print("⚠️ Cảnh báo: Bạn đang bị sốt!")
    print(f"   Nhiệt độ cơ thể: {nhiet_do}°C")
    print("   Khuyến nghị: Hãy nghỉ ngơi và uống nhiều nước.")
    print("   Nếu sốt cao, hãy đi khám bác sĩ.")

print("Chương trình kiểm tra sức khỏe kết thúc.")
```

---

---

# Module 4: Câu lệnh `if-else`

## 🎯 Mục tiêu

> Thực hiện hành động A khi điều kiện đúng, hành động B khi điều kiện sai — **luôn có một nhánh được chạy**.

---

## 4.1. Cú pháp

```python
if điều_kiện:
    # Code khi điều kiện ĐÚNG (True)
else:
    # Code khi điều kiện SAI (False)
```

**Sơ đồ:**

```
        ┌──────────────────┐
        │   Kiểm tra điều  │
        │       kiện       │
        └────────┬─────────┘
                 │
          ┌──────┴──────┐
          │             │
       True ✅       False ❌
          │             │
    ┌─────┴─────┐ ┌─────┴─────┐
    │  Khối if  │ │ Khối else │
    └─────┬─────┘ └─────┬─────┘
          │             │
          └──────┬──────┘
                 ▼
          Tiếp tục...
```

## 4.2. Ví dụ thực hành

```python
# === KIỂM TRA ĐỦ TUỔI LÁI XE ===

tuoi = int(input("Nhập tuổi của bạn: "))

if tuoi >= 18:
    print("✅ Bạn đủ tuổi để thi bằng lái xe!")
    print("   Hãy đăng ký tại trung tâm sát hạch gần nhất.")
else:
    nam_cho = 18 - tuoi
    print("❌ Bạn chưa đủ tuổi để thi bằng lái xe.")
    print(f"   Bạn cần chờ thêm {nam_cho} năm nữa.")
```

**Kết quả (nhập 16):**

```
Nhập tuổi của bạn: 16
❌ Bạn chưa đủ tuổi để thi bằng lái xe.
   Bạn cần chờ thêm 2 năm nữa.
```

## 4.3. Thêm ví dụ

```python
# === KIỂM TRA SỐ CHẴN / LẺ ===

so = int(input("Nhập một số nguyên: "))

if so % 2 == 0:
    print(f"✅ {so} là số CHẴN")
else:
    print(f"🔹 {so} là số LẺ")
```

```python
# === KIỂM TRA MẬT KHẨU ===

mat_khau_dung = "python123"
mat_khau_nhap = input("Nhập mật khẩu: ")

if mat_khau_nhap == mat_khau_dung:
    print("🔓 Đăng nhập thành công! Chào mừng bạn.")
else:
    print("🔒 Sai mật khẩu! Vui lòng thử lại.")
```

---

---

# Module 5: Câu lệnh `if-elif-else`

## 🎯 Mục tiêu

> Xử lý **NHIỀU trường hợp** khác nhau — Python kiểm tra từng điều kiện từ trên xuống dưới.

---

## 5.1. Cú pháp

```python
if điều_kiện_1:
    # Code khi điều kiện 1 ĐÚNG
elif điều_kiện_2:
    # Code khi điều kiện 2 ĐÚNG
elif điều_kiện_3:
    # Code khi điều kiện 3 ĐÚNG
else:
    # Code khi KHÔNG điều kiện nào đúng
```

> 💡 `elif` = viết tắt của **"else if"** (nếu không thì kiểm tra tiếp).

**Sơ đồ:**

```
    ┌─ Điều kiện 1 ─┐
    │                │
  True ✅         False ❌
    │                │
  Khối 1       ┌─ Điều kiện 2 ─┐
    │          │                │
    │        True ✅         False ❌
    │          │                │
    │        Khối 2       ┌─ Điều kiện 3 ─┐
    │          │          │                │
    │          │        True ✅         False ❌
    │          │          │                │
    │          │        Khối 3          Khối else
    │          │          │                │
    └──────────┴──────────┴────────────────┘
                         ▼
                   Tiếp tục...
```

> ⚠️ **Quan trọng**: Chỉ **MỘT** khối code được thực hiện. Khi tìm thấy điều kiện đúng đầu tiên, Python **bỏ qua** tất cả các `elif`/`else` phía sau!

## 5.2. Ví dụ: Xếp loại học lực

```python
# === XẾP LOẠI HỌC LỰC ===

diem = float(input("Nhập điểm trung bình (0-10): "))

if diem >= 9.0:
    xep_loai = "Xuất sắc 🏆"
elif diem >= 8.0:
    xep_loai = "Giỏi 🥇"
elif diem >= 6.5:
    xep_loai = "Khá 🥈"
elif diem >= 5.0:
    xep_loai = "Trung bình 🥉"
elif diem >= 3.5:
    xep_loai = "Yếu ⚠️"
else:
    xep_loai = "Kém ❌"

print(f"\nĐiểm: {diem} → Xếp loại: {xep_loai}")
```

**Kết quả (nhập 7.5):**

```
Nhập điểm trung bình (0-10): 7.5

Điểm: 7.5 → Xếp loại: Khá 🥈
```

## 5.3. Ví dụ: Tính giá vé xem phim

```python
# === TÍNH GIÁ VÉ XEM PHIM ===

print("🎬 HỆ THỐNG BÁN VÉ XEM PHIM")
print("-" * 35)

tuoi = int(input("Nhập tuổi khách hàng: "))

if tuoi < 5:
    gia_ve = 0
    doi_tuong = "Trẻ em dưới 5 tuổi (MIỄN PHÍ)"
elif tuoi <= 12:
    gia_ve = 45_000
    doi_tuong = "Trẻ em (5-12 tuổi)"
elif tuoi <= 22:
    gia_ve = 55_000
    doi_tuong = "Học sinh / Sinh viên"
elif tuoi <= 60:
    gia_ve = 75_000
    doi_tuong = "Người lớn"
else:
    gia_ve = 40_000
    doi_tuong = "Người cao tuổi (ưu đãi)"

print(f"\n🎫 Thông tin vé:")
print(f"   Đối tượng: {doi_tuong}")
print(f"   Giá vé   : {gia_ve:,} VNĐ")
```

## 5.4. Kết hợp với toán tử logic

```python
# === KIỂM TRA ĐIỀU KIỆN NHẬP HỌC ===

print("🏫 HỆ THỐNG KIỂM TRA ĐIỀU KIỆN NHẬP HỌC")
print("=" * 45)

diem_toan = float(input("Điểm Toán: "))
diem_van = float(input("Điểm Văn: "))
diem_anh = float(input("Điểm Anh: "))

tong_diem = diem_toan + diem_van + diem_anh
dtb = tong_diem / 3

print(f"\n📊 Tổng điểm: {tong_diem:.1f} | Trung bình: {dtb:.2f}")

# Kiều kiện: Tổng >= 21 VÀ không có môn nào dưới 5
if tong_diem >= 24 and diem_toan >= 5 and diem_van >= 5 and diem_anh >= 5:
    print("🎉 CHÚC MỪNG! Bạn ĐỖ với kết quả XUẤT SẮC!")
elif tong_diem >= 21 and diem_toan >= 5 and diem_van >= 5 and diem_anh >= 5:
    print("✅ Bạn ĐỖ! Đủ điều kiện nhập học.")
elif tong_diem >= 21:
    print("⚠️ Tổng điểm đủ nhưng có môn dưới 5. KHÔNG ĐỖ.")
else:
    thieu = 21 - tong_diem
    print(f"❌ Bạn KHÔNG ĐỖ. Thiếu {thieu:.1f} điểm.")
```

---

---

# Module 6: Điều kiện lồng nhau (Nested if)

## 🎯 Mục tiêu

> Đặt câu lệnh `if` **bên trong** một câu lệnh `if` khác để xử lý logic phức tạp.

---

## 6.1. Cú pháp

```python
if điều_kiện_ngoài:
    # Code khi điều kiện ngoài ĐÚNG

    if điều_kiện_trong:
        # Code khi CẢ HAI điều kiện đều ĐÚNG
    else:
        # Điều kiện ngoài đúng, điều kiện trong sai
else:
    # Điều kiện ngoài sai
```

## 6.2. Ví dụ: Hệ thống đăng nhập

```python
# === HỆ THỐNG ĐĂNG NHẬP ===

print("🔐 HỆ THỐNG ĐĂNG NHẬP")
print("-" * 30)

# Tài khoản mẫu
USERNAME = "admin"
PASSWORD = "python2026"

ten_dn = input("Tên đăng nhập: ")

if ten_dn == USERNAME:
    # Tên đúng → kiểm tra mật khẩu
    mat_khau = input("Mật khẩu: ")

    if mat_khau == PASSWORD:
        print("\n🎉 Đăng nhập thành công!")
        print(f"   Chào mừng {ten_dn}!")
    else:
        print("\n❌ Sai mật khẩu! Vui lòng thử lại.")
else:
    print(f"\n❌ Tên đăng nhập '{ten_dn}' không tồn tại!")
```

## 6.3. Ví dụ: Phân loại tam giác

```python
# === PHÂN LOẠI TAM GIÁC ===

print("📐 CHƯƠNG TRÌNH PHÂN LOẠI TAM GIÁC")
print("-" * 38)

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Bước 1: Kiểm tra có phải tam giác không
if a + b > c and a + c > b and b + c > a:
    print(f"\n✅ Ba cạnh ({a}, {b}, {c}) tạo thành tam giác.")

    # Bước 2: Phân loại
    if a == b == c:
        print("   → Tam giác ĐỀU")
    elif a == b or b == c or a == c:
        print("   → Tam giác CÂN")
    else:
        print("   → Tam giác THƯỜNG")

    # Bước 3: Kiểm tra vuông (Pytago)
    canh = sorted([a, b, c])  # Sắp xếp tăng dần
    if canh[2]**2 == canh[0]**2 + canh[1]**2:
        print("   → Đây là tam giác VUÔNG 📐")
else:
    print(f"\n❌ Ba cạnh ({a}, {b}, {c}) KHÔNG tạo thành tam giác!")
```

> ⚠️ **Lời khuyên**: Không nên lồng quá **3 cấp** `if`. Nếu logic quá phức tạp, hãy dùng `elif` hoặc tách thành hàm (function — học ở buổi sau).

---

---

# Module 7: Toán tử ba ngôi & Kỹ thuật nâng cao

## 🎯 Mục tiêu

> Viết điều kiện **ngắn gọn hơn** trong một số trường hợp đơn giản.

---

## 7.1. Toán tử ba ngôi (Ternary Operator)

Viết `if-else` trên **MỘT DÒNG**:

```python
# Cú pháp:
kết_quả = giá_trị_nếu_đúng if điều_kiện else giá_trị_nếu_sai
```

```python
tuoi = 20

# Cách thường
if tuoi >= 18:
    trang_thai = "Trưởng thành"
else:
    trang_thai = "Vị thành niên"

# Cách viết gọn (toán tử ba ngôi)
trang_thai = "Trưởng thành" if tuoi >= 18 else "Vị thành niên"
print(trang_thai)  # Trưởng thành
```

**Thêm ví dụ:**

```python
diem = 7
ket_qua = "Đỗ ✅" if diem >= 5 else "Trượt ❌"
print(ket_qua)  # Đỗ ✅

so = -3
loai = "Dương" if so > 0 else ("Âm" if so < 0 else "Không")
print(f"{so} là số {loai}")  # -3 là số Âm
```

## 7.2. Toán tử `in` — Kiểm tra thành viên

```python
# Kiểm tra giá trị có nằm trong danh sách không
mau_yeu_thich = input("Nhập màu yêu thích: ")

if mau_yeu_thich in ["đỏ", "xanh", "vàng"]:
    print("Đó là một trong ba màu cơ bản!")
else:
    print("Đó không phải màu cơ bản.")

# Kiểm tra ký tự trong chuỗi
email = input("Nhập email: ")
if "@" in email and "." in email:
    print("✅ Email hợp lệ (cơ bản)")
else:
    print("❌ Email không hợp lệ!")
```

## 7.3. Giá trị Truthy và Falsy

Python coi một số giá trị là "như False" (**Falsy**):

| Giá trị Falsy       | Loại            |
| ------------------- | --------------- |
| `False`             | bool            |
| `0`, `0.0`          | Số              |
| `""` _(chuỗi rỗng)_ | str             |
| `None`              | NoneType        |
| `[]`, `{}`, `()`    | Collection rỗng |

```python
ten = input("Nhập tên: ")

# Thay vì: if ten != ""
if ten:
    print(f"Xin chào {ten}!")
else:
    print("Bạn chưa nhập tên!")

# Tương tự với số
so = 0
if not so:
    print("Số bằng 0 hoặc chưa được gán")
```

## 7.4. `match-case` (Python 3.10+)

Tương tự `switch-case` trong các ngôn ngữ khác:

```python
# === MENU NHÀ HÀNG ===

print("📋 MENU:")
print("1. Phở    - 50,000đ")
print("2. Cơm    - 35,000đ")
print("3. Bún    - 40,000đ")

lua_chon = input("\nChọn món (1-3): ")

match lua_chon:
    case "1":
        print("🍜 Bạn chọn: Phở — 50,000đ")
    case "2":
        print("🍚 Bạn chọn: Cơm — 35,000đ")
    case "3":
        print("🍜 Bạn chọn: Bún — 40,000đ")
    case _:
        print("❌ Lựa chọn không hợp lệ!")
```

---

---

# 📝 Bài tập thực hành tổng hợp

## 📌 Bài 1: Xếp loại BMI _(Cơ bản)_

```
Đề bài:
- Nhập cân nặng (kg) và chiều cao (cm)
- Tính BMI = cân nặng / (chiều cao mét)²
- Xếp loại:
  + BMI < 18.5       → Thiếu cân
  + 18.5 ≤ BMI < 25  → Bình thường
  + 25 ≤ BMI < 30    → Thừa cân
  + BMI ≥ 30         → Béo phì
```

<details>
<summary>💡 Xem gợi ý</summary>

```python
can_nang = float(input("Cân nặng (kg): "))
chieu_cao_cm = float(input("Chiều cao (cm): "))
chieu_cao_m = chieu_cao_cm / 100
bmi = can_nang / (chieu_cao_m ** 2)

if bmi < 18.5:
    print(f"BMI = {bmi:.1f} → Thiếu cân")
elif bmi < 25:
    print(f"BMI = {bmi:.1f} → Bình thường ✅")
elif bmi < 30:
    print(f"BMI = {bmi:.1f} → Thừa cân ⚠️")
else:
    print(f"BMI = {bmi:.1f} → Béo phì ❌")
```

</details>

---

## 📌 Bài 2: Tính tiền điện _(Trung bình)_

```
Đề bài: Tính tiền điện theo bậc thang
- 50 kWh đầu tiên         : 1,678 đ/kWh
- Từ 51 đến 100 kWh       : 1,734 đ/kWh
- Từ 101 đến 200 kWh      : 2,014 đ/kWh
- Từ 201 đến 300 kWh      : 2,536 đ/kWh
- Từ 301 đến 400 kWh      : 2,834 đ/kWh
- Từ 401 kWh trở lên      : 2,927 đ/kWh

Nhập số kWh tiêu thụ → In ra tổng tiền điện.
```

<details>
<summary>💡 Xem lời giải</summary>

```python
print("⚡ TÍNH TIỀN ĐIỆN THEO BẬC THANG")
print("=" * 38)

kwh = float(input("Nhập số kWh tiêu thụ: "))
tien = 0

if kwh <= 50:
    tien = kwh * 1678
elif kwh <= 100:
    tien = 50 * 1678 + (kwh - 50) * 1734
elif kwh <= 200:
    tien = 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
elif kwh <= 300:
    tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + (kwh - 200) * 2536
elif kwh <= 400:
    tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (kwh - 300) * 2834
else:
    tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2834 + (kwh - 400) * 2927

print(f"\n📊 Kết quả:")
print(f"   Số điện tiêu thụ : {kwh:.0f} kWh")
print(f"   Tổng tiền điện   : {tien:,.0f} VNĐ")
```

</details>

---

## 📌 Bài 3: Máy ATM mini _(Nâng cao)_

```
Đề bài: Mô phỏng rút tiền ATM
- Số dư ban đầu: 5,000,000 VNĐ
- Nhập mã PIN (đúng: "1234")
- Nếu PIN đúng:
  + Nhập số tiền cần rút
  + Số tiền phải chia hết cho 50,000
  + Số tiền không được lớn hơn số dư
  + Nếu hợp lệ → rút thành công, in số dư còn lại
- Nếu PIN sai: thông báo lỗi
```

<details>
<summary>💡 Xem lời giải</summary>

```python
print("🏧 MÁY ATM MINI")
print("=" * 30)

so_du = 5_000_000
PIN = "1234"

pin_nhap = input("Nhập mã PIN: ")

if pin_nhap == PIN:
    print(f"✅ Xác thực thành công! Số dư: {so_du:,} VNĐ")

    so_tien = int(input("Nhập số tiền cần rút: "))

    if so_tien <= 0:
        print("❌ Số tiền phải lớn hơn 0!")
    elif so_tien % 50_000 != 0:
        print("❌ Số tiền phải chia hết cho 50,000!")
    elif so_tien > so_du:
        print("❌ Số dư không đủ!")
    else:
        so_du -= so_tien
        print(f"\n🎉 Rút thành công {so_tien:,} VNĐ!")
        print(f"💰 Số dư còn lại: {so_du:,} VNĐ")
else:
    print("❌ Sai mã PIN! Giao dịch bị hủy.")
```

</details>

---

## 📌 Bài 4: Trò chơi Oẳn Tù Tì _(Thử thách)_

```
Đề bài:
- Người chơi nhập: "kéo", "búa", hoặc "bao"
- Máy tính chọn ngẫu nhiên
- Xác định người thắng
```

<details>
<summary>💡 Xem lời giải</summary>

```python
import random  # Thư viện tạo số ngẫu nhiên (sẽ học kỹ sau)

print("✊✌️🖐️ OẲN TÙ TÌ")
print("-" * 25)

lua_chon = ["kéo", "búa", "bao"]

nguoi_choi = input("Bạn chọn (kéo/búa/bao): ").lower()

if nguoi_choi not in lua_chon:
    print("❌ Lựa chọn không hợp lệ!")
else:
    may_tinh = random.choice(lua_chon)
    print(f"🤖 Máy tính chọn: {may_tinh}")

    if nguoi_choi == may_tinh:
        print("🤝 HÒA!")
    elif (nguoi_choi == "kéo" and may_tinh == "bao") or \
         (nguoi_choi == "búa" and may_tinh == "kéo") or \
         (nguoi_choi == "bao" and may_tinh == "búa"):
        print("🎉 BẠN THẮNG!")
    else:
        print("😢 BẠN THUA!")
```

</details>

---

## 📌 Checklist tổng kết Buổi 2

| #   | Nội dung                                 | Trạng thái |
| --- | ---------------------------------------- | ---------- |
| 1   | Sử dụng thành thạo 6 toán tử so sánh     | ⬜         |
| 2   | Kết hợp điều kiện với `and`, `or`, `not` | ⬜         |
| 3   | Viết câu lệnh `if` đơn giản              | ⬜         |
| 4   | Viết câu lệnh `if-else`                  | ⬜         |
| 5   | Viết câu lệnh `if-elif-else` nhiều nhánh | ⬜         |
| 6   | Hiểu và áp dụng `if` lồng nhau (nested)  | ⬜         |
| 7   | Dùng toán tử ba ngôi viết gọn            | ⬜         |
| 8   | Hiểu Truthy / Falsy                      | ⬜         |
| 9   | Hoàn thành ít nhất 3/4 bài tập           | ⬜         |

---

> **📢 Hẹn gặp lại ở Buổi 3!**
>
> Ở buổi tiếp theo, chúng ta sẽ học về **Vòng lặp (for/while)** — công cụ giúp chương trình lặp lại hành động mà không cần viết code trùng lặp! 🔁

---

_© 2026 — Giáo trình Python | Biên soạn cho lớp học KITE_
