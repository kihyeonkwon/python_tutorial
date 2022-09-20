
option = ['가위', '바위', '보']


def get_person_select():
    while True:
        person_select = input('가위, 바위, 보 중에서 선택해주세요')
        if person_select in option:
            break
        else:
            print('값을 정확하게 입력해주시기 바랍니다')
        return 1
