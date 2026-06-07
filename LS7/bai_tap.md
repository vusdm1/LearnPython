# BÀI TẬP — VÒNG LẶP VỚI LIST

---

## Bài tập 1 — Duyệt và in dữ liệu (Cấp độ 1)

### Bài 1.1: In danh sách với chỉ số

**Yêu cầu:** Cho danh sách tên học sinh. In ra theo định dạng "STT: Tên"

**Input:**
```python
hoc_sinh = ["An", "Bình", "Chi", "Dũng", "Em"]
```

**Output mong đợi:**
```
1: An
2: Bình
3: Chi
4: Dũng
5: Em
```

---

### Bài 1.2: In những học sinh đạt

**Yêu cầu:** Cho danh sách điểm. In ra những học sinh đạt (điểm ≥ 5.0)

**Input:**
```python
diem = [7.5, 4.0, 8.0, 5.5, 3.0, 9.0, 4.5]
```

**Output mong đợi:**
```
Điểm đạt: 7.5
Điểm đạt: 8.0
Điểm đạt: 5.5
Điểm đạt: 9.0
```

---

### Bài 1.3: Bảng giá sản phẩm

**Yêu cầu:** In danh sách sản phẩm dưới dạng bảng

**Input:**
```python
san_pham = [("Bánh mì", 12000), ("Sữa", 25000), ("Trứng", 4000), ("Dưa hành", 8000)]
```

**Output mong đợi:**
```
=========================
Sản phẩm       Giá (đ)
=========================
Bánh mì        12,000
Sữa            25,000
Trứng           4,000
Dưa hành        8,000
=========================
```

---

### Bài 1.4: In các số lẻ

**Yêu cầu:** In ra các số lẻ từ danh sách

**Input:**
```python
so = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Output mong đợi:**
```
Các số lẻ: 1 3 5 7 9
```

---

## Bài tập 2 — Tính toán và tích lũy (Cấp độ 2)

### Bài 2.1: Thống kê điểm lớp

**Yêu cầu:** Tính tổng, trung bình, max, min của danh sách điểm

**Input:**
```python
diem = [7.5, 8.0, 6.5, 5.0, 9.0]
```

**Output mong đợi:**
```
Tổng: 36.0
Trung bình: 7.2
Điểm cao nhất: 9.0
Điểm thấp nhất: 5.0
```

---

### Bài 2.2: Đếm học sinh đạt/trượt

**Yêu cầu:** Đếm bao nhiêu học sinh đạt (≥ 5.0), bao nhiêu trượt, tính tỉ lệ

**Input:**
```python
diem = [7.5, 4.0, 8.0, 5.5, 3.0, 9.0, 4.5, 5.0, 6.5]
```

**Output mong đợi:**
```
Tổng học sinh: 9
Học sinh đạt: 6 (66.67%)
Học sinh trượt: 3 (33.33%)
```

---

### Bài 2.3: Tính tổng tiền giỏ hàng

**Yêu cầu:** Tính thành tiền từng sản phẩm và tổng cộng

**Input:**
```python
gio_hang = [
    ("Bánh mì", 12000, 2),
    ("Sữa", 25000, 3),
    ("Trứng", 4000, 6),
]
```

**Output mong đợi:**
```
Bánh mì     12,000 × 2 =  24,000 đ
Sữa         25,000 × 3 =  75,000 đ
Trứng        4,000 × 6 =  24,000 đ
=====================================
Tổng cộng             123,000 đ
```

---

### Bài 2.4: Tính độ dài tổng cộng

**Yêu cầu:** Tính tổng độ dài của tất cả chuỗi trong list

**Input:**
```python
words = ["Hello", "World", "Python", "Programming"]
```

**Output mong đợi:**
```
Tổng độ dài: 28
Trung bình độ dài: 7.0
```

---

## Bài tập 3 — Lọc và chuyển đổi dữ liệu (Cấp độ 3)

### Bài 3.1: Lọc điểm đạt

**Yêu cầu:** Tạo danh sách riêng gồm điểm đạt và điểm trượt

**Input:**
```python
diem = [7.5, 4.0, 8.0, 5.5, 3.0, 9.0, 4.5]
```

**Output mong đợi:**
```
Điểm đạt: [7.5, 8.0, 5.5, 9.0]
Điểm trượt: [4.0, 3.0, 4.5]
```

---

### Bài 3.2: Xếp loại học sinh

**Yêu cầu:** Chuyển điểm số sang xếp loại (>= 8: "Giỏi", >= 6.5: "Khá", >= 5: "TB", < 5: "Yếu")

**Input:**
```python
diem = [7.5, 4.0, 8.0, 5.5, 3.0, 9.0, 4.5]
```

**Output mong đợi:**
```
7.5 → Khá
4.0 → Yếu
8.0 → Giỏi
5.5 → TB
3.0 → Yếu
9.0 → Giỏi
4.5 → Yếu

