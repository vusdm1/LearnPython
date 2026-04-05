# 📝 Bài tập thực hành MỚI — Tổng hợp Buổi 1, 2, 3

> 🎯 **Lưu ý:** Các bài tập dưới đây kết hợp kiến thức từ cả 3 buổi học:
> - **Buổi 1:** Biến, kiểu dữ liệu, phép toán, input/output, f-string
> - **Buổi 2:** if/elif/else, toán tử so sánh & logic, điều kiện lồng nhau
> - **Buổi 3:** Hàm, tham số, return, biến cục bộ, tách bài toán thành hàm
>
> 📄 **Lời giải** được đặt riêng trong file: `Buoi_03_Loi_Giai_Moi.md`

---

## 📌 Bài 1: Hệ thống tính cước phí gửi xe _(Trung bình)_

```
📋 Bối cảnh:
Bãi giữ xe thông minh tính phí theo loại xe và thời gian gửi.

Bảng giá (tính theo giờ):
- Xe đạp:
  + 2 giờ đầu: Miễn phí
  + Từ giờ thứ 3 trở đi: 2,000 đ/giờ
- Xe máy:
  + 1 giờ đầu: 5,000 đ
  + Từ giờ thứ 2 đến giờ thứ 4: 3,000 đ/giờ
  + Từ giờ thứ 5 trở đi: 5,000 đ/giờ
- Ô tô:
  + 1 giờ đầu: 20,000 đ
  + Từ giờ thứ 2 đến giờ thứ 3: 10,000 đ/giờ
  + Từ giờ thứ 4 trở đi: 15,000 đ/giờ

Giảm giá:
- Gửi ban đêm (sau 22h): giảm 30%
- Khách VIP: giảm thêm 10% trên tổng

📝 Yêu cầu:
1. Viết hàm `tinh_phi_gui_xe(loai_xe, so_gio)` → trả về phí TRƯỚC giảm giá
2. Viết hàm `ap_dung_giam_gia(phi, ban_dem, la_vip)` → trả về phí SAU giảm giá
3. Viết hàm `ten_loai_xe(ma_xe)` → đổi mã ("xd", "xm", "ot") thành tên đầy đủ
4. Viết hàm `in_ve_xe(ten_khach, loai_xe, so_gio, ban_dem, la_vip)` → in vé
5. Chương trình chính: nhập thông tin → tính phí → in vé

📌 Ví dụ kết quả mong đợi:
╔══════════════════════════════════╗
║       VÉ GIỮ XE THÔNG MINH      ║
╠══════════════════════════════════╣
║ Khách hàng : Trần Văn B          ║
║ Loại xe    : Xe máy               ║
║ Thời gian  : 6 giờ                ║
║ Phí gốc    : 21,000 đồng          ║
║ Giảm giá   : 2,100 đồng           ║
║ Thành tiền : 18,900 đồng          ║
╚══════════════════════════════════╝
```

---

## 📌 Bài 2: Máy tính điểm trung bình có hệ số _(Trung bình)_

```
📋 Bối cảnh:
Giáo viên cần chương trình tính điểm trung bình có hệ số cho học sinh.

Quy tắc tính:
- Điểm miệng (hệ số 1): 1 cột
- Điểm 15 phút (hệ số 1): 1 cột
- Điểm 1 tiết (hệ số 2): 1 cột
- Điểm thi cuối kỳ (hệ số 3): 1 cột

Công thức: ĐTB = (miệng×1 + 15p×1 + 1tiết×2 + thi×3) / 7

Xếp loại:
- ĐTB ≥ 9.0 → "Xuất sắc 🌟"
- ĐTB ≥ 8.0 → "Giỏi 🥇"
- ĐTB ≥ 6.5 → "Khá 🥈"
- ĐTB ≥ 5.0 → "Trung bình 🥉"
- ĐTB ≥ 3.5 → "Yếu ⚠️"
- ĐTB < 3.5 → "Kém ❌"

Nhận xét đặc biệt:
- Nếu điểm thi ≥ 8.0 VÀ ĐTB ≥ 7.0 → "📈 Tiến bộ rõ rệt!"
- Nếu điểm thi < điểm miệng - 2 → "📉 Cần ôn tập kỹ hơn!"

📝 Yêu cầu:
1. Viết hàm `nhap_diem(ten_cot)` → nhập điểm, kiểm tra 0-10, trả về điểm
2. Viết hàm `tinh_dtb_he_so(mieng, muoi_lam, mot_tiet, thi)` → trả về ĐTB
3. Viết hàm `xep_loai(dtb)` → trả về chuỗi xếp loại
4. Viết hàm `nhan_xet(mieng, thi, dtb)` → trả về nhận xét đặc biệt
5. Viết hàm `in_phieu_diem(ten_hs, ten_mon, mieng, muoi_lam, mot_tiet, thi)`
   → in phiếu điểm hoàn chỉnh
```

