class Car:

    def drive(self):
        self.speed = 60

    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def __str__(self):
        return f"{self.color}색의 {self.model} 모델의 차고 현재 속도는 {self.speed}입니다."


myCar = Car(0, "blue", "E-Class")
yourCar = Car(0, "white", "S-Class")

print(myCar.speed)
print(yourCar.speed)
myCar.drive()
print(myCar.speed)
yourCar.speed = 70
print(yourCar.speed)
# yourCar.drive()
# print(myCar.speed)
# print(yourCar.speed)


# otherCar = Car(30, "red", "bus")
# print(myCar)
# print(yourCar)
# print(otherCar)


# print(hex(id(myCar)))
# print(hex(id(yourCar)))
# print(hex(id(otherCar)))