Danh sách xếp loại: ['Khá', 'Yếu', 'Giỏi', 'TB', 'Yếu', 'Giỏi', 'Yếu']
```

---

### Bài 3.3: Tăng điểm bổ sung

**Yêu cầu:** Tăng 0.5 điểm cho tất cả (nếu điểm < 5.0 thì tăng để thành 5.0 tối đa)

**Input:**
```python
diem = [6.5, 7.0, 8.5, 4.5, 4.0, 5.0]
```

**Output mong đợi:**
```
Điểm gốc:      [6.5, 7.0, 8.5, 4.5, 4.0, 5.0]
Điểm tăng:     [7.0, 7.5, 9.0, 5.0, 4.5, 5.5]
```

---

### Bài 3.4: Chuyển đổi nhiệt độ

**Yêu cầu:** Chuyển danh sách nhiệt độ Celsius sang Fahrenheit (F = C × 9/5 + 32)

**Input:**
```python
celsius = [0, 10, 20, 30, 37, 100]
```

**Output mong đợi:**
```
°C → °F
0  → 32.0
10 → 50.0
20 → 68.0
30 → 86.0
37 → 98.6
100 → 212.0
```

---

### Bài 3.5: Lấy tên học sinh cần phụ đạo

**Yêu cầu:** Tạo danh sách tên học sinh có điểm < 5.0

**Input:**
```python
hoc_sinh = ["An", "Bình", "Chi", "Dũng", "Em", "Phong"]
diem = [7.5, 4.0, 8.0, 5.5, 3.0, 9.0]
```

**Output mong đợi:**
```
Học sinh cần phụ đạo: ['Bình', 'Em']
```

---

## Bài tập 4 — Duyệt lồng (Cấp độ 4)

### Bài 4.1: Ma trận — Tính tổng tất cả phần tử

**Yêu cầu:** Duyệt ma trận 2 chiều và tính tổng

**Input:**
```python
ma_tran = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

**Output mong đợi:**
```
Ma trận:
1 2 3
4 5 6
7 8 9

Tổng tất cả: 45
Trung bình: 5.0
```

---

### Bài 4.2: Tính điểm TB của từng học sinh

**Yêu cầu:** Mỗi hàng là điểm 3 môn của một học sinh, tính TB mỗi hàng

**Input:**
```python
diem_3_mon = [
    [8.5, 7.5, 9.0],    # An
    [6.0, 5.0, 4.5],    # Bình
    [9.5, 8.5, 9.0],    # Chi
]
```

**Output mong đợi:**
```
An:    8.5 + 7.5 + 9.0 = 8.33
Bình:  6.0 + 5.0 + 4.5 = 5.17
Chi:   9.5 + 8.5 + 9.0 = 9.00
```

---

### Bài 4.3: Tính tổng từng môn

**Yêu cầu:** Tính tổng điểm từng cột (từng môn)

**Input:**
```python
diem_3_mon = [
    [8.5, 7.5, 9.0],
    [6.0, 5.0, 4.5],
    [9.5, 8.5, 9.0],
]
# Toán, Lý, Hóa
```

**Output mong đợi:**
```
Tổng Toán: 24.0
Tổng Lý: 21.0
Tổng Hóa: 22.5
```

---

### Bài 4.4: Kiểm tra ma trận vuông

**Yêu cầu:** Kiểm tra các ma trận có phải vuông (số hàng = số cột) không

**Input:**
```python
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2], [3, 4]]
m3 = [[1, 2, 3], [4, 5, 6]]
```

**Output mong đợi:**
```
Ma trận 1 (3×3): Là ma trận vuông
Ma trận 2 (2×2): Là ma trận vuông
Ma trận 3 (2×3): Không phải ma trận vuông
```

---

## Bài tập 5 — Xử lý phức tạp với điều kiện (Cấp độ 5)

### Bài 5.1: Bảng báo cáo điểm học sinh

**Yêu cầu:** Tạo bảng báo cáo đầy đủ với điểm TB và xếp loại

**Input:**
```python
hoc_sinh = [
    ["An",    [8.5, 7.5, 9.0]],
    ["Bình",  [6.0, 5.0, 4.5]],
    ["Chi",   [9.5, 8.5, 9.0]],
    ["Dũng",  [5.5, 6.0, 5.0]],
    ["Em",    [7.0, 7.5, 8.0]],
]
```

**Output mong đợi:**
```
================================================
Tên      Toán    Lý    Hóa    ĐTB   Xếp loại
================================================
An        8.5    7.5    9.0   8.33   Giỏi
Bình      6.0    5.0    4.5   5.17   TB
Chi       9.5    8.5    9.0   9.00   Giỏi
Dũng      5.5    6.0    5.0   5.50   TB
Em        7.0    7.5    8.0   7.50   Khá
================================================

Thống kê xếp loại:
- Giỏi: 2 học sinh (An, Chi)
- Khá: 1 học sinh (Em)
- TB: 2 học sinh (Bình, Dũng)
- Yếu: 0 học sinh
```

---

### Bài 5.2: Báo cáo bán hàng

