# def hello(name):
#     greetings = "안녕하세요 " + name + "님"
#     print(greetings)
#     print("뭘하든지간에")
#     return greetings


# your_name = input()
# result = hello(your_name)
# print(result)


def hello(name):
    greetings = "안녕하세요 " + name + "님"
    return greetings


def howareyou(greetings):
    greetings += " 잘 지내시나요?"
    return greetings


your_name = input()
result = hello(your_name)
result = howareyou(result)

print(result)

# my_number = 42
# my_str_number = str(42)
# print(my_str_number)

# print(result)
