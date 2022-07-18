class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius 
        self.area = radius * radius * self.pi

    def getCircumference(self):
        return self.radius * self.pi * 2

c = Circle(5)

print('반지름은 : ',c.radius)
print('넓이는 : ',c.area)
print('둘레는 : ',c.getCircumference())