**Yêu cầu:** Thống kê doanh thu, sản phẩm bán chạy, theo loại

**Input:**
```python
ban_hang = [
    ["Bánh mì", "Tinh tuý", 15000, 10],
    ["Sữa", "Sữa tươi", 25000, 8],
    ["Trứng", "Protein", 4000, 50],
    ["Rau muống", "Rau xanh", 8000, 15],
    ["Cá hộp", "Tinh tuý", 35000, 5],
]
```

**Output mong đợi:**
```
========================================
Sản phẩm    Loại       Giá    SL  Doanh thu
========================================
Bánh mì     Tinh tuý   15000  10  150,000 đ
Sữa         Sữa tươi   25000   8  200,000 đ
Trứng       Protein     4000  50  200,000 đ
Rau muống   Rau xanh    8000  15  120,000 đ
Cá hộp      Tinh tuý   35000   5  175,000 đ
========================================
Tổng doanh thu: 845,000 đ

Thống kê theo loại:
- Tinh tuý: 325,000 đ (3 sản phẩm)
- Sữa tươi: 200,000 đ (1 sản phẩm)
- Protein: 200,000 đ (1 sản phẩm)
- Rau xanh: 120,000 đ (1 sản phẩm)

Sản phẩm bán chạy: Trứng (50 cái)
Sản phẩm doanh thu cao nhất: Trứng (200,000 đ)
```

---

### Bài 5.3: Phân tích thống kê điểm lớp

**Yêu cầu:** Phân tích chi tiết về phân bố điểm

**Input:**
```python
diem = [7.5, 4.0, 8.0, 5.5, 3.0, 9.0, 4.5, 6.0, 7.0, 8.5, 5.5, 6.5, 8.5, 3.5, 9.5]
```

**Output mong đợi:**
```
=== PHÂN TÍCH ĐIỂM LỚP HỌC ===
Tổng học sinh: 15

Thống kê cơ bản:
- Min: 3.0
- Max: 9.5
- Trung bình: 6.47

Phân loại theo điểm:
- Yếu (< 5.0):     4 HS (26.67%) ****
- TB (5.0-6.9):    5 HS (33.33%) *****
- Khá (7.0-7.9):   3 HS (20.00%) ***
- Giỏi (>= 8.0):   3 HS (20.00%) ***

Số HS cần phụ đạo (< 6.0): 4
Danh sách: [4.0, 3.0, 4.5, 3.5]
```

---

### Bài 5.4: Sắp xếp và xếp hạng

**Yêu cầu:** Xếp hạng học sinh theo điểm TB từ cao đến thấp

**Input:**
```python
hoc_sinh = [
    ["An",    [8.5, 7.5, 9.0]],
    ["Bình",  [6.0, 5.0, 4.5]],
    ["Chi",   [9.5, 8.5, 9.0]],
    ["Dũng",  [5.5, 6.0, 5.0]],
    ["Em",    [7.0, 7.5, 8.0]],
]
```

**Output mong đợi:**
```
XẾP HẠNG THEO ĐIỂM TRUNG BÌNH

1. Chi  — ĐTB: 9.00 (Giỏi)
2. An   — ĐTB: 8.33 (Giỏi)
3. Em   — ĐTB: 7.50 (Khá)
4. Dũng — ĐTB: 5.50 (TB)
5. Bình — ĐTB: 5.17 (TB)
```

---

### Bài 5.5: Cập nhật danh sách động

**Yêu cầu:** Thêm/xóa học sinh và cập nhật báo cáo

**Input (ban đầu):**
```python
hoc_sinh = ["An", "Bình", "Chi"]
diem = [8.5, 6.0, 9.5]

# Thêm: Dũng — 5.5
# Thêm: Em — 7.5
# Xóa: Bình
```

**Output mong đợi:**
```
=== DANH SÁCH BAN ĐẦU ===
An     8.5
Bình   6.0
Chi    9.5

=== THÊM DŨNG ===
An     8.5
Bình   6.0
Chi    9.5
Dũng   5.5

=== THÊM EM ===
An     8.5
Bình   6.0
Chi    9.5
Dũng   5.5
Em     7.5

=== XÓA BÌNH ===
An     8.5
Chi    9.5
Dũng   5.5
Em     7.5

Thống kê cuối cùng:
- Tổng HS: 4
- ĐTB: 7.75
- Cao nhất: 9.5
- Thấp nhất: 5.5
```

---

## BẢNG KIỂM TRA KỸ NĂNG

| Bài tập | Cấp độ | Kỹ năng chính                | Số bài |
|---------|--------|------------------------------|--------|
| 1       | 1      | Duyệt, in dữ liệu            | 4      |
| 2       | 2      | Tính toán, tích lũy          | 4      |
| 3       | 3      | Lọc, chuyển đổi              | 5      |
| 4       | 4      | Vòng lặp lồng                | 4      |
| 5       | 5      | Xử lý phức tạp, thống kê     | 5      |
| **Tổng**|        |                              | **22** |

---
