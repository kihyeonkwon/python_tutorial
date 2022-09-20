from random import randint

row1 = ["■", "■", "■"]
row2 = ["■", "■", "■"]
row3 = ["■", "■", "■"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

count = 0
real_hor = randint(1, 3)
real_ver = randint(1, 3)
while True:
    count += 1
    position = input("where do you want to put the treasure?")

    horizonal = int(position[0])  # 1
    vertical = int(position[1])  # 2
    selected_row = map[vertical - 1]
    if horizonal == real_hor and vertical == real_ver:
        selected_row[horizonal - 1] = "O"
        print(f"{row1}\n{row2}\n{row3}")
        print(f"축하합니다 {count}만에 성공!")
        break
    else:
        selected_row[horizonal - 1] = "X"
        print(f"{row1}\n{row2}\n{row3}")
