# 🐍 GIÁO TRÌNH PYTHON — BUỔI 5

## **LUYỆN TẬP TỔNG HỢP: DỰ ÁN MINI**

> _"Kiến thức chỉ thực sự thuộc về bạn khi bạn tự tay xây dựng được một thứ gì đó hoàn chỉnh."_

| Thông tin buổi học     | Chi tiết                                                              |
| ---------------------- | --------------------------------------------------------------------- |
| **Buổi**               | 05                                                                    |
| **Chủ đề**             | Tích hợp biến, điều kiện, vòng lặp, hàm — giải quyết bài toán thực tế |
| **Thời lượng**         | ~3 giờ (bao gồm thực hành và xây dựng dự án)                          |
| **Yêu cầu**            | Đã hoàn thành Buổi 1 → 4 (biến, điều kiện, hàm, vòng lặp)             |
| **Mục tiêu tổng quát** | Biết kết hợp mọi kiến thức đã học để xây dựng chương trình hoàn chỉnh |

---

# 📌 MỤC LỤC

- [Module 1: Ôn tập nhanh — Công cụ bạn đã có](#module-1-ôn-tập-nhanh--công-cụ-bạn-đã-có)
- [Module 2: Tư duy giải bài toán — Từ ý tưởng đến code](#module-2-tư-duy-giải-bài-toán--từ-ý-tưởng-đến-code)
- [Module 3: Thực hành có hướng dẫn](#module-3-thực-hành-có-hướng-dẫn)
- [Module 4: Kỹ thuật debug cơ bản](#module-4-kỹ-thuật-debug-cơ-bản)
- [📝 Dự án Mini](#-dự-án-mini)

---

---

# Module 1: Ôn tập nhanh — Công cụ bạn đã có

## 🎯 Mục tiêu

> Nhìn lại toàn bộ kiến thức từ Buổi 1 → 4 như một bộ công cụ hoàn chỉnh.

---

## 1.1. Bảng tổng hợp kiến thức

| Buổi | Kiến thức             | Vai trò                    | Ví dụ                               |
| ---- | --------------------- | -------------------------- | ----------------------------------- |
| 1    | Biến, kiểu dữ liệu    | Lưu trữ dữ liệu            | `ten = "An"`, `diem = 8.5`          |
| 1    | `input()` / `print()` | Nhận và hiển thị thông tin | `ten = input("Tên: ")`              |
| 1    | f-string              | Hiển thị kết quả đẹp       | `f"Xin chào {ten}!"`                |
| 2    | `if/elif/else`        | Rẽ nhánh, ra quyết định    | `if diem >= 5: ...`                 |
| 2    | Toán tử logic         | Kết hợp điều kiện          | `and`, `or`, `not`                  |
| 3    | Hàm (`def`)           | Đóng gói, tái sử dụng      | `def tinh_tong(a, b): return a + b` |
| 3    | `return`              | Trả kết quả từ hàm         | `return ket_qua`                    |
| 4    | `for` / `range()`     | Lặp theo số lần            | `for i in range(10): ...`           |
| 4    | `while`               | Lặp theo điều kiện         | `while chay: ...`                   |
| 4    | `break` / `continue`  | Điều khiển vòng lặp        | Thoát sớm / Bỏ qua lượt             |

## 1.2. Quy tắc kết hợp

Mọi chương trình phức tạp đều được xây dựng từ 4 khối cơ bản:

```
┌──────────────────────────────────────────┐
│         CHƯƠNG TRÌNH PYTHON              │
│                                          │
│  1. BIẾN         → Lưu trữ dữ liệu      │
│  2. ĐIỀU KIỆN    → Ra quyết định         │
│  3. VÒNG LẶP     → Lặp lại công việc     │
│  4. HÀM          → Tổ chức, tái sử dụng  │
│                                          │
│  Input → Xử lý → Output                  │
└──────────────────────────────────────────┘
```

## 1.3. Bài tập ôn tập nhanh — Đoán kết quả

### Câu 1:

```python
def dem_ky_tu(chuoi, ky_tu):
    dem = 0
    for c in chuoi:
        if c == ky_tu:
            dem = dem + 1
    return dem

print(dem_ky_tu("banana", "a"))
```

<details>
<summary>👀 Xem đáp án</summary>

```
3
```

Có 3 chữ "a" trong "banana".

</details>

### Câu 2:

```python
tong = 0
i = 1
while i <= 10:
    if i % 2 == 0:
        tong = tong + i
    i = i + 1
print(tong)
```

<details>
<summary>👀 Xem đáp án</summary>

```
30
```

Tổng các số chẵn từ 1 đến 10: 2 + 4 + 6 + 8 + 10 = 30.

</details>

### Câu 3:

```python
def xu_ly(n):
    ket_qua = ""
    while n > 0:
        ket_qua = str(n % 10) + ket_qua
        n = n // 10
    return ket_qua

print(xu_ly(12345))
```

<details>
<summary>👀 Xem đáp án</summary>

```
12345
```

Hàm tách từng chữ số và nối lại thành chuỗi — kết quả giống số ban đầu (dạng chuỗi).

</details>

---

---

# Module 2: Tư duy giải bài toán — Từ ý tưởng đến code

## 🎯 Mục tiêu

> Biết cách phân tích bài toán và lập kế hoạch trước khi code.

---

## 2.1. Quy trình 5 bước

Mỗi khi gặp một bài toán, hãy đi qua 5 bước:

```
Bước 1: ĐỌC KỸ đề bài — chương trình cần làm gì?
Bước 2: XÁC ĐỊNH Input / Output — nhận vào gì, trả ra gì?
Bước 3: PHÁC THẢO giải thuật — liệt kê các bước bằng tiếng Việt
Bước 4: TÁCH HÀM — bước nào nên đóng gói thành hàm?
Bước 5: VIẾT CODE — chuyển giải thuật thành Python
```

## 2.2. Ví dụ minh họa đầy đủ

**Bài toán:** Viết chương trình nhập N số từ bàn phím, tìm số lớn nhất, nhỏ nhất, và tính trung bình.

### Bước 1: Đọc kỹ

- Chương trình nhập nhiều số
- Tìm max, min, trung bình

### Bước 2: Input / Output

```
Input:  N (số lượng), rồi nhập N số
Output: Số lớn nhất, nhỏ nhất, trung bình
```

### Bước 3: Phác thảo giải thuật

```
1. Nhập N
2. Lặp N lần:
   a. Nhập 1 số
   b. Cộng vào tổng
   c. So sánh với max → cập nhật
   d. So sánh với min → cập nhật
3. Tính trung bình = tổng / N
4. In kết quả
```

### Bước 4: Tách hàm

```
- nhap_so() → nhập và kiểm tra 1 số
- in_ket_qua(max, min, tb) → in đẹp
```

### Bước 5: Viết code

```python
def nhap_so(stt):
    """Nhập 1 số từ bàn phím."""
    return float(input(f"  Nhập số thứ {stt}: "))


def in_ket_qua(so_max, so_min, trung_binh, n):
    """In kết quả phân tích."""
    print(f"\n📊 KẾT QUẢ ({n} số):")
    print(f"  Lớn nhất  : {so_max}")
    print(f"  Nhỏ nhất  : {so_min}")
    print(f"  Trung bình: {trung_binh:.2f}")


# === CHƯƠNG TRÌNH CHÍNH ===
n = int(input("Nhập số lượng N: "))

if n <= 0:
    print("❌ N phải lớn hơn 0!")
else:
    # Nhập số đầu tiên = khởi tạo max, min
    so_dau = nhap_so(1)
    tong = so_dau
    so_max = so_dau
    so_min = so_dau

    # Nhập các số còn lại
    for i in range(2, n + 1):
        so = nhap_so(i)
        tong = tong + so

        if so > so_max:
            so_max = so
        if so < so_min:
            so_min = so

    trung_binh = tong / n
    in_ket_qua(so_max, so_min, trung_binh, n)
```

**Chạy thử:**

```
Nhập số lượng N: 4
  Nhập số thứ 1: 15
  Nhập số thứ 2: 7
  Nhập số thứ 3: 23
  Nhập số thứ 4: 11

📊 KẾT QUẢ (4 số):
  Lớn nhất  : 23.0
  Nhỏ nhất  : 7.0
  Trung bình: 14.00
```

> 🌟 **Quy tắc vàng:** Đừng bao giờ viết code ngay khi đọc xong đề. Hãy dành 2-3 phút phác thảo trước!

---

---

# Module 3: Thực hành có hướng dẫn

## 🎯 Mục tiêu

> Thực hành giải bài toán tổng hợp theo từng bước, có hướng dẫn chi tiết.

---

## 3.1. Bài thực hành: Trò chơi "Số may mắn"

**Đề bài:** Viết trò chơi: máy chọn 1 số bí mật (cố định = 42). Người chơi liên tục đoán (tối đa 5 lần). Mỗi lần đoán, chương trình gợi ý "Cao hơn/Thấp hơn". Cuối trò chơi, xếp hạng dựa trên số lần đoán.

### Bước 1: Input / Output

```
Input:  Lần lượt nhập các số dự đoán
Output: Gợi ý, kết quả, xếp hạng
```

### Bước 2: Tách hàm

```python
def tao_so_bi_mat():
    return 42

def goi_y(du_doan, bi_mat):
    # Trả về gợi ý

def xep_hang(so_luot):
    # Trả về xếp hạng
```

### Bước 3: Code hoàn chỉnh

```python
def tao_so_bi_mat():
    """Trả về số bí mật."""
    return 42


def goi_y(du_doan, bi_mat):
    """Trả về gợi ý so sánh."""
    if du_doan > bi_mat:
        return "📈 Số bí mật THẤP HƠN!"
    else:
        return "📉 Số bí mật CAO HƠN!"


def xep_hang(so_luot):
    """Xếp hạng dựa trên số lượt đoán."""
    if so_luot == 1:
        return "🏆 Thần đoán! Đoán đúng lần đầu!"
    elif so_luot <= 3:
        return "⭐ Xuất sắc!"
    elif so_luot <= 5:
        return "👍 Tốt lắm!"
    else:
        return "😅 Cần cố gắng hơn"


# === CHƯƠNG TRÌNH CHÍNH ===
print("🎮 TRÒ CHƠI SỐ MAY MẮN")
print("Đoán số bí mật (1-100). Bạn có 5 lượt!")
print("-" * 35)

bi_mat = tao_so_bi_mat()
max_luot = 5
thang = False

for luot in range(1, max_luot + 1):
    du_doan = int(input(f"\nLượt {luot}/{max_luot}: Nhập số đoán: "))

    if du_doan == bi_mat:
        print(f"🎯 ĐÚNG RỒI! Bạn đoán đúng sau {luot} lượt!")
        print(xep_hang(luot))
        thang = True
        break

    print(goi_y(du_doan, bi_mat))

if not thang:
    print(f"\n❌ Hết lượt! Đáp án là {bi_mat}.")
```

## 3.2. Bài thực hành: Máy tính điểm thi

**Đề bài:** Nhập điểm cho nhiều học sinh (nhập tên = "stop" để dừng). Sau khi nhập xong, in bảng tổng kết.

### Code hoàn chỉnh

```python
def nhap_diem():
    """Nhập điểm, kiểm tra 0-10. Yêu cầu nhập lại nếu sai."""
    while True:
        diem = float(input("  Điểm (0-10): "))
        if diem >= 0 and diem <= 10:
            return diem
        print("  ⚠️ Điểm phải từ 0 đến 10!")


def xep_loai(diem):
    """Xếp loại theo điểm."""
    if diem >= 9:
        return "Xuất sắc"
    elif diem >= 8:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5:
        return "TB"
    else:
        return "Yếu"


# === CHƯƠNG TRÌNH CHÍNH ===
print("📋 NHẬP ĐIỂM THI")
print('(Nhập tên = "stop" để kết thúc)\n')

dem = 0
tong = 0
diem_max = -1
diem_min = 11
bang = ""
dem_xuat_sac = 0
dem_yeu = 0

while True:
    ten = input(f"Học sinh {dem + 1} — Tên: ")

    if ten == "stop":
        break

    diem = nhap_diem()
    loai = xep_loai(diem)

    dem = dem + 1
    tong = tong + diem

    if diem > diem_max:
        diem_max = diem
    if diem < diem_min:
        diem_min = diem

    if diem >= 9:
        dem_xuat_sac = dem_xuat_sac + 1
    if diem < 5:
        dem_yeu = dem_yeu + 1

    dong = f"  {dem:>2}. {ten:<15} {diem:>5.1f}   {loai}\n"
    bang = bang + dong

    print(f"  → {loai}\n")

# In kết quả
if dem == 0:
    print("⚠️ Chưa có học sinh nào!")
else:
    dtb = tong / dem

    print("\n" + "═" * 45)
    print("📊 BẢNG KẾT QUẢ THI")
    print("═" * 45)
    print(f"  {'STT':<5} {'Tên':<15} {'Điểm':>5}   Loại")
    print("─" * 45)
    print(bang, end="")
    print("─" * 45)
    print(f"  Sĩ số         : {dem}")
    print(f"  ĐTB lớp       : {dtb:.2f}")
    print(f"  Điểm cao nhất : {diem_max}")
    print(f"  Điểm thấp nhất: {diem_min}")
    print(f"  Xuất sắc      : {dem_xuat_sac}")
    print(f"  Yếu           : {dem_yeu}")
    print("═" * 45)
```

**Chạy thử:**

```
📋 NHẬP ĐIỂM THI
(Nhập tên = "stop" để kết thúc)

Học sinh 1 — Tên: Nguyễn An
  Điểm (0-10): 8.5
  → Giỏi

Học sinh 2 — Tên: Trần Bình
  Điểm (0-10): 6.0
  → TB

Học sinh 3 — Tên: Lê Chi
  Điểm (0-10): 9.5
  → Xuất sắc

Học sinh 4 — Tên: stop

═════════════════════════════════════════════
📊 BẢNG KẾT QUẢ THI
═════════════════════════════════════════════
  STT   Tên             Điểm   Loại
─────────────────────────────────────────────
   1. Nguyễn An          8.5   Giỏi
   2. Trần Bình          6.0   TB
   3. Lê Chi             9.5   Xuất sắc
─────────────────────────────────────────────
  Sĩ số         : 3
  ĐTB lớp       : 8.00
  Điểm cao nhất : 9.5
  Điểm thấp nhất: 6.0
  Xuất sắc      : 1
  Yếu           : 0
═════════════════════════════════════════════
```

---

---

# Module 4: Kỹ thuật debug cơ bản

## 🎯 Mục tiêu

> Biết cách tìm và sửa lỗi trong chương trình Python.

---

## 4.1. Ba loại lỗi phổ biến

| Loại lỗi        | Mô tả                            | Ví dụ                          |
| --------------- | -------------------------------- | ------------------------------ |
| **Lỗi cú pháp** | Viết sai cú pháp Python          | Thiếu `:`, thụt dòng sai       |
| **Lỗi runtime** | Lỗi xảy ra khi chạy              | Chia cho 0, biến chưa khai báo |
| **Lỗi logic**   | Code chạy được nhưng sai kết quả | Dùng `>` thay vì `>=`          |

## 4.2. Kỹ thuật "print debug"

Cách đơn giản nhất để debug: thêm `print()` để xem giá trị biến.

### Ví dụ: Hàm tính tổng bị sai

```python
# ❌ Code bị lỗi
def tinh_tong(n):
    tong = 0
    for i in range(n):   # BUG: range(n) chạy từ 0 đến n-1
        tong = tong + i
    return tong

print(tinh_tong(5))  # Mong đợi 15, nhưng ra 10!
```

### Thêm print để debug:

```python
def tinh_tong(n):
    tong = 0
    for i in range(n):
        print(f"  DEBUG: i={i}, tong trước={tong}")  # Dòng debug
        tong = tong + i
    return tong

print(tinh_tong(5))
```

```
  DEBUG: i=0, tong trước=0
  DEBUG: i=1, tong trước=0
  DEBUG: i=2, tong trước=1
  DEBUG: i=3, tong trước=3
  DEBUG: i=4, tong trước=6
10
```

→ Phát hiện: `i` chạy từ 0 đến 4 thay vì 1 đến 5!

### Sửa lỗi:

```python
# ✅ Code đúng
def tinh_tong(n):
    tong = 0
    for i in range(1, n + 1):  # range(1, n+1) chạy từ 1 đến n
        tong = tong + i
    return tong

print(tinh_tong(5))  # 15 ✅
```

## 4.3. Bảng theo dõi biến (Trace table)

Khi gặp lỗi logic, hãy vẽ bảng theo dõi:

```python
# Tìm lỗi trong đoạn code này
dem = 0
so = 1
while so < 10:
    if so % 2 == 0:
        dem = dem + 1
    so = so + 2  # BUG: chỉ duyệt số lẻ!
print(f"Số chẵn từ 1-10: {dem}")  # Ra 0, mong đợi 5!
```

| Lượt | `so` | `so % 2 == 0` | `dem` | Ghi chú      |
| ---- | ---- | ------------- | ----- | ------------ |
| 1    | 1    | False         | 0     | so += 2 → 3  |
| 2    | 3    | False         | 0     | so += 2 → 5  |
| 3    | 5    | False         | 0     | so += 2 → 7  |
| 4    | 7    | False         | 0     | so += 2 → 9  |
| 5    | 9    | False         | 0     | so += 2 → 11 |

→ Phát hiện: `so` bắt đầu từ 1 và nhảy 2, nên **chỉ duyệt số lẻ**!

## 4.4. Checklist debug

Khi bài code không chạy đúng, hãy kiểm tra:

- [ ] Biến tích lũy đã khởi tạo **trước** vòng lặp chưa?
- [ ] `range()` có đúng giá trị bắt đầu và kết thúc không?
- [ ] Biến điều kiện trong `while` có được cập nhật không?
- [ ] Dùng `=` (gán) hay `==` (so sánh)?
- [ ] Hàm có `return` giá trị đúng chỗ không?
- [ ] Thụt đầu dòng có đúng không?

### Bài tập debug

**Tìm và sửa 3 lỗi trong code sau:**

```python
def tinh_giai_thua(n)
    ket_qua = 0
    for i in range(1, n + 1):
        ket_qua = ket_qua * i
    return ket_qua

print(tinh_giai_thua(5))  # Mong đợi 120
```

<details>
<summary>👀 Xem đáp án</summary>

3 lỗi:

1. **Thiếu dấu `:`** ở dòng `def tinh_giai_thua(n)` → sửa: `def tinh_giai_thua(n):`
2. **Khởi tạo sai**: `ket_qua = 0` → nhân với 0 luôn ra 0 → sửa: `ket_qua = 1`
3. Không có lỗi thứ 3 — nhưng nếu `n = 0` thì nên trả về 1 (0! = 1)

```python
def tinh_giai_thua(n):    # Sửa: thêm dấu :
    ket_qua = 1           # Sửa: 0 → 1
    for i in range(1, n + 1):
        ket_qua = ket_qua * i
    return ket_qua

print(tinh_giai_thua(5))  # 120 ✅
```

</details>

---

---

# 📝 Dự án Mini

> 🎯 Đây là các dự án tổng hợp **tất cả kiến thức từ Buổi 1 → 4**:
>
> - Biến, kiểu dữ liệu, f-string
> - Câu điều kiện `if/elif/else`
> - Hàm `def`, `return`, tham số
> - Vòng lặp `for`, `while`, `break`, `continue`
>
> Mỗi dự án có **mô tả chi tiết**, **test case**, và **hướng dẫn tách hàm**.
>
> 📄 **Lời giải** được đặt riêng trong file: `Buoi_05_Loi_Giai.md`

---

## 📌 Dự án 1: Ứng dụng Quiz trắc nghiệm _(Trung bình)_

```
📋 Bối cảnh:
Viết chương trình hỏi đáp trắc nghiệm về kiến thức tổng quát.
Chương trình hỏi 5 câu, mỗi câu có 4 đáp án A/B/C/D.
Sau khi hoàn thành, in kết quả chi tiết.

Ngân hàng câu hỏi (cố định trong code):
- Câu 1: "Thủ đô của Việt Nam?" — A.HCM B.Đà Nẵng C.Hà Nội D.Huế → Đáp án: C
- Câu 2: "Python là ngôn ngữ gì?" — A.Biên dịch B.Thông dịch C.Máy D.Assembly → Đáp án: B
- Câu 3: "1 KB = ? byte" — A.100 B.500 C.1000 D.1024 → Đáp án: D
- Câu 4: "Ai phát minh Python?" — A.Bill Gates B.Guido C.Elon Musk D.Steve Jobs → Đáp án: B
- Câu 5: "HTML dùng để?" — A.Lập trình B.Cơ sở dữ liệu C.Tạo web D.Đồ hoạ → Đáp án: C

📝 Yêu cầu:
1. Viết hàm lay_cau_hoi(stt) → trả về chuỗi câu hỏi
2. Viết hàm lay_dap_an(stt) → trả về đáp án đúng (A/B/C/D)
3. Viết hàm kiem_tra(tra_loi, dap_an) → trả về True/False
4. Viết hàm xep_hang(diem) → trả về xếp hạng
5. Dùng vòng lặp for qua 5 câu
6. Mỗi câu: in câu hỏi → nhập đáp án → kiểm tra → tính điểm
7. Cuối: in bảng kết quả chi tiết

📌 Test case:
   🧠 QUIZ KIẾN THỨC TỔNG QUÁT
   ════════════════════════════════

   Câu 1/5: Thủ đô của Việt Nam?
   A. HCM    B. Đà Nẵng    C. Hà Nội    D. Huế
   Đáp án của bạn: C
   ✅ Chính xác!

   Câu 2/5: Python là ngôn ngữ gì?
   A. Biên dịch    B. Thông dịch    C. Máy    D. Assembly
   Đáp án của bạn: A
   ❌ Sai! Đáp án đúng: B

   ... (tiếp tục)

   ════════════════════════════════
   📊 KẾT QUẢ
   ════════════════════════════════
   Câu 1: ✅    Câu 2: ❌    Câu 3: ✅
   Câu 4: ✅    Câu 5: ✅
   ────────────────────────────────
   Điểm: 4/5 (80%)
   Xếp hạng: ⭐ Giỏi!
   ════════════════════════════════
```

---

### 💡 Giải thích tiêu chí xếp hạng (Dự án 1)

Để hàm `xep_hang(diem)` dễ viết và dễ hiểu, có thể xếp hạng theo **số câu đúng trên 5 câu** như sau:

| Điểm (đúng/5) | Tỷ lệ  | Xếp hạng gợi ý |
| ------------- | ------ | -------------- |
| 5/5           | 100%   | 🏆 Xuất sắc!   |
| 4/5           | 80%    | ⭐ Giỏi!       |
| 3/5           | 60%    | 👍 Khá         |
| 2/5           | 40%    | 🙂 Trung bình  |
| 0-1/5         | 0%-20% | 📚 Cần cố gắng |

✅ Với test case mẫu `4/5 (80%)` thì xếp hạng đúng là: **⭐ Giỏi!**

Gợi ý logic trong hàm `xep_hang(diem)`:

- Nếu `diem == 5` → "🏆 Xuất sắc!"
- Nếu `diem == 4` → "⭐ Giỏi!"
- Nếu `diem == 3` → "👍 Khá"
- Nếu `diem == 2` → "🙂 Trung bình"
- Còn lại → "📚 Cần cố gắng"

---

## 📌 Dự án 2: Sổ tay từ điển Anh-Việt mini _(Trung bình)_

```
📋 Bối cảnh:
Viết chương trình tra từ điển Anh-Việt đơn giản.
Dữ liệu từ điển cố định trong code (dùng chuỗi, chưa học list/dict).

Từ điển (10 từ):
- "hello" → "xin chào"
- "goodbye" → "tạm biệt"
- "thank" → "cảm ơn"
- "sorry" → "xin lỗi"
- "love" → "yêu thương"
- "friend" → "bạn bè"
- "school" → "trường học"
- "teacher" → "giáo viên"
- "student" → "học sinh"
- "python" → "con trăn / ngôn ngữ lập trình"

📝 Yêu cầu:
1. Viết hàm tra_tu(tu_tieng_anh) → trả về nghĩa tiếng Việt
   Trả về "Không tìm thấy" nếu từ không có trong từ điển
2. Viết hàm in_menu() → in menu chức năng
3. Chương trình vòng lặp chính:
   - 1: Tra từ (nhập từ → hiển thị nghĩa)
   - 2: Xem tất cả từ vựng
   - 3: Kiểm tra từ vựng (chương trình hỏi nghĩa, người dùng đoán từ)
   - 0: Thoát
4. Chức năng kiểm tra: hỏi 5 từ ngẫu nhiên (cố định thứ tự),
   người dùng nhập từ tiếng Anh → chấm điểm

📌 Test case:
   📖 TỪ ĐIỂN ANH-VIỆT MINI
   1. Tra từ
   2. Xem tất cả từ vựng
   3. Kiểm tra từ vựng
   0. Thoát

   Chọn: 1
   Nhập từ tiếng Anh: hello
   → "hello" = "xin chào"

   Chọn: 1
   Nhập từ tiếng Anh: cat
   → Không tìm thấy từ "cat"!

   Chọn: 2

   📚 TẤT CẢ TỪ VỰNG:
   ───────────────────────────────────
   hello        → xin chào
   goodbye      → tạm biệt
   thank        → cảm ơn
   sorry        → xin lỗi
   love         → yêu thương
   friend       → bạn bè
   school       → trường học
   teacher      → giáo viên
   student      → học sinh
   python       → con trăn / ngôn ngữ LP
   ───────────────────────────────────

   Chọn: 3
   📝 KIỂM TRA TỪ VỰNG (5 câu)

   Câu 1: "xin chào" tiếng Anh là gì? hello
   ✅ Đúng!

   Câu 2: "bạn bè" tiếng Anh là gì? family
   ❌ Sai! Đáp án: friend

   ... Kết quả: 4/5 (80%)

   Chọn: 0
   👋 Tạm biệt!
```

---

## 📌 Dự án 3: Hệ thống quản lý thư viện mini _(Nâng cao)_

```
📋 Bối cảnh:
Viết chương trình quản lý mượn sách cho thư viện trường.
(Dùng biến chuỗi để lưu trạng thái sách, vì chưa học list)

Danh sách sách (5 cuốn — trạng thái ban đầu: tất cả "có sẵn"):
- Mã 1: "Doraemon tập 1" — Trạng thái: có sẵn
- Mã 2: "Harry Potter" — Trạng thái: có sẵn
- Mã 3: "Conan tập 5" — Trạng thái: có sẵn
- Mã 4: "Lập trình Python" — Trạng thái: có sẵn
- Mã 5: "Toán lớp 8" — Trạng thái: có sẵn

📝 Yêu cầu:
1. Viết hàm lay_ten_sach(ma) → tên sách
2. Viết hàm in_danh_sach(tt1, tt2, tt3, tt4, tt5) → in bảng sách + trạng thái
3. Viết hàm in_menu() → menu chức năng
4. Chương trình vòng lặp chính:
   - 1: Xem danh sách sách
   - 2: Mượn sách (nhập mã → kiểm tra → đổi trạng thái)
   - 3: Trả sách (nhập mã → kiểm tra → đổi trạng thái)
   - 4: Thống kê (đếm sách có sẵn / đang mượn)
   - 0: Thoát
5. Khi mượn: kiểm tra sách có sẵn không, nhập tên người mượn
6. Khi trả: kiểm tra sách có đang mượn không

📌 Test case:
   📚 THƯ VIỆN TRƯỜNG HỌC
   1. Xem danh sách sách
   2. Mượn sách
   3. Trả sách
   4. Thống kê
   0. Thoát

   Chọn: 1
   ┌────┬──────────────────┬────────────┐
   │ Mã │ Tên sách          │ Trạng thái │
   ├────┼──────────────────┼────────────┤
   │  1 │ Doraemon tập 1    │ ✅ Có sẵn  │
   │  2 │ Harry Potter      │ ✅ Có sẵn  │
   │  3 │ Conan tập 5       │ ✅ Có sẵn  │
   │  4 │ Lập trình Python  │ ✅ Có sẵn  │
   │  5 │ Toán lớp 8        │ ✅ Có sẵn  │
   └────┴──────────────────┴────────────┘

   Chọn: 2
   Nhập mã sách cần mượn: 2
   Nhập tên người mượn: Nguyễn An
   ✅ "Nguyễn An" đã mượn thành công "Harry Potter"!

   Chọn: 2
   Nhập mã sách cần mượn: 2
   ❌ Sách "Harry Potter" đang được mượn!

   Chọn: 3
   Nhập mã sách cần trả: 2
   ✅ Đã trả thành công "Harry Potter"!

   Chọn: 4
   📊 THỐNG KÊ:
   Tổng sách     : 5
   Có sẵn        : 5
   Đang mượn     : 0
```

---

## 📌 Dự án 4: Game phiêu lưu văn bản _(Nâng cao)_

```
📋 Bối cảnh:
Viết trò chơi phiêu lưu dạng text (text adventure game).
Người chơi đưa ra lựa chọn ở mỗi tình huống, mỗi lựa chọn
dẫn đến kịch bản khác nhau.

Cốt truyện:
- Người chơi là một nhà thám hiểm trong rừng rậm
- Bắt đầu với 100 điểm sức khỏe, 0 vàng
- Qua mỗi tình huống, sức khỏe/vàng thay đổi
- Game kết thúc khi: sức khỏe <= 0 (thua) hoặc đi qua hết 5 tình huống (thắng)

Tình huống:
1. "Bạn gặp một ngã ba đường"
   a) Đi trái (rừng rậm) → mất 20 sức khỏe, được 30 vàng
   b) Đi phải (suối) → hồi 10 sức khỏe, được 10 vàng

2. "Bạn gặp một con quái vật"
   a) Chiến đấu → mất 40 sức khỏe, được 50 vàng
   b) Bỏ chạy → mất 10 sức khỏe, mất 5 vàng

3. "Bạn tìm thấy một ngôi nhà bỏ hoang"
   a) Vào khám phá → 50% được 60 vàng, 50% mất 30 sức khỏe
      (Dùng: nếu vàng hiện tại chẵn → được, lẻ → mất)
   b) Đi qua → không thay đổi gì

4. "Bạn gặp một thương nhân"
   a) Mua thuốc (20 vàng) → hồi 50 sức khỏe (nếu đủ vàng)
   b) Mua bản đồ (30 vàng) → được 40 vàng thưởng (nếu đủ vàng)
   c) Bỏ qua → không thay đổi gì

5. "Bạn đến cửa hang kho báu"
   a) Vào hang → nếu sức khỏe ≥ 50: được 100 vàng (THẮNG LỚN)
                  nếu sức khỏe < 50: mất 30 sức khỏe
   b) Quay về → kết thúc an toàn

📝 Yêu cầu:
1. Viết hàm in_trang_thai(suc_khoe, vang) → in thanh trạng thái
2. Viết hàm tinh_huong_1(suc_khoe, vang) → trả về (suc_khoe, vang) mới
3. Viết hàm tinh_huong_2(suc_khoe, vang) → trả về (suc_khoe, vang) mới
4. Tương tự cho tình huống 3, 4, 5
5. Viết hàm kiem_tra_song(suc_khoe) → True/False
6. Viết hàm xep_hang_cuoi(suc_khoe, vang) → xếp hạng kết thúc
7. Dùng for lặp qua 5 tình huống, break nếu sức khỏe <= 0

📌 Test case:
   🗡️ PHIÊU LƯU TRONG RỪNG RẬM
   ═══════════════════════════════
   ❤️ Sức khỏe: 100    💰 Vàng: 0

   ── Tình huống 1/5 ──
   Bạn gặp một ngã ba đường.
   a) Đi bên trái (rừng rậm)
   b) Đi bên phải (suối)
   Lựa chọn: a
   🌲 Rừng rậm nguy hiểm! Mất 20 sức khỏe, nhưng tìm được 30 vàng!
   ❤️ Sức khỏe: 80    💰 Vàng: 30

   ── Tình huống 2/5 ──
   Bạn gặp một con quái vật!
   a) Chiến đấu
   b) Bỏ chạy
   Lựa chọn: a
   ⚔️ Chiến đấu dũng cảm! Mất 40 sức khỏe, được 50 vàng!
   ❤️ Sức khỏe: 40    💰 Vàng: 80

   ... (tiếp tục)

   ═══════════════════════════════
   🏁 KẾT THÚC PHIÊU LƯU!
   ❤️ Sức khỏe cuối: 60    💰 Vàng: 150
   🌟 Xếp hạng: Nhà thám hiểm dày dạn!
   ═══════════════════════════════
```

---

## 📌 Dự án 5: Máy tính khoa học mini _(Nâng cao)_

```
📋 Bối cảnh:
Viết máy tính khoa học có menu, hỗ trợ nhiều phép tính.

📝 Chức năng:
1. Cộng/Trừ/Nhân/Chia (2 số)
2. Tính lũy thừa (a^n — dùng vòng lặp, KHÔNG dùng **)
3. Tính giai thừa (n!)
4. Kiểm tra số nguyên tố
5. Phân tích thừa số nguyên tố
6. Tính UCLN (Ước chung lớn nhất)
7. Tính BCNN (Bội chung nhỏ nhất)
8. Đổi hệ cơ số (thập phân → nhị phân)
0. Thoát

📝 Yêu cầu:
1. Mỗi chức năng là 1 hàm riêng biệt
2. Chương trình chạy trong vòng lặp while
3. Sau mỗi phép tính, hỏi "Tính tiếp?" → quay lại menu
4. Validate dữ liệu đầu vào cho mỗi phép tính

📌 Test case:
   🧮 MÁY TÍNH KHOA HỌC MINI
   ═══════════════════════════
   1. ➕ Cộng/Trừ/Nhân/Chia
   2. 🔢 Tính lũy thừa (a^n)
   3. ❗ Tính giai thừa (n!)
   4. 🔍 Kiểm tra số nguyên tố
   5. 📊 Phân tích thừa số NT
   6. 🔗 Tính ƯCLN
   7. 🔗 Tính BCNN
   8. 💻 Đổi sang nhị phân
   0. 🚪 Thoát
   ═══════════════════════════
   Chọn: 3
   Nhập n: 6
   → 6! = 720

   Chọn: 4
   Nhập số: 17
   → 17 LÀ số nguyên tố ✅

   Chọn: 6
   Nhập số thứ nhất: 12
   Nhập số thứ hai: 18
   → ƯCLN(12, 18) = 6

   Chọn: 8
   Nhập số thập phân: 25
   → 25 (thập phân) = 11001 (nhị phân)

   Chọn: 0
   👋 Tạm biệt!
```

---

## 📌 Dự án 6: Hệ thống thi trắc nghiệm toán học _(Thử thách)_

```
📋 Bối cảnh:
Viết chương trình tạo bài thi toán tự động. Chương trình tự
tạo các phép tính ngẫu nhiên (dùng số cố định vì chưa học random),
học sinh trả lời, chương trình chấm điểm.

📝 Yêu cầu:
1. Viết hàm tao_phep_tinh(stt) → trả về (a, b, phep_tinh, dap_an)
   Dùng các phép tính cố định nhưng đa dạng:
   - Câu 1: 15 + 27 = 42
   - Câu 2: 83 - 45 = 38
   - Câu 3: 12 * 6 = 72
   - Câu 4: 96 / 8 = 12
   - Câu 5: 17 + 38 = 55
   - Câu 6: 100 - 67 = 33
   - Câu 7: 15 * 9 = 135
   - Câu 8: 144 / 12 = 12
   - Câu 9: 256 + 189 = 445
   - Câu 10: 1000 - 573 = 427
2. Viết hàm bat_dau_thi(so_cau) → điều phối bài thi
   - Hỏi từng câu, nhập đáp án
   - Nếu đúng: +10 điểm, in ✅
   - Nếu sai: +0 điểm, in ❌ + đáp án đúng
   - Tính thời gian: đếm số câu đúng liên tiếp (streak)
3. Viết hàm in_ket_qua(dung, sai, tong_diem, streak_max)
   → in bảng kết quả chi tiết
4. Menu chọn:
   - Thi 5 câu (dễ)
   - Thi 10 câu (đầy đủ)
   - Xem lại đáp án
   - Thoát

📌 Test case:
   📝 THI TRẮC NGHIỆM TOÁN HỌC
   ═══════════════════════════════
   1. Thi 5 câu (Dễ)
   2. Thi 10 câu (Đầy đủ)
   0. Thoát
   Chọn: 1

   ── BẮT ĐẦU THI ──

   Câu 1: 15 + 27 = ?
   Đáp án: 42
   ✅ Chính xác! (+10 điểm) 🔥 Streak: 1

   Câu 2: 83 - 45 = ?
   Đáp án: 40
   ❌ Sai! Đáp án đúng: 38. Streak reset!

   Câu 3: 12 × 6 = ?
   Đáp án: 72
   ✅ Chính xác! (+10 điểm) 🔥 Streak: 1

   ... (tiếp tục)

   ═══════════════════════════════
   📊 KẾT QUẢ BÀI THI
   ═══════════════════════════════
   Số câu đúng   : 4/5
   Số câu sai    : 1/5
   Tổng điểm     : 40/50
   Streak cao nhất: 3 🔥
   Xếp loại      : Giỏi ⭐
   ═══════════════════════════════
```

---

### 💡 Giải thích tiêu chí xếp hạng (Dự án 6)

Để hàm `in_ket_qua(...)` rõ ràng, có thể xếp loại theo **tỷ lệ câu đúng** (hoặc tương đương theo tổng điểm).

Vì mỗi câu đúng được `10` điểm:

$$
	ext{Tỷ lệ đúng (\%)} = \frac{\text{Số câu đúng}}{\text{Tổng số câu}} \times 100
$$

và

$$
	ext{Tổng điểm} = \text{Số câu đúng} \times 10
$$

| Tỷ lệ đúng | Mức xếp hạng gợi ý |
| ---------- | ------------------ |
| 90% - 100% | 🏆 Xuất sắc        |
| 70% - 89%  | ⭐ Giỏi            |
| 50% - 69%  | 👍 Khá             |
| 30% - 49%  | 🙂 Trung bình      |
| < 30%      | 📚 Cần cố gắng     |

✅ Với test case mẫu `4/5 = 80%` (tương đương `40/50` điểm) thì xếp loại hợp lý là: **Giỏi ⭐**.

Gợi ý điều kiện trong code:

- Nếu `ty_le >= 90` → `"Xuất sắc 🏆"`
- Nếu `ty_le >= 70` → `"Giỏi ⭐"`
- Nếu `ty_le >= 50` → `"Khá 👍"`
- Nếu `ty_le >= 30` → `"Trung bình 🙂"`
- Còn lại → `"Cần cố gắng 📚"`

---

## 📌 Checklist tổng kết Buổi 5

| #   | Nội dung                                            | Trạng thái |
| --- | --------------------------------------------------- | ---------- |
| 1   | Biết kết hợp biến + điều kiện + hàm + vòng lặp      | ⬜         |
| 2   | Biết phân tích bài toán theo quy trình 5 bước       | ⬜         |
| 3   | Biết tách bài toán thành các hàm hợp lý             | ⬜         |
| 4   | Biết dùng kỹ thuật print debug để tìm lỗi           | ⬜         |
| 5   | Biết dùng bảng theo dõi (trace table) để hiểu logic | ⬜         |
| 6   | Biết viết chương trình có menu + vòng lặp chính     | ⬜         |
| 7   | Biết dùng biến tích lũy trong vòng lặp              | ⬜         |
| 8   | Biết validate dữ liệu đầu vào                       | ⬜         |
| 9   | Hoàn thành ít nhất 2/6 dự án mini                   | ⬜         |
| 10  | Tự tin xây dựng chương trình Python hoàn chỉnh      | ⬜         |

---

## 🏆 Lời kết — Giai đoạn Nền tảng

> 🎉 **Chúc mừng!** Nếu bạn đã hoàn thành 5 buổi học, bạn đã nắm vững **nền tảng lập trình Python**:
>
> - ✅ Biến, kiểu dữ liệu, input/output
> - ✅ Câu điều kiện if/elif/else
> - ✅ Hàm, tham số, return
> - ✅ Vòng lặp for, while, break, continue
> - ✅ Tư duy giải bài toán + tổ chức code
>
> Đây là nền tảng cực kỳ vững chắc để bạn tiến tới các chủ đề nâng cao hơn như:
>
> - **List** (danh sách) — lưu trữ nhiều dữ liệu
> - **Dictionary** (từ điển) — lưu trữ dạng key-value
> - **File I/O** — đọc/ghi file
> - **Module** — sử dụng thư viện có sẵn
>
> _"Mỗi dòng code bạn viết hôm nay là một bước tiến trên hành trình lập trình viên."_ 🐍

---

_© 2026 — Giáo trình Python | Biên soạn cho lớp học KITE_
