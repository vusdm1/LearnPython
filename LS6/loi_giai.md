# LỜI GIẢI — DANH SÁCH (LIST)

> Bài tập tại `bai_tap.md` | Bài giảng tại `bai_giang.md`

---

## Lời giải Bài tập 2 — Tạo List

```python
# 1. Tạo list môn học
mon_hoc = ["Toán", "Lý", "Hóa", "Văn", "Thể dục"]

# 2. Tạo list số nguyên tố
so_nguyen_to = [2, 3, 5, 7, 11, 13, 17, 19]

# 3. Tạo list ngày trong tuần
tuan = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]

# 4. In thông tin
print("Số môn học:", len(mon_hoc))
print("Có môn Toán không?", "Toán" in mon_hoc)
print("Môn đầu tiên:", mon_hoc[0])
print("Môn cuối cùng:", mon_hoc[-1])
```

**Kết quả:**
```
Số môn học: 5
Có môn Toán không? True
Môn đầu tiên: Toán
Môn cuối cùng: Thể dục
```

---

## Lời giải Bài tập 3 — Truy cập dữ liệu

```python
nhiet_do = [28, 31, 29, 33, 27, 35, 30]

# 1. Nhiệt độ thứ Tư (index 2)
print(f"Nhiệt độ thứ Tư: {nhiet_do[2]}°C")

# 2. Cuối tuần (Thứ 7 = index 5, Chủ Nhật = index 6)
print("Cuối tuần:", nhiet_do[5:])

# 3. Đầu tuần (index 0, 1, 2)
print("Đầu tuần:", nhiet_do[:3])

# 4. Đảo ngược
print("Ngược lại:", nhiet_do[::-1])

# 5. Nóng nhất và mát nhất
print(f"Nóng nhất: {max(nhiet_do)}°C | Mát nhất: {min(nhiet_do)}°C")
```

**Kết quả:**
```
Nhiệt độ thứ Tư: 29°C
Cuối tuần: [35, 30]
Đầu tuần: [28, 31, 29]
Ngược lại: [30, 35, 27, 33, 29, 31, 28]
Nóng nhất: 35°C | Mát nhất: 27°C
```

---

## Lời giải Bài tập 4 — Sửa đổi dữ liệu

```python
thanh_vien = ["An", "Bình", "Chi", "Dũng"]
print("Ban đầu:   ", thanh_vien)

# 1. Thêm "Em" vào cuối
thanh_vien.append("Em")
print("Sau bước 1:", thanh_vien)

# 2. Thêm "Phong" vào đầu (index 0)
thanh_vien.insert(0, "Phong")
print("Sau bước 2:", thanh_vien)

# 3. Ghép thêm list mới
thanh_vien.extend(["Quỳnh", "Rồng"])
print("Sau bước 3:", thanh_vien)

# 4. Xóa "Chi"
thanh_vien.remove("Chi")
print("Sau bước 4:", thanh_vien)

# 5. Lấy ra thành viên cuối
nguoi_roi = thanh_vien.pop()
print("Người rời CLB:", nguoi_roi)
print("Sau bước 5:", thanh_vien)

# 6. Thay "Bình" bằng "Bình Minh"
vi_tri_binh = thanh_vien.index("Bình")
thanh_vien[vi_tri_binh] = "Bình Minh"
print("Sau bước 6:", thanh_vien)
```

**Kết quả:**
```
Ban đầu:    ['An', 'Bình', 'Chi', 'Dũng']
Sau bước 1: ['An', 'Bình', 'Chi', 'Dũng', 'Em']
Sau bước 2: ['Phong', 'An', 'Bình', 'Chi', 'Dũng', 'Em']
Sau bước 3: ['Phong', 'An', 'Bình', 'Chi', 'Dũng', 'Em', 'Quỳnh', 'Rồng']
Sau bước 4: ['Phong', 'An', 'Bình', 'Dũng', 'Em', 'Quỳnh', 'Rồng']
Người rời CLB: Rồng
Sau bước 5: ['Phong', 'An', 'Bình', 'Dũng', 'Em', 'Quỳnh']
Sau bước 6: ['Phong', 'An', 'Bình Minh', 'Dũng', 'Em', 'Quỳnh']
```

---

## Lời giải Bài tập 5 — Thao tác dữ liệu

```python
diem_toan = [7.5, 4.0, 9.0, 6.5, 8.0, 3.5, 7.0, 5.5, 9.5, 6.0]

# 1. Sắp xếp từ cao đến thấp (không thay đổi list gốc)
diem_sap_xep = sorted(diem_toan, reverse=True)
print("Xếp hạng điểm:", diem_sap_xep)

# 2. Điểm trung bình
diem_tb = sum(diem_toan) / len(diem_toan)
print(f"Điểm trung bình: {diem_tb:.2f}")

# 3. Lọc điểm đạt (>= 5.0)
diem_dat = [d for d in diem_toan if d >= 5.0]
print("Điểm đạt:", diem_dat)

# 4. Xếp loại bằng List Comprehension
def xep_loai(d):
    if d >= 8.0:
        return "Giỏi"
    elif d >= 6.5:
        return "Khá"
    elif d >= 5.0:
        return "TB"
    else:
        return "Yếu"

loai = [xep_loai(d) for d in diem_toan]
print("Xếp loại:", loai)

# 5. Đếm học sinh Giỏi
so_gioi = loai.count("Giỏi")
print("Số học sinh Giỏi:", so_gioi)
```

