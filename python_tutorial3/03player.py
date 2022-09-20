possible_values = ["가위", "바위", "보"]

while True:
    player_value = input("가위, 바위, 보 중에서 내주세요")

    if player_value in possible_values:
        break
    else:
        print("제대로 입력하세요.")

print(player_value, "를 선택했습니다!")
print("게임 진행")
