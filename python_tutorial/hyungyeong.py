import random
def get_user_input():
    while True:
        player_input = input('=' * 40+'\n가위, 바위, 보? ')
        if player_input in option:
            break
        else:
            print('다시 입력하세요')
    return player_input

    
score = 0
while True:
    option = ['가위', '바위', '보']
    player_input = get_user_input()
    computer = random.randint(0, 2)
    computer_input = option[computer]
    print('컴퓨터는 {0}를 내고, 당신은 {1}을 냈습니다.'.format(computer_input, player_input))
    if computer_input == player_input:
        print('비겼습니다')
    elif computer_input == "가위":
        if player_input == "바위":
            score += 1
            print('이겼습니다')
        elif player_input == "보":
            print('졌습니다')
    elif computer_input == "바위":
        if player_input == "보":
            score += 1
            print('이겼습니다')
        elif player_input == "가위":
            print('졌습니다')
    elif computer_input == "보":
        if player_input == "가위":
            score += 1
            print('이겼습니다.')
        elif player_input == "바위":
            print('졌습니다')
    else:
        print('예상치 못한 경우 발생')
    if score == 5:
        print('당신은 가위바위보의 신입니다!')
        print('=' * 40)
        break
    print('현재 점수는 {0}입니다.'.format(score))
    print('=' * 40)