**Kết quả:**
```
Xếp hạng điểm: [9.5, 9.0, 8.0, 7.5, 7.0, 6.5, 6.0, 5.5, 4.0, 3.5]
Điểm trung bình: 6.65
Điểm đạt: [7.5, 9.0, 6.5, 8.0, 7.0, 5.5, 9.5, 6.0]
Xếp loại: ['Khá', 'Yếu', 'Giỏi', 'Khá', 'Giỏi', 'Yếu', 'Khá', 'TB', 'Giỏi', 'TB']
Số học sinh Giỏi: 3
```

---

## Lời giải Bài tập 6 — Thực hành tuần tự

```python
lop_hoc = [
    ["An",    8.0, 7.5, 9.0],
    ["Bình",  6.0, 5.0, 4.5],
    ["Chi",   9.5, 8.5, 9.0],
    ["Dũng",  5.5, 6.0, 5.0],
    ["Em",    7.0, 7.5, 8.0],
]

def xep_loai(dtb):
    if dtb >= 8.0:   return "Giỏi"
    elif dtb >= 6.5: return "Khá"
    elif dtb >= 5.0: return "Trung Bình"
    else:            return "Yếu"

dem_loai = {"Giỏi": 0, "Khá": 0, "Trung Bình": 0, "Yếu": 0}

print("=" * 53)
print(f" {'Tên':<8} {'Toán':>5} {'Lý':>5} {'Hóa':>5}  {'ĐTB':>5}  {'Xếp loại'}")
print("=" * 53)

for hs in lop_hoc:
    ten = hs[0]
    toan, ly, hoa = hs[1], hs[2], hs[3]
    dtb = round((toan + ly + hoa) / 3, 2)
    loai = xep_loai(dtb)
    dem_loai[loai] += 1
    print(f" {ten:<8} {toan:>5.1f} {ly:>5.1f} {hoa:>5.1f}  {dtb:>5.2f}  {loai}")

print("=" * 53)
print(f"Lớp có {dem_loai['Giỏi']} HS Giỏi, {dem_loai['Khá']} HS Khá, "
      f"{dem_loai['Trung Bình']} HS Trung Bình, {dem_loai['Yếu']} HS Yếu")
```

**Kết quả:**
```
=====================================================
 Tên      Toán    Lý   Hóa    ĐTB  Xếp loại
=====================================================
 An         8.0   7.5   9.0   8.17  Giỏi
 Bình       6.0   5.0   4.5   5.17  Trung Bình
 Chi        9.5   8.5   9.0   9.00  Giỏi
 Dũng       5.5   6.0   5.0   5.50  Trung Bình
 Em         7.0   7.5   8.0   7.50  Khá
=====================================================
Lớp có 2 HS Giỏi, 1 HS Khá, 2 HS Trung Bình, 0 HS Yếu
```

---

## Lời giải Bài tập LỚN

