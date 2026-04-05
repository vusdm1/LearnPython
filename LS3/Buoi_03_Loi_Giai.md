# 📝 LỜI GIẢI — Bài tập nâng cao Buổi 3

> 📌 **File đề bài:** `Buoi_03_Ham_Trong_Python.md` (phần Bài tập thực hành nâng cao)

---

---

## 📌 Bài 1: Hệ thống tính tiền điện hàng tháng

<details>
<summary>💡 Xem lời giải</summary>

```python
def tinh_tien_dien(so_kwh):
    """Tính tiền điện theo bậc thang, trả về tiền TRƯỚC thuế."""
    tien = 0

    if so_kwh <= 50:
        tien = so_kwh * 1678
    elif so_kwh <= 100:
        tien = 50 * 1678 + (so_kwh - 50) * 1734
    elif so_kwh <= 200:
        tien = 50 * 1678 + 50 * 1734 + (so_kwh - 100) * 2014
    elif so_kwh <= 300:
        tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + (so_kwh - 200) * 2536
    else:
        tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (so_kwh - 300) * 2834

    return tien


def tinh_thue(so_tien, thue_suat=0.08):
    """Tính tiền thuế VAT."""
    return so_tien * thue_suat


def in_hoa_don(ten_kh, so_kwh):
    """In hóa đơn tiền điện đẹp ra màn hình."""
    tien_dien = tinh_tien_dien(so_kwh)
    thue = tinh_thue(tien_dien)
    tong = tien_dien + thue

    print("╔══════════════════════════════════╗")
    print("║      HÓA ĐƠN TIỀN ĐIỆN         ║")
    print("╠══════════════════════════════════╣")
    print(f"║ Khách hàng : {ten_kh}")
    print(f"║ Số điện    : {so_kwh} kWh")
    print(f"║ Tiền điện  : {tien_dien:,.0f} đồng")
    print(f"║ Thuế VAT   : {thue:,.0f} đồng")
    print(f"║ Tổng cộng  : {tong:,.0f} đồng")
    print("╚══════════════════════════════════╝")


# === CHƯƠNG TRÌNH CHÍNH ===
ten = input("Nhập tên khách hàng: ")
kwh = float(input("Nhập số kWh tiêu thụ: "))

if kwh < 0:
    print("❌ Số kWh không hợp lệ!")
else:
    in_hoa_don(ten, kwh)
```

</details>

---

## 📌 Bài 2: Máy tính chỉ số BMI thông minh

<details>
<summary>💡 Xem lời giải</summary>

```python
def kiem_tra_du_lieu(can_nang, chieu_cao):
    """Kiểm tra dữ liệu đầu vào hợp lệ."""
    if can_nang <= 0:
        return False
    if chieu_cao <= 0 or chieu_cao >= 300:
        return False
    return True


def tinh_bmi(can_nang, chieu_cao_cm):
    """Tính chỉ số BMI. Chiều cao nhập bằng cm, đổi sang m."""
    chieu_cao_m = chieu_cao_cm / 100
    bmi = can_nang / (chieu_cao_m ** 2)
    return bmi


def phan_loai_bmi(bmi):
    """Phân loại BMI theo chuẩn WHO."""
    if bmi < 16.0:
        return "Gầy độ III (Nguy hiểm) 🔴"
    elif bmi < 17.0:
        return "Gầy độ II ⚠️"
    elif bmi < 18.5:
        return "Gầy độ I"
    elif bmi < 25.0:
        return "Bình thường ✅"
    elif bmi < 30.0:
        return "Thừa cân ⚠️"
    elif bmi < 35.0:
        return "Béo phì độ I 🔴"
    else:
        return "Béo phì độ II (Nguy hiểm) 🔴"


def loi_khuyen(phan_loai):
    """Đưa ra lời khuyên dựa trên phân loại."""
    if "Gầy" in phan_loai:
        return "💬 Bạn nên tăng cường dinh dưỡng và ăn uống đầy đủ hơn."
    elif "Bình thường" in phan_loai:
        return "💬 Tuyệt vời! Hãy duy trì chế độ ăn uống và tập luyện hiện tại."
    elif "Thừa cân" in phan_loai:
        return "💬 Bạn nên tập thể dục thường xuyên và giảm đồ ăn nhiều dầu mỡ."
    else:
        return "💬 Bạn nên đi khám bác sĩ để được tư vấn chế độ ăn phù hợp."


# === CHƯƠNG TRÌNH CHÍNH ===
print("🏥 CHƯƠNG TRÌNH TÍNH CHỈ SỐ BMI")
print("=" * 35)

can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (cm): "))

if kiem_tra_du_lieu(can_nang, chieu_cao):
    bmi = tinh_bmi(can_nang, chieu_cao)
    loai = phan_loai_bmi(bmi)
    khuyen = loi_khuyen(loai)

    print(f"\n📊 Kết quả:")
    print(f"   Chỉ số BMI : {bmi:.1f}")
    print(f"   Phân loại  : {loai}")
    print(f"   {khuyen}")
else:
    print("❌ Dữ liệu không hợp lệ! Vui lòng kiểm tra lại.")
```

