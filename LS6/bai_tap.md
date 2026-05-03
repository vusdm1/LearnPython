# BÀI TẬP — DANH SÁCH (LIST)

---

## Bài tập 2 — Tạo List

**Viết chương trình thực hiện các yêu cầu sau:**

1. Tạo list `mon_hoc` chứa 5 môn học bạn yêu thích.
2. Tạo list `so_nguyen_to` chứa các số nguyên tố từ 1 đến 20: `[2, 3, 5, 7, 11, 13, 17, 19]`.
3. Tạo list `tuan` gồm 7 ngày trong tuần bằng cách khai báo trực tiếp.
4. In ra:
   - Số môn học trong `mon_hoc`
   - Kiểm tra xem "Toán" có trong `mon_hoc` không
   - Môn học đầu tiên và cuối cùng trong danh sách

**Ví dụ kết quả mong đợi:**

```
Số môn học: 5
Có môn Toán không? True
Môn đầu tiên: Toán
Môn cuối cùng: Thể dục
```

---

## Bài tập 3 — Truy cập dữ liệu

Cho danh sách nhiệt độ 7 ngày trong tuần (°C):

```python
nhiet_do = [28, 31, 29, 33, 27, 35, 30]
#  ngày:    T2  T3  T4  T5  T6  T7  CN
```

**Thực hiện:**

1. In ra nhiệt độ ngày thứ Tư (index 2).
2. In ra nhiệt độ ngày cuối tuần (Thứ 7 và Chủ Nhật).
3. In ra nhiệt độ 3 ngày đầu tuần (Thứ 2, 3, 4).
4. In ra danh sách nhiệt độ theo thứ tự ngược lại (từ Chủ Nhật về Thứ 2).
5. In ra ngày nóng nhất và mát nhất trong tuần.

**Ví dụ kết quả mong đợi:**

```
Nhiệt độ thứ Tư: 29°C
Cuối tuần: [35, 30]
Đầu tuần: [28, 31, 29]
Ngược lại: [30, 35, 27, 33, 29, 31, 28]
Nóng nhất: 35°C | Mát nhất: 27°C
```

---

## Bài tập 4 — Sửa đổi dữ liệu

Bạn đang quản lý danh sách thành viên một câu lạc bộ:

```python
thanh_vien = ["An", "Bình", "Chi", "Dũng"]
```

**Thực hiện theo thứ tự:**

1. Thêm "Em" vào cuối danh sách.
2. Thêm "Phong" vào vị trí đầu tiên (index 0).
3. Ghép thêm list `["Quỳnh", "Rồng"]` vào cuối danh sách.
4. Xóa "Chi" khỏi danh sách.
5. Lấy ra (pop) thành viên cuối cùng và in ra tên người đó.
6. Thay đổi tên "Bình" thành "Bình Minh".
7. In danh sách sau mỗi thao tác để thấy sự thay đổi.

**Ví dụ kết quả mong đợi:**

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

## Bài tập 5 — Thao tác dữ liệu

Cho danh sách điểm thi môn Toán của 10 học sinh:

```python
diem_toan = [7.5, 4.0, 9.0, 6.5, 8.0, 3.5, 7.0, 5.5, 9.5, 6.0]
```

**Thực hiện:**

1. Sắp xếp điểm từ **cao đến thấp** và in ra (không thay đổi list gốc).
2. Tính điểm **trung bình** của cả lớp (làm tròn 2 chữ số).
3. Dùng **List Comprehension** lọc ra danh sách điểm của học sinh **đạt** (≥ 5.0).
4. Dùng **List Comprehension** tạo danh sách **xếp loại**: nếu điểm ≥ 8.0 là `"Giỏi"`, ≥ 6.5 là `"Khá"`, ≥ 5.0 là `"TB"`, còn lại là `"Yếu"`.
5. Đếm xem có bao nhiêu học sinh đạt loại "Giỏi".

**Ví dụ kết quả mong đợi:**

```
Xếp hạng điểm: [9.5, 9.0, 8.0, 7.5, 7.0, 6.5, 6.0, 5.5, 4.0, 3.5]
Điểm trung bình: 6.65
Điểm đạt: [7.5, 9.0, 6.5, 8.0, 7.0, 5.5, 9.5, 6.0]
Xếp loại: ['Khá', 'Yếu', 'Giỏi', 'Khá', 'Giỏi', 'Yếu', 'Khá', 'TB', 'Giỏi', 'TB']
Số học sinh Giỏi: 3
```

---

## Bài tập 6 — Thực hành tuần tự

Cho danh sách điểm thi 3 môn của 5 học sinh:

