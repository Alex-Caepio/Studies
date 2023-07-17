spam, ham = 'yum', 'YUM'
print(spam, ham, sep=', ', end='!\n')

[spam, ham] = ['yum', 'YUM']
print(spam, ham, sep=', ', end='!\n')

a, b, c = 'spa'

print(a, b, c, sep=', ', end='!\n')

a, *b = 'spam'
print(a, b, sep=', ', end='!\n')

spam = ham = 'lunch'
print(spam, ham, sep=', ', end='!\n')

a = 1

b = 2

a, b = b, a

print(a, b, sep=', ', end='!\n')

result = f'{a} + {b} = {a + b}'
print(result)

my_string = 'Helo {name}, {greeting}'.format(name='John', greeting='hi')
print(my_string)

name = 'Oleg'
name_1 = 'Oleg'
name_2 = 'Petr'
name_3 = 'Sergei'

print(5) if name == 'Oleg' else print(10)

name = 'Oleg'  # True
name = ''  # False
name = ' '  # True
name = 2  # True
name = 0  # False
name = 0.0  # False
name = 0.1  # True
name = None  # False
name = []  # False
name = [1, 2, 3]  # True
name = {}  # False
name = {'name': 'Oleg'}  # True
name = ()  # False
name = (1, 2, 3)  # True

a = 'a'
b = 'b'

c = a == b

if c:
    print('Equal')
else:
    print('Not equal')

name = 'Oleg'
surname = 'Liasota'

name_2 = 'Petr'
surname_2 = 'Petrov'

if (name == 'Oleg2' and surname == 'Liasota') and (name_2 == 'Petr' and surname_2 == 'Petrov'):
    print('Equal')
else:
    print('Not equal')

res = name == 'Oleg1' and surname == 'Liasota'
print(res)

a = 10

while a > 0:
    print(a)
    a -= 1

a = range(1, 6)

for item in a:
    if item == 2:
        continue
    if item == 4:
        break
    print(item)

a = [1, 2, 3, 4, 5]
a = b
b = [1, 2, 3, 4, 5, 6]

print(a)