</details>

---

## 📌 Bài 3: Chương trình đổi tiền tệ

<details>
<summary>💡 Xem lời giải</summary>

```python
def lay_ty_gia(loai_tien):
    """Trả về tỷ giá quy đổi sang VNĐ. Trả -1 nếu không hỗ trợ."""
    if loai_tien == "USD":
        return 25450
    elif loai_tien == "EUR":
        return 27200
    elif loai_tien == "JPY":
        return 168
    elif loai_tien == "KRW":
        return 18.5
    else:
        return -1


def tinh_phi(so_luong):
    """Trả về phần trăm phí dịch vụ."""
    if so_luong < 100:
        return 0.02
    elif so_luong < 1000:
        return 0.015
    else:
        return 0.01


def doi_tien(so_luong, loai_tien):
    """Đổi ngoại tệ sang VNĐ sau khi trừ phí. Trả -1 nếu loại tiền không hợp lệ."""
    ty_gia = lay_ty_gia(loai_tien)
    if ty_gia == -1:
        return -1

    tong_vnd = so_luong * ty_gia
    phi = tinh_phi(so_luong)
    tien_phi = tong_vnd * phi
    tien_nhan = tong_vnd - tien_phi

    return tien_nhan


def in_phieu_doi(ten_khach, so_luong, loai_tien):
    """In phiếu đổi tiền."""
    ty_gia = lay_ty_gia(loai_tien)

    if ty_gia == -1:
        print(f"❌ Loại tiền '{loai_tien}' không được hỗ trợ!")
        return

    phi = tinh_phi(so_luong)
    tong_vnd = so_luong * ty_gia
    tien_phi = tong_vnd * phi
    tien_nhan = doi_tien(so_luong, loai_tien)

    print("\n" + "=" * 40)
    print("   💱 PHIẾU ĐỔI TIỀN TỆ")
    print("=" * 40)
    print(f"   Khách hàng  : {ten_khach}")
    print(f"   Loại tiền   : {loai_tien}")
    print(f"   Số lượng    : {so_luong:,.2f} {loai_tien}")
    print(f"   Tỷ giá      : 1 {loai_tien} = {ty_gia:,.1f} VNĐ")
    print(f"   Thành tiền  : {tong_vnd:,.0f} VNĐ")
    print(f"   Phí DV ({phi*100:.1f}%): {tien_phi:,.0f} VNĐ")
    print("-" * 40)
    print(f"   💰 THỰC NHẬN : {tien_nhan:,.0f} VNĐ")
    print("=" * 40)


# === CHƯƠNG TRÌNH CHÍNH ===
print("💱 QUẦY ĐỔI TIỀN SÂN BAY")
print("-" * 30)
print("Loại tiền hỗ trợ:")
print("1. USD (Đô la Mỹ)")
print("2. EUR (Euro)")
print("3. JPY (Yên Nhật)")
print("4. KRW (Won Hàn Quốc)")

lua_chon = input("\nChọn loại tiền (1-4): ")

if lua_chon == "1":
    loai = "USD"
elif lua_chon == "2":
    loai = "EUR"
elif lua_chon == "3":
    loai = "JPY"
elif lua_chon == "4":
    loai = "KRW"
else:
    print("❌ Lựa chọn không hợp lệ!")
    loai = ""

if loai != "":
    ten = input("Nhập tên khách hàng: ")
    so_luong = float(input(f"Nhập số {loai} cần đổi: "))

    if so_luong <= 0:
        print("❌ Số lượng phải lớn hơn 0!")
    else:
        in_phieu_doi(ten, so_luong, loai)
```

