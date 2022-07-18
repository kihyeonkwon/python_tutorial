# def my_sum(a, b, c, d, e):
#     result = a + b + c + d, e
#     return result


# a = 1
# b = 2
# c = 3
# d = 4
# e = 6
# print(my_sum(a, b, c, d, e ))


def my_sum(*args):
    result = 0
    print(args[1])
    for x in args:
        result += x
    return result


print(my_sum(1, 2, 3, 4, 5, 6, 7))
