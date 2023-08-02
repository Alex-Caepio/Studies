from random import choice


def product(n, func):
    result = 1
    for number in range(1, n):
        result *= func(number)
    return result


def square(x):
    return x * x


def cube(x):
    return x ** 3


print(product(3, square))
print(product(3, cube))


def my_function(a, b, func):
    result = func([a, b])
    return result


print(my_function(2, 3, sum))


def colorize(thing):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color

    result = get_color() + ' ' + thing
    return result


print(colorize('apple'))


def make_color():
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color

    return get_color


first_color = make_color()
print(first_color())
