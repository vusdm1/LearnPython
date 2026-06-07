# BÀI 7: VÒNG LẶP VỚI LIST — XỬ LÝ DỮ LIỆU NÂNG CAO

---

## Mục tiêu bài học

- Hiểu cách kết hợp vòng lặp và List để xử lý dữ liệu phức tạp
- Làm quen với vòng lặp lồng nhau (nested loops)
- Thực hành tính toán, lọc, chuyển đổi dữ liệu
- Xây dựng báo cáo và thống kê từ danh sách

---

## 1. VÒNG LẶP LỒNG NHAU VỚI LIST

### 1.1 Khái niệm vòng lặp lồng

Khi xử lý dữ liệu phức tạp, ta thường cần duyệt **lồng nhau** (nested loops) để truy cập các phần tử trong nhiều cấp độ.

```python
# Danh sách lồng (các danh sách con)
diem_lop = [
    [7.5, 8.0, 9.0],    # Học sinh An: Toán, Lý, Hóa
    [6.0, 5.0, 4.5],    # Học sinh Bình
    [9.5, 8.5, 9.0],    # Học sinh Chi
]

# Duyệt vòng lặp lồng nhau
for i in range(len(diem_lop)):
    print(f"Học sinh {i+1}:")
    for j in range(len(diem_lop[i])):
        print(f"  Môn {j+1}: {diem_lop[i][j]}")
```

### 1.2 Cách viết ngắn gọn hơn

```python
for hoc_sinh in diem_lop:
    print(f"Điểm: {hoc_sinh}")
    for diem in hoc_sinh:
        print(f"  - {diem}")
```

---

## 2. XỬ LÝ DỮ LIỆU VỚI TỪNG PHẦN TỬ

### 2.1 Tính tổng và trung bình

```python
diem = [8.5, 7.0, 9.0, 6.5, 8.0]

tong = 0
for d in diem:
    tong += d

trung_binh = tong / len(diem)
print(f"Tổng: {tong} | Trung bình: {trung_binh:.2f}")

# Hoặc dùng hàm built-in
print(f"Tổng: {sum(diem)} | Trung bình: {sum(diem)/len(diem):.2f}")
```

### 2.2 Lọc và xây dựng list mới

```python
diem = [6.5, 3.0, 8.0, 5.5, 9.0, 4.0, 7.5]

# Cách 1: Dùng vòng lặp
diem_dat = []
for d in diem:
    if d >= 5.0:
        diem_dat.append(d)

# Cách 2: Dùng List Comprehension (ngắn gọn hơn)
diem_dat = [d for d in diem if d >= 5.0]

print(f"Điểm đạt: {diem_dat}")
print(f"Học sinh đạt: {len(diem_dat)}/{len(diem)}")
```

### 2.3 Chuyển đổi dữ liệu

```python
# Chuyển celsius sang fahrenheit
nhiet_do_c = [20, 25, 30, 35]

# Cách 1: Vòng lặp
nhiet_do_f = []
for c in nhiet_do_c:
    f = (c * 9/5) + 32
    nhiet_do_f.append(f)

# Cách 2: List Comprehension
nhiet_do_f = [(c * 9/5) + 32 for c in nhiet_do_c]

print(f"°C: {nhiet_do_c}")
print(f"°F: {nhiet_do_f}")
```

---

## 3. XỬ LÝ DANH SÁCH TỪ ĐIỂN (LIST CỦA TUPLE)

### 3.1 Danh sách Tuple

```python
# Danh sách sản phẩm: (tên, giá, số lượng)
san_pham = [
    ("Bánh mì", 12000, 5),
    ("Sữa tươi", 25000, 3),
    ("Trứng gà", 4000, 10),
]

# Tính thành tiền từng sản phẩm
tong_tien = 0
for ten, gia, so_luong in san_pham:
    thanh_tien = gia * so_luong
    tong_tien += thanh_tien
    print(f"{ten:<12} {gia:>8,}₫ × {so_luong:>2} = {thanh_tien:>10,}₫")

print(f"\nTổng cộng: {tong_tien:,}₫")
```

**Kết quả:**

```
Bánh mì              12,000₫ ×  5 =     60,000₫
Sữa tươi             25,000₫ ×  3 =     75,000₫
Trứng gà              4,000₫ × 10 =     40,000₫

Tổng cộng: 175,000₫
```

---

## 4. TÌM KIẾM VÀ SO SÁNH TRONG DANH SÁCH

### 4.1 Tìm vị trí phần tử

```python
hoc_sinh = ["An", "Bình", "Chi", "Dũng", "An"]

# Tìm index đầu tiên
if "Chi" in hoc_sinh:
    vi_tri = hoc_sinh.index("Chi")
    print(f"Chi ở vị trí: {vi_tri}")

# Tìm tất cả vị trí
vi_tri_an = []
for i in range(len(hoc_sinh)):
    if hoc_sinh[i] == "An":
        vi_tri_an.append(i)

print(f"Vị trí 'An': {vi_tri_an}")
```

### 4.2 Tìm giá trị lớn nhất / nhỏ nhất kèm vị trí

```python
diem = [6.5, 9.0, 7.5, 8.0, 5.0, 9.0]

# Tìm điểm cao nhất
diem_max = max(diem)
vi_tri_max = diem.index(diem_max)
print(f"Điểm cao nhất: {diem_max} (vị trí {vi_tri_max})")

# Tìm tất cả vị trí có điểm cao nhất
vi_tri_cao_nhat = [i for i in range(len(diem)) if diem[i] == diem_max]
print(f"Vị trí điểm cao nhất: {vi_tri_cao_nhat}")
```

