# List Dict Set
my_list = [1, 2, 3]
print(id(my_list))
new_list = my_list
print(id(new_list))

my_list[0] = 4
print(my_list)
print(new_list)