</details>

---

## 📌 Bài 4: Hệ thống xếp hạng học sinh cuối kỳ

<details>
<summary>💡 Xem lời giải</summary>

```python
def nhap_diem(ten_mon):
    """Nhập điểm và kiểm tra hợp lệ (0-10). Trả -1 nếu không hợp lệ."""
    diem = float(input(f"Nhập điểm {ten_mon}: "))
    if diem < 0 or diem > 10:
        print(f"❌ Điểm {ten_mon} không hợp lệ! Phải từ 0 đến 10.")
        return -1
    return diem


def tinh_dtb(toan, van, anh, ly, hoa):
    """Tính điểm trung bình 5 môn."""
    return (toan + van + anh + ly + hoa) / 5


def diem_thap_nhat(toan, van, anh, ly, hoa):
    """Tìm điểm thấp nhất trong 5 môn."""
    diem_min = toan
    if van < diem_min:
        diem_min = van
    if anh < diem_min:
        diem_min = anh
    if ly < diem_min:
        diem_min = ly
    if hoa < diem_min:
        diem_min = hoa
    return diem_min


def dem_diem_cao(toan, van, anh, ly, hoa):
    """Đếm số môn có điểm >= 9.0."""
    dem = 0
    if toan >= 9.0:
        dem += 1
    if van >= 9.0:
        dem += 1
    if anh >= 9.0:
        dem += 1
    if ly >= 9.0:
        dem += 1
    if hoa >= 9.0:
        dem += 1
    return dem


def xep_loai(dtb, diem_min):
    """Xếp loại học lực dựa trên ĐTB và điểm thấp nhất."""
    if dtb >= 8.0 and diem_min >= 6.5:
        return "Giỏi 🥇"
    elif dtb >= 6.5 and diem_min >= 5.0:
        return "Khá 🥈"
    elif dtb >= 5.0 and diem_min >= 3.5:
        return "Trung bình 🥉"
    elif dtb >= 3.5:
        return "Yếu ⚠️"
    else:
        return "Kém ❌"


def kiem_tra_danh_hieu(toan, van, anh, ly, hoa):
    """Kiểm tra danh hiệu đặc biệt."""
    danh_hieu = ""

    so_mon_cao = dem_diem_cao(toan, van, anh, ly, hoa)
    if so_mon_cao >= 3:
        danh_hieu = danh_hieu + "⭐ Học sinh xuất sắc  "

    if toan >= 9.0 and anh >= 9.0:
        danh_hieu = danh_hieu + "🏆 Ứng viên học bổng"

    if danh_hieu == "":
        danh_hieu = "Không có"

    return danh_hieu


def in_bang_diem(ten, toan, van, anh, ly, hoa):
    """In bảng điểm hoàn chỉnh."""
    dtb = tinh_dtb(toan, van, anh, ly, hoa)
    diem_min = diem_thap_nhat(toan, van, anh, ly, hoa)
    hoc_luc = xep_loai(dtb, diem_min)
    danh_hieu = kiem_tra_danh_hieu(toan, van, anh, ly, hoa)

    print("\n" + "=" * 40)
    print("   📋 BẢNG ĐIỂM HỌC SINH")
    print("=" * 40)
    print(f"   Họ tên     : {ten}")
    print("-" * 40)
    print(f"   Toán       : {toan}")
    print(f"   Văn        : {van}")
    print(f"   Anh        : {anh}")
    print(f"   Lý         : {ly}")
    print(f"   Hóa        : {hoa}")
    print("-" * 40)
    print(f"   ĐTB        : {dtb:.2f}")
    print(f"   Xếp loại   : {hoc_luc}")
    print(f"   Danh hiệu  : {danh_hieu}")
    print("=" * 40)


# === CHƯƠNG TRÌNH CHÍNH ===
print("🏫 HỆ THỐNG XẾP HẠNG HỌC SINH")
print("-" * 35)

ten_hs = input("Nhập họ tên học sinh: ")

toan = nhap_diem("Toán")
van = nhap_diem("Văn")
anh = nhap_diem("Anh")
ly = nhap_diem("Lý")
hoa = nhap_diem("Hóa")

# Kiểm tra tất cả điểm hợp lệ
if toan == -1 or van == -1 or anh == -1 or ly == -1 or hoa == -1:
    print("\n❌ Có điểm không hợp lệ! Không thể xếp loại.")
else:
    in_bang_diem(ten_hs, toan, van, anh, ly, hoa)
```

