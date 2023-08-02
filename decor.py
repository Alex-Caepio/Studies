from functools import reduce

list_obj = [-10, 1, 2, 3, -7, 4, 5, 6, 7, 8, 9]


def decor(func):
    def wrapper(x):
        result = list(map(lambda a: a * 2 + 10, x))
        func(result)

    return wrapper


@decor
def calc_1(list_obj: list):
    print(list_obj)


calc_1(list_obj)


def decor_1(func):
    def wrapper(x):
        result = list(filter(lambda x: x < 0, x))
        func(result)

    return wrapper


def decor_2(func):
    def wrapper(x):
        result = reduce(lambda x, y: (x + y) * 2, x)
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


calc_2(list_obj)
calc_3(list_obj)
