class Person:
    def talk(self):
        print("안녕하세요 저는" + self.name + "입니다.")
        print("제 나이는" + self.age + "입니다.")
        print("제 취미는" + self.hobby + "입니다.")
        print()

    def __init__(self, name, age, hobby):
        print("이닛 함수 실행중")
        self.name = name
        self.age = age
        self.hobby = hobby


x = Person("권기현", "20", "피아노")
y = Person("오형석", "20", "기타")
z = Person("정형빈", "20", "캐스터넷츠")

x.talk()
y.talk()
z.talk()

# members = []

# members.append(x)
# members.append(y)
# members.append(z)

# for member in members:
#     print(member.name)
#     print(member.age)
#     print(member.hobby)
