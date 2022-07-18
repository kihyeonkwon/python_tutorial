class Car:
    def __init__(self, owner):
        self.handle = 0
        self.car_type = "normal"
        self.owner = owner

    def turn_left(self):
        self.handle -= 90
        print("핸들 각도: ", self.handle)

    def turn_right(self):
        self.handle += 90
        print("핸들 각도: ", self.handle)

    def show_status(self):
        print("owner:", self.owner)
        print("car_type:", self.car_type)


class Van(Car):
    def __init__(self, owner):
        super().__init__(owner)
        self.door = "closed"
        self.car_type = "van"

    def open_door(self):
        self.door = "open"
        print("문을 열었습니다.")

    def close_door(self):
        self.door = "closed"
        print("문을 닫았습니다.")


myVan = Van("기현")
myVan.show_status()

myVan.turn_left()
myVan.turn_right()
