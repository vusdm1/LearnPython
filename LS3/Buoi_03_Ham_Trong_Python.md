# 🐍 GIÁO TRÌNH PYTHON — BUỔI 3

## **HÀM TRONG PYTHON: VIẾT MỘT LẦN, DÙNG NHIỀU LẦN**

> _"Người lập trình giỏi không chỉ viết code chạy được, mà còn viết code gọn gàng, dễ tái sử dụng và dễ nâng cấp."_

| Thông tin buổi học     | Chi tiết                                                                    |
| ---------------------- | --------------------------------------------------------------------------- |
| **Buổi**               | 03                                                                          |
| **Chủ đề**             | Hàm trong Python — định nghĩa hàm, tham số, `return`, viết và gọi hàm      |
| **Thời lượng**         | ~2 - 3 giờ (bao gồm thực hành)                                              |
| **Yêu cầu**            | Đã nắm kiến thức cơ bản về biến, kiểu dữ liệu, `input/output`, câu điều kiện |
| **Mục tiêu tổng quát** | Biết chia chương trình thành các hàm nhỏ, rõ ràng và tái sử dụng được       |

---

# 📌 MỤC LỤC

- [Module 1: Vì sao cần dùng hàm?](#module-1-vì-sao-cần-dùng-hàm)
- [Module 2: Định nghĩa hàm và gọi hàm](#module-2-định-nghĩa-hàm-và-gọi-hàm)
- [Module 3: Tham số (parameters) và đối số (arguments)](#module-3-tham-số-parameters-và-đối-số-arguments)
- [Module 4: Giá trị trả về với `return`](#module-4-giá-trị-trả-về-với-return)
- [Module 5: Biến cục bộ và phạm vi hoạt động](#module-5-biến-cục-bộ-và-phạm-vi-hoạt-động)
- [Module 6: Thực hành xây dựng chương trình bằng hàm](#module-6-thực-hành-xây-dựng-chương-trình-bằng-hàm)
- [📚 Phương pháp học hàm hiệu quả](#-phương-pháp-học-hàm-hiệu-quả)
- [📝 Bài tập thực hành tổng hợp](#-bài-tập-thực-hành-tổng-hợp)

---

---

# Module 1: Vì sao cần dùng hàm?

## 🎯 Mục tiêu

> Hiểu được hàm là công cụ giúp chương trình **gọn hơn, rõ hơn, dễ sửa hơn**.

---

## 1.1. Hàm là gì?

Hàm (`function`) là một **khối lệnh có tên**, dùng để thực hiện một nhiệm vụ cụ thể.

Ví dụ đời thường:

- Máy xay sinh tố có nút `xay_sinh_to()`
- Máy giặt có nút `giat_quan_ao()`
- Trong Python, ta có thể tự tạo các "nút chức năng" như `chao_hoc_sinh()`, `tinh_tong()`, `kiem_tra_chan()`

## 1.2. Tại sao phải dùng hàm?

Nếu không dùng hàm, chương trình thường:

- Bị lặp code nhiều lần
- Khó đọc, khó tìm lỗi
- Khó nâng cấp khi bài toán lớn hơn

### Ví dụ chưa dùng hàm

```python
print("Xin chào An!")
print("Chúc bạn học Python thật tốt!")

print("Xin chào Bình!")
print("Chúc bạn học Python thật tốt!")

print("Xin chào Chi!")
print("Chúc bạn học Python thật tốt!")
```

### Ví dụ dùng hàm

```python
def chao_hoc_sinh(ten):
    print(f"Xin chào {ten}!")
    print("Chúc bạn học Python thật tốt!")

chao_hoc_sinh("An")
chao_hoc_sinh("Bình")
chao_hoc_sinh("Chi")
```

> 💡 Một câu rất quan trọng: **Hàm giúp ta "đóng gói" một công việc để dùng lại nhiều lần.**

## 1.3. Khi nào nên tách thành hàm?

Hãy nghĩ đến việc tạo hàm khi:

- Một đoạn code được lặp lại từ 2 lần trở lên
- Một nhiệm vụ có thể đặt tên rõ ràng
- Bạn muốn chia bài toán lớn thành nhiều bước nhỏ
- Bạn muốn kiểm tra từng phần chương trình riêng biệt

---

### ✅ Kiểm tra nhanh Module 1

Đoạn nào nên tách thành hàm?

1. In tiêu đề chương trình ở nhiều nơi
2. Tính điểm trung bình cho nhiều học sinh
3. Kiểm tra mật khẩu hợp lệ nhiều lần

<details>
<summary>👀 Xem đáp án</summary>

Cả 3 trường hợp trên đều rất nên tách thành hàm vì có thể tái sử dụng nhiều lần.

</details>

---

---

# Module 2: Định nghĩa hàm và gọi hàm

## 🎯 Mục tiêu

> Biết cách tự tạo một hàm bằng `def` và gọi hàm để chương trình thực thi.

---

## 2.1. Cú pháp cơ bản

```python
def ten_ham():
    # Khối lệnh của hàm
    print("Đây là một hàm")
```

**Giải thích:**

- `def` là từ khóa để định nghĩa hàm
- `ten_ham` là tên do ta tự đặt
- `()` là nơi chứa tham số nếu cần
- `:` báo hiệu bắt đầu khối lệnh
- Phần bên trong phải **thụt đầu dòng**

## 2.2. Ví dụ đầu tiên

```python
def xin_chao():
    print("Xin chào các bạn học sinh KITE!")
    print("Hôm nay chúng ta học về hàm trong Python.")

xin_chao()
```

**Kết quả:**

```
Xin chào các bạn học sinh KITE!
Hôm nay chúng ta học về hàm trong Python.
```

## 2.3. Gọi hàm nhiều lần

```python
def ve_duong_ke():
    print("-" * 30)

ve_duong_ke()
print("MENU CHƯƠNG TRÌNH")
ve_duong_ke()
print("1. Bắt đầu")
print("2. Thoát")
ve_duong_ke()
```

> 💡 Định nghĩa hàm là **tạo ra công cụ**, còn gọi hàm là **sử dụng công cụ đó**.

## 2.4. Quy tắc đặt tên hàm

Nên đặt tên hàm:

- Ngắn gọn nhưng có ý nghĩa
- Viết bằng `snake_case`
- Diễn tả đúng hành động

### Ví dụ tên tốt

```python
def tinh_tong():
    pass

def kiem_tra_so_chan():
    pass

def in_menu():
    pass
```

### Ví dụ tên chưa tốt

```python
def a():
    pass

def lam_cai_gi_do():
    pass
```

---

---

# Module 3: Tham số (parameters) và đối số (arguments)

## 🎯 Mục tiêu

> Hiểu cách truyền dữ liệu vào hàm để hàm làm việc linh hoạt hơn.

---

## 3.1. Tham số là gì?

**Tham số** (`parameter`) là biến được khai báo trong phần định nghĩa hàm.

```python
def xin_chao(ten):
    print(f"Xin chào {ten}!")
```

Ở đây:

- `ten` là **tham số**

Khi gọi hàm:

```python
xin_chao("Lan")
```

- `"Lan"` là **đối số** (`argument`)

## 3.2. Hàm có một tham số

```python
def chao_ten(ten):
    print(f"Chào bạn {ten}, chúc bạn học tốt!")

chao_ten("Minh")
chao_ten("Ngọc")
```

## 3.3. Hàm có nhiều tham số

```python
def gioi_thieu(ten, tuoi, lop):
    print(f"Tên: {ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Lớp: {lop}")

gioi_thieu("An", 13, "8A1")
```

## 3.4. Thứ tự tham số rất quan trọng

```python
def tinh_hieu(a, b):
    print(a - b)

tinh_hieu(10, 3)  # 7
tinh_hieu(3, 10)  # -7
```

> ⚠️ Hàm nhận dữ liệu theo đúng vị trí nếu bạn truyền đối số theo cách thông thường.

## 3.5. Tham số mặc định

Ta có thể gán giá trị mặc định cho tham số:

```python
def chao(ten, loi_chuc="Chúc bạn một ngày tốt lành!"):
    print(f"Xin chào {ten}!")
    print(loi_chuc)

chao("Hà")
print()
chao("Nam", "Chúc bạn học Python thật vui!")
```

**Ý nghĩa:**

- Nếu không truyền `loi_chuc`, Python dùng giá trị mặc định
- Nếu có truyền, giá trị mới sẽ được dùng

---

### ✅ Kiểm tra nhanh Module 3

Đoán kết quả:

```python
def nhan_doi(x):
    print(x * 2)

nhan_doi(5)
nhan_doi(1.5)
nhan_doi("Hi")
```

<details>
<summary>👀 Xem đáp án</summary>

```python
nhan_doi(5)    # 10
nhan_doi(1.5)  # 3.0
nhan_doi("Hi") # HiHi
```

> Vì toán tử `*` trong Python hoạt động khác nhau tùy kiểu dữ liệu.

</details>

---

---

# Module 4: Giá trị trả về với `return`

## 🎯 Mục tiêu

> Biết cách để hàm **trả dữ liệu về** cho nơi đã gọi nó.

---

## 4.1. `return` dùng để làm gì?

`return` giúp hàm gửi kết quả về cho chương trình.

```python
def tinh_tong(a, b):
    return a + b

ket_qua = tinh_tong(4, 6)
print(ket_qua)  # 10
```

## 4.2. Khác nhau giữa `print()` và `return`

| `print()`                         | `return`                                 |
| --------------------------------- | ---------------------------------------- |
| In kết quả ra màn hình            | Trả kết quả về cho nơi gọi hàm           |
| Thường để hiển thị                | Thường để xử lý tiếp trong chương trình  |
| Không thuận tiện để tái sử dụng   | Rất thuận tiện cho tính toán và ghép nối |

### Ví dụ so sánh

```python
def tinh_tong_print(a, b):
    print(a + b)

def tinh_tong_return(a, b):
    return a + b

tinh_tong_print(2, 3)  # In ra 5

ket_qua = tinh_tong_return(2, 3)
print(ket_qua * 10)    # 50
```

> 💡 Nếu muốn dùng kết quả để tính tiếp, gần như bạn nên nghĩ đến `return`.

## 4.3. Hàm có thể trả về nhiều kiểu dữ liệu

```python
def lay_ten_day_du(ho, ten):
    return ho + " " + ten

def la_so_chan(so):
    return so % 2 == 0

print(lay_ten_day_du("Nguyễn", "An"))
print(la_so_chan(8))
```

## 4.4. Khi gặp `return`, hàm dừng lại

```python
def kiem_tra_diem(diem):
    if diem >= 5:
        return "Đỗ"

    return "Trượt"

print(kiem_tra_diem(8))
print(kiem_tra_diem(4))
```

## 4.5. Hàm không ghi `return` thì sao?

Nếu hàm không có `return`, Python mặc định trả về `None`.

```python
def thong_bao():
    print("Đang xử lý...")

ket_qua = thong_bao()
print(ket_qua)  # None
```

---

---

# Module 5: Biến cục bộ và phạm vi hoạt động

## 🎯 Mục tiêu

> Hiểu rằng biến tạo ra bên trong hàm thường chỉ sống bên trong hàm đó.

---

## 5.1. Biến cục bộ (local variable)

```python
def tinh_binh_phuong(x):
    ket_qua = x ** 2
    print(f"Bình phương là: {ket_qua}")

tinh_binh_phuong(5)
```

Ở ví dụ trên:

- `ket_qua` là biến cục bộ
- Nó chỉ dùng được bên trong `tinh_binh_phuong()`

## 5.2. Ví dụ lỗi thường gặp

```python
def tao_thong_bao():
    loi_nhan = "Chúc bạn học tốt!"

tao_thong_bao()
print(loi_nhan)  # Lỗi: NameError
```

## 5.3. Cách đúng nếu muốn lấy dữ liệu ra ngoài

```python
def tao_thong_bao():
    loi_nhan = "Chúc bạn học tốt!"
    return loi_nhan

thong_bao = tao_thong_bao()
print(thong_bao)
```

> 💡 Quy tắc an toàn cho người mới: **Muốn lấy kết quả từ hàm ra ngoài, hãy ưu tiên dùng `return`.**

---

---

# Module 6: Thực hành xây dựng chương trình bằng hàm

## 🎯 Mục tiêu

> Biết chia một bài toán thành nhiều hàm nhỏ thay vì viết tất cả trong một khối lớn.

---

## 6.1. Tư duy chia bài toán

Ví dụ bài toán: nhập điểm 3 môn và xếp loại học sinh.

Ta có thể chia thành 3 hàm:

1. Hàm nhập điểm
2. Hàm tính điểm trung bình
3. Hàm xếp loại

### Cách viết rõ ràng

```python
def nhap_diem(mon_hoc):
    return float(input(f"Nhập điểm {mon_hoc}: "))

def tinh_diem_trung_binh(toan, van, anh):
    return (toan + van + anh) / 3

def xep_loai_hoc_luc(dtb):
    if dtb >= 8.0:
        return "Giỏi"
    if dtb >= 6.5:
        return "Khá"
    if dtb >= 5.0:
        return "Trung bình"
    return "Yếu"

diem_toan = nhap_diem("Toán")
diem_van = nhap_diem("Văn")
diem_anh = nhap_diem("Anh")

dtb = tinh_diem_trung_binh(diem_toan, diem_van, diem_anh)
hoc_luc = xep_loai_hoc_luc(dtb)

print(f"\nĐiểm trung bình: {dtb:.2f}")
print(f"Xếp loại: {hoc_luc}")
```

## 6.2. Ví dụ: Máy tính mini bằng hàm

```python
def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Không thể chia cho 0"
    return a / b

print("🧮 MÁY TÍNH MINI")
so_1 = float(input("Nhập số thứ nhất: "))
so_2 = float(input("Nhập số thứ hai: "))

print("Cộng:", cong(so_1, so_2))
print("Trừ :", tru(so_1, so_2))
print("Nhân:", nhan(so_1, so_2))
print("Chia:", chia(so_1, so_2))
```

## 6.3. Mẫu suy nghĩ chuyên nghiệp khi viết hàm

Trước khi code, hãy tự hỏi 4 câu:

1. Hàm này làm đúng **một việc gì**?
2. Nó cần nhận **dữ liệu gì**?
3. Nó nên **in ra màn hình** hay **trả về kết quả**?
4. Tên hàm đã đủ rõ để người khác nhìn là hiểu chưa?

> 🌟 Đây là thói quen giúp học sinh tiến bộ nhanh từ "viết được code" sang "viết code có tổ chức".

---

---

# 📚 Phương pháp học hàm hiệu quả

## 1. Học theo vòng 4 bước

1. Đọc ví dụ mẫu và tự giải thích từng dòng
2. Gõ lại bằng tay, không copy-paste
3. Tự thay đổi dữ liệu đầu vào để quan sát kết quả
4. Tự viết lại từ trí nhớ sau 15 - 30 phút

## 2. Công thức học rất hiệu quả cho người mới

Mỗi khi gặp một hàm, hãy trả lời:

- Hàm tên gì?
- Nhận vào cái gì?
- Làm việc gì?
- Trả về cái gì?

Ví dụ:

```python
def tinh_chu_vi_hcn(dai, rong):
    return (dai + rong) * 2
```

Phân tích:

- Tên hàm: `tinh_chu_vi_hcn`
- Nhận vào: `dai`, `rong`
- Làm việc: tính chu vi hình chữ nhật
- Trả về: kết quả số

## 3. Sai lầm phổ biến cần tránh

- Quên gọi hàm sau khi định nghĩa
- Nhầm giữa `print()` và `return`
- Truyền thiếu đối số cho hàm
- Đặt tên hàm quá mơ hồ
- Viết một hàm làm quá nhiều việc

## 4. Mẹo luyện tập chuyên nghiệp

- Mỗi ngày viết 3 hàm ngắn về các chủ đề quen thuộc
- Với mỗi bài toán, thử tách thành ít nhất 2 hàm
- Sau khi chạy đúng, hãy tự hỏi: "Đoạn nào còn lặp để đưa vào hàm?"
- Khi sửa lỗi, kiểm tra từng hàm riêng thay vì nhìn toàn bộ chương trình

---

---

# 📝 Bài tập thực hành nâng cao — Tổng hợp Buổi 1, 2, 3

> 🎯 **Lưu ý:** Các bài tập dưới đây kết hợp kiến thức từ cả 3 buổi học:
> - **Buổi 1:** Biến, kiểu dữ liệu, phép toán, input/output, f-string
> - **Buổi 2:** if/elif/else, toán tử so sánh & logic, điều kiện lồng nhau
> - **Buổi 3:** Hàm, tham số, return, biến cục bộ, tách bài toán thành hàm
>
> 📄 **Lời giải** được đặt riêng trong file: `Buoi_03_Loi_Giai.md`

---

## 📌 Bài 1: Hệ thống tính tiền điện hàng tháng _(Trung bình)_

```
📋 Bối cảnh:
Công ty điện lực tính tiền theo bậc thang:
- Bậc 1: 50 kWh đầu tiên → 1.678 đồng/kWh
- Bậc 2: Từ kWh 51 đến 100 → 1.734 đồng/kWh
- Bậc 3: Từ kWh 101 đến 200 → 2.014 đồng/kWh
- Bậc 4: Từ kWh 201 đến 300 → 2.536 đồng/kWh
- Bậc 5: Từ kWh 301 trở lên → 2.834 đồng/kWh
Thuế VAT: 8%

📝 Yêu cầu:
1. Viết hàm `tinh_tien_dien(so_kwh)` → trả về số tiền TRƯỚC thuế
2. Viết hàm `tinh_thue(so_tien, thue_suat=0.08)` → trả về tiền thuế
3. Viết hàm `in_hoa_don(ten_kh, so_kwh)` → in hóa đơn đẹp ra màn hình
4. Chương trình chính: nhập tên khách hàng và số kWh, rồi in hóa đơn

📌 Ví dụ kết quả mong đợi:
╔══════════════════════════════════╗
║      HÓA ĐƠN TIỀN ĐIỆN         ║
╠══════════════════════════════════╣
║ Khách hàng : Nguyễn Văn A       ║
║ Số điện    : 150 kWh             ║
║ Tiền điện  : 254,900 đồng        ║
║ Thuế VAT   : 20,392 đồng         ║
║ Tổng cộng  : 275,292 đồng        ║
╚══════════════════════════════════╝
```

---

## 📌 Bài 2: Máy tính chỉ số BMI thông minh _(Trung bình)_

```
📋 Bối cảnh:
Phòng khám cần một chương trình tính BMI và đưa ra lời khuyên
cho bệnh nhân dựa trên kết quả.

Công thức: BMI = cân nặng (kg) / chiều cao (m)²

Bảng phân loại (theo WHO):
- BMI < 16.0     → Gầy độ III (Nguy hiểm)
- 16.0 ≤ BMI < 17.0 → Gầy độ II
- 17.0 ≤ BMI < 18.5 → Gầy độ I
- 18.5 ≤ BMI < 25.0 → Bình thường ✅
- 25.0 ≤ BMI < 30.0 → Thừa cân
- 30.0 ≤ BMI < 35.0 → Béo phì độ I
- BMI ≥ 35.0     → Béo phì độ II (Nguy hiểm)

📝 Yêu cầu:
1. Viết hàm `tinh_bmi(can_nang, chieu_cao_cm)` → trả về chỉ số BMI
   (Lưu ý: người dùng nhập chiều cao bằng cm, hàm phải đổi sang m)
2. Viết hàm `phan_loai_bmi(bmi)` → trả về chuỗi phân loại
3. Viết hàm `loi_khuyen(phan_loai)` → trả về lời khuyên phù hợp
4. Viết hàm `kiem_tra_du_lieu(can_nang, chieu_cao)` → trả về True/False
   (kiểm tra cân nặng > 0, chiều cao > 0 và chiều cao < 300)
5. Chương trình chính: nhập thông tin, kiểm tra → tính → phân loại → khuyên
```

---

## 📌 Bài 3: Chương trình đổi tiền tệ _(Trung bình)_

```
📋 Bối cảnh:
Quầy đổi tiền tại sân bay cần chương trình hỗ trợ nhân viên
đổi tiền nhanh cho khách du lịch.

Tỷ giá cố định:
- 1 USD = 25,450 VNĐ
- 1 EUR = 27,200 VNĐ
- 1 JPY = 168 VNĐ
- 1 KRW = 18.5 VNĐ

Phí dịch vụ:
- Đổi dưới 100 đơn vị ngoại tệ: phí 2%
- Đổi từ 100 đến dưới 1000: phí 1.5%
- Đổi từ 1000 trở lên: phí 1%

📝 Yêu cầu:
1. Viết hàm `lay_ty_gia(loai_tien)` → trả về tỷ giá, nếu không hỗ trợ trả về -1
2. Viết hàm `tinh_phi(so_luong)` → trả về phần trăm phí (dạng số thực, VD: 0.02)
3. Viết hàm `doi_tien(so_luong, loai_tien)` → trả về số tiền VNĐ sau phí
4. Viết hàm `in_phieu_doi(ten_khach, so_luong, loai_tien)` → in phiếu đổi tiền
5. Chương trình: hiển thị menu loại tiền → nhập thông tin → in phiếu
```

---

## 📌 Bài 4: Hệ thống xếp hạng học sinh cuối kỳ _(Nâng cao)_

```
📋 Bối cảnh:
Trường THCS cần chương trình xếp hạng học sinh dựa trên điểm
5 môn: Toán, Văn, Anh, Lý, Hóa.

Quy tắc xếp loại:
- Giỏi: ĐTB ≥ 8.0 VÀ không có môn nào dưới 6.5
- Khá: ĐTB ≥ 6.5 VÀ không có môn nào dưới 5.0
- Trung bình: ĐTB ≥ 5.0 VÀ không có môn nào dưới 3.5
- Yếu: ĐTB ≥ 3.5
- Kém: ĐTB < 3.5

Danh hiệu đặc biệt:
- Nếu có ít nhất 3 môn đạt 9.0 trở lên → "Học sinh xuất sắc ⭐"
- Nếu điểm Toán ≥ 9.0 VÀ điểm Anh ≥ 9.0 → "Ứng viên học bổng 🏆"

📝 Yêu cầu:
1. Viết hàm `nhap_diem(ten_mon)` → nhập và kiểm tra điểm hợp lệ (0-10)
   Nếu điểm không hợp lệ, in thông báo lỗi và trả về -1
2. Viết hàm `tinh_dtb(toan, van, anh, ly, hoa)` → trả về ĐTB
3. Viết hàm `diem_thap_nhat(toan, van, anh, ly, hoa)` → trả về điểm thấp nhất
4. Viết hàm `dem_diem_cao(toan, van, anh, ly, hoa)` → đếm số môn ≥ 9.0
5. Viết hàm `xep_loai(dtb, diem_min)` → trả về xếp loại
6. Viết hàm `kiem_tra_danh_hieu(toan, van, anh, ly, hoa)` → trả về danh hiệu
7. Viết hàm `in_bang_diem(ten, ...)` → in bảng điểm hoàn chỉnh
```

---

## 📌 Bài 5: Trò chơi "Đoán số bí mật" _(Nâng cao)_

```
📋 Bối cảnh:
Viết một trò chơi đoán số đơn giản. Máy tính chọn trước một số bí mật,
người chơi được đoán 1 lần, chương trình sẽ đưa ra gợi ý.

📝 Yêu cầu:
1. Viết hàm `tao_so_bi_mat()` → trả về một số cố định (VD: 42)
   (Vì chưa học random, ta dùng số cố định nhưng ẩn trong hàm)
2. Viết hàm `kiem_tra_du_doan(du_doan, so_bi_mat)` → trả về:
   - "Chính xác!" nếu đoán đúng
   - "Quá cao!" nếu đoán lớn hơn
   - "Quá thấp!" nếu đoán nhỏ hơn
3. Viết hàm `tinh_do_chinh_xac(du_doan, so_bi_mat)` → trả về
   phần trăm chính xác = 100 - abs(du_doan - so_bi_mat)
   (nếu kết quả < 0 thì trả về 0)
4. Viết hàm `xep_hang_nguoi_choi(do_chinh_xac)` → trả về:
   - 100% → "🏆 Thiên tài!"
   - ≥ 90% → "⭐ Rất giỏi!"
   - ≥ 70% → "👍 Khá tốt!"
   - ≥ 50% → "🤔 Tạm được"
   - < 50% → "😅 Cần cố gắng hơn"
5. Chương trình: chào người chơi → nhập dự đoán → kiểm tra → xếp hạng
```

---

## 📌 Bài 6: Ứng dụng quản lý chi tiêu cá nhân _(Nâng cao)_

```
📋 Bối cảnh:
Bạn muốn viết chương trình giúp quản lý chi tiêu trong ngày.
Chương trình cho phép nhập một khoản chi tiêu và phân tích ngay.

Phân loại chi tiêu:
- "an_uong": Ăn uống
- "di_lai": Di lại
- "giai_tri": Giải trí
- "hoc_tap": Học tập
- "khac": Khác

Quy tắc đánh giá:
- Chi tiêu ăn uống > 200,000đ/ngày → "⚠️ Ăn uống hơi nhiều"
- Chi tiêu giải trí > 100,000đ/ngày → "⚠️ Giải trí hơi nhiều"
- Tổng chi tiêu > 500,000đ/ngày → "🚨 Chi tiêu vượt ngân sách!"
- Tổng chi tiêu ≤ 300,000đ/ngày → "✅ Chi tiêu tiết kiệm!"

📝 Yêu cầu:
1. Viết hàm `nhap_chi_tieu(loai)` → nhập số tiền, kiểm tra ≥ 0, trả về số tiền
2. Viết hàm `tinh_tong(an_uong, di_lai, giai_tri, hoc_tap, khac)` → tổng
3. Viết hàm `tinh_phan_tram(so_tien, tong)` → trả về phần trăm (làm tròn 1 chữ số)
4. Viết hàm `danh_gia_chi_tieu(an_uong, giai_tri, tong)` → trả về chuỗi đánh giá
5. Viết hàm `in_bao_cao(...)` → in báo cáo chi tiêu đầy đủ:
   - Tên từng khoản + số tiền + phần trăm
   - Tổng chi tiêu
   - Đánh giá
```

---

## 📌 Bài 7: Chương trình tính lương nhân viên _(Nâng cao)_

```
📋 Bối cảnh:
Công ty cần chương trình tính lương cho nhân viên part-time.

Quy tắc:
- Lương cơ bản: số giờ làm × đơn giá/giờ
- Nếu làm trên 8 giờ/ngày: phần vượt tính gấp 1.5 lần
- Phụ cấp chức vụ:
  + "nhan_vien": 0 đồng
  + "to_truong": 500,000 đồng
  + "quan_ly": 1,500,000 đồng
- Khấu trừ bảo hiểm: 10.5% trên lương cơ bản (KHÔNG tính phụ cấp)
- Thuế thu nhập (trên tổng thu nhập trước thuế):
  + Dưới 5,000,000 → Miễn thuế
  + Từ 5,000,000 đến dưới 10,000,000 → Thuế 5%
  + Từ 10,000,000 trở lên → Thuế 10%

📝 Yêu cầu:
1. Viết hàm `tinh_luong_co_ban(so_gio, don_gia)` → tính lương có OT
2. Viết hàm `lay_phu_cap(chuc_vu)` → trả về phụ cấp
3. Viết hàm `tinh_bao_hiem(luong_co_ban)` → trả về tiền bảo hiểm
4. Viết hàm `tinh_thue_thu_nhap(tong_thu_nhap)` → trả về tiền thuế
5. Viết hàm `tinh_luong_thuc_nhan(so_gio, don_gia, chuc_vu)` → lương thực nhận
6. Viết hàm `in_phieu_luong(ten, so_gio, don_gia, chuc_vu)` → in phiếu lương
```

---

## 📌 Bài 8: Hệ thống đăng ký tài khoản đơn giản _(Thử thách)_

```
📋 Bối cảnh:
Viết chương trình mô phỏng đăng ký tài khoản trên website.

Quy tắc kiểm tra:
🔹 Tên đăng nhập:
  - Độ dài từ 4 đến 20 ký tự
  - Không được chứa khoảng trắng

🔹 Mật khẩu:
  - Độ dài ít nhất 6 ký tự
  - Không được giống tên đăng nhập
  - Nhập mật khẩu 2 lần phải trùng khớp

🔹 Email:
  - Phải chứa ký tự "@"
  - Phải chứa dấu "."
  - Không được chứa khoảng trắng

🔹 Tuổi:
  - Phải từ 13 trở lên (chính sách bảo mật cho trẻ em)

📝 Yêu cầu:
1. Viết hàm `kiem_tra_ten(ten_dang_nhap)` → trả về (True/False, thông_báo)
   VD: (False, "Tên quá ngắn! Cần ít nhất 4 ký tự.")
2. Viết hàm `kiem_tra_mat_khau(mat_khau, ten_dang_nhap)` → (True/False, thông_báo)
3. Viết hàm `kiem_tra_email(email)` → (True/False, thông_báo)
4. Viết hàm `kiem_tra_tuoi(tuoi)` → (True/False, thông_báo)
5. Viết hàm `dang_ky()` → hàm chính điều phối toàn bộ quy trình:
   - Nhập từng thông tin
   - Gọi hàm kiểm tra tương ứng
   - Nếu TẤT CẢ hợp lệ → in "✅ Đăng ký thành công!"
   - Nếu có lỗi → in tổng hợp các lỗi

💡 Gợi ý:
- Dùng `len()` để đo độ dài chuỗi: len("hello") = 5
- Dùng `in` để kiểm tra ký tự: " " in "xin chao" = True
- Dùng `x.lower()` nếu muốn so sánh không phân biệt hoa/thường
```

---

## 📌 Checklist tổng kết Buổi 3

| #   | Nội dung                                                    | Trạng thái |
| --- | ----------------------------------------------------------- | ---------- |
| 1   | Hiểu hàm là gì và vì sao cần dùng hàm                      | ⬜         |
| 2   | Biết định nghĩa hàm với `def`                               | ⬜         |
| 3   | Biết gọi hàm đúng cách                                      | ⬜         |
| 4   | Hiểu tham số và đối số                                      | ⬜         |
| 5   | Biết dùng `return` để trả về kết quả                        | ⬜         |
| 6   | Phân biệt được `print()` và `return`                        | ⬜         |
| 7   | Hiểu biến cục bộ bên trong hàm                              | ⬜         |
| 8   | Tách được một bài toán thành nhiều hàm nhỏ                  | ⬜         |
| 9   | Hoàn thành ít nhất 3/5 bài tập                              | ⬜         |
| 10  | Tự viết được một chương trình ngắn có sử dụng nhiều hàm     | ⬜         |

---

> **📢 Hẹn gặp lại ở Buổi 4!**
>
> Ở buổi tiếp theo, chúng ta có thể học về **vòng lặp (`for`, `while`)** để kết hợp với hàm, giúp chương trình tự động xử lý nhiều dữ liệu hơn mà không phải viết lặp code. 🔁

---

_© 2026 — Giáo trình Python | Biên soạn cho lớp học KITE_
