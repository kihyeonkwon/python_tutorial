import random

score = 0

while True:
    option = ['가위', '바위', '보']
    computer = random.randint(0, 2)
    computer_value = option[computer]

    while True : 
        player_value = input('가위 바위 보?')
        if player_value in option:
            break
        print('제대로 입력바람!!!')


    print(f'플레이어는 {player_value}를 선택, 컴퓨터는 {computer_value}를 선택했습니다')
    if computer_value == player_value:
        print('비겼습니다')
    elif player_value == '가위':
        if computer_value == '바위':
            print('졌습니다')
        else:
            score += 1
            print('이겼습니다')
    elif player_value == '바위':
        if computer_value == '보':
            print('졌습니다')
        else:
            score += 1
            print('이겼습니다')
    elif player_value == '보':
        if computer_value == '가위':
            print('졌습니다')
        else:
            score += 1
            print('이겼습니다')
    print(f'현재 스코어는 {score}')

    if score>10:
        print('승리했습니다! 가위바위보의 신!')
        break
