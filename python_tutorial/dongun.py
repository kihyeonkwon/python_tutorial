class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.area = radius * radius * self.pi

    def getCircumference(self):
        circumference = 2 * self.radius * self.pi
        return circumference


c = Circle(5)
c2 = Circle(10)
c3 = Circle(15)


print("반지름은 : ", c.radius)
print("넓이는 : ", c.area)
print("둘레는 : ", c.getCircumference())

print("반지름은 : ", c2.radius)
print("넓이는 : ", c2.area)
print("둘레는 : ", c2.getCircumference())

print("반지름은 : ", c3.radius)
print("넓이는 : ", c3.area)
print("둘레는 : ", c3.getCircumference())
