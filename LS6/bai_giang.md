# BÀI 6: DANH SÁCH (LIST) TRONG PYTHON

---

## Mục tiêu bài học

- Hiểu List là gì và khi nào nên dùng
- Tạo, truy cập, sửa đổi và thao tác dữ liệu trong List
- Làm quen với các phương thức phổ biến của List
- Thực hành tuần tự qua ví dụ và bài tập

---

## 1. GIỚI THIỆU VỀ LIST

**List** (danh sách) là một kiểu dữ liệu dùng để lưu trữ **nhiều giá trị trong một biến duy nhất**.

| Đặc điểm           | Mô tả                                      |
| ------------------ | ------------------------------------------ |
| Có thứ tự          | Các phần tử có vị trí cố định (index)      |
| Có thể thay đổi    | Thêm, xóa, sửa được sau khi tạo            |
| Cho phép trùng lặp | Có thể có các giá trị giống nhau           |
| Đa kiểu dữ liệu    | Chứa được số, chuỗi, boolean, list khác... |

```
List:  [ "Táo", "Cam", "Xoài", "Ổi" ]
Index:     0      1      2       3
```

---

## 2. TẠO LIST

### 2.1 Các cách tạo List

```python
# Tạo list rỗng
ds_trong = []
ds_trong2 = list()

# Tạo list với giá trị ban đầu
fruits = ["táo", "cam", "xoài"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Python", 3, True, 3.14]

# Tạo list từ range
so_chan = list(range(0, 11, 2))   # [0, 2, 4, 6, 8, 10]

# Tạo list lồng nhau (nested list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### 2.2 Kiểm tra thông tin List

```python
fruits = ["táo", "cam", "xoài", "cam"]

print(len(fruits))       # 4  — số phần tử
print(type(fruits))      # <class 'list'>
print("cam" in fruits)   # True — kiểm tra tồn tại
```

### Ví dụ 2 — Tạo danh sách học sinh

```python
# Tạo danh sách tên học sinh trong lớp
hoc_sinh = ["An", "Bình", "Chi", "Dũng", "Em"]

print("Danh sách lớp:", hoc_sinh)
print("Sĩ số:", len(hoc_sinh), "học sinh")
print("Có 'Chi' trong lớp không?", "Chi" in hoc_sinh)
```

**Kết quả:**

```
Danh sách lớp: ['An', 'Bình', 'Chi', 'Dũng', 'Em']
Sĩ số: 5 học sinh
Có 'Chi' trong lớp không? True
```

> **Bài tập 2** — Xem file `bai_tap.md`, phần **Bài tập 2**

---

## 3. TRUY CẬP DỮ LIỆU TRONG LIST

### 3.1 Truy cập theo chỉ số (Indexing)

Python đánh số từ **0** (từ đầu) hoặc **-1** (từ cuối).

```python
fruits = ["táo", "cam", "xoài", "ổi", "nho"]
#  index:   0      1      2      3     4
#  index:  -5     -4     -3     -2    -1

print(fruits[0])    # táo   — phần tử đầu tiên
print(fruits[2])    # xoài  — phần tử thứ 3
print(fruits[-1])   # nho   — phần tử cuối cùng
print(fruits[-2])   # ổi    — phần tử áp chót
```

### 3.2 Cắt danh sách (Slicing)

Cú pháp: `list[start : stop : step]`

- `start` — bắt đầu từ đây (mặc định: 0)
- `stop` — dừng trước đây (không bao gồm)
- `step` — bước nhảy (mặc định: 1)

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[1:4])    # [20, 30, 40]   — từ index 1 đến 3
print(numbers[:3])     # [10, 20, 30]   — 3 phần tử đầu
print(numbers[4:])     # [50, 60, 70]   — từ index 4 đến hết
print(numbers[::2])    # [10, 30, 50, 70] — mỗi 2 phần tử
print(numbers[::-1])   # [70, 60, 50, 40, 30, 20, 10] — đảo ngược
```

