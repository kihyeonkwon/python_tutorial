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
        print("owner: ", self.owner)
        print("car_type:", self.car_type)
        print("handle :", self.handle)


class Van(Car):
    def __init__(self, owner):
        print("van의 __init__ 실행시작")
        super().__init__(owner)
        self.backdoor = "closed"
        self.car_type = "van"
        print("van의 __init__ 실행끝")

    def open_door(self):
        self.backdoor = "open"

    def close_door(self):
        self.backdoor = "closed"

    def show_status(self):
        print("owner: ", self.owner)
        print("car_type:", self.car_type)
        print("handle :", self.handle)
        print("backdoor :", self.backdoor)


# myCar = Car("강기훈")
# myCar.show_status()
myVan = Van("강기훈")
myVan.show_status()
# myVan.show_status()

myCar = Car("임동근")
myCar.show_status()
