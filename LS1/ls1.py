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