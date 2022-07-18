def my_function(name):
  intro = name + "님" +  " 안녕하세요"
  outro = name + "님" +  " 잘가세요" 
  print("상관없는 아무말")
  return outro


name = input("이름 입력해주세요 : ")
amuguna = my_function(name)

print(amuguna)


