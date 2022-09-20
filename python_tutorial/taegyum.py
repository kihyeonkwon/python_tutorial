import random
import get_input
option = ['가위', '바위', '보']

computer_select = option[random.randrange(0, 3)]
person_select = get_input.get_person_select()
print(f'사용자는{person_select}는 입력하였고 컴퓨터는 {computer_select}는 선택하였습니다.')


if person_select == '가위':
    if computer_select == '가위':
        print('비겼습니다.')
    elif computer_select == '바위':
        print('당신은 졌습니다.')
    else:
        print('당신은 이겼습니다.')
elif person_select == '바위':
    if computer_select == '가위':
        print('당신은 이겼습니다')
    elif computer_select == '바위':
        print('비겼습니다.')
    else:
        print('당신은 졌습니다.')
else:
    if computer_select == '가위':
        print('당신은 졌습니다')
    elif computer_select == '바위':
        print('당신은 이겼습니다.')
    else:
        print('비겼습니다.')
