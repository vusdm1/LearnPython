# 🐍 GIÁO TRÌNH PYTHON — BUỔI 1

## **NHẬP MÔN PYTHON: TỪ SỐ 0 ĐẾN CHƯƠNG TRÌNH ĐẦU TIÊN**

> _"Mọi chuyên gia đều từng là người mới bắt đầu."_ — Helen Hayes

| Thông tin buổi học         | Chi tiết                                                           |
| -------------------------- | ------------------------------------------------------------------ |
| **Buổi**                   | 01 / Tổng số buổi                                                  |
| **Chủ đề**                 | Nhập môn Python — Biến, Kiểu dữ liệu, Phép toán, Nhập/Xuất         |
| **Thời lượng**             | ~2 - 3 giờ (bao gồm thực hành)                                     |
| **Yêu cầu trước buổi học** | Máy tính có kết nối Internet                                       |
| **Mục tiêu tổng quát**     | Cài đặt môi trường, viết và chạy được chương trình Python đầu tiên |

---

# 📌 MỤC LỤC

- [Module 1: Cài đặt môi trường & Chạy chương trình đầu tiên](#module-1-cài-đặt-môi-trường--chạy-chương-trình-đầu-tiên)
- [Module 2: Biến (Variables) và Kiểu dữ liệu (Data Types)](#module-2-biến-variables-và-kiểu-dữ-liệu-data-types)
- [Module 3: Các phép toán cơ bản (Operators)](#module-3-các-phép-toán-cơ-bản-operators)
- [Module 4: Nhập/Xuất dữ liệu (Input/Output)](#module-4-nhậpxuất-dữ-liệu-inputoutput)
- [📝 Bài tập thực hành tổng hợp](#-bài-tập-thực-hành-tổng-hợp)
- [📚 Tài liệu tham khảo thêm](#-tài-liệu-tham-khảo-thêm)

---

---

# Module 1: Cài đặt môi trường & Chạy chương trình đầu tiên

## 🎯 Mục tiêu

> Giúp máy tính của bạn **"hiểu"** được ngôn ngữ Python và chạy thành công chương trình đầu tiên.

---

## 1.1. Python là gì?

Python là một **ngôn ngữ lập trình bậc cao**, được tạo ra bởi **Guido van Rossum** vào năm **1991**. Python nổi tiếng vì:

| Đặc điểm                        | Mô tả                                            |
| ------------------------------- | ------------------------------------------------ |
| 🧹 **Cú pháp sạch đẹp**         | Code Python đọc gần giống tiếng Anh, rất dễ hiểu |
| 🚀 **Đa mục đích**              | Web, AI, Data Science, Tự động hóa, Game...      |
| 📦 **Hệ sinh thái khổng lồ**    | Hơn 400.000+ thư viện miễn phí trên PyPI         |
| 👶 **Thân thiện với người mới** | Là ngôn ngữ được khuyến khích học đầu tiên       |

**Ai đang dùng Python?**

- Google, Netflix, Instagram, Spotify, NASA, Tesla...
- Các nhà khoa học dữ liệu, kỹ sư AI trên toàn thế giới.

---

## 1.2. Cài đặt Python

### 📥 Bước 1: Tải Python

1. Truy cập website chính thức: **[https://www.python.org/downloads/](https://www.python.org/downloads/)**
2. Nhấn nút **"Download Python 3.12.x"** (hoặc phiên bản mới nhất).
3. File tải về sẽ có dạng:
   - **Windows**: `python-3.12.x-amd64.exe`
   - **macOS**: `python-3.12.x-macos11.pkg`

### 🖥️ Bước 2: Cài đặt (theo hệ điều hành)

#### 🪟 Trên Windows

```
1. Mở file .exe vừa tải
2. ⚠️ QUAN TRỌNG: Tích vào ô "Add Python 3.12 to PATH" ở góc dưới cùng
3. Nhấn "Install Now"
4. Đợi cài đặt hoàn tất → Nhấn "Close"
```

> ⚠️ **CẢNH BÁO QUAN TRỌNG**
>
> Nếu bạn **QUÊN** tích ô **"Add Python to PATH"**, Python sẽ được cài nhưng Terminal/CMD sẽ **không nhận ra** lệnh `python`. Bạn sẽ phải cài lại hoặc thêm PATH thủ công (khá phức tạp cho người mới).

#### 🍎 Trên macOS

```
1. Mở file .pkg vừa tải
2. Làm theo hướng dẫn trên màn hình (Next → Next → Install)
3. Nhập mật khẩu máy nếu được yêu cầu
4. Hoàn tất
```

> 💡 **Mẹo cho macOS**: macOS thường đã có Python 2 sẵn. Sau khi cài, hãy dùng lệnh `python3` thay vì `python` để chạy đúng phiên bản.

#### 🐧 Trên Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### ✅ Bước 3: Kiểm tra cài đặt thành công

Mở **Terminal** (macOS/Linux) hoặc **Command Prompt / PowerShell** (Windows), gõ:

```bash
python --version
```

Hoặc (trên macOS/Linux):

```bash
python3 --version
```

**Kết quả mong đợi:**

```
Python 3.12.x
```

> ✅ Nếu bạn thấy dòng trên → **Xin chúc mừng!** Python đã được cài đặt thành công! 🎉

---

## 1.3. Trình soạn thảo mã nguồn (IDE / Code Editor)

IDE (Integrated Development Environment) là **"xưởng làm việc"** của lập trình viên. Dưới đây là các lựa chọn phổ biến:

### 🏆 Lựa chọn 1: Visual Studio Code (VS Code) — **KHUYÊN DÙNG**

|             |                                                                  |
| ----------- | ---------------------------------------------------------------- |
| **Tải về**  | [https://code.visualstudio.com/](https://code.visualstudio.com/) |
| **Ưu điểm** | Miễn phí, nhẹ, nhiều extension, hỗ trợ đa ngôn ngữ               |
| **Phù hợp** | Mọi cấp độ, đặc biệt người mới                                   |

**Sau khi cài VS Code, cài thêm Extension cho Python:**

```
1. Mở VS Code
2. Nhấn Ctrl+Shift+X (hoặc Cmd+Shift+X trên Mac) để mở Extensions
3. Tìm "Python" (của Microsoft) → Nhấn Install
4. Tìm "Python Debugger" → Nhấn Install (tùy chọn)
```

### 🏆 Lựa chọn 2: PyCharm

|             |                                                                          |
| ----------- | ------------------------------------------------------------------------ |
| **Tải về**  | [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/) |
| **Ưu điểm** | IDE chuyên nghiệp cho Python, tự động hoàn thành code mạnh mẽ            |
| **Phù hợp** | Người muốn IDE chuyên biệt cho Python                                    |

> 💡 Chọn bản **Community Edition** (miễn phí) là đủ dùng.

### ☁️ Lựa chọn 3: Google Colab — **Không cần cài đặt gì cả!**

|              |                                                                          |
| ------------ | ------------------------------------------------------------------------ |
| **Truy cập** | [https://colab.research.google.com/](https://colab.research.google.com/) |
| **Ưu điểm**  | Chạy trực tiếp trên trình duyệt, miễn phí GPU                            |
| **Phù hợp**  | Người muốn bắt đầu ngay, không muốn cài phần mềm                         |

**Cách dùng Google Colab:**

```
1. Đăng nhập bằng tài khoản Google
2. Nhấn "New Notebook"
3. Gõ code vào ô (cell) và nhấn Shift+Enter để chạy
```

---

## 1.4. Chương trình "Hello World" — Chương trình đầu tiên! 🎉

### 📝 Các bước thực hiện

**Bước 1:** Mở VS Code (hoặc IDE bạn chọn).

**Bước 2:** Tạo một thư mục mới cho dự án, ví dụ: `hoc_python`.

**Bước 3:** Tạo file mới tên `hello.py`.

> 💡 **Lưu ý**: File Python luôn có đuôi `.py`

**Bước 4:** Gõ đoạn code sau vào file:

```python
# Đây là chương trình Python đầu tiên của tôi!
# Dòng bắt đầu bằng dấu # là "comment" - ghi chú, Python sẽ bỏ qua nó.

print("Chào mừng bạn đến với Python!")
```

**Bước 5:** Chạy chương trình.

**Cách 1 — Chạy từ Terminal trong VS Code:**

```bash
# Mở Terminal trong VS Code: Ctrl+` (hoặc Cmd+` trên Mac)
# Gõ lệnh sau:
python hello.py
```

**Cách 2 — Nhấn nút Run ▶️:**

- Nhấn nút ▶️ (Run) ở góc phải phía trên file trong VS Code.

**Kết quả hiển thị trên Terminal:**

```
Chào mừng bạn đến với Python!
```

### 🧪 Thử nghiệm thêm

Hãy thử thay đổi nội dung trong `print()` và chạy lại:

```python
print("Xin chào! Tôi đang học Python!")
print("Python thật thú vị!")
print("🐍🐍🐍")
```

**Kết quả:**

```
Xin chào! Tôi đang học Python!
Python thật thú vị!
🐍🐍🐍
```

### 💡 Giải thích chi tiết

| Thành phần | Giải thích                                                         |
| ---------- | ------------------------------------------------------------------ |
| `print()`  | Hàm (function) dùng để **in/xuất** nội dung ra màn hình            |
| `"..."`    | Dấu nháy kép bao quanh nội dung cần in (gọi là **chuỗi / string**) |
| `# ...`    | **Comment** — ghi chú cho người đọc, Python sẽ bỏ qua              |

---

### ✅ Kiểm tra kiến thức Module 1

- [ ] Đã cài Python thành công và kiểm tra version
- [ ] Đã cài IDE / Code Editor
- [ ] Đã tạo và chạy thành công file `hello.py`

---

---

# Module 2: Biến (Variables) và Kiểu dữ liệu (Data Types)

## 🎯 Mục tiêu

> Hiểu cách **lưu trữ** và **phân loại** thông tin trong Python.

---

## 2.1. Biến (Variable) là gì?

Hãy tưởng tượng biến như một **chiếc hộp có dán nhãn**:

- **Nhãn** = tên biến
- **Đồ bên trong** = giá trị (value)

```
┌─────────────┐
│   age = 25  │    ← "age" là nhãn, 25 là đồ bên trong
│  ┌───────┐  │
│  │  25   │  │
│  └───────┘  │
└─────────────┘
```

### Cú pháp khai báo biến

```python
tên_biến = giá_trị
```

> 💡 **Khác biệt quan trọng**: Trong Python, bạn **KHÔNG CẦN** khai báo kiểu dữ liệu (khác với Java, C++). Python tự động nhận biết kiểu dữ liệu!

**So sánh:**

```java
// Trong Java (cần khai báo kiểu)
int age = 25;
String name = "Python";
```

```python
# Trong Python (không cần khai báo kiểu)
age = 25
name = "Python"
```

### Ví dụ thực tế:

```python
# Khai báo các biến
ho_ten = "Nguyễn Văn A"
tuoi = 20
diem_trung_binh = 8.5
dang_hoc_python = True

# In ra giá trị
print(ho_ten)           # Kết quả: Nguyễn Văn A
print(tuoi)             # Kết quả: 20
print(diem_trung_binh)  # Kết quả: 8.5
print(dang_hoc_python)  # Kết quả: True
```

---

## 2.2. Quy tắc đặt tên biến

### ✅ Quy tắc BẮT BUỘC

| Quy tắc                       | Ví dụ đúng ✅           | Ví dụ sai ❌             |
| ----------------------------- | ----------------------- | ------------------------ |
| Bắt đầu bằng chữ cái hoặc `_` | `name`, `_count`        | `1name`, `@value`        |
| Chỉ chứa chữ cái, số, `_`     | `my_var`, `age2`        | `my-var`, `my var`       |
| **Phân biệt HOA / thường**    | `Age` ≠ `age` ≠ `AGE`   | —                        |
| Không dùng từ khóa Python     | `my_class`, `user_type` | `class`, `type`, `print` |

### 📖 Quy ước đặt tên (Best Practices)

```python
# ✅ CÁCH ĐẶT TÊN TỐT (snake_case — chữ thường, ngăn cách bằng _)
first_name = "An"
student_age = 20
total_score = 100
is_active = True

# ❌ CÁCH ĐẶT TÊN NÊN TRÁNH
x = "An"          # Quá ngắn, không rõ nghĩa
a = 20             # Không biết "a" là gì
firstName = "An"   # CamelCase — dùng cho class, không dùng cho biến thường
```

### 🔒 Danh sách từ khóa Python (KHÔNG được dùng làm tên biến)

```python
# Bạn có thể xem danh sách từ khóa bằng lệnh:
import keyword
print(keyword.kwlist)

# Kết quả:
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
#  'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#  'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
#  'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
#  'while', 'with', 'yield']
```

---

## 2.3. Các kiểu dữ liệu cơ bản (Data Types)

Python có **4 kiểu dữ liệu cơ bản** mà bạn sẽ dùng thường xuyên:

### 📊 Bảng tổng quan

| Kiểu dữ liệu | Từ khóa | Mô tả                      | Ví dụ                          |
| ------------ | ------- | -------------------------- | ------------------------------ |
| Số nguyên    | `int`   | Số không có phần thập phân | `25`, `-10`, `0`, `1000`       |
| Số thực      | `float` | Số có phần thập phân       | `3.14`, `-0.5`, `2.0`          |
| Chuỗi        | `str`   | Văn bản, ký tự             | `"Hello"`, `'Python'`, `"123"` |
| Boolean      | `bool`  | Đúng hoặc Sai              | `True`, `False`                |

---

### 🔢 2.3.1. Số nguyên — `int` (Integer)

Là số **không có phần thập phân**, có thể âm hoặc dương.

```python
tuoi = 25
nam_sinh = 2001
so_am = -10
so_khong = 0
so_lon = 1_000_000  # Có thể dùng dấu _ để dễ đọc (Python bỏ qua _)

print(tuoi)       # 25
print(so_lon)     # 1000000
print(type(tuoi)) # <class 'int'>
```

> 💡 **Mẹo**: Python hỗ trợ số nguyên có **kích thước không giới hạn**! Bạn có thể lưu số lớn bao nhiêu cũng được.

```python
so_rat_lon = 99999999999999999999999999999999
print(so_rat_lon)      # Hoàn toàn ok!
print(type(so_rat_lon)) # <class 'int'>
```

---

### 🔢 2.3.2. Số thực — `float` (Floating-point)

Là số **có phần thập phân**.

```python
pi = 3.14159
nhiet_do = -5.5
diem = 9.0  # Dù là 9 "chẵn" nhưng có dấu . nên vẫn là float

print(pi)         # 3.14159
print(type(diem)) # <class 'float'>
```

> ⚠️ **Lưu ý quan trọng**: Số thực trong máy tính có thể có **sai số nhỏ** do cách lưu trữ trong bộ nhớ:

```python
print(0.1 + 0.2)  # Kết quả: 0.30000000000000004 (không phải 0.3!)
```

> Đây KHÔNG phải lỗi của Python, mà là đặc điểm chung của mọi ngôn ngữ lập trình khi xử lý số thực.

---

### 📝 2.3.3. Chuỗi — `str` (String)

Là **văn bản**, được đặt trong dấu **nháy đơn** `' '` hoặc **nháy kép** `" "`.

```python
# Cả hai cách đều đúng
ten_1 = "Nguyễn Văn A"
ten_2 = 'Nguyễn Văn A'

# Chuỗi có thể chứa số (nhưng nó vẫn là chuỗi, KHÔNG phải số!)
so_dien_thoai = "0901234567"

print(ten_1)                  # Nguyễn Văn A
print(type(so_dien_thoai))    # <class 'str'>
```

#### Khi nào dùng nháy đơn, khi nào dùng nháy kép?

```python
# Nếu chuỗi chứa dấu nháy đơn → dùng nháy kép bao ngoài
cau_1 = "It's a beautiful day"

# Nếu chuỗi chứa dấu nháy kép → dùng nháy đơn bao ngoài
cau_2 = 'Anh ấy nói "Xin chào"'

# Hoặc dùng ký tự escape: \"  \'
cau_3 = "Anh ấy nói \"Xin chào\""
```

#### Chuỗi nhiều dòng (Multi-line string)

```python
# Dùng 3 dấu nháy kép hoặc 3 dấu nháy đơn
thong_bao = """
Xin chào các bạn!
Chào mừng đến với lớp học Python.
Chúc các bạn học tốt!
"""
print(thong_bao)
```

**Kết quả:**

```
Xin chào các bạn!
Chào mừng đến với lớp học Python.
Chúc các bạn học tốt!
```

#### Nối chuỗi (String Concatenation)

```python
ho = "Nguyễn"
ten = "An"

# Cách 1: Dùng dấu +
ho_ten = ho + " " + ten
print(ho_ten)  # Nguyễn An

# Cách 2: Dùng f-string (sẽ học kỹ hơn ở Module 4)
print(f"Họ tên: {ho} {ten}")  # Họ tên: Nguyễn An
```

> ⚠️ **Lỗi thường gặp**: Không thể nối chuỗi với số trực tiếp!

```python
tuoi = 25

# ❌ SAI — sẽ báo lỗi TypeError
# print("Tôi " + tuoi + " tuổi")

# ✅ ĐÚNG — phải chuyển số thành chuỗi bằng str()
print("Tôi " + str(tuoi) + " tuổi")  # Tôi 25 tuổi

# ✅ ĐÚNG (cách tốt hơn) — dùng f-string
print(f"Tôi {tuoi} tuổi")  # Tôi 25 tuổi
```

---

### ✅❌ 2.3.4. Boolean — `bool`

Chỉ có **2 giá trị**: `True` (Đúng) hoặc `False` (Sai).

```python
dang_hoc = True
da_tot_nghiep = False

print(dang_hoc)          # True
print(type(dang_hoc))    # <class 'bool'>
```

> 💡 **Lưu ý**: `True` và `False` phải viết **HOA chữ cái đầu**!

```python
# ✅ Đúng
x = True
y = False

# ❌ Sai — sẽ báo lỗi
# x = true   (lỗi NameError)
# y = FALSE  (lỗi NameError)
```

**Boolean thường dùng trong so sánh:**

```python
print(10 > 5)     # True
print(3 == 7)     # False
print("a" != "b") # True
```

---

## 2.4. Kiểm tra kiểu dữ liệu với `type()`

Hàm `type()` rất hữu ích để kiểm tra biến đang chứa kiểu dữ liệu gì:

```python
a = 42
b = 3.14
c = "Hello"
d = True

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>
```

---

## 2.5. Ép kiểu (Type Casting / Type Conversion)

Đôi khi bạn cần **chuyển đổi** giữa các kiểu dữ liệu:

```python
# str → int
tuoi_str = "25"
tuoi_int = int(tuoi_str)
print(tuoi_int + 5)  # 30 ✅ (vì giờ nó là số, cộng được)

# int → str
so = 100
so_str = str(so)
print("Điểm: " + so_str)  # Điểm: 100 ✅

# int → float
x = 10
y = float(x)
print(y)        # 10.0
print(type(y))  # <class 'float'>

# float → int (cắt bỏ phần thập phân, KHÔNG làm tròn)
z = 9.99
w = int(z)
print(w)  # 9 (không phải 10!)
```

### 📊 Bảng tóm tắt ép kiểu

| Hàm       | Chuyển đổi thành | Ví dụ           | Kết quả |
| --------- | ---------------- | --------------- | ------- |
| `int()`   | Số nguyên        | `int("25")`     | `25`    |
| `float()` | Số thực          | `float("3.14")` | `3.14`  |
| `str()`   | Chuỗi            | `str(100)`      | `"100"` |
| `bool()`  | Boolean          | `bool(1)`       | `True`  |

### ⚠️ Lỗi thường gặp khi ép kiểu

```python
# ❌ Không thể chuyển chữ thành số!
# int("hello")  → ValueError: invalid literal for int()

# ❌ Không thể chuyển chuỗi có dấu chấm thành int trực tiếp!
# int("3.14")   → ValueError

# ✅ Phải qua float trước
int(float("3.14"))  # → 3
```

---

### ✅ Kiểm tra kiến thức Module 2

- [ ] Biết cách khai báo biến trong Python
- [ ] Phân biệt được 4 kiểu dữ liệu cơ bản: `int`, `float`, `str`, `bool`
- [ ] Biết dùng `type()` để kiểm tra kiểu dữ liệu
- [ ] Biết cách ép kiểu với `int()`, `float()`, `str()`

---

---

# Module 3: Các phép toán cơ bản (Operators)

## 🎯 Mục tiêu

> Thực hiện các **tính toán** trên dữ liệu bằng các phép toán trong Python.

---

## 3.1. Phép toán số học (Arithmetic Operators)

### 📊 Bảng tổng hợp

| Phép toán       | Ký hiệu | Ví dụ     | Kết quả | Giải thích                             |
| --------------- | ------- | --------- | ------- | -------------------------------------- |
| Cộng            | `+`     | `10 + 5`  | `15`    | Tính tổng                              |
| Trừ             | `-`     | `10 - 5`  | `5`     | Tính hiệu                              |
| Nhân            | `*`     | `10 * 5`  | `50`    | Tính tích                              |
| Chia            | `/`     | `10 / 4`  | `2.5`   | Chia thường (kết quả luôn là `float`)  |
| Chia lấy nguyên | `//`    | `10 // 4` | `2`     | Chỉ lấy phần nguyên, bỏ phần thập phân |
| Chia lấy dư     | `%`     | `10 % 3`  | `1`     | Lấy phần dư (10 ÷ 3 = 3 dư **1**)      |
| Lũy thừa        | `**`    | `2 ** 3`  | `8`     | 2 mũ 3 = 2 × 2 × 2 = 8                 |

### 🧪 Ví dụ thực hành chi tiết

```python
a = 10
b = 3

# Các phép toán cơ bản
print(f"{a} + {b} = {a + b}")   # 10 + 3 = 13
print(f"{a} - {b} = {a - b}")   # 10 - 3 = 7
print(f"{a} * {b} = {a * b}")   # 10 * 3 = 30
print(f"{a} / {b} = {a / b}")   # 10 / 3 = 3.3333333333333335

# Phép chia đặc biệt
print(f"{a} // {b} = {a // b}") # 10 // 3 = 3  (chia lấy nguyên)
print(f"{a} % {b} = {a % b}")   # 10 % 3 = 1   (chia lấy dư)

# Lũy thừa
print(f"{2} ** {10} = {2 ** 10}") # 2 ** 10 = 1024
```

### 🎓 Ứng dụng thực tế

```python
# Ví dụ 1: Tính diện tích hình tròn
ban_kinh = 5
dien_tich = 3.14159 * ban_kinh ** 2
print(f"Diện tích hình tròn bán kính {ban_kinh}: {dien_tich}")
# Kết quả: Diện tích hình tròn bán kính 5: 78.53975

# Ví dụ 2: Đổi giây sang phút và giây
tong_giay = 150
phut = tong_giay // 60  # 150 // 60 = 2 phút
giay = tong_giay % 60   # 150 % 60 = 30 giây
print(f"{tong_giay} giây = {phut} phút {giay} giây")
# Kết quả: 150 giây = 2 phút 30 giây

# Ví dụ 3: Kiểm tra số chẵn/lẻ
so = 17
if so % 2 == 0:
    print(f"{so} là số chẵn")
else:
    print(f"{so} là số lẻ")
# Kết quả: 17 là số lẻ
```

---

## 3.2. Thứ tự ưu tiên phép toán

Python thực hiện phép toán theo thứ tự ưu tiên (giống Toán học):

| Thứ tự         | Phép toán                                | Ký hiệu             |
| -------------- | ---------------------------------------- | ------------------- |
| 1️⃣ (cao nhất)  | Ngoặc                                    | `()`                |
| 2️⃣             | Lũy thừa                                 | `**`                |
| 3️⃣             | Nhân, Chia, Chia lấy nguyên, Chia lấy dư | `*`, `/`, `//`, `%` |
| 4️⃣ (thấp nhất) | Cộng, Trừ                                | `+`, `-`            |

> 💡 **Mẹo nhớ**: Khi không chắc, hãy **dùng ngoặc `()`** để rõ ràng!

```python
# Không có ngoặc — theo thứ tự ưu tiên
ket_qua_1 = 2 + 3 * 4      # = 2 + 12 = 14 (nhân trước, cộng sau)
print(ket_qua_1)             # 14

# Có ngoặc — thực hiện trong ngoặc trước
ket_qua_2 = (2 + 3) * 4    # = 5 * 4 = 20
print(ket_qua_2)             # 20

# Ví dụ phức tạp hơn
ket_qua_3 = 2 ** 3 + 4 * 2  # = 8 + 8 = 16
print(ket_qua_3)              # 16

ket_qua_4 = 2 ** (3 + 4) * 2  # = 2^7 * 2 = 128 * 2 = 256
print(ket_qua_4)                # 256
```

---

## 3.3. Phép toán so sánh (Comparison Operators)

Kết quả của phép so sánh luôn là **Boolean** (`True` hoặc `False`):

| Phép toán         | Ký hiệu | Ví dụ    | Kết quả |
| ----------------- | ------- | -------- | ------- |
| Bằng nhau         | `==`    | `5 == 5` | `True`  |
| Khác nhau         | `!=`    | `5 != 3` | `True`  |
| Lớn hơn           | `>`     | `5 > 3`  | `True`  |
| Nhỏ hơn           | `<`     | `5 < 3`  | `False` |
| Lớn hơn hoặc bằng | `>=`    | `5 >= 5` | `True`  |
| Nhỏ hơn hoặc bằng | `<=`    | `3 <= 5` | `True`  |

```python
x = 10
y = 20

print(x == y)   # False
print(x != y)   # True
print(x < y)    # True
print(x >= 10)  # True
```

> ⚠️ **Lỗi phổ biến**: Nhầm lẫn giữa `=` (gán giá trị) và `==` (so sánh)!

```python
x = 5    # Gán giá trị 5 cho biến x
x == 5   # So sánh x có bằng 5 không → True
```

---

## 3.4. Phép gán tắt (Assignment Operators)

Thay vì viết dài, Python cho phép **viết tắt**:

| Viết đầy đủ  | Viết tắt  | Ví dụ                           |
| ------------ | --------- | ------------------------------- |
| `x = x + 5`  | `x += 5`  | `x = 10` → `x += 5` → `x = 15`  |
| `x = x - 3`  | `x -= 3`  | `x = 10` → `x -= 3` → `x = 7`   |
| `x = x * 2`  | `x *= 2`  | `x = 10` → `x *= 2` → `x = 20`  |
| `x = x / 4`  | `x /= 4`  | `x = 10` → `x /= 4` → `x = 2.5` |
| `x = x ** 2` | `x **= 2` | `x = 3` → `x **= 2` → `x = 9`   |

```python
diem = 0
print(f"Điểm ban đầu: {diem}")  # 0

diem += 10   # Cộng 10 điểm
print(f"Sau khi cộng 10: {diem}")  # 10

diem += 5    # Cộng thêm 5
print(f"Sau khi cộng 5: {diem}")   # 15

diem -= 3    # Trừ 3
print(f"Sau khi trừ 3: {diem}")    # 12

diem *= 2    # Nhân đôi
print(f"Sau khi nhân 2: {diem}")   # 24
```

---

### ✅ Kiểm tra kiến thức Module 3

- [ ] Nắm được 7 phép toán số học
- [ ] Hiểu thứ tự ưu tiên phép toán
- [ ] Phân biệt được `=` (gán) và `==` (so sánh)
- [ ] Biết dùng phép gán tắt (`+=`, `-=`, `*=`...)

---

---

# Module 4: Nhập/Xuất dữ liệu (Input/Output)

## 🎯 Mục tiêu

> Biết cách **tương tác với người dùng**: nhận dữ liệu từ bàn phím và hiển thị kết quả ra màn hình.

---

## 4.1. Xuất dữ liệu — `print()` (Output)

### Cách sử dụng cơ bản

```python
# In một giá trị
print("Hello Python!")

# In nhiều giá trị (cách nhau bằng dấu phẩy)
print("Tên:", "An", "- Tuổi:", 20)
# Kết quả: Tên: An - Tuổi: 20
```

### Các cách format chuỗi khi in

#### 🏆 Cách 1: f-string (Khuyên dùng — Python 3.6+)

Đây là cách **hiện đại** và **dễ đọc nhất**:

```python
ten = "An"
tuoi = 20
diem = 9.5678

# Cách dùng cơ bản
print(f"Xin chào {ten}, bạn {tuoi} tuổi.")
# Kết quả: Xin chào An, bạn 20 tuổi.

# Tính toán trong f-string
print(f"Năm sau bạn {tuoi + 1} tuổi.")
# Kết quả: Năm sau bạn 21 tuổi.

# Định dạng số thập phân (làm tròn 2 chữ số)
print(f"Điểm trung bình: {diem:.2f}")
# Kết quả: Điểm trung bình: 9.57

# Định dạng số có dấu phân cách hàng nghìn
so_lon = 1500000
print(f"Doanh thu: {so_lon:,} VNĐ")
# Kết quả: Doanh thu: 1,500,000 VNĐ
```

#### Cách 2: Dùng `.format()`

```python
ten = "An"
tuoi = 20

print("Xin chào {}, bạn {} tuổi.".format(ten, tuoi))
# Kết quả: Xin chào An, bạn 20 tuổi.

# Hoặc dùng chỉ số
print("Xin chào {0}, bạn {1} tuổi. Đúng không {0}?".format(ten, tuoi))
# Kết quả: Xin chào An, bạn 20 tuổi. Đúng không An?
```

#### Cách 3: Dùng dấu `%` (cách cũ)

```python
ten = "An"
tuoi = 20

print("Xin chào %s, bạn %d tuổi." % (ten, tuoi))
# %s = string (chuỗi), %d = integer (số nguyên), %f = float (số thực)
```

> 💡 **Lời khuyên**: Hãy ưu tiên dùng **f-string** vì nó dễ đọc, dễ viết, và là cách hiện đại nhất!

### Tùy chỉnh `print()` nâng cao

```python
# Thay đổi ký tự ngăn cách (sep)
print("Python", "Java", "C++", sep=" | ")
# Kết quả: Python | Java | C++

print("2026", "03", "04", sep="/")
# Kết quả: 2026/03/04

# Thay đổi ký tự kết thúc (end) — mặc định là xuống dòng \n
print("Đang tải", end="")
print("...", end="")
print(" Hoàn thành!")
# Kết quả: Đang tải... Hoàn thành!

# In trên cùng 1 dòng
for i in range(5):
    print(i, end=" ")
# Kết quả: 0 1 2 3 4
```

---

## 4.2. Nhập dữ liệu — `input()` (Input)

### Cách sử dụng cơ bản

```python
ten = input("Nhập tên của bạn: ")
print(f"Xin chào {ten}!")
```

**Khi chạy:**

```
Nhập tên của bạn: An       ← Người dùng gõ "An" rồi nhấn Enter
Xin chào An!               ← Chương trình in ra kết quả
```

### ⚠️ Lưu ý QUAN TRỌNG: `input()` luôn trả về CHUỖI!

```python
# Vấn đề: input() luôn trả về kiểu str (chuỗi)
tuoi = input("Nhập tuổi: ")
print(type(tuoi))  # <class 'str'> ← Đây là chuỗi "25", KHÔNG phải số 25!

# ❌ SAI — nếu cộng sẽ bị nối chuỗi
tuoi = input("Nhập tuổi: ")       # Nhập: 25
print(tuoi + 5)                    # ❌ TypeError!

# ❌ SAI — nối chuỗi thay vì cộng số
tuoi = input("Nhập tuổi: ")       # Nhập: 25
print(tuoi + tuoi)                 # "2525" (nối chuỗi, KHÔNG phải 50!)
```

### ✅ Giải pháp: Ép kiểu dữ liệu

```python
# Nhập số nguyên
tuoi = int(input("Nhập tuổi: "))
print(type(tuoi))   # <class 'int'> ✅
print(tuoi + 5)     # 30 ✅ (cộng số đúng)

# Nhập số thực
chieu_cao = float(input("Nhập chiều cao (m): "))
print(type(chieu_cao))   # <class 'float'>

# Nhập nhiều giá trị trên cùng 1 dòng
# Ví dụ: người dùng nhập "10 20"
a, b = input("Nhập 2 số (cách nhau bằng dấu cách): ").split()
a = int(a)
b = int(b)
print(f"Tổng: {a + b}")
```

### 🛡️ Xử lý lỗi khi nhập sai (nâng cao — tham khảo)

```python
# Nếu người dùng nhập chữ thay vì số → chương trình sẽ bị lỗi!
# Cách xử lý an toàn:

try:
    tuoi = int(input("Nhập tuổi: "))
    print(f"Bạn {tuoi} tuổi.")
except ValueError:
    print("❌ Lỗi: Vui lòng nhập một số nguyên!")
```

> 💡 Đừng lo nếu chưa hiểu `try/except`, chúng ta sẽ học kỹ hơn ở các buổi sau!

---

## 4.3. Ví dụ tổng hợp

### 📝 Ví dụ: Máy tính đơn giản

```python
# === MÁY TÍNH ĐƠN GIẢN ===

print("=" * 30)
print("   MÁY TÍNH ĐƠN GIẢN")
print("=" * 30)

# Nhập 2 số
so_1 = float(input("Nhập số thứ nhất: "))
so_2 = float(input("Nhập số thứ hai: "))

# Tính toán
print(f"\n--- KẾT QUẢ ---")
print(f"{so_1} + {so_2} = {so_1 + so_2}")
print(f"{so_1} - {so_2} = {so_1 - so_2}")
print(f"{so_1} × {so_2} = {so_1 * so_2}")

if so_2 != 0:
    print(f"{so_1} ÷ {so_2} = {so_1 / so_2:.2f}")
else:
    print("Không thể chia cho 0!")
```

**Khi chạy:**

```
==============================
   MÁY TÍNH ĐƠN GIẢN
==============================
Nhập số thứ nhất: 10
Nhập số thứ hai: 3

--- KẾT QUẢ ---
10.0 + 3.0 = 13.0
10.0 - 3.0 = 7.0
10.0 × 3.0 = 30.0
10.0 ÷ 3.0 = 3.33
```

---

### ✅ Kiểm tra kiến thức Module 4

- [ ] Biết dùng `print()` để xuất dữ liệu
- [ ] Biết dùng f-string để format chuỗi
- [ ] Biết dùng `input()` để nhập dữ liệu
- [ ] Hiểu `input()` luôn trả về `str` và biết cách ép kiểu

---

---

# 📝 Bài tập thực hành tổng hợp

## 🎯 Đề bài

> Viết một chương trình nhỏ thực hiện các bước sau:
>
> 1. Yêu cầu người dùng nhập **tên**.
> 2. Yêu cầu người dùng nhập **năm sinh**.
> 3. Tính **số tuổi hiện tại** của người dùng.
> 4. In ra màn hình thông báo: **"Chào [Tên], năm nay bạn [Số tuổi] tuổi. Chúc bạn học Python vui vẻ!"**

---

## 📋 Hướng dẫn từng bước

### Bước 1: Phân tích bài toán

Trước khi viết code, hãy suy nghĩ:

```
📌 Cần nhập gì?
   → Tên (chuỗi — str)
   → Năm sinh (số nguyên — int)

📌 Cần tính gì?
   → Tuổi = Năm hiện tại - Năm sinh

📌 Cần xuất gì?
   → Câu chào có chứa tên và tuổi
```

### Bước 2: Viết code

Tạo file `bai_tap_01.py` và gõ:

```python
# ============================================
# BÀI TẬP THỰC HÀNH BUỔI 1
# Chương trình: Chào mừng & Tính tuổi
# ============================================

# Bước 1: Nhập tên
ten = input("Vui lòng nhập tên của bạn: ")

# Bước 2: Nhập năm sinh (chú ý: phải ép kiểu sang int!)
nam_sinh = int(input("Nhập năm sinh của bạn: "))

# Bước 3: Tính tuổi
nam_hien_tai = 2026  # Năm hiện tại
tuoi = nam_hien_tai - nam_sinh

# Bước 4: In kết quả
print(f"Chào {ten}, năm nay bạn {tuoi} tuổi. Chúc bạn học Python vui vẻ!")
```

### Bước 3: Chạy và kiểm tra

```
Vui lòng nhập tên của bạn: An
Nhập năm sinh của bạn: 2001
Chào An, năm nay bạn 25 tuổi. Chúc bạn học Python vui vẻ!
```

---

## 🌟 Nâng cao (Thử thách thêm)

Nếu bạn đã hoàn thành bài tập cơ bản, hãy thử **nâng cấp** chương trình:

### 🏅 Thử thách 1: Thêm thông tin

```python
# ============================================
# BÀI TẬP NÂNG CAO 1
# Thu thập thông tin cá nhân
# ============================================

print("=" * 40)
print("   CHƯƠNG TRÌNH THU THẬP THÔNG TIN")
print("=" * 40)

# Nhập thông tin
ten = input("\n👤 Nhập tên của bạn: ")
nam_sinh = int(input("📅 Nhập năm sinh: "))
thanh_pho = input("🏙️ Bạn đang sống ở đâu? ")
chieu_cao = float(input("📏 Chiều cao của bạn (cm): "))

# Tính toán
nam_hien_tai = 2026
tuoi = nam_hien_tai - nam_sinh
chieu_cao_m = chieu_cao / 100  # Đổi cm sang m

# Xuất kết quả
print("\n" + "=" * 40)
print("   📋 THÔNG TIN CÁ NHÂN")
print("=" * 40)
print(f"   Họ tên     : {ten}")
print(f"   Tuổi       : {tuoi}")
print(f"   Thành phố  : {thanh_pho}")
print(f"   Chiều cao  : {chieu_cao_m:.2f} m")
print("=" * 40)
print(f"\n🎉 Chào {ten}, chúc bạn học Python vui vẻ!")
```

**Kết quả mẫu:**

```
========================================
   CHƯƠNG TRÌNH THU THẬP THÔNG TIN
========================================

👤 Nhập tên của bạn: An
📅 Nhập năm sinh: 2001
🏙️ Bạn đang sống ở đâu? Hà Nội
📏 Chiều cao của bạn (cm): 170

========================================
   📋 THÔNG TIN CÁ NHÂN
========================================
   Họ tên     : An
   Tuổi       : 25
   Thành phố  : Hà Nội
   Chiều cao  : 1.70 m
========================================

🎉 Chào An, chúc bạn học Python vui vẻ!
```

### 🏅 Thử thách 2: Máy tính BMI

```python
# ============================================
# BÀI TẬP NÂNG CAO 2
# Tính chỉ số BMI (Body Mass Index)
# ============================================

print("🏥 CHƯƠNG TRÌNH TÍNH CHỈ SỐ BMI")
print("-" * 35)

# Nhập dữ liệu
ten = input("Nhập tên: ")
can_nang = float(input("Cân nặng (kg): "))
chieu_cao = float(input("Chiều cao (cm): "))

# Tính BMI
# Công thức: BMI = cân nặng / (chiều cao mét) ^ 2
chieu_cao_m = chieu_cao / 100
bmi = can_nang / (chieu_cao_m ** 2)

# Xuất kết quả
print(f"\n📊 Kết quả của {ten}:")
print(f"   Cân nặng  : {can_nang} kg")
print(f"   Chiều cao : {chieu_cao_m:.2f} m")
print(f"   Chỉ số BMI: {bmi:.1f}")
print(f"\n💡 Tham khảo:")
print(f"   BMI < 18.5     : Thiếu cân")
print(f"   18.5 ≤ BMI < 25: Bình thường")
print(f"   25 ≤ BMI < 30  : Thừa cân")
print(f"   BMI ≥ 30       : Béo phì")
```

### 🏅 Thử thách 3: Đổi tiền tệ

```python
# ============================================
# BÀI TẬP NÂNG CAO 3
# Chương trình đổi tiền VND ↔ USD
# ============================================

print("💰 CHƯƠNG TRÌNH ĐỔI TIỀN VND → USD")
print("-" * 35)

# Tỷ giá (tham khảo)
ty_gia = 25_450  # 1 USD = 25,450 VND

# Nhập số tiền VND
so_tien_vnd = float(input("Nhập số tiền VND: "))

# Tính toán
so_tien_usd = so_tien_vnd / ty_gia

# Xuất kết quả
print(f"\n💱 Kết quả quy đổi:")
print(f"   {so_tien_vnd:,.0f} VND = {so_tien_usd:,.2f} USD")
print(f"   (Tỷ giá: 1 USD = {ty_gia:,} VND)")
```

---

## 📌 Checklist tổng kết Buổi 1

Hãy tự đánh giá — bạn đã nắm được bao nhiêu?

| #   | Nội dung                                                     | Trạng thái |
| --- | ------------------------------------------------------------ | ---------- |
| 1   | Cài đặt Python thành công                                    | ⬜         |
| 2   | Cài đặt VS Code + Extension Python                           | ⬜         |
| 3   | Viết và chạy được chương trình `hello.py`                    | ⬜         |
| 4   | Hiểu khái niệm **biến** và cách khai báo                     | ⬜         |
| 5   | Phân biệt 4 kiểu dữ liệu: `int`, `float`, `str`, `bool`      | ⬜         |
| 6   | Biết dùng `type()` kiểm tra kiểu dữ liệu                     | ⬜         |
| 7   | Biết ép kiểu: `int()`, `float()`, `str()`                    | ⬜         |
| 8   | Thực hiện các phép toán: `+`, `-`, `*`, `/`, `//`, `%`, `**` | ⬜         |
| 9   | Hiểu thứ tự ưu tiên phép toán                                | ⬜         |
| 10  | Dùng `print()` và f-string để in dữ liệu                     | ⬜         |
| 11  | Dùng `input()` để nhập dữ liệu từ bàn phím                   | ⬜         |
| 12  | Hiểu `input()` trả về `str` và biết cách ép kiểu             | ⬜         |
| 13  | Hoàn thành bài tập thực hành tổng hợp                        | ⬜         |

---

# 📚 Tài liệu tham khảo thêm

| Nguồn                | Link                                                      | Ghi chú             |
| -------------------- | --------------------------------------------------------- | ------------------- |
| Python Official Docs | [docs.python.org](https://docs.python.org/3/)             | Tài liệu chính thức |
| W3Schools Python     | [w3schools.com/python](https://www.w3schools.com/python/) | Tutorial dễ hiểu    |
| Real Python          | [realpython.com](https://realpython.com/)                 | Bài viết chuyên sâu |
| Python Tutor         | [pythontutor.com](https://pythontutor.com/)               | Trực quan hóa code  |

---

> **📢 Hẹn gặp lại ở Buổi 2!**
>
> Ở buổi tiếp theo, chúng ta sẽ học về **Câu lệnh điều kiện (if/elif/else)** và **Vòng lặp (for/while)** — hai công cụ giúp chương trình của bạn "thông minh" hơn! 🚀

---

_© 2026 — Giáo trình Python | Biên soạn cho lớp học KITE_