</details>

---

## 📌 Bài 5: Trò chơi "Đoán số bí mật"

<details>
<summary>💡 Xem lời giải</summary>

```python
def tao_so_bi_mat():
    """Trả về số bí mật (cố định vì chưa học random)."""
    return 42


def kiem_tra_du_doan(du_doan, so_bi_mat):
    """Kiểm tra dự đoán so với số bí mật."""
    if du_doan == so_bi_mat:
        return "🎯 Chính xác!"
    elif du_doan > so_bi_mat:
        return "📈 Quá cao!"
    else:
        return "📉 Quá thấp!"


def tinh_do_chinh_xac(du_doan, so_bi_mat):
    """Tính phần trăm chính xác."""
    do_lech = du_doan - so_bi_mat

    # Tính giá trị tuyệt đối không dùng abs()
    if do_lech < 0:
        do_lech = -do_lech

    do_chinh_xac = 100 - do_lech

    if do_chinh_xac < 0:
        return 0
    return do_chinh_xac


def xep_hang_nguoi_choi(do_chinh_xac):
    """Xếp hạng người chơi dựa trên độ chính xác."""
    if do_chinh_xac == 100:
        return "🏆 Thiên tài!"
    elif do_chinh_xac >= 90:
        return "⭐ Rất giỏi!"
    elif do_chinh_xac >= 70:
        return "👍 Khá tốt!"
    elif do_chinh_xac >= 50:
        return "🤔 Tạm được"
    else:
        return "😅 Cần cố gắng hơn"


# === CHƯƠNG TRÌNH CHÍNH ===
print("🎮 TRÒ CHƠI ĐOÁN SỐ BÍ MẬT")
print("=" * 35)
print("Luật chơi: Đoán một số từ 1 đến 100.")
print("Bạn có 1 lần đoán. Chúc may mắn!\n")

ten_nguoi_choi = input("Nhập tên của bạn: ")
print(f"\nChào {ten_nguoi_choi}! Hãy đoán số bí mật nhé!")

du_doan = int(input("Nhập số dự đoán (1-100): "))
so_bi_mat = tao_so_bi_mat()

ket_qua = kiem_tra_du_doan(du_doan, so_bi_mat)
do_cx = tinh_do_chinh_xac(du_doan, so_bi_mat)
hang = xep_hang_nguoi_choi(do_cx)

print(f"\n📊 KẾT QUẢ:")
print(f"   Số bí mật      : {so_bi_mat}")
print(f"   Bạn đoán       : {du_doan}")
print(f"   Kết quả        : {ket_qua}")
print(f"   Độ chính xác   : {do_cx:.0f}%")
print(f"   Xếp hạng       : {hang}")
```

</details>

---

## 📌 Bài 6: Ứng dụng quản lý chi tiêu cá nhân

<details>
<summary>💡 Xem lời giải</summary>

