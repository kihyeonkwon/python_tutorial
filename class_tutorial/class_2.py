class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("동물 makes a noise.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print("멍멍")
        
coco = Dog("코코")
coco.bark()
coco.speak()