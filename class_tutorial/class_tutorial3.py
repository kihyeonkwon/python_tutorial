class Car:
    def __init__(self, owner):
        print("car의 __init__ 실행중")
        self.handle = 0
        self.car_type = "normal"
        self.owner = owner
        print("car의 __init__ 끝")

    def turn_left(self):
        self.handle -= 90
        print("핸들 각도: ", self.handle)

    def turn_right(self):
        self.handle += 90
        print("핸들 각도: ", self.handle)

    def show_status(self):
        print("car_type:", self.car_type)
        print("handle :", self.handle)


myCar = Car("나")


class Van(Car):

    def __init__(self, owner):
        super().__init__(owner)

    def turn_left(self):
        self.handle -= 45
        print("핸들 각도: ", self.handle)


myVan = Van("나")
myVan.show_status()
