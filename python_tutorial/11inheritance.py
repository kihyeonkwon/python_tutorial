class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")


class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("Cat created")

    def whoAmI(self):
        print("Meow!")


dog = Dog()
cat = Cat()
dog.whoAmI()
cat.whoAmI()