```python
# ── Dữ liệu ban đầu ──────────────────────────────────────
hoc_sinh = ["An", "Bình", "Chi", "Dũng", "Em", "Phong"]
diem_van  = [7.5, 8.0, 6.5, 5.0, 9.0, 4.5]
diem_toan = [8.5, 6.0, 9.0, 7.0, 8.0, 5.5]
diem_anh  = [6.0, 7.5, 8.5, 6.5, 7.0, 6.0]

# ── Hàm tiện ích ─────────────────────────────────────────
def xep_loai(dtb):
    if dtb >= 8.0:   return "Giỏi"
    elif dtb >= 6.5: return "Khá"
    elif dtb >= 5.0: return "Trung Bình"
    else:            return "Yếu"

# ── PHẦN 3: Thêm Quỳnh, xóa Phong TRƯỚC khi tính ────────

# 9. Xóa Phong
idx_phong = hoc_sinh.index("Phong")
hoc_sinh.pop(idx_phong)
diem_van.pop(idx_phong)
diem_toan.pop(idx_phong)
diem_anh.pop(idx_phong)

# 8. Thêm Quỳnh
hoc_sinh.append("Quỳnh")
diem_van.append(9.0)
diem_toan.append(9.5)
diem_anh.append(8.5)

# ── PHẦN 1: Thống kê cơ bản ──────────────────────────────

# Tính điểm trung bình từng học sinh
diem_tb = [
    round((v + t + a) / 3, 2)
    for v, t, a in zip(diem_van, diem_toan, diem_anh)
]

# Học sinh cao nhất / thấp nhất
max_dtb = max(diem_tb)
min_dtb = min(diem_tb)
hs_gioi_nhat = hoc_sinh[diem_tb.index(max_dtb)]
hs_yeu_nhat  = hoc_sinh[diem_tb.index(min_dtb)]

# ĐTB cả lớp từng môn
dtb_van  = round(sum(diem_van)  / len(diem_van),  2)
dtb_toan = round(sum(diem_toan) / len(diem_toan), 2)
dtb_anh  = round(sum(diem_anh)  / len(diem_anh),  2)

# ── PHẦN 2: Phân loại ────────────────────────────────────
xep_loai_list = [xep_loai(d) for d in diem_tb]

dem = {"Giỏi": [], "Khá": [], "Trung Bình": [], "Yếu": []}
for ten, loai in zip(hoc_sinh, xep_loai_list):
    dem[loai].append(ten)

# ── PHẦN 3 (tiếp): Cần phụ đạo ──────────────────────────
can_phu_dao = [ten for ten, dtb in zip(hoc_sinh, diem_tb) if dtb < 6.0]

# Sắp xếp theo điểm TB giảm dần
thu_tu = sorted(zip(hoc_sinh, diem_tb), key=lambda x: x[1], reverse=True)

# ── IN KẾT QUẢ ───────────────────────────────────────────
print("=" * 60)
print("          BẢNG ĐIỂM LỚP HỌC")
print("=" * 60)
print(f" {'Tên':<8} {'Văn':>5} {'Toán':>6} {'Anh':>5}  {'ĐTB':>5}  Xếp loại")
print("-" * 60)

for ten, v, t, a, dtb, loai in zip(
        hoc_sinh, diem_van, diem_toan, diem_anh, diem_tb, xep_loai_list):
    print(f" {ten:<8} {v:>5.1f} {t:>6.1f} {a:>5.1f}  {dtb:>5.2f}  {loai}")

print("=" * 60)

for loai in ["Giỏi", "Khá", "Trung Bình", "Yếu"]:
    ds = dem[loai]
    ten_ds = ", ".join(ds) if ds else "-"
    print(f"Học sinh {loai:<11} ({len(ds)}): {ten_ds}")

print()
print("Cần phụ đạo:", can_phu_dao if can_phu_dao else "[]")
print()
print("Xếp hạng theo điểm TB (cao → thấp):")
for hang, (ten, dtb) in enumerate(thu_tu, 1):
    print(f"  {hang}. {ten:<8} — {dtb:.2f}")

print()
print(f"ĐTB môn Văn: {dtb_van:.2f} | Toán: {dtb_toan:.2f} | Anh: {dtb_anh:.2f}")
print(f"Cao nhất: {hs_gioi_nhat} ({max_dtb}) | Thấp nhất: {hs_yeu_nhat} ({min_dtb})")
```

**Kết quả:**
```
============================================================
          BẢNG ĐIỂM LỚP HỌC
============================================================
 Tên       Văn   Toán   Anh    ĐTB  Xếp loại
------------------------------------------------------------
 An        7.5    8.5   6.0   7.33  Khá
 Bình      8.0    6.0   7.5   7.17  Khá
 Chi       6.5    9.0   8.5   8.00  Giỏi
 Dũng      5.0    7.0   6.5   6.17  Khá
 Em        9.0    8.0   7.0   8.00  Giỏi
 Quỳnh     9.0    9.5   8.5   9.00  Giỏi
============================================================
Học sinh Giỏi       (3): Chi, Em, Quỳnh
Học sinh Khá        (3): An, Bình, Dũng
Học sinh Trung Bình (0): -
Học sinh Yếu        (0): -

Cần phụ đạo: []

Xếp hạng theo điểm TB (cao → thấp):
  1. Quỳnh    — 9.00
  2. Chi      — 8.00
  3. Em       — 8.00
  4. An       — 7.33
  5. Bình     — 7.17
  6. Dũng     — 6.17

ĐTB môn Văn: 7.50 | Toán: 8.33 | Anh: 7.58
Cao nhất: Quỳnh (9.0) | Thấp nhất: Dũng (6.17)
```

---

### Giải thích các kỹ thuật quan trọng

| Kỹ thuật | Dùng ở đâu | Tác dụng |
|---|---|---|
| `zip(a, b, c)` | Duyệt nhiều list cùng lúc | Tránh lỗi index phức tạp |
| `sorted(..., key=lambda x: x[1])` | Sắp xếp danh sách tuple | Sắp xếp theo tiêu chí tùy chỉnh |
| `list.index(value)` | Tìm vị trí Phong để xóa | Không cần biết index trước |
| `list comprehension` với `zip` | Tính điểm TB | Ngắn gọn hơn vòng for thông thường |
| `dict` với list values | Nhóm học sinh theo xếp loại | Tra cứu nhanh theo nhóm |
