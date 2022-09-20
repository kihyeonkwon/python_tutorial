import random
import get_input

option = ["가위", "바위", "보"]
computer = random.randint(0, 2)
computer_value = option[computer]
user_value = get_input.get_user_value()


print(f"플레이어는 {user_value}를 선택, 컴퓨터는 {computer_value}를 선택했습니다")
if computer_value == user_value:
    print("비겼습니다")
elif user_value == "가위":
    if computer_value == "바위":
        print("졌습니다")
    else:
        print("이겼습니다")
elif user_value == "바위":
    if computer_value == "보":
        print("졌습니다")
    else:
        print("이겼습니다")
elif user_value == "보":
    if computer_value == "가위":
        print("졌습니다")
    else:
        print("이겼습니다")
else:
    print("예상치 못한 경우입니다.")
