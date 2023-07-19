def welcome(name, end123='!'):
    return f"Привет, {name}{end123}"


print(welcome(end123="!!!", name="Вася"))
print(welcome("Петя"))
print(welcome("Маша"))
print(welcome("Даша"))
print(welcome("Саша"))
print(welcome("Глаша"))
print(welcome("Катя"))
print(welcome("Коля"))
print(welcome("Ваня"))


def datetime():
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y %H:%M")


print(datetime())

c = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
res = {'1': 1, '2': 2, '3': 3}


def arguments(*args, **kwargs):
    print(args)
    print(kwargs)


arguments(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, name="Вася", age=20, city="Москва")
arguments(*c, **res)

n = 100


def func(n):
    print(n)
    if n < 0:
        return
    func(n - 1)


func(n)

c = '1234567890'


# make sum of all numbers in string c with recursion
def sum_of_numbers(c):
    if len(c) == 1:
        return int(c)
    return int(c[0]) + sum_of_numbers(c[1:])


print(sum_of_numbers(c))

a_list = [i for i in range(1, 100) if i % 10 == 0]
