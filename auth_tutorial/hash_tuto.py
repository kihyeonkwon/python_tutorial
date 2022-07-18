password = 29
hashed_password = 29%4
y = int(input())
hashed_input = y%4

if hashed_password == hashed_input:
    print("로그인 성공")