---

## 📌 Bài 3: Trạm xăng tự động _(Trung bình)_

```
📋 Bối cảnh:
Trạm xăng cần chương trình tính tiền cho khách hàng.

Bảng giá nhiên liệu (đ/lít):
- Xăng RON 95: 25,670
- Xăng RON 92: 23,820
- Dầu Diesel: 21,350

Chương trình khuyến mãi:
- Mua từ 30 lít trở lên: giảm 500đ/lít
- Mua từ 50 lít trở lên: giảm 800đ/lít
- Khách có thẻ thành viên: tích lũy 1% giá trị đơn hàng (tính điểm)

Hình thức thanh toán:
- Tiền mặt: không phụ thu
- Thẻ ngân hàng: phụ thu 1%

📝 Yêu cầu:
1. Viết hàm `lay_gia_nhien_lieu(loai)` → trả về giá/lít, -1 nếu không hợp lệ
2. Viết hàm `tinh_giam_gia_lit(so_lit)` → trả về số tiền giảm trên mỗi lít
3. Viết hàm `tinh_tien(loai, so_lit)` → trả về (tiền gốc, tiền sau giảm)
4. Viết hàm `tinh_tich_luy(tien, co_the_tv)` → trả về điểm tích lũy
5. Viết hàm `tinh_phu_thu(tien, hinh_thuc)` → trả về tiền phụ thu
6. Viết hàm `in_hoa_don_xang(ten_khach, loai, so_lit, co_the_tv, hinh_thuc)`
   → in hóa đơn đầy đủ
```

---

## 📌 Bài 4: Chương trình đặt vé xem phim _(Nâng cao)_

```
📋 Bối cảnh:
Rạp chiếu phim cần hệ thống đặt vé đơn giản.

Bảng giá vé (1 vé):
- Phim 2D: 65,000 đồng
- Phim 3D: 95,000 đồng
- Phim IMAX: 150,000 đồng

Phụ thu theo suất chiếu:
- Suất sáng (trước 12h): Không phụ thu
- Suất chiều (12h - 17h): Phụ thu 10,000đ/vé
- Suất tối (sau 17h): Phụ thu 20,000đ/vé

Giảm giá theo đối tượng:
- Học sinh/sinh viên: giảm 20%
- Người cao tuổi (≥ 60 tuổi): giảm 30%
- Trẻ em (< 6 tuổi): Miễn phí

Combo bắp nước:
- Combo A (Bắp nhỏ + Nước nhỏ): 49,000đ
- Combo B (Bắp lớn + 2 Nước): 79,000đ
- Không mua combo: 0đ

📝 Yêu cầu:
1. Viết hàm `gia_ve_co_ban(loai_phim)` → trả về giá vé, -1 nếu không hợp lệ
2. Viết hàm `phu_thu_suat_chieu(suat)` → trả về tiền phụ thu/vé
3. Viết hàm `giam_gia_doi_tuong(tuoi, la_hoc_sinh)` → trả về % giảm (0.0 - 1.0)
4. Viết hàm `gia_combo(ma_combo)` → trả về giá combo
5. Viết hàm `tinh_tien_ve(loai_phim, suat, tuoi, la_hs, so_ve, ma_combo)`
   → trả về tổng tiền
6. Viết hàm `in_ve_phim(ten_khach, ...)` → in vé phim đẹp
7. Chương trình chính: hiển thị menu → nhập thông tin → in vé
```

---

## 📌 Bài 5: Hệ thống kiểm tra sức khỏe mini _(Nâng cao)_

