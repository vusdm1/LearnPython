print("💰 CHƯƠNG TRÌNH ĐỔI TIỀN VND → USD")
print("-" * 35)
print("------------------------------------")

ty_gia=25_450

so_tien_vnd= float(input("Nhập Số Tiền VND:  "))
so_tien_usd= so_tien_vnd/ty_gia


print(f"\n💱 Kết quả quy đổi:")
print(f"   {so_tien_vnd:,.0f} VND = {so_tien_usd:,.2f} USD")
print(f"   (Tỷ giá: 1 USD = {ty_gia:,} VND)")