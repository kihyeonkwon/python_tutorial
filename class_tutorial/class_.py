class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0
    def accelerate(self):
        self.speed += 10
    def brake(self):
        self.speed -= 10
    def get_speed(self):
        return self.speed
    
car = Car("소나타", "빨간색")
car.accelerate()
car.speed = 'sldjflas'
car.accelerate()



