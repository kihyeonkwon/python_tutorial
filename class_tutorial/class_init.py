class Person:
    def __init__(self, first):
        self.name = first


class Korean(Person):
    def __init__(self, first,  second):
        super().__init__(first)
        self.registration_number = second


korean1 = Korean("윤선", "020520")
print(korean1.registration_number)
print(korean1.name)
