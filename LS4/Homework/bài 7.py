so_bi_mat = 37  
max_lan = 7       

print(" TRÒ CHƠI ĐOÁN SỐ (1-100)")
print("Bạn có", max_lan, "lượt đoán. Chúc may mắn!\n")

for turn in range(1, max_lan + 1):
    guess = int(input(f"Lượt {turn}/{max_lan} — Nhập số: "))
    
    if guess == so_bi_mat:
        print(f" CHÍNH XÁC! Bạn đoán đúng sau {turn} lượt!")
        break
    
    elif guess > so_bi_mat:
        print(f" Số bí mật THẤP HƠN {guess}")
    
    else:
        print(f" Số bí mật CAO HƠN {guess}")
    if turn == max_lan:
        print(f"\n Hết lượt! Số bí mật là {so_bi_mat}. Chúc bạn may mắn lần sau!")