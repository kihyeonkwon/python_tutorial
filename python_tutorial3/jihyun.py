from get_input import picked

com_win_count = 0
user_win_count = 0

while com_win_count < 2 and user_win_count < 2:

    com_pick, user_pick = picked()  # 호출한 함수에서 전달받은 두 개의 값을 각각 변수에 할당
    result = [com_pick, user_pick]  # 각 값을 리스트로 묶어줌
    print(f"computer: {com_pick} vs user: {user_pick}")  # 정답 확인용 코드

    # 순서 : com_pick, user_pick / 사용자가 승리할 경우의 가짓수을 저장
    user_win_case = [["바위", "보"], ["가위", "바위"], ["보", "가위"]]

    if com_pick == user_pick:  # 컴퓨터의 선택과 사용자의 선택이 똑같다면
        print("무승부입니다.")

    elif result in user_win_case:  # 사용자가 승리할 경우의 가짓수를 담은 리스트 안에 일치하는 값이 있다면
        print("이겼습니다.")
        user_win_count += 1

    else:
        print("졌습니다.")
        com_win_count += 1

    print(f"현재 스코어는 computer: {com_win_count} vs user: {user_win_count} 입니다.")
