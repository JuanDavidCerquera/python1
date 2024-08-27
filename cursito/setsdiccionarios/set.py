my_set = {'python', 'java', 'c++'}
print(type(my_set))
print(my_set)

my_set.add('hola')
print(my_set)
my_set.add('c#')
print(my_set)
my_set.add('hola')
print(my_set)
my_set.add('hola')
print(my_set)


my_set_2 = {'python', 'java', 'c++'}


my_set.difference_update(my_set_2)

print(my_set)