```python
def nhap_chi_tieu(loai):
    """Nhập số tiền chi tiêu, kiểm tra >= 0."""
    so_tien = float(input(f"  Nhập chi tiêu {loai}: "))
    if so_tien < 0:
        print(f"  ⚠️ Số tiền không hợp lệ! Đặt về 0.")
        return 0
    return so_tien


def tinh_tong(an_uong, di_lai, giai_tri, hoc_tap, khac):
    """Tính tổng chi tiêu."""
    return an_uong + di_lai + giai_tri + hoc_tap + khac


def tinh_phan_tram(so_tien, tong):
    """Tính phần trăm, làm tròn 1 chữ số."""
    if tong == 0:
        return 0.0
    phan_tram = (so_tien / tong) * 100
    return round(phan_tram, 1)


def danh_gia_chi_tieu(an_uong, giai_tri, tong):
    """Đánh giá tổng hợp chi tiêu."""
    danh_gia = ""

    if an_uong > 200000:
        danh_gia = danh_gia + "⚠️ Ăn uống hơi nhiều. "

    if giai_tri > 100000:
        danh_gia = danh_gia + "⚠️ Giải trí hơi nhiều. "

    if tong > 500000:
        danh_gia = danh_gia + "🚨 Chi tiêu vượt ngân sách!"
    elif tong <= 300000:
        danh_gia = danh_gia + "✅ Chi tiêu tiết kiệm!"
    else:
        danh_gia = danh_gia + "👍 Chi tiêu hợp lý."

    return danh_gia


def in_bao_cao(an_uong, di_lai, giai_tri, hoc_tap, khac):
    """In báo cáo chi tiêu đầy đủ."""
    tong = tinh_tong(an_uong, di_lai, giai_tri, hoc_tap, khac)

    print("\n" + "=" * 45)
    print("   💰 BÁO CÁO CHI TIÊU TRONG NGÀY")
    print("=" * 45)
    print(f"   🍜 Ăn uống   : {an_uong:>10,.0f}đ ({tinh_phan_tram(an_uong, tong)}%)")
    print(f"   🚗 Di lại    : {di_lai:>10,.0f}đ ({tinh_phan_tram(di_lai, tong)}%)")
    print(f"   🎮 Giải trí  : {giai_tri:>10,.0f}đ ({tinh_phan_tram(giai_tri, tong)}%)")
    print(f"   📚 Học tập   : {hoc_tap:>10,.0f}đ ({tinh_phan_tram(hoc_tap, tong)}%)")
    print(f"   📦 Khác      : {khac:>10,.0f}đ ({tinh_phan_tram(khac, tong)}%)")
    print("-" * 45)
    print(f"   💵 TỔNG CỘNG : {tong:>10,.0f}đ")
    print("-" * 45)

    danh_gia = danh_gia_chi_tieu(an_uong, giai_tri, tong)
    print(f"   📝 Đánh giá  : {danh_gia}")
    print("=" * 45)


# === CHƯƠNG TRÌNH CHÍNH ===
print("💰 QUẢN LÝ CHI TIÊU CÁ NHÂN")
print("-" * 35)
print("Nhập chi tiêu cho từng mục:\n")

an_uong = nhap_chi_tieu("Ăn uống")
di_lai = nhap_chi_tieu("Di lại")
giai_tri = nhap_chi_tieu("Giải trí")
hoc_tap = nhap_chi_tieu("Học tập")
khac = nhap_chi_tieu("Khác")

in_bao_cao(an_uong, di_lai, giai_tri, hoc_tap, khac)
```

</details>

---

## 📌 Bài 7: Chương trình tính lương nhân viên

<details>
<summary>💡 Xem lời giải</summary>

