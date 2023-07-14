tuple_1 = (1, 2, 3)
tuple_2 = ('one', 'hello')
tuple_3 = (3, 2.3, 'three')

print(tuple_1, tuple_2, tuple_3, sep='///', end='\n!!!!!\n')
print(tuple_1[1])

new_tuple = (tuple_1[0], 3, tuple_1[2])
print(new_tuple)

x, y, z = 12, 13, 14
print(x, y, z)

first_name, last_name, date_of_birth = ('John', 'Smith', 1986)
print(first_name, last_name, date_of_birth)

tuple_4 = (1, 2, 5, 1, 7, 9)
print(tuple_4.count(1))

greetings_tuple = ('hi', 'hello', 'hi', 'hey')
print(greetings_tuple.count('hi'))

print(tuple_4.index(1))
print(greetings_tuple.index('hi'))

print(len([1, 2] * 4))