---

## 5. ĐẾM VÀ THỐNG KÊ

### 5.1 Đếm các giá trị

```python
diem = [5, 6, 7, 5, 8, 5, 9, 6, 7]

# Đếm từng giá trị
dem_5 = diem.count(5)
dem_6 = diem.count(6)
print(f"Số lần 5 xuất hiện: {dem_5}")
print(f"Số lần 6 xuất hiện: {dem_6}")

# Đếm theo điều kiện (danh sách kết quả)
so_dau = len([d for d in diem if d >= 5])
so_truot = len([d for d in diem if d < 5])
print(f"Đạt: {so_dau} | Trượt: {so_truot}")
```

### 5.2 Tạo dict thống kê

```python
diem = [5, 6, 7, 5, 8, 5, 9, 6, 7]

# Tạo dict thống kê (nâng cao)
thong_ke = {}
for d in diem:
    if d in thong_ke:
        thong_ke[d] += 1
    else:
        thong_ke[d] = 1

print(f"Thống kê: {thong_ke}")  # {5: 3, 6: 2, 7: 2, 8: 1, 9: 1}
```

---

## 6. VÍ DỤ THỰC TẾ — XỬ LÝ BẢNG ĐIỂM PHỨC TẠP

### 6.1 Xử lý danh sách học sinh với nhiều môn

```python
# Danh sách: [Tên, [Toán, Lý, Hóa]]
hoc_sinh = [
    ["An",    [8.5, 7.5, 9.0]],
    ["Bình",  [6.0, 5.0, 4.5]],
    ["Chi",   [9.5, 8.5, 9.0]],
    ["Dũng",  [5.5, 6.0, 5.0]],
]

print("=" * 50)
print(f"{'Tên':<10} {'Toán':>7} {'Lý':>7} {'Hóa':>7} {'ĐTB':>7} {'Xếp loại':>10}")
print("=" * 50)

for ten, diem_3_mon in hoc_sinh:
    diem_tb = sum(diem_3_mon) / len(diem_3_mon)
    
    if diem_tb >= 8.0:
        xep_loai = "Giỏi"
    elif diem_tb >= 6.5:
        xep_loai = "Khá"
    elif diem_tb >= 5.0:
        xep_loai = "TB"
    else:
        xep_loai = "Yếu"
    
    print(f"{ten:<10} {diem_3_mon[0]:>7.1f} {diem_3_mon[1]:>7.1f} {diem_3_mon[2]:>7.1f} {diem_tb:>7.2f} {xep_loai:>10}")

print("=" * 50)
```

**Kết quả:**

```
==================================================
Tên             Toán      Lý      Hóa      ĐTB   Xếp loại
==================================================
An            8.5       7.5       9.0     8.33       Giỏi
Bình          6.0       5.0       4.5     5.17         TB
Chi           9.5       8.5       9.0     9.00       Giỏi
Dũng          5.5       6.0       5.0     5.50         TB
==================================================
```

---

## 7. LUYỆN TẬP THEO CẤP ĐỘ

### Cấp độ 1: Duyệt và in

```python
# Bài: In các phần tử lẻ từ danh sách
so = [1, 2, 3, 4, 5, 6, 7, 8]
for x in so:
    if x % 2 != 0:
        print(x, end=" ")  # 1 3 5 7
```

### Cấp độ 2: Xử lý và tích lũy

```python
# Bài: Tính tổng các số dương
so = [-5, 3, -2, 8, -1, 4]
tong = 0
for x in so:
    if x > 0:
        tong += x
print(tong)  # 15
```

### Cấp độ 3: Lọc và chuyển đổi

```python
# Bài: Tạo danh sách bình phương của số lẻ
so = [1, 2, 3, 4, 5, 6, 7, 8]
binh_phuong_le = []
for x in so:
    if x % 2 != 0:
        binh_phuong_le.append(x ** 2)
print(binh_phuong_le)  # [1, 9, 25, 49]

# Hoặc dùng List Comprehension:
binh_phuong_le = [x ** 2 for x in so if x % 2 != 0]
```

### Cấp độ 4: Duyệt lồng và tích lũy

```python
# Bài: Tính tổng tất cả phần tử trong list lồng
ma_tran = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tong = 0
for hang in ma_tran:
    for phan_tu in hang:
        tong += phan_tu
print(tong)  # 45
```

### Cấp độ 5: Xử lý phức tạp với điều kiện

```python
# Bài: Tạo ma trận các số chẵn từ 1 đến 20, chia thành 2 hàng
so_chan = [x for x in range(1, 21) if x % 2 == 0]
ma_tran = []
for i in range(0, len(so_chan), 5):
    ma_tran.append(so_chan[i:i+5])
print(ma_tran)
# [[2, 4, 6, 8, 10], [12, 14, 16, 18, 20]]
```

> **Bài tập** — Xem file `bai_tap.md`

---

## BẢNG TỔNG KẾT

| Kỹ thuật               | Mô tả                              |
|------------------------|-----------------------------------|
| Vòng lặp lồng          | Duyệt trong list có chứa list      |
| Accumulation           | Tích lũy giá trị trong vòng lặp    |
| Filtering              | Lọc phần tử theo điều kiện         |
| Transformation         | Chuyển đổi từng phần tử            |
| Unpacking              | Gán giá trị từ tuple vào biến      |
| List Comprehension     | Tạo list mới từ list hiện tại      |
| Searching              | Tìm vị trí, max, min               |
| Counting               | Đếm số lần xuất hiện               |

---