```
📋 Bối cảnh:
Trạm y tế trường học cần chương trình kiểm tra nhanh sức khỏe
học sinh dựa trên các chỉ số cơ bản.

Chỉ số cần kiểm tra:
1. Nhịp tim (lần/phút):
   - < 60: "Nhịp tim chậm ⚠️"
   - 60-100: "Bình thường ✅"
   - > 100: "Nhịp tim nhanh ⚠️"

2. Huyết áp (mmHg - tâm thu/tâm trương):
   - Tâm thu < 90: "Huyết áp thấp ⚠️"
   - 90-120 tâm thu VÀ 60-80 tâm trương: "Bình thường ✅"
   - 121-139 tâm thu HOẶC 81-89 tâm trương: "Tiền cao HA"
   - ≥ 140 tâm thu HOẶC ≥ 90 tâm trương: "Cao huyết áp 🔴"

3. Thân nhiệt (°C):
   - < 35.0: "Hạ thân nhiệt 🔴"
   - 35.0-37.2: "Bình thường ✅"
   - 37.3-38.0: "Sốt nhẹ ⚠️"
   - 38.1-39.0: "Sốt vừa 🔴"
   - > 39.0: "Sốt cao! Cần đi bệnh viện 🚨"

Đánh giá tổng thể:
- Tất cả bình thường → "🟢 Sức khỏe tốt!"
- Có 1 chỉ số bất thường → "🟡 Cần theo dõi"
- Có 2 chỉ số bất thường trở lên → "🔴 Cần khám bác sĩ ngay"

📝 Yêu cầu:
1. Viết hàm `kiem_tra_nhip_tim(nhip_tim)` → trả về (trang_thai, binh_thuong)
   (binh_thuong = True/False)
2. Viết hàm `kiem_tra_huyet_ap(tam_thu, tam_truong)` → trả về (trang_thai, binh_thuong)
3. Viết hàm `kiem_tra_than_nhiet(nhiet_do)` → trả về (trang_thai, binh_thuong)
4. Viết hàm `danh_gia_tong_the(bt_nhip, bt_ha, bt_nhiet)` → trả về đánh giá
5. Viết hàm `loi_khuyen_suc_khoe(trang_thai_nhip, trang_thai_ha, trang_thai_nhiet)`
   → trả về chuỗi lời khuyên tổng hợp
6. Viết hàm `in_phieu_kham(ten_hs, lop, ...)` → in phiếu khám sức khỏe
```

---

## 📌 Bài 6: Ứng dụng chia bill nhà hàng _(Nâng cao)_

```
📋 Bối cảnh:
Nhóm bạn đi ăn nhà hàng và cần chia bill. Chương trình giúp
tính tiền mỗi người phải trả.

Quy tắc:
- Tổng hóa đơn do người dùng nhập
- Thuế VAT: 8%
- Phí dịch vụ: 5% (tính trên giá trước thuế)
- Tip (tiền boa): người dùng chọn
  + Không tip: 0%
  + Tip ít: 5%
  + Tip vừa: 10%
  + Tip nhiều: 15%

Cách chia:
- Chia đều cho N người
- Nếu có người được miễn (VD: người được mời), tính riêng

Quy tắc làm tròn:
- Nếu kết quả lẻ, làm tròn LÊN hàng nghìn
  VD: 87,350đ → 88,000đ

📝 Yêu cầu:
1. Viết hàm `tinh_thue(tien_goc, thue_suat=0.08)` → tiền thuế
2. Viết hàm `tinh_phi_dich_vu(tien_goc, phi=0.05)` → tiền phí DV
3. Viết hàm `tinh_tip(tien_goc, muc_tip)` → tiền tip
   (muc_tip: 0, 1, 2, 3 tương ứng 0%, 5%, 10%, 15%)
4. Viết hàm `tinh_tong_bill(tien_goc, muc_tip)` → tổng sau thuế + phí + tip
5. Viết hàm `lam_tron_len(so_tien)` → làm tròn lên hàng nghìn
6. Viết hàm `chia_bill(tong, so_nguoi, so_mien)` → số tiền mỗi người trả
7. Viết hàm `in_bill(tien_goc, so_nguoi, so_mien, muc_tip)` → in bill đẹp
```

---

## 📌 Bài 7: Hệ thống tính cước taxi _(Nâng cao)_