### 3.3 Truy cập List lồng nhau

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0])       # [1, 2, 3]  — hàng đầu tiên
print(matrix[1][2])    # 6          — hàng 2, cột 3
```

### Ví dụ 3 — Truy cập điểm số học sinh

```python
diem = [6.5, 7.0, 8.5, 9.0, 5.5, 10.0, 7.5]

print("Điểm đầu tiên:", diem[0])
print("Điểm cuối cùng:", diem[-1])
print("3 điểm đầu:", diem[:3])
print("Điểm từ giữa trở đi:", diem[3:])
print("Điểm cao nhất:", max(diem))
print("Điểm thấp nhất:", min(diem))
```

**Kết quả:**

```
Điểm đầu tiên: 6.5
Điểm cuối cùng: 7.5
3 điểm đầu: [6.5, 7.0, 8.5]
Điểm từ giữa trở đi: [9.0, 5.5, 10.0, 7.5]
Điểm cao nhất: 10.0
Điểm thấp nhất: 5.5
```

> **Bài tập 3** — Xem file `bai_tap.md`, phần **Bài tập 3**

---

## 4. SỬA ĐỔI DỮ LIỆU TRONG LIST

### 4.1 Thay đổi phần tử

```python
colors = ["đỏ", "xanh", "vàng"]

colors[1] = "tím"          # Thay phần tử ở index 1
print(colors)              # ['đỏ', 'tím', 'vàng']

colors[0:2] = ["trắng", "đen"]  # Thay nhiều phần tử
print(colors)              # ['trắng', 'đen', 'vàng']
```

### 4.2 Thêm phần tử

| Phương thức    | Tác dụng                     |
| -------------- | ---------------------------- |
| `append(x)`    | Thêm `x` vào **cuối** list   |
| `insert(i, x)` | Thêm `x` vào **vị trí `i`**  |
| `extend(ds)`   | Ghép danh sách `ds` vào cuối |

```python
fruits = ["táo", "cam"]

fruits.append("xoài")           # ['táo', 'cam', 'xoài']
fruits.insert(1, "ổi")          # ['táo', 'ổi', 'cam', 'xoài']
fruits.extend(["nho", "dưa"])   # ['táo', 'ổi', 'cam', 'xoài', 'nho', 'dưa']
```

### 4.3 Xóa phần tử

| Phương thức   | Tác dụng                                                |
| ------------- | ------------------------------------------------------- |
| `remove(x)`   | Xóa phần tử đầu tiên có giá trị `x`                     |
| `pop(i)`      | Xóa và **trả về** phần tử ở vị trí `i` (mặc định: cuối) |
| `del list[i]` | Xóa phần tử tại index `i`                               |
| `clear()`     | Xóa **toàn bộ** phần tử                                 |

```python
animals = ["mèo", "chó", "chim", "cá", "chó"]

animals.remove("chó")    # xóa "chó" đầu tiên  → ['mèo', 'chim', 'cá', 'chó']
removed = animals.pop()  # lấy ra phần tử cuối → removed = 'chó'
del animals[1]           # xóa index 1         → ['mèo', 'cá']
print(animals)           # ['mèo', 'cá']
```

### Ví dụ 4 — Quản lý giỏ hàng

```python
gio_hang = ["bánh mì", "sữa", "trứng"]

# Thêm sản phẩm
gio_hang.append("rau xanh")
gio_hang.insert(0, "thịt bò")   # thêm vào đầu giỏ
print("Sau khi thêm:", gio_hang)

