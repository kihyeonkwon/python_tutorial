def my_function(name, greetings):
    sentence = name + "님" + greetings
    print(sentence)
    return sentence


name = input("이름 입력해주세요 : ")
greetings = input("인삿말 : ")
a = my_function(name, greetings)
print(a)