```python
def tinh_luong_co_ban(so_gio, don_gia):
    """Tính lương cơ bản, có tính OT nếu làm trên 8 giờ."""
    if so_gio <= 8:
        return so_gio * don_gia
    else:
        luong_thuong = 8 * don_gia
        luong_ot = (so_gio - 8) * don_gia * 1.5
        return luong_thuong + luong_ot


def lay_phu_cap(chuc_vu):
    """Trả về phụ cấp theo chức vụ."""
    if chuc_vu == "nhan_vien":
        return 0
    elif chuc_vu == "to_truong":
        return 500000
    elif chuc_vu == "quan_ly":
        return 1500000
    else:
        return 0


def tinh_bao_hiem(luong_co_ban):
    """Tính khấu trừ bảo hiểm 10.5% trên lương cơ bản."""
    return luong_co_ban * 0.105


def tinh_thue_thu_nhap(tong_thu_nhap):
    """Tính thuế thu nhập cá nhân."""
    if tong_thu_nhap < 5000000:
        return 0
    elif tong_thu_nhap < 10000000:
        return tong_thu_nhap * 0.05
    else:
        return tong_thu_nhap * 0.10


def tinh_luong_thuc_nhan(so_gio, don_gia, chuc_vu):
    """Tính lương thực nhận sau các khoản khấu trừ."""
    luong_cb = tinh_luong_co_ban(so_gio, don_gia)
    phu_cap = lay_phu_cap(chuc_vu)
    tong_thu_nhap = luong_cb + phu_cap

    bao_hiem = tinh_bao_hiem(luong_cb)
    thue = tinh_thue_thu_nhap(tong_thu_nhap)

    thuc_nhan = tong_thu_nhap - bao_hiem - thue
    return thuc_nhan


def in_phieu_luong(ten, so_gio, don_gia, chuc_vu):
    """In phiếu lương chi tiết."""
    luong_cb = tinh_luong_co_ban(so_gio, don_gia)
    phu_cap = lay_phu_cap(chuc_vu)
    tong_thu_nhap = luong_cb + phu_cap
    bao_hiem = tinh_bao_hiem(luong_cb)
    thue = tinh_thue_thu_nhap(tong_thu_nhap)
    thuc_nhan = tinh_luong_thuc_nhan(so_gio, don_gia, chuc_vu)

    # Xác định tên chức vụ để hiển thị
    if chuc_vu == "nhan_vien":
        ten_cv = "Nhân viên"
    elif chuc_vu == "to_truong":
        ten_cv = "Tổ trưởng"
    elif chuc_vu == "quan_ly":
        ten_cv = "Quản lý"
    else:
        ten_cv = "Không xác định"

    print("\n" + "=" * 45)
    print("   📄 PHIẾU LƯƠNG NHÂN VIÊN")
    print("=" * 45)
    print(f"   Họ tên      : {ten}")
    print(f"   Chức vụ     : {ten_cv}")
    print(f"   Số giờ làm  : {so_gio} giờ")
    print(f"   Đơn giá     : {don_gia:,.0f} đ/giờ")
    print("-" * 45)
    print(f"   Lương cơ bản : {luong_cb:>12,.0f} đ")
    print(f"   Phụ cấp      : {phu_cap:>12,.0f} đ")
    print(f"   Tổng thu nhập: {tong_thu_nhap:>12,.0f} đ")
    print("-" * 45)
    print(f"   Bảo hiểm     : -{bao_hiem:>11,.0f} đ")
    print(f"   Thuế TNCN    : -{thue:>11,.0f} đ")
    print("=" * 45)
    print(f"   💰 THỰC NHẬN : {thuc_nhan:>12,.0f} đ")
    print("=" * 45)


# === CHƯƠNG TRÌNH CHÍNH ===
print("📄 HỆ THỐNG TÍNH LƯƠNG")
print("-" * 30)

ten_nv = input("Nhập tên nhân viên: ")
so_gio = float(input("Số giờ làm việc: "))
don_gia = float(input("Đơn giá/giờ (VNĐ): "))

print("\nChọn chức vụ:")
print("1. Nhân viên")
print("2. Tổ trưởng")
print("3. Quản lý")
lc = input("Chọn (1-3): ")

if lc == "1":
    chuc_vu = "nhan_vien"
elif lc == "2":
    chuc_vu = "to_truong"
elif lc == "3":
    chuc_vu = "quan_ly"
else:
    print("❌ Lựa chọn không hợp lệ!")
    chuc_vu = ""

if chuc_vu != "" and so_gio > 0 and don_gia > 0:
    in_phieu_luong(ten_nv, so_gio, don_gia, chuc_vu)
else:
    if chuc_vu != "":
        print("❌ Số giờ và đơn giá phải lớn hơn 0!")
```

</details>

---

## 📌 Bài 8: Hệ thống đăng ký tài khoản đơn giản

<details>
<summary>💡 Xem lời giải</summary>