# Xóa sản phẩm không cần
gio_hang.remove("sữa")
san_pham_lay_ra = gio_hang.pop(-1)  # lấy ra sản phẩm cuối
print("Đã bỏ:", san_pham_lay_ra)
print("Giỏ hàng còn lại:", gio_hang)
```

**Kết quả:**

```
Sau khi thêm: ['thịt bò', 'bánh mì', 'sữa', 'trứng', 'rau xanh']
Đã bỏ: rau xanh
Giỏ hàng còn lại: ['thịt bò', 'bánh mì', 'trứng']
```

> **Bài tập 4** — Xem file `bai_tap.md`, phần **Bài tập 4**

---

## 5. THAO TÁC DỮ LIỆU TRONG LIST

### 5.1 Sắp xếp và đảo ngược

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.sort()              # sắp xếp tăng dần (thay đổi list gốc)
print(numbers)              # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)  # sắp xếp giảm dần
print(numbers)              # [9, 6, 5, 4, 3, 2, 1, 1]

numbers.reverse()           # đảo ngược thứ tự hiện tại
print(numbers)              # [1, 1, 2, 3, 4, 5, 6, 9]

# sorted() — tạo list mới, không thay đổi list gốc
names = ["Cúc", "An", "Bình"]
sorted_names = sorted(names)
print(sorted_names)         # ['An', 'Bình', 'Cúc']
print(names)                # ['Cúc', 'An', 'Bình'] — không đổi
```

### 5.2 Tìm kiếm và đếm

```python
scores = [8, 6, 9, 7, 6, 10, 6]

print(scores.count(6))      # 3   — đếm số lần xuất hiện của 6
print(scores.index(9))      # 2   — vị trí đầu tiên của 9
print(sum(scores))          # 52  — tổng
print(max(scores))          # 10  — lớn nhất
print(min(scores))          # 6   — nhỏ nhất
```

### 5.3 Sao chép List

```python
original = [1, 2, 3]

# SAI: gán trực tiếp (cả hai cùng trỏ vào một vùng nhớ)
wrong_copy = original
wrong_copy.append(4)
print(original)    # [1, 2, 3, 4] — original cũng bị thay đổi!

# ĐÚNG: dùng .copy() hoặc slicing [:]
original = [1, 2, 3]
right_copy = original.copy()   # hoặc: original[:]
right_copy.append(4)
print(original)    # [1, 2, 3]   — original không đổi
```

### 5.4 List Comprehension (Tạo list nhanh)

Cú pháp: `[biểu_thức for biến in iterable if điều_kiện]`

```python
# Cách thông thường
binh_phuong = []
for i in range(1, 6):
    binh_phuong.append(i ** 2)

# Dùng List Comprehension — ngắn gọn hơn
binh_phuong = [i ** 2 for i in range(1, 6)]
print(binh_phuong)   # [1, 4, 9, 16, 25]

# Có điều kiện lọc
so_chan = [x for x in range(1, 11) if x % 2 == 0]
print(so_chan)        # [2, 4, 6, 8, 10]
```

### Ví dụ 5 — Xử lý bảng điểm lớp học

```python
diem_lop = [6.5, 8.0, 5.0, 9.5, 7.0, 4.5, 8.5, 6.0]

# Sắp xếp điểm
diem_sap_xep = sorted(diem_lop, reverse=True)
print("Xếp hạng điểm:", diem_sap_xep)

# Thống kê
print(f"Điểm TB: {sum(diem_lop)/len(diem_lop):.2f}")
print(f"Cao nhất: {max(diem_lop)} | Thấp nhất: {min(diem_lop)}")

# Lọc học sinh đạt (>= 5.0)
diem_dat = [d for d in diem_lop if d >= 5.0]
print(f"Số HS đạt: {len(diem_dat)}/{len(diem_lop)}")

# Cộng thêm 0.5 điểm thưởng cho tất cả
diem_thuong = [d + 0.5 for d in diem_lop]
print("Điểm sau thưởng:", diem_thuong)
```

**Kết quả:**

```
Xếp hạng điểm: [9.5, 8.5, 8.0, 7.0, 6.5, 6.0, 5.0, 4.5]
Điểm TB: 6.88
Cao nhất: 9.5 | Thấp nhất: 4.5
Số HS đạt: 7/8
Điểm sau thưởng: [7.0, 8.5, 5.5, 10.0, 7.5, 5.0, 9.0, 6.5]
```

