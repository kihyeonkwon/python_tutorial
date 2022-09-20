class Person:
    species = "homo sapiens"
    age = 0

    def walk(self, destination):
        print(destination, "으로 걷고 있습니다.")

    def talk(self, something):
        print(something, "이라고 말했습니다.")


person1 = Person()

person1.walk("서울")


# print(Person.species)
# person1.walk()
