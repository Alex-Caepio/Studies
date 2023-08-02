func = lambda x=int(input('Введите число: ')): 'чётное' if x % 2 == 0 else 'нечётное'
print(func())

numbers = [5, 2, 8, 1, 6]
sorted_numbers = sorted(numbers, key=lambda x: x % 2)
print(sorted_numbers)  # Выведет: [2, 8, 6, 5, 1]

# is_even_odd = lambda x: 'четное' if x % 2 == 0 else 'нечетное'
#
# number1 = 10
# number2 = 7
#
# print(is_even_odd(number1))
# print(is_even_odd(number2))

a: tuple = 'ДеД', 'дерево', 'шалаш', 'кабак'
res = tuple(filter(lambda x: x == x[::-1], a))
print(res)