```
📋 Bối cảnh:
Hãng taxi cần chương trình tính cước phí cho khách.

Bảng cước (đ/km):
- 1 km đầu tiên (mở cửa): 15,000 đ
- Từ km 2 đến km 30: 13,500 đ/km
- Từ km 31 trở đi: 11,000 đ/km

Phụ phí:
- Giờ cao điểm (7h-9h, 17h-19h): phụ thu 25%
- Ban đêm (22h-5h): phụ thu 30%
- Giờ bình thường: không phụ thu
- Phí cầu đường (nếu có): do người dùng nhập

Loại xe:
- "4_cho": hệ số 1.0
- "7_cho": hệ số 1.3
- "vip": hệ số 1.8

Chương trình thành viên:
- Khách thường: không giảm
- Thành viên Bạc (≥ 10 chuyến): giảm 5%
- Thành viên Vàng (≥ 50 chuyến): giảm 10%
- Thành viên Kim Cương (≥ 100 chuyến): giảm 15%

📝 Yêu cầu:
1. Viết hàm `tinh_cuoc_co_ban(so_km)` → cước theo bảng giá
2. Viết hàm `he_so_gio(gio_di)` → trả về hệ số phụ thu (1.0, 1.25, 1.3)
3. Viết hàm `he_so_loai_xe(loai_xe)` → trả về hệ số xe
4. Viết hàm `giam_gia_thanh_vien(so_chuyen)` → trả về % giảm
5. Viết hàm `tinh_cuoc_tong(so_km, gio_di, loai_xe, so_chuyen, phi_cau_duong)`
   → tổng cước
6. Viết hàm `in_hoa_don_taxi(ten_khach, ...)` → in hóa đơn taxi
```

---

## 📌 Bài 8: Chương trình tư vấn gói cước điện thoại _(Thử thách)_

```
📋 Bối cảnh:
Nhà mạng cần chương trình tư vấn gói cước cho khách hàng
dựa trên nhu cầu sử dụng.

Các gói cước:
- Gói TIẾT KIỆM (TK49): 49,000đ/tháng
  + 2GB data tốc độ cao
  + 50 phút gọi nội mạng
  + 0 phút ngoại mạng
  + 30 SMS

- Gói PHỔ THÔNG (PT79): 79,000đ/tháng
  + 5GB data tốc độ cao
  + 200 phút gọi nội mạng
  + 50 phút ngoại mạng
  + 50 SMS

- Gói CAO CẤP (CC129): 129,000đ/tháng
  + 15GB data tốc độ cao
  + Gọi nội mạng không giới hạn
  + 200 phút ngoại mạng
  + SMS không giới hạn

- Gói VIP (VIP199): 199,000đ/tháng
  + Data không giới hạn
  + Gọi tất cả mạng không giới hạn
  + SMS không giới hạn

Cước phát sinh (nếu dùng quá gói):
- Data thêm: 30,000đ/GB
- Gọi thêm nội mạng: 890đ/phút
- Gọi thêm ngoại mạng: 1,490đ/phút
- SMS thêm: 350đ/tin

📝 Yêu cầu:
1. Viết hàm `thong_tin_goi(ten_goi)` → trả về (gia, data_gb, noi_mang, ngoai_mang, sms)
   Trả về (-1, 0, 0, 0, 0) nếu gói không tồn tại
2. Viết hàm `tinh_cuoc_phat_sinh(ten_goi, data_dung, goi_noi, goi_ngoai, sms_dung)`
   → trả về tiền phát sinh
3. Viết hàm `tinh_tong_cuoc(ten_goi, data_dung, goi_noi, goi_ngoai, sms_dung)`
   → trả về tổng cước tháng
4. Viết hàm `tu_van_goi(data_can, goi_noi_can, goi_ngoai_can, sms_can)`
   → trả về tên gói phù hợp nhất (gói rẻ nhất mà đủ nhu cầu)
5. Viết hàm `so_sanh_2_goi(goi_1, goi_2, data_dung, goi_noi, goi_ngoai, sms_dung)`
   → trả về tên gói rẻ hơn và chênh lệch
6. Viết hàm `in_bang_cuoc(ten_khach, ten_goi, data_dung, goi_noi, goi_ngoai, sms_dung)`
   → in bảng cước chi tiết
```

---

_📌 Bài tập bổ sung cho Buổi 3 — Giáo trình Python | KITE_
