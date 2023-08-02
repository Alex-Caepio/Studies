from functools import wraps


def sum_decor(func):
    @wraps(func)
    def wrapper(*args):
        print(f'You are using {func.__name__}')
        print(f'Function documentation: {func.__doc__}')

    return wrapper


@sum_decor
def suma(a, b):
    """This function sums two numbers"""
    print(a + b)


# suma(2, 5)
print(suma.__doc__)
print(suma.__name__)
