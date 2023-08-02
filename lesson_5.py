from functools import reduce


def calculate():
    """This function calculates the sum of two numbers"""
    return 5 + 10


print(calculate.__doc__)

res = lambda x, y: x + y

print(res(5, 10))

res = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in res:
    print(i + 1)

res = [i + 1 for i in res]
print(res)

print(list(map(lambda x: x + 1, res)))

print(list(filter(lambda x: x % 2 == 0, res)))

my_list = [-10, 1, 2, 3, -7, 4, 5, 6, 7, 8, 9]


def decor(func):
    def wrapper(x):
        print("До выполнения функции")
        result = list(map(lambda x: x * 2 + 10, my_list))
        func(result)

    return wrapper


def decor_1(func):
    def wrapper(x):
        print("До выполнения функции")
        result = list(filter(lambda x: x < 0, my_list))
        func(result)

    return wrapper


def decor_2(func):
    def wrapper(x):
        print("До выполнения функции")
        result = reduce(lambda x, y: (x + y) * 2, my_list)
        func(result)

    return wrapper


@decor
def calc_1(list_obj: list):
    print(list_obj)


@decor_1
def calc_2(list_obj: list):
    print(list_obj)


@decor_2
def calc_3(list_obj: list):
    print(list_obj)


calc_1(my_list)
calc_2(my_list)
calc_3(my_list)


def calc_2(list_obj: list):
    print(list_obj)


def calc_3(list_obj: list):
    print(list_obj)
