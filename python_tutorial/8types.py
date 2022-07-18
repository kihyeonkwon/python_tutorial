class Person:
    def talk(self):
        print("안녕하세요 저는" + self.name +"입니다.")

    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby


x = Person("김동근", "20", "피아노")
x.talk()
print(x.name)