```python
def kiem_tra_ten(ten_dang_nhap):
    """Kiểm tra tên đăng nhập hợp lệ. Trả về (True/False, thông_báo)."""
    if len(ten_dang_nhap) < 4:
        return False, "Tên quá ngắn! Cần ít nhất 4 ký tự."

    if len(ten_dang_nhap) > 20:
        return False, "Tên quá dài! Tối đa 20 ký tự."

    if " " in ten_dang_nhap:
        return False, "Tên không được chứa khoảng trắng!"

    return True, "✅ Tên đăng nhập hợp lệ."


def kiem_tra_mat_khau(mat_khau, ten_dang_nhap):
    """Kiểm tra mật khẩu hợp lệ. Trả về (True/False, thông_báo)."""
    if len(mat_khau) < 6:
        return False, "Mật khẩu quá ngắn! Cần ít nhất 6 ký tự."

    if mat_khau == ten_dang_nhap:
        return False, "Mật khẩu không được giống tên đăng nhập!"

    return True, "✅ Mật khẩu hợp lệ."


def kiem_tra_email(email):
    """Kiểm tra email hợp lệ. Trả về (True/False, thông_báo)."""
    if " " in email:
        return False, "Email không được chứa khoảng trắng!"

    if "@" not in email:
        return False, "Email phải chứa ký tự '@'!"

    if "." not in email:
        return False, "Email phải chứa dấu '.'!"

    return True, "✅ Email hợp lệ."


def kiem_tra_tuoi(tuoi):
    """Kiểm tra tuổi hợp lệ. Trả về (True/False, thông_báo)."""
    if tuoi < 13:
        return False, f"Bạn chưa đủ tuổi! Cần ít nhất 13 tuổi (hiện tại: {tuoi})."

    return True, "✅ Tuổi hợp lệ."


def dang_ky():
    """Hàm chính điều phối quy trình đăng ký."""
    print("📝 ĐĂNG KÝ TÀI KHOẢN MỚI")
    print("=" * 35)

    # --- Bước 1: Nhập tên đăng nhập ---
    ten_dn = input("\n🔹 Tên đăng nhập: ")
    ten_ok, ten_msg = kiem_tra_ten(ten_dn)

    # --- Bước 2: Nhập mật khẩu ---
    mk = input("🔹 Mật khẩu: ")
    mk_ok, mk_msg = kiem_tra_mat_khau(mk, ten_dn)

    # Kiểm tra nhập lại mật khẩu
    mk_xac_nhan = False
    if mk_ok:
        mk2 = input("🔹 Nhập lại mật khẩu: ")
        if mk != mk2:
            mk_ok = False
            mk_msg = "Mật khẩu nhập lại không khớp!"
        else:
            mk_xac_nhan = True

    # --- Bước 3: Nhập email ---
    email = input("🔹 Email: ")
    email_ok, email_msg = kiem_tra_email(email)

    # --- Bước 4: Nhập tuổi ---
    tuoi = int(input("🔹 Tuổi: "))
    tuoi_ok, tuoi_msg = kiem_tra_tuoi(tuoi)

    # --- Bước 5: Tổng hợp kết quả ---
    print("\n" + "=" * 35)
    print("📋 KẾT QUẢ KIỂM TRA:")
    print("-" * 35)
    print(f"   Tên ĐN  : {ten_msg}")
    print(f"   Mật khẩu: {mk_msg}")
    print(f"   Email   : {email_msg}")
    print(f"   Tuổi    : {tuoi_msg}")
    print("-" * 35)

    if ten_ok and mk_ok and email_ok and tuoi_ok:
        print("\n🎉 ĐĂNG KÝ THÀNH CÔNG!")
        print(f"   Chào mừng {ten_dn} đến với hệ thống!")
    else:
        # Đếm số lỗi
        so_loi = 0
        if not ten_ok:
            so_loi += 1
        if not mk_ok:
            so_loi += 1
        if not email_ok:
            so_loi += 1
        if not tuoi_ok:
            so_loi += 1

        print(f"\n❌ ĐĂNG KÝ THẤT BẠI! Có {so_loi} lỗi cần sửa.")
        print("   Vui lòng kiểm tra lại thông tin ở trên.")


# === CHẠY CHƯƠNG TRÌNH ===
dang_ky()
```

</details>

---

_📌 Lời giải tham khảo cho Buổi 3 — Giáo trình Python | KITE_
