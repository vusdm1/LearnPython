import random

player = input("kéo / búa / bao: ").strip()

if player not in ["kéo", "búa", "bao"]:
    print("Lựa chọn không hợp lệ!")
else:
    computer = random.choice(["kéo", "búa", "bao"])

    print("Máy:", computer)

    if player == computer:
        print("Hòa")
    elif player == "kéo" and computer == "bao":
        print("Bạn thắng")
    elif player == "búa" and computer == "kéo":
        print("Bạn thắng")
    elif player == "bao" and computer == "búa":
        print("Bạn thắng")
    else:
        print("Bạn thua")
