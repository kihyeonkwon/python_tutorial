import random

score = 0
while True: 
    option = ['가위', '바위', '보']
    while True:
        player_value = input('가위 바위 보?')
        if player_value in option:
            break
        print('값을 정확히 입력해주세요!')

    computer = random.randint(0, 2)
    computer_value = option[computer]


    print(f'플레이어는 {player_value}를 선택, 컴퓨터는 {computer_value}를 선택했습니다')

    if computer_value == player_value:
        print('비겼습니다')
    elif player_value == '가위':
        if computer_value == '바위':
            print('졌습니다')
        else:
            score = score + 1
            print('이겼습니다')

    elif player_value == '바위':
        if computer_value == '보':
            print('졌습니다')
        
        else:
            score = score + 1
            print('이겼습니다')
        
    elif player_value == '보':
        if computer_value == '가위':
            print('졌습니다')
        
        else:
            score = score + 1
            print('이겼습니다')
    else:
        print("예상치 못한 경우 발생")

    
    print(f"현재 점수는 {score}입니다.")
    if score >=5 :
        print('가위바위보의 신!!!')
        break