> **Bài tập 5** — Xem file `bai_tap.md`, phần **Bài tập 5**

---

## 6. THỰC HÀNH TUẦN TỰ — DUYỆT QUA LIST

### 6.1 Vòng lặp for với List

```python
fruits = ["táo", "cam", "xoài"]

# Duyệt theo giá trị
for fruit in fruits:
    print("Trái cây:", fruit)

# Duyệt theo index
for i in range(len(fruits)):
    print(f"[{i}] {fruits[i]}")

# Duyệt cả index và giá trị — dùng enumerate()
for i, fruit in enumerate(fruits):
    print(f"STT {i+1}: {fruit}")
```

### 6.2 Xử lý tuần tự với điều kiện

```python
diem = [7, 4, 9, 5, 3, 8, 6]
dau = 0
truot = 0

for d in diem:
    if d >= 5:
        dau += 1
        print(f"Điểm {d} — ĐẠT")
    else:
        truot += 1
        print(f"Điểm {d} — TRƯỢT")

print(f"\nTổng kết: {dau} đạt, {truot} trượt")
```

### Ví dụ 6 — Tính tiền giỏ hàng

```python
gio_hang = [
    ("Bánh mì", 15000, 2),
    ("Sữa tươi", 35000, 3),
    ("Trứng gà", 5000, 10),
]

tong_tien = 0
print("=" * 35)
print(f"{'Sản phẩm':<12} {'Đơn giá':>8} {'SL':>4} {'Thành tiền':>10}")
print("=" * 35)

for ten, don_gia, so_luong in gio_hang:
    thanh_tien = don_gia * so_luong
    tong_tien += thanh_tien
    print(f"{ten:<12} {don_gia:>8,} {so_luong:>4} {thanh_tien:>10,}")

print("=" * 35)
print(f"{'TỔNG CỘNG':>24} {tong_tien:>10,} đ")
```

**Kết quả:**

```
===================================
Sản phẩm      Đơn giá   SL Thành tiền
===================================
Bánh mì         15,000    2     30,000
Sữa tươi        35,000    3    105,000
Trứng gà         5,000   10     50,000
===================================
                   TỔNG CỘNG    185,000 đ
```

> **Bài tập 6** — Xem file `bai_tap.md`, phần **Bài tập 6**

---

## BẢNG TỔNG KẾT CÁC PHƯƠNG THỨC LIST

| Phương thức / Hàm     | Mô tả                  | Thay đổi list gốc? |
| --------------------- | ---------------------- | :----------------: |
| `len(ds)`             | Số phần tử             |       Không        |
| `ds.append(x)`        | Thêm vào cuối          |         Có         |
| `ds.insert(i, x)`     | Thêm vào vị trí i      |         Có         |
| `ds.extend(ds2)`      | Ghép danh sách         |         Có         |
| `ds.remove(x)`        | Xóa giá trị x đầu tiên |         Có         |
| `ds.pop(i)`           | Xóa & trả về phần tử   |         Có         |
| `ds.clear()`          | Xóa toàn bộ            |         Có         |
| `ds.sort()`           | Sắp xếp tại chỗ        |         Có         |
| `sorted(ds)`          | Trả về list đã sắp xếp |       Không        |
| `ds.reverse()`        | Đảo ngược tại chỗ      |         Có         |
| `ds.count(x)`         | Đếm số lần x xuất hiện |       Không        |
| `ds.index(x)`         | Vị trí đầu tiên của x  |       Không        |
| `ds.copy()`           | Sao chép list          |       Không        |
| `sum(ds)`             | Tổng các phần tử       |       Không        |
| `max(ds)` / `min(ds)` | Lớn nhất / nhỏ nhất    |       Không        |

---
