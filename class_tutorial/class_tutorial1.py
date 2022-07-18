class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):
        self.speed = 60

    def __str__(self):
        return f"{self.color}색의 {self.model} 모델의 차"


myCar = Car(0, "blue", "E-Class")
yourCar = Car(0, "white", "S-Class")

print(myCar.speed)
print(yourCar.speed)
myCar.drive()
print(myCar.speed)
print(yourCar.speed)
yourCar.drive()
print(myCar.speed)
print(yourCar.speed)


otherCar = Car(0, "white", "S-Class")
print(myCar)
print(yourCar)
print(otherCar)


print(id(myCar))
print(id(yourCar))
print(id(otherCar))
