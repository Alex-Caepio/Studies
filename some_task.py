my_list = [2, 3, 6, 10]

my_list.append(8)

my_list[2] = 3

my_tuple = tuple(my_list)

print(my_tuple)

my_dict = {'Василий': 100, 'Петр': 'долг 200'}

my_dict['Ян'] = 100

my_dict['Василий'] = 50

del my_dict['Петр']

print(my_dict)

oleg_debt = my_dict.get('Олег', 0)

print(oleg_debt)
