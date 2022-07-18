class Circle():
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        self.area = radius * radius * self.pi

    def getCircumference(self):
        circumference = 2 * self.radius * self.pi
        return circumference

ljkdsjvklsdf = Circle(5)

print('반지름은 : ', ljkdsjvklsdf.radius)
print('넓이는 : ', ljkdsjvklsdf.area)
print('둘레는 : ', ljkdsjvklsdf.getCircumference())