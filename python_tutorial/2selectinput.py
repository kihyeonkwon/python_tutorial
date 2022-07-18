option = ['가위', '바위', '보']

while True:
    player_value = input('가위 바위 보 중에서 골라주세요')
    if player_value in option:
        break
    else:
        print('값을 정확히 입력해주세요!')


print(f'{player_value}를 고르셨네요ㅎㅎ')

