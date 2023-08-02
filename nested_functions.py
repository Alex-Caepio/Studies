def product(n, func):
    result = 1
    for number in range(1, n):
        result *= func(number)
    return result


def square(x):
    return x * x


print(product(4, square))