```python
# Mỗi phần tử: [Tên, Toán, Lý, Hóa]
lop_hoc = [
    ["An",    8.0, 7.5, 9.0],
    ["Bình",  6.0, 5.0, 4.5],
    ["Chi",   9.5, 8.5, 9.0],
    ["Dũng",  5.5, 6.0, 5.0],
    ["Em",    7.0, 7.5, 8.0],
]
```

**Duyệt qua danh sách và in bảng kết quả:**

1. Tính điểm trung bình 3 môn của từng học sinh (làm tròn 2 chữ số).
2. Xếp loại: ≥ 8.0 = "Giỏi", ≥ 6.5 = "Khá", ≥ 5.0 = "Trung Bình", < 5.0 = "Yếu".
3. In bảng kết quả theo định dạng:

```
=====================================================
 Tên       Toán    Lý    Hóa   ĐTB   Xếp loại
=====================================================
 An         8.0   7.5    9.0  8.17   Giỏi
 Bình       6.0   5.0    4.5  5.17   Trung Bình
 Chi        9.5   8.5    9.0  9.00   Giỏi
 Dũng       5.5   6.0    5.0  5.50   Trung Bình
 Em         7.0   7.5    8.0  7.50   Khá
=====================================================
Lớp có 2 HS Giỏi, 1 HS Khá, 2 HS Trung Bình, 0 HS Yếu
```

---

## BÀI TẬP LỚN — Hệ thống quản lý học sinh

### Đề bài

Xây dựng chương trình quản lý điểm học sinh đơn giản cho một lớp học gồm các chức năng sau:

**Dữ liệu ban đầu:**

```python
hoc_sinh = ["An", "Bình", "Chi", "Dũng", "Em", "Phong"]
diem_van = [7.5, 8.0, 6.5, 5.0, 9.0, 4.5]
diem_toan = [8.5, 6.0, 9.0, 7.0, 8.0, 5.5]
diem_anh = [6.0, 7.5, 8.5, 6.5, 7.0, 6.0]
```

**Yêu cầu:**

**Phần 1 — Thống kê cơ bản:**

1. Tính điểm trung bình 3 môn của **từng học sinh**.
2. Tìm học sinh có điểm trung bình **cao nhất** và **thấp nhất**.
3. Tính điểm trung bình **của cả lớp** cho từng môn.

**Phần 2 — Phân loại:** 4. Tạo list `xep_loai` dựa theo điểm trung bình:

- ≥ 8.0: "Giỏi"
- ≥ 6.5: "Khá"
- ≥ 5.0: "Trung Bình"
- < 5.0: "Yếu"

5. Đếm số học sinh mỗi loại và in kết quả.

**Phần 3 — Xử lý danh sách:** 6. Tạo list `can_phu_dao` gồm tên các học sinh có điểm trung bình **dưới 6.0**. 7. Sắp xếp và in danh sách học sinh **theo thứ tự điểm trung bình giảm dần** (kèm tên và điểm TB). 8. **Thêm** một học sinh mới: `"Quỳnh"` với điểm `Văn=9.0, Toán=9.5, Anh=8.5`. 9. **Xóa** học sinh "Phong" khỏi tất cả các danh sách. 10. In bảng kết quả cuối cùng sau khi cập nhật.

**Kết quả mong đợi (tham khảo):**

```
============================================================
           BẢNG ĐIỂM LỚP HỌC
============================================================
 Tên     Văn   Toán   Anh    ĐTB   Xếp loại
------------------------------------------------------------
 An      7.5    8.5   6.0   7.33   Khá
 Bình    8.0    6.0   7.5   7.17   Khá
 Chi     6.5    9.0   8.5   8.00   Giỏi
 Dũng    5.0    7.0   6.5   6.17   Khá
 Em      9.0    8.0   7.0   8.00   Giỏi
 Quỳnh   9.0    9.5   8.5   9.00   Giỏi
============================================================
Học sinh Giỏi  (3): Chi, Em, Quỳnh
Học sinh Khá   (3): An, Bình, Dũng
Học sinh TB    (0): -
Học sinh Yếu   (0): -

Cần phụ đạo: []

Xếp hạng theo điểm TB (cao → thấp):
  1. Quỳnh  — 9.00
  2. Chi    — 8.00
  3. Em     — 8.00
  4. An     — 7.33
  5. Bình   — 7.17
  6. Dũng   — 6.17

ĐTB môn Văn:  7.50 | Toán: 8.00 | Anh: 7.33
```

> **Gợi ý:** Dùng `zip()` để duyệt nhiều list song song, dùng `sorted()` với `key=` để sắp xếp theo điều kiện tùy chỉnh.
